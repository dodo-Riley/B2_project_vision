# -*- coding: utf-8 -*-
"""
Created on Wed Mar 16 17:38:38 2022

@author: rkdtk
"""

import os
import glob

# 경로 수정할 
s_path = './*s*.*'

for f in glob.glob(s_path):
    os.remove(f)
