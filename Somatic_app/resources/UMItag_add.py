import os
import sys
import re
import argparse
import pysam

def bamaddtag(bamFile,outputFile):
    bam = pysam.AlignmentFile(bamFile)
    bam_output = pysam.AlignmentFile(outputFile, "wb", template=bam)
    for r in bam:
        r_new = r.__copy__()
        r_new.tags += [('XV',1)]
        r_new.tags += [('XW',0)]
        bam_output.write(r_new)

def build_parser():
    parser = argparse.ArgumentParser(description=__doc__,formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument("--bam", type=str, required=True,help="bam to add UMI tag")
    parser.add_argument("--outbam", type=str, required=True,help="output bam file")
    return parser

def main():
    parser = build_parser()
    args = parser.parse_args()
    bam = args.bam
    output = args.outbam
    bamaddtag(bam,output)

if __name__ == "__main__":
    main()
