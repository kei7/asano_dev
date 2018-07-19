#! /usr/bin/env python
# -*- coding: utf-8 -*-
import numpy as np

def time_range_f(time,time_range,frame_start,frame_end):
    if(time <= time_range+frame_start):
        time_low = frame_start
        time_high = 2*time_range+frame_start
    elif(time >= frame_end -time_range):
        time_low = frame_end - 2*time_range
        time_high = frame_end
    else:
        time_low = time - time_range
        time_high = time + time_range
    return [time_low,time_high]

#2段階検出8
def excitation_vmem(vmem_wave,t_range = 200,high_thr = 0.65,low_thr = 0.35,detect_diff = 30):
    #検出用定数
    zero_thr = 0.5
    #detc_diff = 110
    list = []
    for n in range(vmem_waves.shape[1]):
        trig = 0
        active_time = np.array([0])
        for t in range(1,vmem_waves.shape[0]):
            [T_l,T_h] = time_range_f(t,t_range,fr_start,fr_end)
            if (trig == 0 or trig[n,0] == 1):
                if (vmem_waves[t-1,n] >= low_thr*(np.max(vmem_waves[T_l:T_h,n])-np.min(vmem_waves[T_l:T_h,n]))+np.min(vmem_waves[T_l:T_h,n]) and vmem_waves[t,n] <= low_thr*(np.max(vmem_waves[T_l:T_h,n])-np.min(vmem_waves[T_l:T_h,n]))+np.min(vmem_waves[T_l:T_h,n])):
                    trig = -1
                    #if(n == 3):
                    #    print([n+1,t,-1])
            elif (trig == 0 or trig[n,0] == -1):
                if (vmem_waves[t-1,n] <= high_thr*(np.max(vmem_waves[T_l:T_h,n])-np.min(vmem_waves[T_l:T_h,n]))+np.min(vmem_waves[T_l:T_h,n]) and vmem_waves[t,n] >= high_thr*(np.max(vmem_waves[T_l:T_h,n])-np.min(vmem_waves[T_l:T_h,n]))+np.min(vmem_waves[T_l:T_h,n])):
                    trig[n,0] = 1
            if (active_time[-1] +detect_diff < t and (trig == -1)):
                if (vmem_waves[t-1,n] <= zero_thr*(np.max(vmem_waves[T_l:T_h,n])-np.min(vmem_waves[T_l:T_h,n]))+np.min(vmem_waves[T_l:T_h,n]) and vmem_waves[t,n] >= zero_thr*(np.max(vmem_waves[T_l:T_h,n])-np.min(vmem_waves[T_l:T_h,n])) +np.min(vmem_waves[T_l:T_h,n])):
                    #np.vstack((opt_time_rise[n],t))
                    active_time.append(t)
        active_time[0,0] = n+1
        list.append(active_time)
    return list
