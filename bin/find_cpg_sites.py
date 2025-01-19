#!/usr/bin/env python3

import argparse
import os
import sys
from typing import Optional, TextIO
from Bio import SeqIO

def find_cpg_sites(fasta_file: str, output: TextIO) -> None:
    """
    Find CpG dinucleotides from a FASTA file and write to the given output.
    
    Parameters:
    fasta_file (str): Input FASTA file path.
    output (TextIO): Output file object to write BED format data.
    """
    for record in SeqIO.parse(fasta_file, "fasta"):
        sequence = str(record.seq)
        seq_id = record.id
        for i in range(len(sequence) - 1):
            if sequence[i:i + 2] == "CG":
                output.write(f"{seq_id}\t{i}\t{i+2}\tCpG\n")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Find CpG sites in a FASTA file and output as BED format.")
    parser.add_argument("input_file", help="Input FASTA file")
    parser.add_argument("output_file", nargs='?', help="Output BED file (optional)")
    parser.add_argument("--parameter", help="Optional second parameter")
    args = parser.parse_args()

    input_file = args.input_file
    if not input_file.lower().endswith(('.fa', '.fasta')):
        raise ValueError("Input file must have .fa or .fasta extension")

    if args.output_file:
        with open(args.output_file, 'w') as output:
            find_cpg_sites(input_file, output)
    else:
        find_cpg_sites(input_file, sys.stdout)

    if args.parameter:
        print(f"Optional parameter provided: {args.parameter}", file=sys.stderr)