Here we want to visualize which genomes & clades were already present in OMA, which we update, and which ones we add.
The workflow is like this: 
1. Get the NCBI Taxonomy IDs of all species present in OMA (https://omabrowser.org/api/taxonomy/33090/?type=json ) as well as all our NCBI Taxonomy IDs (`ncbi_ids_*.txt`)
2. Make a common tree on NCBI taxonomy https://www.ncbi.nlm.nih.gov/Taxonomy/CommonTree/wwwcmt.cgi (`species_all_nw`) and translate the NCBI IDs to species names (`species_common.nw`, `species_oma_only.nw`, `species_ours_only.nw` generated from the equivalient `ncbi_ids_*.txt` files)
3. Mark the species according to "ours_only", "oma_only", "common" and visualize with nw_utils (`plot_tree.rb`, `species_all.svg`)
