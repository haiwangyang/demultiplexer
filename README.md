# demultiplexer
Demultiplex bam file with mixed species.

## Background
We used two approaches to multiplex our RNA-seq experiment to maximize the usage of each Illumina lane. The first approach was dual indexes, and the second one was distantly related species. Demultiplexation for the first approach can be easily conducted by CASAVA (v1.8.2), and afterwards fastq files with reads from mixed species were available. I wrote the this package (i.e., **demultiplexer**) to perform the second round of demuliplexation.

## How to use the package
* Obtain fastq with RNA-seq reads from mixed species<br>
* Obtain genomes (in fasta format) for those species<br>
* Add prefix of species name for each scaffold/chromosome<br>
For instance, "2L" => "dmel_2L"<br>
* merge those genomes with modified scaffold/chromosome name<br>
For instance, dmel_dpse_dvir_ERCC.fasta, a genome file with dmel, dpse, dvir, and ERCC<br>
* index the merged genome with HiSAT2 (or STAR)<br>
./build_hisat2_index.sh dmel_dpse_dvir_ERCC<br>
or<br>
./build_star_index.sh dmel_dpse_dvir_ERCC<br>
* Obtain bam file with reads mapped to genomes of multiple species<br>
./generate_mixed_bam.sh dmel_dpse_dvir_ERCC<br>
or download an example mixed bam file by this command<br>
python3 download.py<br>
* Run demultiplexer<br>
python3 demultiplexer.py<br>


