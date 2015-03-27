
import pysalt
import os, sys

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
