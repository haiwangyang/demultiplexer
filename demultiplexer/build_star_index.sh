f=$1
module load STAR/2.4.2a; STAR --runMode genomeGenerate --genomeDir genome/${f}_st --genomeFastaFiles genome/${f}.fasta --runThreadN 4 --limitGenomeGenerateRAM 19692513152
