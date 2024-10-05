## Genomic References

This is a repository of genomic references to be provided for reproducible access across different bioinformatic analyses. Though primarily fasta files, indexes and other references may be included--provided the files are not too large for reasonable use within GitHub.

#### Git Large File Storage (LFS) 
These files are tracked byLHS: fq.gz 

Steps required to set up LHS:

```
mamba install git-lfs
git lfs install
git lfs track "*.fq.gz"
git lfs track "*.gz"
git lfs track "*.ht2"
git add .gitattributes
```

### DNA References
- Homo_sapiens.GRCh38.111.genome.fa.gz
  ```
  wget http://ftp.ensembl.org/pub/release-111/fasta/homo_sapiens/dna/Homo_sapiens.GRCh38.dna.primary_assembly.fa.gz -o Homo_sapiens.GRCh38.111.primary_assembly.fa.gz
  ```
- Homo_sapiens.GRCh38.111.gff3.gz
 ```
 wget https://ftp.ensembl.org/pub/release-111/gtf/homo_sapiens/Homo_sapiens.GRCh38.111.chr.gtf.gz -o Homo_sapiens.GRCh38.111.chr.gtf.gz
 ``` 

- Arabidopsis_thaliana.TAIR10.dna.toplevel.fa.gz
```
wget https://ftp.ensemblgenomes.ebi.ac.uk/pub/plants/release-59/fasta/arabidopsis_thaliana/dna/Arabidopsis_thaliana.TAIR10.dna.toplevel.fa.gz
```

### RNA References
These are a variety of RNA fasta sequences originally forked from from chlab/db curated by @y9c. These are useful for filtering various RNA sequences from experimental sequencing samples. 

### BAT-seq
These are fasta files for templates used in the BAT-seq processing.

- 200merMeth.fa (Methylation Sites: 123+, 124-)
- 5mc164.fa (Methylation Sites: 77+, 127+, 93-, 128-)
- pUC19.fa (Mathylation Sites: All CpG sites are 100% methylated)
- lambda.fa (Methlyation Sites: No sites)









