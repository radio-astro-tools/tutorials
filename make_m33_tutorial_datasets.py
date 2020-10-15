# Create the smaller cutouts of the M33 CO and HI cubes to host and
# be available for download online for the tutorials.


import astropy.units as u
from spectral_cube import SpectralCube
from pathlib import Path

# When running, change to the location of the data for `workingdir_co` and `workingdir_hi`
# e.g.,
# outputdir = Path("/home/ekoch/ownCloud/code_development/radio_astro_tools/")
# workingdir_co = Path("/home/ekoch/ownCloud/Data/M33/ALMA/")
# workingdir_hi = Path("/home/ekoch/storage/M33/HI/17B-162/")

# By default, the current directory is used.

outputdir = Path(".")

workingdir_co = Path(".")

workingdir_hi = Path(".")

# Cut region from the CO(2-1) data cube.

cube = SpectralCube.read(workingdir_co / "Brick1Tile1_12CO21_0p7kms.image.pbcor_K.fits")

y, x = 145, 340

size = 32

cube_cutout = cube[:, y-size:y+size, x-size:x+size]

cube_cutout.write(outputdir / "M33_ALMA_ACA_12CO21.cutout.fits", overwrite=True)

# Cutout a similar region from the HI B+C-config cube.

hi_cube = SpectralCube.read(workingdir_hi / "M33_14B_17B_HI_contsub_width_1kms.image.pbcor.GBT_feathered.fits", use_dask=True)

hi_cube_cutout = hi_cube.subcube(xlo=cube_cutout.longitude_extrema[1],
                                 xhi=cube_cutout.longitude_extrema[0],
                                 ylo=cube_cutout.latitude_extrema[0],
                                 yhi=cube_cutout.latitude_extrema[1])

# Convert to K
hi_cube_cutout = hi_cube_cutout.to(u.K)

hi_cube_cutout.write(outputdir / "M33_VLA_BCconfig_wGBT_HI.cutout.fits", overwrite=True)
