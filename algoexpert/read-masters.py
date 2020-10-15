import subprocess
import numpy as np
from argparse import ArgumentParser as arp
import os

def run(cmd):
    p = subprocess.run(cmd,
            capture_output=True,
            text=True)
    if p.stdout or p.stderr:
        print(p.stdout, p.stderr)

def get_args():
    p = arp(description="read videos given a master list")
    p.add_argument("inp")
    args = p.parse_args()
    return args.inp

def main():
    afile = get_args()
    height = '1080'
    with open(afile,"r") as f:
        count = 1
        for line in f.readlines():
            url = line.strip()[1:-1]
            outdir = f"{count:02}"
            os.makedirs(outdir, exist_ok=True)
            os.chdir(outdir)
            cmd = [ 
                    'node',
                    '../vimeo-downloader.js',
                    url,
                    height]
            run(cmd)
            print(" ".join(map(str, cmd)))
            cmd = [
                    "mkvmerge",
                    "-o",
                    f"{count:02}.mkv",
                    "*.m4v",
                    "*.m4a"
                    ]
            run(cmd)
            print(" ".join(map(str, cmd)))
            os.chdir("..")
            count += 1

main()
