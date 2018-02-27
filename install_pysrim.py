### PYSRIM : Python wrapper for SRIM calculation
### Project initiated by : Christopher Ostrouchov
### Modified by : Victor Garric : victor.garric@cea.fr, 2018

### Cette instalation requier l'installation préalable de wine et xvfb
### Si ce n'est pas fait contactez votre administrateur pour execution de la commande :
### sudo apt-get install wine xvfb

### INSTALLATION DE SRIM et PYSRIM

import os
origin=os.getcwd()

print("*** Installation locale de PySrim ***")
print("***\t\t Téléchargement de SRIM ***")
os.system('wget -O ~/SRIM.exe http://srim.org/SRIM/SRIM-2013-Std.e')
print("***\t\t Extraction de SRIM ***")
os.chdir(os.path.expanduser('~/'))
os.system('unzip SRIM.exe -d ~/SRIM')

print("***\t\t Configuration du coeur WINE pour SRIM (1/2) ***")
os.system('WINEARCH=win32 WINEPREFIX=~/.wine wine wineboot')

print("***\t\t Configuration du coeur WINE pour SRIM (2/2) ***")
os.chdir(os.path.expanduser('~/SRIM/SRIM-Setup'))
os.system("wine 'MSVBvm50.exe'")
os.system("wine regsvr32 ComCtl32.ocx")
os.system("wine regsvr32 ComDlg32.ocx")
os.system("wine regsvr32 MSFlxGrd.ocx")
os.system("wine regsvr32 RichTx32.ocx")
os.system("wine regsvr32 TabCtl32.ocx")

print("***\t\t Installation de PySRIM (1/2) ***")
os.chdir(origin+'/Source')
os.system("pip3 install --user .")
print("***\t\t Installation de PySRIM (2/2) ***")
os.system("pip3 install --user seaborn pandas matplotlib docopt numpy")

print("*** Installation Terminée ***")
