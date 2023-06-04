# -*- coding: utf-8 -*-
"""
Created on Sat Nov 14 08:51:10 2022
@author: Yueru Wen
"""

import numpy as np
from scipy.interpolate import RegularGridInterpolator
import pickle
  
fo = open('FY4A-LUT-band3.npy','rb')
dem=pickle.load(fo) 
soz=pickle.load(fo) 
saz=pickle.load(fo) 
aod=pickle.load(fo) 
wv=pickle.load(fo) 
o3=pickle.load(fo) 
raa=pickle.load(fo) 
x1a=pickle.load(fo) 
x1b=pickle.load(fo)
x1c=pickle.load(fo) 
fo.close()

rg1a = RegularGridInterpolator((dem, soz, saz,aod,wv,o3,raa), x1a,method='linear', bounds_error=False, fill_value=np.nan)
rg1b = RegularGridInterpolator((dem, soz, saz,aod,wv,o3,raa), x1b,method='linear', bounds_error=False, fill_value=np.nan)
rg1c = RegularGridInterpolator((dem, soz, saz,aod,wv,o3,raa), x1c,method='linear', bounds_error=False, fill_value=np.nan)         

xa=rg1a([0, 30, 40, 0.1, 3.0, 0.25, 60.])
xb=rg1b([0, 30, 40, 0.1, 3.0, 0.25, 60.])
xc=rg1c([0, 30, 40, 0.1, 3.0, 0.25, 60.])

print(xa,xb,xc)
