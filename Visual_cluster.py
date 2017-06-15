#coding:utf-8
import os
import os.path as osp
import re
import cv2
import math
import numpy as np

def visual_one_gallery(galleryPath,output_gallery_path):
    """"
    input:gallery path,which include many directories(clusters)
    output:an directories include many Visual_cluster_imgs.
    """
    cluster_name=os.listdir(galleryPath)
    for clster in cluster_name:
        cluster_path=osp.join(galleryPath,clster)
        imgs=os.listdir(cluster_path)

        imgs_num=len(imgs)
        paint_W=int(math.ceil(math.sqrt(imgs_num)))
        paint = np.ones((112*paint_W,96*paint_W,3),np.uint8)
        paint = np.multiply(paint,188)
        for i in range(paint_W):
            for j in range(paint_W):
                if i*paint_W+j<imgs_num:
                    im_path=osp.join(cluster_path,imgs[i*paint_W+j])
                    img=cv2.imread(im_path)
                    img=cv2.resize(img,(96,112))
                    paint[i*112:(i+1)*112,j*96:(j+1)*96,:]=img.copy()

       # cv2.imshow("paint",paint)
        #cv2.waitKey(0)
        visual_name=clster+".jpg"
        savePath=osp.join(output_gallery_path,visual_name)
        cv2.imwrite(savePath,paint)

root = r'F:\fandy\hack\face\ARecog\example\test\secClustRepo'
outputroot=r'./Visual_gallerys'
if not osp.exists(outputroot):
    os.mkdir(outputroot)
galls=os.listdir(root)
for gal in galls:
    gall_repo_out=osp.join(outputroot,gal)
    if not osp.exists(gall_repo_out):
        os.mkdir(gall_repo_out)
    visual_one_gallery(osp.join(root,gal),gall_repo_out)



