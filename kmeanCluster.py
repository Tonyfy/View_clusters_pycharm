#encoding:utf-8
import os
import os.path as osp
from sklearn.cluster import KMeans
import string
import numpy as np
import shutil

def kmeansCluster(galleryfeatpath):
    """"
    gallerypath:path of gallery feature
    return:cluster result  [clusterID,filename]
    """

    filesname=os.listdir(galleryfeatpath)
    labels=[]
    for filename in filesname:
        labels.append(filename.split("_")[0])
    D=dict([(i, labels.count(i)) for i in labels])
    clusterNum=len(D.items())

    featfiles=os.listdir(galleryfeatpath)
    feats=np.zeros((len(featfiles),1024))
    for i in range(len(featfiles)):
        f=open(osp.join(galleryfeatpath,featfiles[i]))
        line=f.readline()
        fts=line.split(" ")
        for j in range(len(fts)-1):
            feats[i][j]=float(fts[j])
        f.close()
    kmeans=KMeans(clusterNum,'k-means++',10,300,0.0001).fit(feats)
    return [kmeans,featfiles]

def savekmeansCluster(kmeans,featfiles):
    """"
    after compute Kmeans clustering
    save the result .
    """



featureRepo=osp.join(os.getcwd(),"orlrepo")
clusterRepo=osp.join(os.getcwd(),"clusterRepo")
faceRepo=osp.join(os.getcwd(),"faceRepo")
if not osp.exists(clusterRepo):
    os.mkdir(clusterRepo)

gafeats=os.listdir(featureRepo)


for gaf in gafeats:
    gapath=osp.join(featureRepo,gaf)
    [kmeans,featfiles] = kmeansCluster(gapath)
    clusterID = kmeans.labels_
    resultpath = osp.join(clusterRepo,gaf)
    if not osp.exists(resultpath):
        os.mkdir(resultpath)    #//clusterRepo/E2
    gafacepath=osp.join(faceRepo,gaf)
    for i in range(len(featfiles)):
        filename=featfiles[i].split(".")[0]
        facename=filename+".jpg"
        savepath  =osp.join(resultpath,str(clusterID[i]))
        if not osp.exists(savepath):
            os.mkdir(savepath)   #//clusterRepo/E2/12
        srcpath=osp.join(gafacepath,facename)
        dstpath=osp.join(savepath,facename)   #//clusterRepo/E2/12/2-3.jpg
        shutil.copy(srcpath,dstpath)




