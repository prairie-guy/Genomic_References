#!/usr/bin/env sh

# https://bismap.hoffmanlab.org
# Umap software package efficiently identifies uniquely mappable regions of any genome. Its Bismap extension identifies mappability of the bisulfite-converted genome (methylome).
#
# Download here
# hg38 chr: 1-22, X
#
bismap_src=https://bismap.hoffmanlab.org/raw/hg38/k100.bismap.bedgraph.gz
bismap_bg=k100.bismap.bedgraph.gz
bismap_bed=human_k100.bismap.bed.gz

# Download
wget $bismap_src -O $bismap_bg
echo downloaded $bismap_bg

# Convert chrZ -> Z
echo converting chrZ in $bismap_bg to Z in  $bismap_bed ....
zcat $bismap_bg | sed s/^chr// | gzip > $bismap_bed


# Remove original
rm $bismap_bg
echo $bismap_bed downloaded and converted successfully
