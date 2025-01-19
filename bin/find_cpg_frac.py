#!/usr/bin/env python3

from Bio import SeqIO
import sys

def find_cpg_frac(fasta_file, output_file=None, window_size=1000):
    """
    Calculate CpG dinucleotide fraction in windows across a genome in FASTA format
    and write results to a BED file or stdout.

    This function processes a FASTA file containing genomic sequences and calculates
    the CpG dinucleotide fraction for windows along each sequence. The results are written
    in BED format, where each line represents a window and contains four columns:
    chromosome name, start position (0-based), end position (1-based), and CpG fraction.

    The output follows the BED format conventions:
    - Coordinates are 0-based, half-open intervals.
    - The first base in a chromosome is numbered 0.
    - The chromEnd base is not included in the feature.

    :param fasta_file: Path to the input FASTA file
    :param output_file: Path to the output BED file (if None, output to stdout)
    :param window_size: Size of the window in base pairs (default: 1000)
    """
    def count_cpg(sequence):
        return sum(sequence[i:i+2] == "CG" for i in range(len(sequence) - 1))

    out_f = open(output_file, 'w') if output_file else sys.stdout
    try:
        for record in SeqIO.parse(fasta_file, "fasta"):
            chromosome = record.id
            sequence = str(record.seq).upper()
            seq_length = len(sequence)
            for start in range(0, seq_length, window_size):
                end = min(start + window_size, seq_length)
                window = sequence[start:end]
                cpg_count = count_cpg(window)
                if end < seq_length and window[-1] == 'C' and sequence[end] == 'G':
                    cpg_count += 1
                actual_window_size = end - start
                cpg_fraction = cpg_count / actual_window_size if actual_window_size > 0 else 0
                out_f.write(f"{chromosome}\t{start}\t{end}\t{cpg_fraction:.6f}\n")
    finally:
        if output_file:
            out_f.close()

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(
        prog='find_cpg_frac',
        description="Calculate CpG dinucleotide fraction from FASTA and output to BED format.",
        epilog="""
        Output BED file format:
        - Four columns: chromosome, start, end, CpG fraction
        - Coordinates are 0-based, half-open intervals
        - The first base in a chromosome is numbered 0
        - The chromEnd base is not included in the feature
        - CpG fraction is represented as a fraction between 0 and 1

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
    find_cpg_frac(args.fasta_file, args.output_file, args.window_size)