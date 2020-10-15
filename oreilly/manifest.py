import segment as seg
import sys
import os
import subprocess

def get_args():
    if len(sys.argv) < 2:
        print("Requires a manifest")
    offset = 1 
    manifest_file = sys.argv[1]
    if len(sys.argv) == 3:
        offset = int(sys.argv[2])
    return manifest_file, offset

def delete_files():
    os.chdir("..")
    p = subprocess.run("rm tmp/*",
            capture_output=True, shell=True)
    if p.stdout or p.stderr:
        print(p.stdout, p.stderr)
    os.chdir("tmp")

def get_manifest(afile,offset,dryrun=True):
    outdir = "../manifest"
    with open(afile,"r") as f:
        os.chdir("tmp")
        skip_offset = set()
        for line in f.readlines():
            if offset not in skip_offset:
                index = line.strip()[1:-1]
                out = f"{outdir}/{offset:03}.mp4"
                if not dryrun:
                    seg.run(ainput=index,aoutput="index.m3u8",printidx=[0,3])  
                    seg.read_segments()
                    seg.verify_segments()
                    seg.combine_segments(out)
                print(f"Output file {out}")
                delete_files()
            offset += 1

def main():
    afile, offset = get_args()
    get_manifest(afile, offset,dryrun=False)

main()
