IO.readlines("oma_genomes.json").each do |line|
  f = line.match(/"id": ([0-9]+),/i)
  puts f.captures.first if f
end
