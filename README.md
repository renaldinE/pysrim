# PySrim

PySrim is a code written in python to simulate via Monte Carlo ion treveling through a target. The ions are stopped through the collisions of ions with the nucleus of an atom within the material and excitation of the electron clouds of each atom.

# About this fork

## Introduction

This fork is a modified version of the original code of pysrim. This version in only intended to work on a unix machine. The use of a linux machine allow you to get rid of one main disadvanage : as SRIM is poorly written in visual basic, the simple display of the calculation window, even without any plot, slow down the calculation.
In order to speed up calculations, this forked pysrim warp the display using the "xvfb-run" command. All the display tasks are hidden and the calculation only is running.

## Benchmarking

Assessing the speed up, we choose to launch two calculations on the same machine (10k Ne ions in a 10 micrometers zircone layer using a range of energy from 1 to 20 MeV with a step of 1 MeV, full cascade calculation) : dummy screen method is, on average, 48% faster than windows based calculation.

## New in this fork

Added from usual pysrim and largely inspired example files from the original author, "routine" functions have been added :
* run_calculation : a modified import from the original example files of the author
* auto_ions : a function that run many calculations based on a list of ions
* auto_steps : a function that run one calculation where the layer is divided in many plot to increase spatial resolution
* merge_results : a function to merge the "RANGE" and "VACANCY" files from a stepped calculation
* unique_name and multilayers and elements : using a unique_name variable for each element allow you to create multiple layers with the same element in different states

# Installation

## Unix Dependencies

* wine
* xvfb

## Python Dependencies
* docopt
* matplotlib
* numpy
* pandas
* mpi4py

## Installation (1/2) : Unix requirements

If you don't have `wine` and `xvfb` installed use :

<pre> sudo apt-get install wine xvfb </pre>

## Installation (2/2) : Set up and install everything

All the other requirements are included in the `install_pysrim.py` file. Simply run :
<pre>python3 install_pysrim.py</pre>
Sorry the display is in french ! Will fix that soon !
If your unix version doesn't use python 2 and 3 at the same time, change  `pip3` for `pip` in the installation file.

# Known issues and future developments

* Bha ! Displays are mostly in french and so example file is
