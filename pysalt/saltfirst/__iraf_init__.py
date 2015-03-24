#
# Import script to make all python commands accessible from pyraf/IRAF
#
# Changelog:
# 
# 2015-03-23: Ralf Kotulla
#             First release
#


import pysalt._iraf
import pysalt.saltfirst

tasks = [
    ('saltfirst', 'saltfirst$saltfirst.par', pysalt.saltfirst.saltfirst.saltfirst),
]
pkg_name = 'pipetools'

pysalt._iraf.install(tasks, pkg_name)
