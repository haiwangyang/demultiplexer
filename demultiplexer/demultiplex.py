from __future__ import print_function, division
import gzip
from Bio import SeqIO
from subprocess import Popen, PIPE
import functools
import os,sys

'''
p3 demultiplex.py data/w1118_dpse_dvir_f_ac_r1.mapped.sorted.bam dmel_dpse_dvir_ERCC
'''

def get_speciesList(speciesType):
    """ given speciesType return a list of all species """
    if speciesType == "dmel_dpse_dvir_ERCC":
        return(["dmel","dpse","dvir","ERCC", "uncate"])
    if speciesType == "dmel_dmoj_dper_ERCC":
        return(["dmel","dmoj","dper","ERCC", "uncate"])
    if speciesType == "dwil_dana_dyak_ERCC":
        return(["dwil","dana","dyak","ERCC", "uncate"])
    if speciesType == "dmel_dvir_ERCC":
        return(["dmel","dvir","ERCC", "uncate"])

def demultiplx_bam_file(bamfile, speciesType):
    """ get all species involved """
    speciesList = get_speciesList(speciesType)
    
    """ make file handles for different species """
    outFileHandles = {}
    for species in speciesList:
        outFile = bamfile.replace("bam", species + ".unique_plus_spspmulti.sam")
        outFileHandles[species] =  open(outFile, 'w')
    p = Popen(['samtools', 'view', bamfile], stdout=PIPE)
    
    """ add header to each categorized sam file """
    pH = Popen(['samtools', 'view', "-H", bamfile], stdout=PIPE)
    for line in pH.stdout:
        for species in speciesList:
            outFileHandles[species].write(line)
    
    """ add content to each categorized sam file """
    this_multihit_query_name = ''
    for line in p.stdout:
        lst = line.rstrip().split()
        query_name = lst[0]
        chrom = lst[2]
        if chrom.startswith("ERCC"):
            species = "ERCC"
        else:
            temp = chrom.split("_")
            species = temp[0]
        sequence = lst[9]
        quality = lst[10]
        NH = int(lst[11].replace("NH:i:",""))

        """ if mapped to multiple position """
        if NH > 1:
            if this_multihit_query_name != query_name: # first line of this query_name
                this_multihit_query_name = query_name
                this_multihit_remain = int(NH)
                myDict = {}
                myDict[query_name] = {}
                myDict[query_name][species] = 1
                this_multihit_remain -= 1
            else: # if multihit, but not the first line
                if not species in myDict[query_name].keys():
                    myDict[query_name][species] = 1
                else:
                    myDict[query_name][species] += 1
                if this_multihit_remain == 1:
                    query_names = myDict.keys()
                    if len(query_names) == 1 and len(myDict[query_names[0]].keys()) == 1:
                        outFileHandles[species].write(line)
                    else:
                        outFileHandles["uncate"].write(line)
                    this_multihit_query_name = ''
                    
                this_multihit_remain -= 1
                
        else:            
            outFileHandles[species].write(line)
            
    """ close all file handles """        
    for i in speciesList:
        outFileHandles[species].close()

def main():
    bamfile = sys.argv[1]
    speciesType = sys.argv[2]
    demultiplx_bam_file(bamfile, speciesType)

if __name__ == '__main__':
    main()
