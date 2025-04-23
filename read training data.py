# -*- coding: utf-8 -*-
"""
Created on Mon Apr 14 07:29:21 2025

@author: moaks
"""

import h5py
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import open3d as o3d

# Open the .h5 file
with h5py.File(r"C:\Users\moaks\OneDrive\Documents\Bitbucket\MVP_Benchmark\completion\log\vrcnet_cd_debug_2025-04-21_23-00-07\results.h5", 'r') as f:
    # List all groups
    keys = list(f.keys())
    print("Top-level keys:", keys)
    # Loop through keys and get data
    
    results = f['results'][:]
    # complete_pcds = f['complete_pcds'][:]   # Shape: (N, H, W, C)
    # datasets_ids = f['datasets_ids'][:]   # Shape: (N,)
    # incomplete_pcds = f['incomplete_pcds'][:]   # Shape: (N, H, W, C)
    # labels = f['labels'][:]   # Shape: (N,)
    # number_per_class = f['number_per_class'][:] 
    
    
    # for key in keys:
    #     data = f[key][:]
    #     print(f"Key: {key}, Data shape: {data.shape}, Data type: {data.dtype}")
    




# Open the .h5 file
with h5py.File(r"C:\Users\moaks\OneDrive\Documents\Bitbucket\MVP_Benchmark\completion\data\Spine\dataset_verse_test_complete_pipeline.h5", 'r') as f:
    # List all groups
    keys = list(f.keys())
    print("Top-level keys:", keys)
    # Loop through keys and get data
    
    incomplete_pcds = f['incomplete_pcds'][:]
    complete_pcds = f['complete_pcds'][:]   # Shape: (N, H, W, C)
    # datasets_ids = f['datasets_ids'][:]   # Shape: (N,)
    # incomplete_pcds = f['incomplete_pcds'][:]   # Shape: (N, H, W, C)
    labels = f['labels'][:]   # Shape: (N,)
    # number_per_class = f['number_per_class'][:] 
    
    
    # for key in keys:
    #     data = f[key][:]
    #     print(f"Key: {key}, Data shape: {data.shape}, Data type: {data.dtype}")







incomplete_points = incomplete_pcds[0] 
complete_points = complete_pcds[0] 
resultPoints = results[0]    




inc_pcd = o3d.geometry.PointCloud()
inc_pcd.points = o3d.utility.Vector3dVector(incomplete_points)
inc_pcd.paint_uniform_color([1, 0, 0])  # red

c_pcd = o3d.geometry.PointCloud()
c_pcd.points = o3d.utility.Vector3dVector(complete_points)
c_pcd.paint_uniform_color([0, 0, 1])  # red



res_pcd = o3d.geometry.PointCloud()
res_pcd.points = o3d.utility.Vector3dVector(resultPoints)
res_pcd.paint_uniform_color([0, 1, 0])  # green

o3d.visualization.draw_geometries([inc_pcd, c_pcd, res_pcd])


# fig = plt.figure()
# ax = fig.add_subplot(111, projection='3d')
# ax.scatter(points[:, 0], points[:, 1], points[:, 2], s=1, c='b')
# ax.scatter(incomplete_points[:, 0], incomplete_points[:, 1], incomplete_points[:, 2], s=1, c='r')

# ax.set_xlabel('X')
# ax.set_ylabel('Y')
# ax.set_zlabel('Z')
# plt.title("3D Point Cloud")
# plt.show()