"""
The PySALT user package is the primary reduction and analysis software tools for the SALT telescope.  Currently, these tools include basic data reductions for RSS and SALTICAM in both imaging, spectroscopic, and slot modes. Basic analysis software for slot mode data is also provided.  These tools are primarily written in python/PyRAF with some additional IRAF code.

"""

#import pyraf
#from iraf import pysalt 

import version
__version__=version.full_version #'1.0.0' #pysalt.verno
__revision__=version.git_revision

