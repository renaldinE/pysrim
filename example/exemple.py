# -*- coding: utf-8 -*-
###Importation
from srim.core.target import Target
from srim.core.layer import Layer
from srim.core.ion import Ion
from srim.routine import *
import os
### Param�tres globaux :
    #G�n�raux
calculation= 1 #1 pour rapide, 2 pour full cascade
num_ions = 1e2 #nombre d'ions
subbing = True #Si True, pas d'affichage obligatoire pour le batch

    #Sur les dossiers d'enregistrement et de SRIM
save_directory=None #Si None --> dossier de lecture
SRIM_dir=os.path.expanduser('~/SRIM') #Dossier SRIM


### D�finition des ions
ions = {'identifier': 'He', 'energy': 1e3} # �nergie en eV

step=20000
steps=[(i,i+step) for i in range(0,100000,step)]

### D�finition des couches
layer1 = Layer({
    'Zr': {
        'stoich': 0.34, #Stoechiom�trie
        'E_d': 20.0, # Energie de d�placement
        'lattice': 0.0, #Energie de liaison
        'surface': 3.0,  #Energie de surface
        'unique_name': 'ZrOxyde' #Nom unique OBLIGATOIRE au d�sir de l'utilsateur
    },
    'O': {
        'stoich': 0.66,
        'E_d': 60.0, 
        'lattice': 0.0,
        'surface': 3.0,
        'unique_name': 'OOxyde'
    }
}, density=5.68, width=64000.0, name='Oxyde') #densit�, largeur en angstroms et nom

layer2 = Layer({
    'Zr': {
        'stoich': 1.0, 
        'E_d': 25.0, 
        'lattice': 3.0, 
        'surface': 3.30,  
        'unique_name': 'ZrMetal'
    },
}, density=6.52, width=36000.0, name='Metal') 

target = Target([layer1,layer2]) #reconstitution du mat�riaux

auto_steps(ions,target,num_ions,calculation,save_directory,SRIM_dir,subbing,steps)
merge_results()
