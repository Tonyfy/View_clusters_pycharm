#coding: utf-8

import os
import string
import sys
import re


print "**************by RI value**********************"
print "RI=(TP+TN)/(TP+FP+FN+TN)"
print "TP 应该聚在一类的两个样本被正确地放在一起了"
print "TN 不该聚在一类的两个样本被正确地分开了"
print "FP 不该聚在一类的两个样本被错误地放在一起了"
print "FN 应该聚在一类的两个样本被错误地分开了"
print "**************by F value************"
print "准确率P =TP/(TP+FP)\n召回率R =TP/(TP+FN)"
print "F=(beta^2+1)PR/(beta^2*P+R)"
print "beta<<1,表示更加看重准确率，即看重分对；beta>>1表示看重分全(召回率)"
def calClassFolders(path):
    "cal the class in this dir"
    print "we are statis"+path
    class_count=0      #当前产生了多少个类别
    image_count=0      #当前总共有多少个人脸参与聚类
    imgcube=[]
    classname=[]
    for folder in os.listdir(path):
        classname.append(folder)
        class_count=class_count+1
        imgs=os.listdir(os.path.join(path,folder))
        imgcube.append(imgs)

    for root,dirs,files in os.walk(path):
        for img in files:
             image_count=image_count+1

    print "总共有 %d张人脸\n总计产生 %d个类别\n"%(image_count,class_count)

    TP=0
    TN=0
    FP=0
    FN=0
    clsid=0
    for cla in imgcube:
        len_of_the_cla=len(cla)
        if len_of_the_cla>1:
            TPi=0
            FPi=0
            for i in range(len_of_the_cla):
                #idi=cla[i].split('-')[0]
                idi=re.split(r'-|_',cla[i])[0]
                for j in range(i+1,len_of_the_cla):
                    #idj=cla[j].split('-')[0]
                    idj=re.split(r'-|_',cla[j])[0]
                    if idi==idj:
                        TP=TP+1
                        TPi=TPi+1
                    else:
                        FP=FP+1
                        FPi=FPi+1
            if (len(classname[clsid].split('---TP~')) < 2):
                # print "has been calculated"
                modclassname = classname[clsid] + "---TP~" + str(TPi) + "---FP~" + str(FPi)
            else:
                modclassname = classname[clsid]
            os.rename(os.path.join(path,classname[clsid]),os.path.join(path,modclassname))
        clsid=clsid+1

    len_of_cube=len(imgcube)
    for m in range(len_of_cube):
        cla_m=imgcube[m]
        len_of_cla_m=len(cla_m)
        for n in range(m+1,len_of_cube):
            cla_n=imgcube[n]
            len_of_cla_n=len(cla_n)
            for i in range(len_of_cla_m):
                #idi=cla_m[i].split('-')[0]
                idi=re.split(r'-|_',cla_m[i])[0]
                for j in range(len_of_cla_n):
                     #idj=cla_n[j].split('-')[0]
                     idj=re.split(r'-|_',cla_n[j])[0]
                     if idi==idj:
                        FN=FN+1
                     else:
                         TN=TN+1

    print "TP = %d\nTN = %d\nFP = %d\nFN = %d\n" % (TP, TN, FP, FN)

    print "RI=(TP+TN)/(TP+FP+FN+TN) = %.02f\n\n" % (float(TP + TN) / float(TP + FP + FN + TN + 0.001))

    print "**************by F value************"
    print "准确率P =TP/(TP+FP)\n召回率R =TP/(TP+FN)"
    print "F1 值 = P*R/(P+R)"
    print "F=(beta^2+1)PR/(beta^2*P+R)"
    print "beta<<1,表示更加看重准确率，即看重分对；beta>>1表示看重分全(召回率)"

    beta = 0.5
    print "beta = %.02f\n分对和分全的权值比为 1:%0.2f\n" % (float(beta), float(beta * beta))

    P = float(TP) / (TP + FP + 0.001)
    R = float(TP) / (TP + FN + 0.001)
    print "P = %.02f" % (P)
    print "R = %.02f" % (R)
    F_beta = float(beta * beta + 1) * P * R / (beta * beta * P + R + 0.001)
    print "F = %.02f" % (F_beta)
    F1=2*P * R / (P + R + 0.000000001)
    print "F1 = %.02f" % (F1)
    print "**************end*****************"
    return [P,R,F1]

clusterRepo=os.path.join(os.getcwd(),"secClustRepo")   #clusterRepo path secClustRepo clusterCFSRepo
gallerys = os.listdir(clusterRepo)
Ps=[]
Rs=[]
F1s=[]
result=open("clusterResult.txt","wb")

for Ei in gallerys:
    Eipath = os.path.join(clusterRepo,Ei)
    [P,R,F1]=calClassFolders(Eipath)
    Ps.append(P)
    Rs.append(R)
    F1s.append(F1)
    line=str(("%.3f"%P))+"  "+str(("%.3f"%R))+"  "+str(("%.3f"%F1))+"\n"
    result.writelines(line)
result.close()