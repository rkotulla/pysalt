
import pysalt
import os, sys
from astropy.io import fits

def get_data_filename(filepart):

    if (filepart.find("pysalt$") >= 0):
        # This is most likely the old IRAF style format
        #print "This is IRAF style"
        return filepart.replace("pysalt$", pysalt.__path__[0]+"/")

    #print "putting things together"
    return "%s/%s" % (pysalt.__path__[0], filepart)

def clobberfile(filename):
    """

    Delete a file if it already exists, otherwise do nothing.

    """

    if (os.path.isfile(filename)):
        os.remove(filename)
    return


def get_binning(file_or_hdu):
    
    ccdsum = None
    print "GET BINNING:", type(file_or_hdu)

    if (type(file_or_hdu) == fits.hdu.hdulist.HDUList):
        if ('CCDSUM' in file_or_hdu[0].header):
            ccdsum = file_or_hdu[0].header['CCDSUM']

    elif (type(file_or_hdu) in (fits.hdu.image.PrimaryHDU,
                                fits.hdu.image.ImageHDU)):
        if ('CCDSUM' in file_or_hdu.header):
            ccdsum = file_or_hdu.header['CCDSUM']

    elif (type(file_or_hdu) == fits.header.Header):
        if ('CCDSUM' in file_or_hdu):
            ccdsum = file_or_hdu['CCDSUM']

    elif (type(file_or_hdu) == str):
        hdu = fits.open(file_or_hdu)
        if ('CCDSUM' in hdu[0].header):
            ccdsum = hdu[0].header['CCDSUM']

    if (not ccdsum == None):
        parts = ccdsum.split()
        binx = int(parts[0])
        biny = int(parts[1])
        return binx, biny

    return None, None
            
