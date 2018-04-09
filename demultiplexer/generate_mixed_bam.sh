f=$1
module load hisat/2.0.5 samtools/0.1.19; hisat2 -p 4 -x genome/${f}_hs --max-intronlen 300000 --dta -U fastq/${f}.fastq.gz 2> log/${f}.log | samtools view  -Su - | samtools sort - bam/${f} && samtools index bam/${f}.bam
