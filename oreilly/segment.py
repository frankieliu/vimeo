import os
import sys 
import re
import subprocess 
import numpy as np

"""
https://learning.oreilly.com/videos/ruby-on-rails/9780136733461/9780136733461-ROR6_01_01_00_00

9780136733461-ROR6_00_00_00_00 fetch
index.m3u8 xhr

In list.txt
1. Add a title like 00-00-00-00-introduction
2. Copy links from the above
3. Paste it in list.txt

You can add:
    skip
    srt
    index
    segments
    verify
    combine
    all
    srt/index/segments/verify/combine

"""

def get_input_file():
    if len(sys.argv) < 2:
        print("Please supply an input file")
        print("The format should contain four lines")
        print("per video.")
        print("The first line contains a user supplied name")
        print("The second line contains the text link")
        print("The third line contains the index.m3u8")
        print("The fourth line is an empty line")
        sys.exit(1)
    return sys.argv[1]

def get_params(infile):
    all_params = []
    with open(infile,"r") as f:
        params = []
        for line in f.readlines():
            if line == "\n":
                all_params.append(params)
                params = []
            else:
                params.append(line.strip())
        # take care of remaining params
        if len(params) != 0:
            all_params.append(params)
            params = []
    return all_params

def run(ainput,aoutput,printidx=[0,1]):
    cmd = np.array(['wget',ainput,'-O',aoutput])
    print(" ".join(cmd[printidx]))
    p = subprocess.run(
            cmd,
            capture_output=True,
            text=True)
    if p.stdout or p.stderr: 
        print(p.stdout, p.stderr)

def read_segments():
    with open("index.m3u8","r") as f:
        for line in f.readlines():
            if g := re.search("a.mp4/(seg.+)\?",line):
                # get the name of the ts file 
                out = g.groups()[0]
                run(ainput=line.strip(),
                        aoutput=out,
                        printidx=[0,3])

def verify_segments():
    with open("index.m3u8","r") as f:
        for line in f.readlines():
            if g := re.search("a.mp4/(seg.+)\?",line):
                # get the name of the ts file 
                out = g.groups()[0]
                if not os.path.exists(g.groups()[0]):
                    print(f"Missing: {os.getcwd()} {out}")
                    sys.exit(1)

def combine_segments(out):
    p = subprocess.run("cat $(ls *.ts | sort -n -t '-' -k2) > "+out,
            capture_output=True, shell=True)
    if p.stdout or p.stderr: 
        print(p.stdout, p.stderr)
   
def create_dirs(all_params):
    for params in all_params:
        tmp = params[0].split(" ")
        if len(tmp) == 1:
            cmd, name = "all", tmp[0]
        else:
            cmd, name = tmp
       
        if cmd == "skip" or len(params) !=3: continue
        
        if cmd == "all":
            cmd = ["srt", "index", "segments", "verify", "combine"]
        elif "/" in cmd:
            cmd = cmd.split("/")
        else:
            cmd = [cmd]

        print(f"operating on {name}")
        print(cmd)       

        os.makedirs(name, exist_ok=True)
        os.chdir(name)
        if "srt" in cmd:
            run(ainput=params[1], aoutput=name+".srt")
        if "index" in cmd:
            run(ainput=params[2], aoutput="index.m3u8")
        if "segments" in cmd:
            read_segments()
        if "verify" in cmd:
            verify_segments()
        if "combine" in cmd:
            combine_segments(name + ".mp4")
        os.chdir("..")

def main():
    fname = get_input_file()
    print("reading parameters")
    params = get_params(fname)
    print("downloading...")
    create_dirs(params)

# main()
