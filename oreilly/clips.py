import segment
import sys
import re

def get_args():
    if len(sys.argv) < 3:
        print("Supply input and output directories")
        print("Example: "+
              "python clips.py "+
              "resources/videoclips/combined.json "+
              "resources/clips")
    ainput = sys.argv[1]
    aoutput = sys.argv[2]
    if aoutput[-1] != "/":
        aoutput += "/";
    return ainput, aoutput

def main():
    filein,dirout = get_args()
    with open(filein,"r") as f:
        for afile in f.readlines():
            afile = afile.strip()[1:-1]
            if group := re.search(
                    "9780136733461-ROR6_(\d\d_\d\d_\d\d_\d\d)",
                    afile):
                base = group[1]
                segment.run(ainput=afile,
                        aoutput=dirout+base+".json",
                        printidx=[0,3])
            else:
                print(f"Error: {afile}")

main()
