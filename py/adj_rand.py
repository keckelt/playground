# http://scikit-learn.org/stable/modules/generated/sklearn.metrics.adjusted_rand_score.html
from sklearn.metrics.cluster import adjusted_rand_score


a = [0, 0, 1, 1, 2, 2]
b = [2, 1, 1, 0, 0, 2]

print(adjusted_rand_score(a, b))
print(adjusted_rand_score(b, a))

