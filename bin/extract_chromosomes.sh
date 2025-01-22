#!/usr/bin/env sh

# Function: extract_chromosomes
# Description: Extracts only chromosomal sequences from a FASTA genome assembly file,
#              filtering out scaffolds and other sequence types.
#
# Usage: ./extract_chromosomes.sh input.fasta > output.fasta
#
# Parameters:
#   input.fasta  - A FASTA file containing genomic sequences
#                  Headers must be format:
#                  >chr dna:type other_info
#
# Output:
#   - FASTA file containing only chromosome sequences
#   - Prints to stdout (can be redirected to file)
#   - Retains standard chromosomes (1-19, X, Y, MT for mouse)
#   - Excludes all scaffold sequences
#
# Example input header:
#   >14 dna:chromosome chromosome:GRCm39:14:1:125139656:1 REF
#
# Notes:
# The awk script works as follows:
#   1. /^>/ matches any line starting with ">" (FASTA headers)
#   2. For header lines:
#      - Checks if $2 matches seq_type
#      - If match: sets p=1 (print mode)
#      - If no match: sets p=0 (skip mode)
#   3. For non-header lines (sequence data):
#      - p value remains unchanged from previous header
#      - Lines are printed only when p=1
#   4. The final 'p' condition controls printing:
#      - When p=1: line is printed
#      - When p=0: line is skipped

in=$1
type="dna:chromosome"

awk -v s="$type" '/^>/ {if($2==s) {p=1} else {p=0}} p' "$in"
