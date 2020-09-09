# Create the smaller cutouts of the M33 CO and HI cubes to host and
# be available for download online for the tutorials.


from spectral_cube import SpectralCube
from pathlib import Path

workingdir = Path("/home/ekoch/ownCloud/Data/M33/ALMA/")

cube = SpectralCube.read(workingdir / "Brick1Tile1_12CO21_0p7kms.image.pbcor_K.fits")

y, x = 145, 340

size = 32

cube_cutout = cube[:, y-size:y+size, x-size:x+size]

cube_cutout.write("M33_Brick1Tile1_12CO21_0p7kms.image.pbcor_K.cutout.fits", overwrite=True)
