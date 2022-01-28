import csv
from multiprocessing import Pool
import os
import sys
from urllib.parse import urlparse

file = open('genomes.csv')
csvreader = csv.reader(file)

headers = next(csvreader)

def process_line(line):
  species_name = line[0]
  print("Processing " + species_name)
  url = line[1]
  lineage = line[10]
  filename = species_name.replace(" ", "_") + ".fa"
  filename_dl = species_name.replace(" ", "_") + os.path.basename(urlparse(url).path)
  busco_output_folder = "busco_" + species_name.replace(" ", "_")

  # If the processed fasta file is already present, we don't need to do it again
  if os.path.isfile("filtered_proteomes/" + filename):
    print(" skipping")
  else:
    os.system("wget " + url + " -O " + filename_dl)
    os.system("gunzip " + filename_dl)
    os.system("python " + 'get_longest_transcript.py ' + filename_dl.replace(".gz", "") + " " + filename)
    os.system("busco -i "+filename+" -l "+lineage+" -o '"+ busco_output_folder +"' -m prot")
    os.system("rm " + filename_dl.replace(".gz", ""))
    os.system("mv " + filename + " filtered_proteomes/" + filename)


with Pool(processes=10) as pool:
  pool.map(process_line, list(csvreader))

