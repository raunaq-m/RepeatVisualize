#!/usr/bin/env python
"""
input a genome or next-generation sequencing reads to visualize the content of
repeat sequences present in the genome or ngs data. 
	python visualize_repeats.py --genome <genomeFasFile> [--reads <readsfile>] --coverage INT
	
	--reads 	Can be a single fastq, fasta file. If multiple files, then store
				the list of files in a text file and provide the text file. 
	--genome	Can be a single fasta file for the genome or when multiple files, 
				specify the text file containing the list of all files. 
	--coverage 	Specifies the average sequencing depth of the data, so that the content of 
				repeats can be determined 
"""
import os
import os.path
import sys

import logging
import logging.handlers


repeatslog = logging.getLogger(__name__)

dn = os.path.dirname(__file__)

if __name__ == "__main__":
	import argparse
	import shutil 
	
	# Include a Bio import SeqIO file? Not needed as the file will be directly parsed
	# to the dsk software for k-mer counting 
	
	parser = argparse.ArgumentParser("Visualize the repeat content for a genome or ngs data")
	
	parser.add_argument('-g','--genome',
						help='file of the genome to be used')
	parser.add_argument('-r','--reads',
						help='file containing reads for a genome')
	parser.add_argument('-c','--coverage',type=int,
						help='coverage of the sequenced file',
						default=30)
		
	args = parser.parse_args()
	if (os.path.isfile(args.genome)):
		print args.genome
	elif (os.path.isfile(args.reads)):
		print args.reads
	else:
		print "Enter at least one of reads or genomes file"
		print parser.parse_args(['-h'])
		sys.exit()
	
	print args.genome, args.reads, args.coverage 
	
	