import numpy as np
def pca(x,n):
	xm=np.mean(x,axis=0)
	x1=x-xm
	xcov=np.cov(x1,rowvar=0)
	eigVals,eigVects=np.linalg.eig(np.mat(xcov))
	index=np.argsort(eigVals)
	index_v=index[-1:-(n+1):-1]
	v=eigVects[:,index_v]
	xlow=x1*v
	x_pca=(xlow*v.T)+xm
	return v,x_pca

x=np.random.randn(200,10)
v,x_pca=pca(x,3)
print v
