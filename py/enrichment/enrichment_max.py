from __future__ import division
import random
import math
import matplotlib.pyplot as plt


n = 1200+1

genes = range(1,n+1)  # all my genes
max_scores = []
enrich_top = False

for set_size in range(1,n):
    if enrich_top:
        gene_set = range(1,set_size) # the gene subset that I want to test
    else:
        gene_set = range(n-set_size,n) # the gene subset that I want to test


    score = 0 # running sum
    scores = [score] # enrichment scores of the random walk


    for gene in genes:
        # The score is calculated by walking down the list L, increasing a running-sum statistic when we encounter a gene in S and decreasing when it is not
        if gene in gene_set:
            score += math.sqrt((len(genes)-len(gene_set))/len(gene_set))
        else:
            score -= math.sqrt(len(gene_set)/(len(genes)-len(gene_set)))
        scores.append(score)

    # The ES is the maximum deviation from zero encountered in the random walk; it corresponds to a weighted Kolmogorov-Smirnov-like statistic
    max_scores.insert(len(max_scores) if enrich_top else 0, max(scores, key=abs))


print(max(max_scores, key=abs))
print(max_scores[99])
plt.plot(max_scores)
plt.ylabel('max(ES(S))')
plt.xlabel('Size of Set S')
plt.axhline(linewidth=2, color='g')

plt.show()





