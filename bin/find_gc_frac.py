#!/usr/bin/env python3

from Bio import SeqIO
from Bio.SeqUtils import gc_fraction
import sys

def find_gc_frac(fasta_file, output_file=None, window_size=1000):
    """
    Calculate GC content in windows across a genome in FASTA format
    and write results to a BED file or stdout.

    This function processes a FASTA file containing genomic sequences and calculates
    the GC content for windows along each sequence. The results are written
    in BED format, where each line represents a window and contains four columns:
    chromosome name, start position (0-based), end position (1-based), and GC content
    as a fraction.

    The output follows the BED format conventions:
    - Coordinates are 0-based, half-open intervals.
    - The first base in a chromosome is numbered 0.
    - The chromEnd base is not included in the feature.

    :param fasta_file: Path to the input FASTA file
    :param output_file: Path to the output BED file (if None, output to stdout)
    :param window_size: Size of the window in base pairs (default: 1000)
    """
    out_f = open(output_file, 'w') if output_file else sys.stdout

    try:
        for record in SeqIO.parse(fasta_file, "fasta"):
            chromosome = record.id
            sequence = record.seq
            seq_length = len(sequence)

            for start in range(0, seq_length, window_size):
                end = min(start + window_size, seq_length)
                window = sequence[start:end]
                gc_content = gc_fraction(window)

                # Write to BED file (0-based start, 1-based end)
                out_f.write(f"{chromosome}\t{start}\t{end}\t{gc_content:.6f}\n")
    finally:
        if output_file:
            out_f.close()

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(
        prog='find_gc_frac',
        description="Calculate GC content from FASTA and output to BED format.",
        epilog="""
        Output BED file format:
        - Four columns: chromosome, start, end, GC content
        - Coordinates are 0-based, half-open intervals
        - The first base in a chromosome is numbered 0
        - The chromEnd base is not included in the feature
        - GC content is represented as a fraction between 0 and 1

        Example usage:
        %(prog)s input.fasta -o output.bed -w 500
        %(prog)s input.fasta  # Output to stdout
        """,
        formatter_class=argparse.RawDescriptionHelpFormatter
    )
    parser.add_argument("fasta_file", help="Path to the input FASTA file")
    parser.add_argument("-o", "--output_file", help="Path to the output BED file (if not specified, output to stdout)")
    parser.add_argument("-w", "--window_size", type=int, default=1000,
                        help="Window size in base pairs (default: 1000)")

    args = parser.parse_args()

    find_gc_frac(args.fasta_file, args.output_file, args.window_size)