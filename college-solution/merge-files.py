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
    p = subprocess.Popen(cmd,shell=True)
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
            outdir = f"{count:02}"
            os.makedirs(outdir, exist_ok=True)
            os.chdir(outdir)
            cmd = [ 
                    'node',
                    '../vimeo-downloader.js',
                    url,
                    height]
            # print(" ".join(map(str, cmd)))
            # run2(cmd)
            cmd = [
                    "mkvmerge",
                    "-o",
                    f"{count:02}.mkv",
                    "*.m4v",
                    "*.m4a"
                    ]
            # here we must join so that globbing works correctly
            cmd = " ".join(cmd)
            print(cmd)
            run2(cmd)
            os.chdir("..")
            count += 1

main()
