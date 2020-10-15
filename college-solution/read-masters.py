import subprocess
import numpy as np
from argparse import ArgumentParser as arp
import os
import sys

def run(cmd):
    p = subprocess.run(cmd,
            capture_output=True,
            text=True,
            shell=True)
    if p.stdout or p.stderr:
        print(p.stdout, p.stderr)

def run2(cmd):
    p = subprocess.Popen(cmd, shell=True)
    p.communicate()
    p.wait()

def get_args():
    p = arp(description="read videos given a master list")
    p.add_argument("inp",
            help="input master file")
    p.add_argument("--height", default=1080,
            help="desired height")
    args = p.parse_args()
    return args

def main():
    args = get_args()
    afile = args.inp
    height = args.height
    # print(afile, height)
    # sys.exit(1)
    with open(afile,"r") as f:
        count = 1
        for line in f.readlines():
            url = line.strip()
            
            # skip
            if line[0] == '#':
                count += 1
                continue
            
            # remove quotes 
            if line[0] == "\"":
                url = url[1:-1]
           
            # create output directory
            outdir = f"{count:02}"
            os.makedirs(outdir, exist_ok=True)

            # enter output directory
            os.chdir(outdir)
           
            cmd = [ 
                    'node',
                    '../vimeo-downloader.js',
                    url,
                    height]

            # here we combine because using shell=True
            cmd = " ".join(map(str, cmd))
            print(cmd) 
            run2(cmd)
            
            cmd = [
                    "mkvmerge",
                    "-o",
                    f"{count:02}.mkv",
                    "*.m4v",
                    "*.m4a"
                    ]
            cmd = " ".join(map(str, cmd))
            print(cmd)
            run2(cmd)
           
            os.chdir("..")
            count += 1

main()
