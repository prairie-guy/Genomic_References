# Steps to Generate human_TSS.bed

1. https://genome.ucsc.edu/cgi-bin/hgTables

2. Select
  - human hg38
  - Group = Regulation
  - Track = TSS Peaks
  - Table = robustPeaks
  - Output Format = BED
  - Output filename = 'promoter2' # arbitrary

3. Download Table as 'promoter2.bed'

4. cat promoter2.bed |awk '{print $1 "\t"  $2 + 1000 "\t" $3 - 100 "\t" $6 "\t"  $4}'|sed 's/chr//' > human_promoter.bed
