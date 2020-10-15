from pathlib import Path
from argparse import ArgumentParser as argp
import subprocess
import os

def create_dir(path):
    p = Path(path)
    p.mkdir(parents=True,exist_ok=True)

def gather_lines(lines):
    groups = []
    group = []
    for line in lines:
        line = line.strip() 
        if line == "":
            groups.append(group)
            group = []
        else:
            group.append(line)
    if group:
        groups.append(group)
    return groups

def parse_args():
    ap = argp(description="input file with master.json")
    ap.add_argument("-i","--input")
    args = ap.parse_args()
    return args.input


def main():
    input_file = parse_args()
    print(input_file)
    with open(input_file,'r') as f:
        groups = gather_lines(f.readlines())
    for name, master in groups:
        if name[0].isdigit():
            print(f"{name}")
            Path(f"{name}").mkdir(parents=True, exist_ok=True)
            os.chdir(f"{name}")
            print(f"vimeo-downloader.js {master}")
            subprocess.run(["vimeo-downloader.js", master])
           
            subprocess.run(f"mkvmerge -o {name}.mkv *.m4a *.m4v",
                    shell=True)
            subprocess.run("pwd")
            os.chdir("..")
            subprocess.run("pwd")

main()
