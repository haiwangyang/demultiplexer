#!/usr/bin/env python

"""
Purpose:
    Download big files from NIH helix ftp
"""

import urllib.request
import os

def fetch_binary_file_from_helix_ftp(filename):
    """ 
       get binary file such as bam
    """
    data = urllib.request.urlopen("ftp://helix.nih.gov/pub/haiwang/" + filename)

    # check if the output dir exist, if not create it
    outputdir = "data"
    try:
        os.stat(outputdir)
    except:
        os.mkdir(outputdir)

    with open(outputdir + "/" + filename, 'wb') as f:
        for line in data:
            f.write(line)

def main():
    fetch_binary_file_from_helix_ftp("w1118_dpse_dvir_f_ac_r1.mapped.sorted.bam")

if __name__ == '__main__':
    main()
