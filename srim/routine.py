### PYSRIM : Python wrapper for SRIM calculation
### Project initiated by : Christopher Ostrouchov
### Modified by : Victor Garric : victor.garric@gmail.com, 2018

import os
from collections import Counter
from itertools import count
from scipy.stats import gaussian_kde
from random import randint
from scipy.stats import gaussian_kde
from .srim import SRIM
from .core.target import Target
from .core.layer import Layer
from .core.ion import Ion
from .core.element import Element
from .output import (
    Results, Phonons, Ioniz, Vacancy, 
    NoVacancy, EnergyToRecoils, Range,
    Collision
)
from pathlib import Path
import datetime
import sys

def run_calculation(ion, target, num_ions, calculation=2, save_directory=None, SRIM_dir='~/SRIM', subbing=False, plot_limits=None, angle_ions=0):
    print('\t%s\t%s\t%s\t\t%d\t\t%s\t\t%s' % (datetime.datetime.now().strftime('%d-%m-%Y %H:%M:%S'), ion.symbol, ion.energy,num_ions,plot_limits,angle_ions))
    if plot_limits==None :
        srim = SRIM(target, ion, number_ions=num_ions, calculation=calculation, collisions=2, random_seed=randint(0, 100000),angle_ions=angle_ions)
    else :
        srim = SRIM(target, ion, number_ions=num_ions, calculation=calculation, collisions=2, random_seed=randint(0, 100000),plot_xmin=plot_limits[0],plot_xmax=plot_limits[1],angle_ions=angle_ions)
    results = srim.run(SRIM_dir,subbing=subbing)
    if save_directory==None :
        save_directory = os.getcwd()
    local_dir=os.path.join(save_directory,('%s-%s-%s'%(ion.symbol,ion.energy,str(plot_limits[0])+'-'+str(plot_limits[1]))))
    os.makedirs(local_dir, exist_ok=True)
    SRIM.copy_output_files(SRIM_dir, local_dir)
    print('\t%s\t\t Results saved to %s' % (datetime.datetime.now().strftime('%d-%m-%Y %H:%M:%S'),local_dir))


def auto_steps(ions,target,num_ions,calculation,save_directory,SRIM_dir,subbing,steps,angle_ions):
    print('*** Automated SRIM on Python : Starting ***')
    print('\n')
    print('\t%s\t\t\t%s\t%s\t%s\t%s\t\t%s' % ('Date','Symbole', 'Energie (eV)','Ions calculés','Step','Angle'))
    for step in steps :
        run_calculation(Ion(**ions), target, num_ions, calculation=calculation, save_directory=save_directory, SRIM_dir=SRIM_dir, subbing=subbing, plot_limits=step, angle_ions=angle_ions)
    print('*** Automated SRIM on Python : End ***')

def auto_ions(ions,target,num_ions,calculation,save_directory,SRIM_dir,subbing,steps,angle_ions):
    print('*** Automated SRIM on Python : Starting ***')
    print('\n')
    print('\t%s\t\t\t%s\t%s\t%s\t%s\t\t%s' % ('Date','Symbole', 'Energie (eV)','Ions calculés','Step','Angle'))
    for ion in ions :
        run_calculation(Ion(**ion), target, num_ions, calculation=calculation, save_directory=save_directory, SRIM_dir=SRIM_dir, subbing=subbing, angle_ions=angle_ions)
    print('*** Automated SRIM on Python : End ***')

def auto_angle(ions, target, num_ions, calculation, save_directory, SRIM_dir, subbing, steps, angle_ions):
    print('*** Automated SRIM on Python : Starting ***')
    print('\n')
    print('\t%s\t\t\t%s\t%s\t%s\t%s\t\t%s' % ('Date', 'Symbole', 'Energie (eV)', 'Ions calculés', 'Step', 'Angle'))
    for angle in angle_ions:
        run_calculation(Ion(**ions), target, num_ions, calculation=calculation, save_directory=save_directory,
                        SRIM_dir=SRIM_dir, subbing=subbing, angle_ions=angle_ions)
    print('*** Automated SRIM on Python : End ***')

def merge_results() :
    dirs=[x[0] for x in os.walk(os.getcwd())]
    dirs.pop(0)
    for item in dirs :
        if item.endswith('__pycache__') :
            dirs.remove(item)
    
    dirs.sort()
    total_range=''
    total_vacancy=''
    
    for directory in dirs :
        local_range=open(directory+'/RANGE.txt','r').readlines()
        local_vacancy=open(directory+'/VACANCY.txt','r').readlines()
        for line in local_range :
            if line.startswith('-----------  ') :
                range_start=local_range.index(line)+1
        range_end=len(local_range)
        for line in local_vacancy :
            if line.startswith('-----------  ') :
                vacancy_start=local_vacancy.index(line)+1
        vacancy_end=len(local_vacancy)-1

        for i in range(range_start,range_end) :
            total_range+=(local_range[i])
        for i in range(vacancy_start,vacancy_end) :
            total_vacancy+=(local_vacancy[i])
    
    file_range=open('total_range.txt','w')
    file_range.write(total_range)
    file_range.close()
    
    file_vacancy=open('total_vacancy.txt','w')
    file_vacancy.write(total_vacancy)
    file_vacancy.close()
