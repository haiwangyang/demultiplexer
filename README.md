# demultiplexer
Demultiplex bam file with mixed species.

## Background
We used two approaches to multiplex our RNA-seq experiment to maximize the usage of each Illumina lane. The first approach was dual indexes, and the second one was distantly related species. Demultiplexation for the first approach can be easily conducted by CASAVA (v1.8.2), and afterwards fastq files with reads from mixed species were available. I wrote the this package (i.e., **demultiplexer**) to perform the second round of demuliplexation.

## How to obtain input bam file
* Obtain fastq with RNA-seq reads from mixed species<br>
* Obtain genomes (in fasta format) for those species<br>
* Add prefix of species name for each scaffold/chromosome<br>
For instance, "2L" => "dmel_2L"
* merge those genomes with modified scaffold/chromosome name
For instance, dmel_dpse_dvir_ERCC.fasta, a genome file with dmel, dpse, dvir, and ERCC
* index the merged genome with HiSAT2 (or STAR)
dmel_dpse_dvir_ERCC_hs
* bam file with reads mapped to genomes of multiple species<br>
module load hisat/2.0.5 samtools/0.1.19; hisat2 -p 4 -x dmel_dpse_dvir_ERCC_hs --max-intronlen 300000 --dta -U dmel_dpse_dvir_ERCC.fastq.gz 2> dmel_dpse_dvir_ERCC.log | samtools view  -Su - | samtools sort - dmel_dpse_dvir_ERCC && samtools index dmel_dpse_dvir_ERCC.bam


# pipeline
(1) download the bam file to test<br>
python3 download.py<br>
(2) run demultiplex script<br>
python3 demultiplex.py<br>
