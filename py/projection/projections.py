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
    plt.savefig(title[:3]+'.png', bbox_inches='tight')




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


def factor_scatter_matrix(df, factor, palette=None):
    '''Create a scatter matrix of the variables in df, with differently colored
    points depending on the value of df[factor].
    inputs:
        df: pandas.DataFrame containing the columns to be plotted, as well 
            as factor.
        factor: string or pandas.Series. The column indicating which group 
            each row belongs to.
        palette: A list of hex codes, at least as long as the number of groups.
            If omitted, a predefined palette will be used, but it only includes
            9 groups.
    '''
    import matplotlib.colors
    import numpy as np
    from pandas.plotting import scatter_matrix
    from scipy.stats import gaussian_kde

    if isinstance(factor, basestring):
        factor_name = factor #save off the name
        factor = df[factor] #extract column
        df = df.drop(factor_name,axis=1) # remove from df, so it 
        # doesn't get a row and col in the plot.

    classes = list(set(factor))

    if palette is None:
        palette = ['#e41a1c', '#377eb8', '#4eae4b', 
                   '#994fa1', '#ff8101', '#fdfc33', 
                   '#a8572c', '#f482be', '#999999']

    color_map = dict(zip(classes,palette))

    if len(classes) > len(palette):
        raise ValueError('''Too many groups for the number of colors provided.
We only have {} colors in the palette, but you have {}
groups.'''.format(len(palette), len(classes)))

    colors = factor.apply(lambda group: color_map[group])
    axarr = scatter_matrix(df,figsize=(10,10),marker='o',c=colors,diagonal=None)


    for rc in xrange(len(df.columns)):
        for group in classes:
            y = df[factor == group].iloc[:, rc].values
            gkde = gaussian_kde(y)
            ind = np.linspace(y.min(), y.max(), 1000)
            axarr[rc][rc].plot(ind, gkde.evaluate(ind),c=color_map[group])


import pandas as pd
import numpy as np
data1 = pd.DataFrame(data= np.c_[iris['data'], iris['target']],
                     columns= iris['feature_names'] + ['target'])

factor_scatter_matrix(data1,'target', ['navy', 'turquoise', 'darkorange'])
plt.savefig('scatter_matrix.png', bbox_inches='tight')


#plot(X, 'Sepal length & width')
#plot(X[:, 2:], 'Petal length & width')

pca()
mds()
tsne()

plt.show()
