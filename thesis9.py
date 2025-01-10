#IMPORT LIBRARIES
from astropy.io import fits
import matplotlib.pyplot as plt
import  os
import pandas as pd
import glob


# Open a FITS file whole folder
#for 41 -45
dr=r'E:\DATA\data\data9'
Fits_file9 = glob.glob(os.path.join(dr, '*.fits'))





#for spectral lines
# from https://classic.sdss.org/dr6/algorithms/linestable.php
spectraE = {
    # 1033.82: "O VI",
    # 1215.24: "Lyα",
    # 1240.81: "N V",
    # 1305.53: "O I",
    # 1335.31: "C II",
    # 1397.61: "Si IV",
    # 1399.8: "Si IV + O IV",
    # 1549.48: "C IV",
    # 1640.4: "He II",
    # 1665.85: "O III",
    # 1857.4: "Al III",
    # 1908.734: "C III",
    # 2326.0: "C II",
    # 2439.5: "Ne IV",
    # 2799.117: "Mg II",
    3346.79: "Ne V",
    3426.85: "Ne VI",
    3727.092: "O II",
    3729.875: "O II",
    3889.0: "He I",
    4072.3: "S II",
    4102.89: "Hδ",
    4341.68: "Hγ",
    4364.436: "O III",
    4862.68: "Hβ",
    4932.603: "O III",
    4960.295: "O III",
    5008.240: "O III",
    6302.046: "O I",
    6365.536: "O I",
    6529.03: "N I",
    6549.86: "N II",
    6564.61: "Hα",
    6585.27: "N II",
    6718.29: "S II",
    6732.67: "S II",
    }
spectraA={3934.777: "K",
    3969.588: "H",
    4305.61: "G",
    5176.7: "Mg",
    5895.6: "Na",
    8500.36: "Ca II",
    8544.44: "Ca II",
    8664.52: "Ca II"}

# Create a DataFrame from the dictionary
dfE = pd.DataFrame(list(spectraE.items()), columns=['Wavelength (Å)', 'Spectral Line'])
dfA = pd.DataFrame(list(spectraA.items()), columns=['Wavelength (Å)', 'Spectral Line'])

# Display the DataFrame
print("The emission lines wavelength are : \n",dfE)
print("The absorption lines wavelength are : \n",dfA)
plt.figure(figsize=(10,6))

for a in Fits_file9 :
#Access the data in the primary HDU (Header Data Unit)
#Hdu.open work in single so put in for loop and use x
#SDSS is usually in first ,second and zero extension
    hdulist=fits.open(a)
    header=hdulist[0].header
    data=hdulist[0].data
    data1 = hdulist[1].data
    data2=hdulist[2].data
    flux=data1['flux']
    loglam=data1['loglam']
    wavelength=10**loglam
    rs = data2['z']
    RA=header.get('RA')
    DEC=header.get('DEC')
    print('THE RA,DEC,Z OF',os.path.basename(a),':')
    print(f"The value of z  \n ",rs)
    print(f"The value of right ascension  \n ", RA)
    print(f"The value of Declination  \n ", DEC)
    print('\n')
    plt.plot(wavelength,flux,drawstyle='steps-mid',label=a.split('\\')[-1])#label=x.split('\\')[-1]) is because it only contain file name
    hdulist.close()
#for spectral lines
for wavelength,Line_name in spectraE.items():#because having multiple elements therefor use loop
    plt.axvline(x=wavelength,linestyle='--',color='r')
    plt.text(wavelength, 0.5, Line_name, rotation=90, fontsize=8,
             verticalalignment='center', horizontalalignment='right', alpha=0.7)
for wavelength,Line_name in spectraA.items():
    plt.axvline(x=wavelength,linestyle='--',color='blue')
    plt.text(wavelength, 0.5, Line_name, rotation=90, fontsize=8,
             verticalalignment='center', horizontalalignment='right', alpha=0.7)



#plot setting
plt.title("SPECTROGRAPH")

# plt.text(0, 0, "Blue lines are for absorption and red lines are for emission",
#          fontsize=12, color='black', transform=plt.gca().transAxes)# x=0.5,y=0.1,fontsize=10,This ensures the text is positioned relative to the axes, not the data coordinates.
plt.legend(title="fits files")
plt.xlabel('Wavelength(A)')
plt.ylabel('Flux (10-17 erg/cm2/s/A)')
plt.grid(True)
plt.legend()
plt.show()
