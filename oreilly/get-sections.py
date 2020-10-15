import re
import subprocess

def run(a,b):
    p = subprocess.run(
            [
                'wget',
                line.strip(),
                '-O',
                out
            ],
            capture_output=True,
            text=True)
    print(p.stdout, p.stderr))

with open("index.m3u8","r") as f:
    for line in f.readlines():
        if g := re.search("a.mp4/(seg.+)\?",line):
            out = g.groups()[0]
            print(out)

            if True:
                p = subprocess.run(
                        [
                            'wget',
                            line.strip(),
                            '-O',
                            out
                        ],
                        capture_output=True,
                        text=True)
                print(p.stdout, p.stderr))

