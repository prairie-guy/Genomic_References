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

### DNA Annotation

#### cpg_island.bed
[USCS userApps/cpg_lh program](https://genome.ucsc.edu/cgi-bin/hgTables?db=hg38&hgta_group=regulation&hgta_track=cpgIslandExt&hgta_table=cpgIslandExt&hgta_doSchema=describe+table+schema)

    chrom	    chr1    	Reference sequence chromosome or scaffold
    chromStart 28735	    Start position in chromosome
    chromEnd   29737	    End position in chromosome
    name	    CpG: 111	CpG Island
    length	    1002	    Island Length
    cpgNum	    111	        Number of CpGs in island
    gcNum	    731	        Number of C and G in island
    perCpg	    22.2	    Percentage of island that is CpG
    perGc	    73	        Percentage of island that is C or G
    obsExp	    0.85	    Ratio of observed(cpgNum) to expected(numC*numG/length) CpG in island


    1       2           3           4           5       6       7       8       9       10
    chrom   chromStart  chromEnd	name	    length	cpgNum	gcNum	perCpg	perGc	obsExp
    chr1	28735   	29737	    CpG: 111	1002	111	    731	    22.2	73	    0.85
```
uscs_userApps/bin/cpg_lh human.fa | \ 
            awk '{$2 = $2 - 1; width = $3 - $2;\
            printf("%s\t%d\t%s\t%s %s\t%s\t%s\t%0.0f\t%0.1f\t%s\t%s\n",$1, $2, $3, $5, $6, width, $6, width*$7*0.01, 100.0*2*$6/width, $7, $9);}' | \
            sort -k1,1 -k2,2n > human_cpg_island.bed
```

### RNA References
These are a variety of RNA fasta sequences originally forked from from chlab/db curated by @y9c. These are useful for filtering various RNA sequences from experimental sequencing samples. 

### BAT-seq
These are fasta files for templates used in the BAT-seq processing.

- 200merMeth.fa (Methylation Sites: 123+, 124-)
- 5mc164.fa (Methylation Sites: 77+, 127+, 93-, 128-)
- pUC19.fa (Mathylation Sites: All CpG sites are 100% methylated)
- lambda.fa (Methlyation Sites: No sites)



