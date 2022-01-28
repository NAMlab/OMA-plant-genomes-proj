import argparse
from Bio import SeqIO
from Bio.Seq import Seq
import re
import sys
import logging
  
#checking if the transcript pattern is supplied by the user and making
#regular expression objects of the pattern
def get_longest_transcript(input,output,gene_start,trans_pattern="-[0-9]+"):
    trans_pattern = re.compile(trans_pattern)
  
    '''
    Parsing the gene start pattern so that we can filter out unwanted genes
    '''
    gene_pattern = re.compile(gene_start)
  
    #object to store the gene sequences
    seqs = {}
  
    '''
    Looping through to read and store the longest transscript sequence for each gene
    for each iteration regex replace the trans id to get gene id
    if length is longer than existing sequence replace or add the gene id sequence to dict
    '''
    for record in SeqIO.parse(input, "fasta"):
        # gene_id = record.description.split(" ")[3].replace("gene:", "") # This does not work with Brassica napus
        gene_id = re.compile(r'gene[=:]([^\s]+)').search(record.description).group(1)
        if gene_pattern.match(gene_id) is None:
            continue
        if gene_id in seqs:
            if len(seqs[gene_id].seq) < len(record.seq):
                seqs[gene_id] = record
        else:
            seqs[gene_id] = record
  
    '''
    This creates a list of sequences which can be saved into a file
    '''
    out_seqs = []
    for key in sorted(seqs.keys()):
        curr_seq = seqs[key]
        curr_seq.id = key
        curr_seq.name = ""
        curr_seq.description = ""
        curr_seq.seq = Seq(re.sub(r"[^A-Za-z]","",str(curr_seq.seq)))
        out_seqs.append(curr_seq)
  
    #Write the output file as fasta
    SeqIO.write(out_seqs,output,"fasta")
  
get_longest_transcript(sys.argv[1], sys.argv[2], "", "\.[0-9]+$")
