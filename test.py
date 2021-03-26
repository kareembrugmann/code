#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 24 10:11:28 2021

@author: user
"""



import os
from osgeo import gdal
import glob
import subprocess
import shlex

#set working directory 
wrkdir = "/home/user/scripts/testphotos"
#change to working direcotry 
os.chdir(wrkdir)
# run to allow gdalwarp to run with out error # set to location where 'proj' exists
if 'PROJ_LIB' not in os.environ: os.environ['PROJ_LIB'] = '/home/user/miniconda3/share/proj'
#Proj4 string for image to be projected in 
prj4 = "+proj=lcc +lat_1=49 +lat_2=77 +lat_0=40 +lon_0=-100 +x_0=0 +y_0=0 +ellps=clrk66 +units=m +no_defs"
# 
gtiffDriver = gdal.GetDriverByName( 'GTiff' )


# next steep try with multipl files     

def reproject(proj4string):
    '''
    

    Parameters
    ----------
    proj4string : set of parameter identify an area/projection
    a proj4string that was previously put in variable is used to change projection
    Returns
    -------
    fileneame.reprojected.tif
        DESCRIPTION
        newly reprojected image identifed by new name.


    '''
    #find images ending in .tif in directory
    imgs = glob.glob('*.tif')
    for img in imgs: 
    #choose from list of img which to reproject
        img = imgs[0]
    #assign image
        basename = img[:-0]
    # set input to projection to 
    reprojected = proj4string
    #allow user to run at command line
    #for error:FileNotFoundError: [Errno 2] No such file or directory: 'gdalwarp'
 #find out where the gdal utilities are found on your system and add that path to the command line:
   # I.E /home/user/miniconda3/bin
    reprojectioncmd = '/home/user/miniconda3/bin/gdalwarp -t_srs "'+ reprojected +'" -r cubicspline '+img+" "+basename + '.reprojected.tif'
    command = shlex.split(reprojectioncmd)
    result = subprocess.run(command, capture_output=True, text=True)
    print(result.stdout)
    print(result.stderr)
    return print("reprojection completed")
    
 #########trying to run in loop#####
reproject(prj4)








######first att####
imgs = glob.glob('*.tif')
for img in imgs: 
    img = imgs[0]
    basename = img[:-0]

    cmd = '/home/user/miniconda3/bin/gdalwarp -t_srs "'+prj4+'" -r cubicspline '+img+" "+basename + 'reprojected23.tif'
    command = shlex.split(cmd)
    result = subprocess.run(command, capture_output=True, text=True)
    print(result.stdout)
    print(result.stderr)
    print("Done reprojection")
######

    def reproject(proj4string):
    #find # images in folder
        imgs = glob.glob('*.tif')
        for img in imgs: 
        #choose img
            img = imgs[2]
    #assign image
        basename = img[:-2]
    # set input to projection to 
        reprojected = proj4string
        cmd = '/home/user/miniconda3/bin/gdalwarp -t_srs "'+ reprojected +'" -r cubicspline '+img+" "+basename + 'reprojected.tif'
        command = shlex.split(cmd)
        result = subprocess.run(command, capture_output=True, text=True)
        print(result.stdout)
        print(result.stderr)
        return print("reprojection completed")
    









