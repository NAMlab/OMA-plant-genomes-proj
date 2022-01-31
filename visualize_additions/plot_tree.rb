require "json"

t = ["common", "oma_only", "ours_only"].map do |a|
  [a, 
    IO.readlines("species_#{a}.nw").map do |line|
      f = line.match(/([a-zA-Z\. ]+)/i)
      "'" + f.captures.first + "'" if f
    end.compact!
  ]
end.to_h

puts t.to_json

open("ornaments.map", "w") do |f|
  f.puts('"<circle style=\'fill:blue;stroke:black\' r=\'5\'/>" I ' + t["common"].join(" "))
  f.puts('"<circle style=\'fill:grey;stroke:black\' r=\'5\'/>" I ' + t["oma_only"].join(" "))
  f.puts('"<circle style=\'fill:red;stroke:black\' r=\'5\'/>" I ' + t["ours_only"].join(" "))
end

`./newick-utils-1.5.0/src/nw_display -s -w 1000  -b 'opacity:0' -S -o ornaments.map species_all.nw > species_all.svg`
