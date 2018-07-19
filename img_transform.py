#! /usr/bin/env python
# -*- coding: utf-8 -*-
import numpy as np

position_extra_unip_a = np.array([
    [[2,38],
     [7,49],
     [23,72],
     [32,78],
     [60,82],
     [70,78],
     [88,57],
     [91,46],
     [83,19],
     [76,12],
     [48,6],
     [37,10],
     [19,30],
     [19,41],
     [33,66],
     [43,70],
     [68,62],
     [75,53],
     [72,25],
     [63,20])

position_extra_unip_b = np.array([
    [1,44],
    [6,56],
    [28,81],
    [37,86],
    [73,85],
    [81,77],
    [93,47],
    [91,33],
    [68,7],
    [56,2],
    [23,3],
    [14,10],
    [10,35],
    [14,47],
    [35,70],
    [49,73],
    [73,56],
    [73,42],
    [54,18],
    [42,18]
])

def affine_transform(position_src,position_ref,src_size=256):
    #画像上の座標 = (縦,横)
    assert len(position_src) == len(position_ref),"different size of registration"
    assert len(position_src) >=3 ,"number of registration points should be more than 2"
    list_reg = np.arange(0,len(position_src),1)
    for n in range(20):
        if(position_src[n,0] < 0 or position_src[n,1] < 0 or position_src[n,0] >= src_size or position_src[n,1] > src_size):
            it = (np.where(list_reg == n))
            list_reg = np.delete(list_reg,it)
    assert len(list_reg) >=3 ,"number of registration points should be more than 2"
    position_X = position_src[list_reg,0]
    position_Y = position_src[list_reg,1]
    position_x = position_ref[list_reg,0]
    position_y = position_ref[list_reg,1]
    sig_X = np.sum(position_X)
    sig_Y = np.sum(position_Y)
    sig_XX = np.dot(position_X,position_X)
    sig_YY = np.dot(position_Y,position_Y)
    sig_x = np.sum(position_x)
    sig_y = np.sum(position_y)
    sig_xx = np.dot(position_x,position_x)
    sig_yy = np.dot(position_y,position_y)
    sig_xy = np.dot(position_x,position_y)
    sig_xX = np.dot(position_x,position_X)
    sig_yX = np.dot(position_y,position_X)
    sig_xY = np.dot(position_x,position_Y)
    sig_yY = np.dot(position_y,position_Y)
    sig = len(list_reg)
    af = np.array([[sig_xx,sig_xy,sig_x],
         [sig_xy,sig_yy,sig_y],
         [sig_x,sig_y,sig]
        ])
    bx = np.array([[sig_xX],[sig_yX],[sig_X]])
    by = np.array([[sig_xY],[sig_yY],[sig_Y]])
    coex = np.dot(np.linalg.inv(af),bx)
    coey = np.dot(np.linalg.inv(af),by)
    affine_t = np.array([[coex[0][0],coex[1][0],coex[2][0]],[coey[0][0],coey[1][0],coey[2][0]],[0,0,1]])
    return affine_t

def affine_opt_ext(position_opt,img_size = 256):
    return 0
