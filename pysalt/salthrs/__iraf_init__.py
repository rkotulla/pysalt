#
# Import script to make all python commands accessible from pyraf/IRAF
#
# Changelog:
# 
# 2015-03-23: Ralf Kotulla
#             First release
#

import pysalt._iraf
import pysalt.salthrs

tasks = [
    ('hrsclean', 'salthrs$hrsclean.par', pysalt.salthrs.hrsclean.hrsclean),
    ('hrsprepare', 'salthrs$hrsprepare.par', pysalt.salthrs.hrsprepare.hrsprepare),
    ('hrsstack', 'salthrs$hrsstack.par', pysalt.salthrs.hrsstack.hrsstack),
]
pkg_name = 'saltfp'

pysalt._iraf.install(tasks, pkg_name)
