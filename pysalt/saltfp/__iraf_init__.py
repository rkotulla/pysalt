#
# Import script to make all python commands accessible from pyraf/IRAF
#
# Changelog:
# 
# 2015-03-23: Ralf Kotulla
#             First release
#

import pysalt._iraf
import pysalt.saltfp

tasks = [
    ('saltfpcalibrate', 'saltfp$saltfpcalibrate.par', 
     pysalt.saltfp.saltfpcalibrate.saltfpcalibrate),
    ('saltfpcalprofile', 'saltfp$saltfpcalprofile.par', 
     pysalt.saltfp.saltfpcalprofile.saltfpcalprofile),
    ('saltfpcalring', 'saltfp$saltfpcalring.par', 
     pysalt.saltfp.saltfpcalring.saltfpcalring),
    ('saltfpeprofile', 'saltfp$saltfpeprofile.par', 
     pysalt.saltfp.saltfpeprofile.saltfpeprofile),
    ('saltfpnightring', 'saltfp$saltfpnightring.par', 
     pysalt.saltfp.saltfpnightring.saltfpnightring),
    ('saltfpprep', 'saltfp$saltfpprep.par', 
     pysalt.saltfp.saltfpprep.saltfpprep),
    ('saltfpringfilter', 'saltfp$saltfpringfilter.par', 
     pysalt.saltfp.saltfpringfilter.saltfpringfilter),
    ('saltfpringfind', 'saltfp$saltfpringfind.par', 
     pysalt.saltfp.saltfpringfind.saltfpringfind),
    ('saltfpringfit', 'saltfp$saltfpringfit.par', 
     pysalt.saltfp.saltfpringfit.saltfpringfit),
    ('saltfpskyring', 'saltfp$saltfpskyring.par', 
     pysalt.saltfp.saltfpskyring.saltfpskyring),
    ('saltfpzeropoint', 'saltfp$saltfpzeropoint.par', 
     pysalt.saltfp.saltfpzeropoint.saltfpzeropoint),
]
pkg_name = 'saltfp'

pysalt._iraf.install(tasks, pkg_name)
