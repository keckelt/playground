from __future__ import division
import random
import math
import matplotlib.pyplot as plt
import numpy as np

def enrichment_score(all_genes, gene_set):
    running_sum = 0
    scores = [running_sum] # enrichment scores of the random walk

    for gene in all_genes:
        # The score is calculated by walking down the list, increasing a running-sum statistic when we encounter a gene  and decreasing when it is not
        if gene in gene_set:
            running_sum += math.sqrt((len(all_genes)-len(gene_set))/len(gene_set))
        else:
            running_sum -= math.sqrt(len(gene_set)/(len(all_genes)-len(gene_set)))
        scores.append(running_sum)

    # The ES is the maximum deviation from zero encountered in the random walk; it corresponds to a weighted Kolmogorov-Smirnov-like statistic
    return max(scores, key=abs), scores


# --------------------------------------------------------------------------------------------------------------


n = 1200+1  # number of genes
n_s = 98+1  # number of genes in my set of interest

genes = range(1,n)  # all my genes
random.shuffle(genes) # Order the genes by correlation with clinical outcome / expression / etc.

#gene_set = range(1,n_s) # the gene subset that I want to test
gene_set = random.sample(genes[1:int(n/3)], int(n_s/2)) + random.sample(genes[int(n/3):], int(n_s/2))

set_es, set_running_sum = enrichment_score(genes, gene_set)
print("ES="+str(set_es))



# Calc Significance by comparing with enrichment scores of randomly picked gene sets of the same size
permutations = 1000
set_es_significance = 0
rnd_scores = np.zeros(permutations)

for i in range(1,permutations+1):
    rnd_gene_set = random.sample(genes,len(gene_set))
    rnd_score, __ = enrichment_score(genes, rnd_gene_set)
    rnd_scores[i-1] = rnd_score
    if abs(rnd_score) > abs(set_es):
        set_es_significance += 1/permutations  # increase if a random gene set scored higher

print("Significance(ES)="+str(set_es_significance))



# Calc NES with mean of same sign enrichment scores from permutation:
# https://github.com/tristanbrown/gsea/blob/master/gsea/analysis.py#L211
# https://github.com/mrcinv/GSEA.py/blob/master/gsea/gsea.py#L154
# https://github.com/zqfang/GSEApy/blob/master/gseapy/algorithm.py#L532
set_nes = 0
set_nes_significance = 0

if set_es >= 0:
    rnd_pos_scores = rnd_scores[rnd_scores >= 0]
    set_nes = set_es / np.mean(rnd_pos_scores)
    set_nes_significance = (rnd_pos_scores > set_es).sum()/len(rnd_pos_scores)
else:
    rnd_neg_scores = rnd_scores[rnd_scores < 0]
    set_nes = set_es / abs(np.mean(rnd_neg_scores))
    set_nes_significance = (rnd_neg_scores > set_es).sum()/len(rnd_neg_scores)

print("Means="+str(np.mean(rnd_scores[rnd_scores >= 0]))+" "+str(abs(np.mean(rnd_scores[rnd_scores < 0]))))
print("NES="+str(set_nes))
print("Significance(NES)="+str(set_nes_significance))



#Running Sum Plot
plt.figure(1)
plt.subplot(411)
plt.plot(np.divide(set_running_sum, 7.0))
plt.ylabel('Running Sum')
plt.axhline(linewidth=1, color='grey')

#Location of gene set in ranked list
plt.subplot(412)
plt.xlabel('Gene Rank')
plt.ylabel('Gene found')
x = np.linspace(1, n, n)
y = np.zeros(n)
i = 0
for gene in genes:
    i += 1
    if gene in gene_set:
        y[i] = 1


plt.stem(x, y, markerfmt=' ')


plt.subplot(413)
plt.ylabel('Frequency')
plt.xlabel('Enrichment Score')
plt.hist((rnd_scores), bins=46)


plt.subplot(414)
plt.ylabel('Frequency')
plt.xlabel('Absolute Enrichment Score')
plt.hist(np.absolute(rnd_scores), bins=28)


print(len(rnd_scores))
print(np.sort(np.absolute(rnd_scores))[int(9*len(rnd_scores)/10):])


plt.show()


