import numpy as np
X=np.array([[-1,1],[1,2],[3,2],[4,1],[5,2],[0,1]])
from sklearn.decomposition import PCA
pca=PCA(n_components='mle')
pca.fit(X)
print pca.explained_variance_ratio—_

