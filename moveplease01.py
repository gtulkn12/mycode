#!/usr/bin/env python3
import shutil
import os

#created a default path
os.chdir('/home/student/mycode/')

#moved obj to ceph_storage
shutil.move('raynor.obj', 'ceph_storage/')

#delcared xname user input
xname = input('What is the new name for kerrigan.obj? ')

#renamed kerrigan file name to xname
shutil.move('ceph_storage/kerrigan.obj', 'ceph_storage/' + xname)

