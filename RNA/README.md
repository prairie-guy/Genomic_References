# DATA SOURCE

## reference genome of CONTAMINATION

- Escherichia_coli_BL21 was downloaded from NCBI: CP001509.3
- Staphylococcus_sp.\_MZ1 was download from NCBI: CP076025.1
- Parainfluenza_virus_5 was downloaded from NCBI: NC_006430.1
- Mycoplasma_sp genomes were manually curatted from common lab contamination strains

## reference sequence of GENES (from _Mus musculus_)

- rRNA genes is downloaded from NCBI
- non-coding small RNA genes, including tRNA, snoRNA, miRNA, ... etc were downloaded from NCBI with duplicated records removed.

# CHANGELOGS

> Update in 2023-01-11

patched NCBI annotation for rRNA in mouse (`Mus_musculus.GRCm39.rRNA.fa.gz`)

> Update in 2023-01-09

Update customized annotation (derived from NCBI) for rRNA + small RNA in cress (`Arabidopsis_thaliana.TAIR10.sncRNA.fa.gz`)

NCBI annotation for rRNA + small RNA in cress (`Mus_musculus.GRCm39.sncRNA.fa.gz`)

> Update in 2022-09-29

NCBI annotation for rRNA + small RNA in mouse (`Mus_musculus.GRCm39.sncRNA.fa.gz`)

> Update in 2022-07-29

NCBI annotation for small RNA is better than the ensembl version. So another reference (`Homo_sapiens.GRCh38.sncRNA.fa.gz`) which is based on NCBI database is created.
The `sncRNA` notation mean small non-coding RNA, which include:

| number | type           |
| ------ | -------------- |
| 1      | RNase-MRP-RNA  |
| 1      | RNase-P-RNA    |
| 1      | telomerase-RNA |
| 4      | Y-RNA          |
| 4      | vault-RNA      |
| 4      | scRNA          |
| 22     | rRNA           |
| 49     | scaRNA         |
| 122    | snRNA          |
| 298    | tRNA           |
| 1175   | snoRNA         |
| 1873   | premiRNA       |
