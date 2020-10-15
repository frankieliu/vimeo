from argparse import ArgumentParser as apar
from pathlib import Path
from subprocess import Popen, PIPE, CalledProcessError
import re
import os
from colorama import init
from termcolor import colored
from tqdm import tqdm
import shlex
from simple_wget import wget

def get_resolution(master_out):
    rmin = 1<<31
    out = None
    get_next = True
    with open(master_out) as f:
        for line in f.readlines():
            if m := re.search("RESOLUTION=(\d+)x(\d+)",line):
                print(m.groups()[0:2])
                get_next = int(m.groups()[1]) < rmin
            elif get_next and re.search("^\d+/index.m3u8",line):
                out = line
    return out

def go_through_directory(adir):
    p = Path(adir)
    files = [x for x in p.iterdir() if x.is_file()]
    for afile in files:
        yield afile

def extract(afile,master,print_stdout=True):
    cmd = f"./get-ts.sh {afile} {master}"
    with Popen(shlex.split(cmd),
            stdout=PIPE,
            stderr=PIPE,
            cwd='.',
            bufsize=1, universal_newlines=True) as p:
        for line in p.stdout:
                yield line.strip()
        if p.returncode:
            raise CalledProcessError(p.returncode, p.args)

def get_header(index):
    parts = index.split('/')
    return "/".join(parts[0:-2])

def main():
    init()
    top_index = 0
    json_dir = 'resources/json'
    out_dir = 'resources'
    master_out = "master.wget"
    for afile in go_through_directory(json_dir):
        top_index += 1
        if str(afile)[-1] != 'n':
            print(colored(f"Skipping {top_index} {afile}","green",attrs=["bold"]))
            continue

        # get master and index from har json file
        master_wget = list(extract(afile, 'master'))[0]
        index_wget = [x for x in extract(afile, 'index')]
       
        # create output directory
        outd = f"{out_dir}/{top_index:02}"
        os.makedirs(outd, exist_ok=True)
        os.chdir(outd)
       
        # set to lowest resolution
        print(colored("wget master", 'green', attrs=['bold']))
        wget(master_wget, master_out)
        print(colored("reading resolution", 'green', attrs=['bold']))
        resolution = get_resolution(master_out).split('/')[0]
        print(resolution)
       
        # get list of ts and webttv (subtitle) 
        header = get_header(index_wget[0])
        print(colored("wget index files",'green',attrs=['bold']))
        for i,x in enumerate(index_wget):
            wget(x,f'index{i}')

        # download content
        print(colored("wget ts and webttv",'green',attrs=['bold']))
        for i in range(2):
            folder = resolution if i==0 else 'subtitles'
            with open(f'index{i}') as f:
                lines = list([x for x in f.readlines() if x[0] != '#'])
            for line in tqdm(lines):
                download = "/".join([header, folder, line.strip()])
                wget(download,print_stdout=False)
                # print(download)
        os.chdir("../..")
main()
