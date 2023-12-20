
import sys

def fastaParser(filename):
   current_gene = ""
   genes = {}
   fh = open(filename, 'r')
 
   for line in fh:
       line = line.strip()
       if line.startswith('>'):
           current_gene = line[1:]
           genes[current_gene] = ''
       else:
            join(genes, current_gene, line) 
   return genes
 
def join(gene_dict, gene, line):
    gene_dict[gene] += line
 
genomes = fastaParser(sys.argv[1])
 
print ("There are", len(genomes), "sequences.")
