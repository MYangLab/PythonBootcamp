
import sys

def fastaParser(filename):
   current_gene = ""
   genes = {}
   fh = open(filename, 'r')
 
   for line in fh:
       line = line.strip()
       if line.startswith('>'):
           current_gene = line[1:]
           genes[current_gene] = []  ##CHANGE
       else: 
            join(genes, current_gene, line) 
   
    ##CHANGE ADDED FOR LOOP
   for gene in genes:
       genes[gene] = ''.join(genes[gene])
   return genes
 
def join(gene_dict, gene, line):
    gene_dict[gene].append(line)   ##CHANGE
 
genomes = fastaParser(sys.argv[1])
 
print ("There are", len(genomes), "sequences.")
