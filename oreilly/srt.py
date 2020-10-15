import sys
from argparse import ArgumentParser as aparser
import json

parser = aparser(description="Convert json to srt")
parser.add_argument('inp',
        metavar="<json>",
        type=str,
        help="input json file")
args = parser.parse_args()

with open(args.inp) as jfile:
    jobj = json.load(jfile)
if len(jobj['transcriptions'])>0:
    # print(jobj['title'])
    lines = jobj['transcriptions'][0]['transcription']['lines']
    for i,line in enumerate(lines):
        print(i+1)
        print(line['begin'].replace(".",",")+
             " --> " + 
            line['end'].replace(".",","))
        print(line['text'])
        print();
