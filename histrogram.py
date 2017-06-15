#coding:utf-8


import os
import os.path as osp
import matplotlib.pyplot as plt
import sys
import string
import re
import numpy as np

def getGalleryInfo(gpath):
    """ print "人脸总数 ： "+str(len(filesname))
        print "人物总数 ： "+str(len(D.items()))
        print "高频人物总数 ： "+str(Hc)
    """
    filesname=os.listdir(gpath)
    high_ferq_num =int(len(filesname)*0.02)

    labels=[]
    for filename in filesname:
        labeltmp=re.split(r'-|_',filename)[0];
        labels.append(labeltmp.split("s")[-1])

    D=dict([(i, labels.count(i)) for i in labels])
    L=[]
    C=[]
    Hc=0
    for item in D.items():
        L.append(int(item[0]))
        C.append(int(item[1]))
        if int(item[1])>high_ferq_num:
            Hc+=1
  #  plt.scatter(L,C)
    print "人脸总数 ： "+str(len(filesname))
    print "人物总数 ： "+str(len(D.items()))
    print "高频人物总数 ： "+str(Hc)
    return [L,C,Hc]

root = r'F:\fandy\hack\face\ARecog\example\test'
gallerRepo=osp.join(root,"faceRepo")
galleryname=os.listdir(gallerRepo)
plt.figure(1)
seq=1
for gname in galleryname:
    print "processing "+gname
    [L, C, Hc]=getGalleryInfo(osp.join(gallerRepo,gname))
    plt.subplot(2,4,seq)
    plt.yticks(np.linspace(1,max(C),5))
    plt.scatter(L,C,linewidths=1)
    plt.title(gname)

    seq+=1
plt.show()
