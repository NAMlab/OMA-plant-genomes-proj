import csv
from multiprocessing import Pool
import os
import sys
from urllib.parse import urlparse

file = open('Plant_Genomes_OMA_more_17.01.csv')
csvreader = csv.reader(file)

headers = next(csvreader)

def process_line(line):
  species_name = line[0]
  print("Processing " + species_name)
  url = line[1]
  os.system("wget " + url)
  filename = os.path.basename(urlparse(url).path)
  os.system("gunzip " + filename)
  new_filename = species_name.replace(" ", "_") + ".fa"
  os.system("python " + 'get_longest_transcript.py ' + filename.replace(".gz", "") + " " + new_filename)
  lineage = line[10]
  busco_output_folder = "busco_" + species_name.replace(" ", "_")
  os.system("busco -i "+new_filename+" -l "+lineage+" -o '"+ busco_output_folder +"' -m prot")
  os.system("rm " + filename.replace(".gz", ""))


with Pool(processes=10) as pool:
  pool.map(process_line, list(csvreader))

