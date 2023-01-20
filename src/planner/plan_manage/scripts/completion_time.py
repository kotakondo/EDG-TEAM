#!/usr/bin/env python  
# Kota Kondo

#  python collision_check.py

import bagpy
from bagpy import bagreader
import pandas as pd

import rosbag
import rospy
import math
import tf2_ros
import geometry_msgs.msg
import tf
import numpy as np
import matplotlib.pyplot as plt
import os
import glob
import statistics

if __name__ == '__main__':

    n_agents = 10

    cd_list = [0, 50, 100, 200, 300]

    for cd in cd_list:

        # this gives you 2d array, row gives you each sims data in corresponding dc
        box_plot_list = [] 

        home_dir = "/media/kota/T7/rmader_ral/edg_team"
        # home_dir = "/home/kota/data/edg_team"

        # source directory
        source_dir = home_dir+"/bags/cd"+str(cd)+"ms" # change the source dir accordingly #10 agents

        source_len = len(source_dir)
        source_bags = source_dir + "/*.bag" # change the source dir accordingly
        rosbag_list = glob.glob(source_bags)
        rosbag_list.sort() #alphabetically order
        rosbags = []

        for bag in rosbag_list:
            rosbags.append(bag)

        # read ros bags
        completion_time_per_sim_list = []
        for i in range(len(rosbags)):
            print('rosbag ' + str(rosbags[i]))
            start_time_initialized = False
            finish_time_initialized = False
            start_time = 0.0
            finish_time = 0.0
            for topic, msg, t in  rosbag.Bag(rosbags[i]).read_messages():
                if topic == '/drone_0_ego_planner_node/goal_point':
                    if not start_time_initialized:
                        start_time = t.secs + t.nsecs/1e9
                        print("start_time", start_time)
                        start_time_initialized = True
                    
                if topic == '/goal_reached':
                    if not finish_time_initialized:
                        finish_time = t.secs + t.nsecs/1e9
                        print("finish_time", finish_time)
                        finish_time_initialized = True

            completion_time = finish_time - start_time
            print("completion_time", completion_time)
            completion_time_per_sim_list.append(completion_time)

        os.system('echo "'+source_dir+'" >> '+home_dir+'/completion_time.txt')
        os.system('echo "ave is '+str(round(statistics.mean(completion_time_per_sim_list),2))+'s" >> '+home_dir+'/completion_time.txt')
        os.system('echo "max is '+str(round(max(completion_time_per_sim_list),2))+'s" >> '+home_dir+'/completion_time.txt')
        os.system('echo "min is '+str(round(min(completion_time_per_sim_list),2))+'s" >> '+home_dir+'/completion_time.txt')
        os.system('echo "------------------------------------------------------------" >> '+home_dir+'/completion_time.txt')