import matplotlib.pyplot as plt

from sklearn import decomposition
from sklearn import manifold
from sklearn import datasets


iris = datasets.load_iris()
X = iris.data  # 4 attributes, 150 values, 50 for each flower


def plot(data, title):
    plt.figure()
    colors = ['navy', 'turquoise', 'darkorange']
    lw = 2

    for color, i, target_name in zip(colors, [0, 1, 2], iris.target_names):
        plt.scatter(data[iris.target == i, 0], data[iris.target == i, 1], color=color, alpha=.8, lw=lw,
                    label=target_name)
    plt.legend(loc='best', shadow=False, scatterpoints=1)
    plt.title(title)




def pca():
    pca = decomposition.PCA(n_components=2)
    X_pca = pca.fit_transform(X)

    plot(X_pca, 'PCA of IRIS dataset')


def mds():
    mds = manifold.MDS(n_components=2)
    X_mds = mds.fit_transform(X)
  
    plot(X_mds, 'MDS of Iris dataset')


def tsne():
    tsne = manifold.TSNE(n_components=2)
    X_tsne = tsne.fit_transform(X)
 
    plot(X_tsne, 't-SNE of Iris dataset')




plot(X, 'Sepal length & width')
plot(X[:, 2:], 'Petal length & width')

pca()
mds()
tsne()


plt.show()
