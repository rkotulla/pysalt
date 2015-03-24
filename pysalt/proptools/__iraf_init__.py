#
# Import script to make all python commands accessible from pyraf/IRAF
#
# Changelog:
# 
# 2015-03-23: Ralf Kotulla
#             First release
#

import pysalt._iraf
import pysalt.proptools

tasks = [
    ('masktool',     'proptools$masktool.par',     pysalt.proptools.masktool.masktool),
]
pkg_name = 'proptools'

pysalt._iraf.install(tasks, pkg_name)
