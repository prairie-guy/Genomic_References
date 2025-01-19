#!/usr/bin/env sh

# Download an authoritative TSS file convert: start -> start - 1000, end -> end + 100, chrX -> chr

wget https://reftss.riken.jp/datafiles/current/human/refTSS_v4.1_human_coordinate.hg38.bed.txt.gz

gunzip refTSS_v4.1_human_coordinate.hg38.bed.txt.gz

mv refTSS_v4.1_human_coordinate.hg38.bed.txt refTSS_v4.1_human_coordinate.hg38.bed

cat refTSS_v4.1_human_coordinate.hg38.bed | awk 'NR>1 {print $1 "\t" $2-1000 "\t" $2+100  "\t" $6}' | awk '$2 > 0' | sed 's/chr//' > promoter.bed
