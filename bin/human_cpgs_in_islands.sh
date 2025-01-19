#!/usr/bin/env sh

# Generate bed file containing all CpGs found CpG Islands
# cpgs_in_islands=~/reference/bed/human_cpgs_in_islands.bed

# Run from ~/reference/bin
# Assumes ~/reference/bed

cpgs=../bed/human_cpg.bed
cpg_islands=../bed/human_cpg_islands.bed
cpgs_in_islands=../bed/human_cpgs_in_islands.bed

bedtools intersect -a $cpgs -b $cpg_islands > $cpgs_in_islands
