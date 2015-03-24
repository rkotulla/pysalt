#
# Import script to make all python commands accessible from pyraf/IRAF
#
# Changelog:
# 
# 2015-03-23: Ralf Kotulla
#             First release
#

import pysalt._iraf
import pysalt.saltspec

tasks = [
    ('specarcstraighten', 'saltspec$specarcstraighten.par', 
     pysalt.saltspec.specarcstraighten.specarcstraighten),
    ('speccal', 'saltspec$speccal.par', 
     pysalt.saltspec.speccal.speccal),
    ('specextract', 'saltspec$specextract.par', 
     pysalt.saltspec.specextract.specextract),
    ('specidentify', 'saltspec$specidentify.par', 
     pysalt.saltspec.specidentify.specidentify),
    ('specprepare', 'saltspec$specprepare.par', 
     pysalt.saltspec.specprepare.specprepare),
    ('specrectify', 'saltspec$specrectify.par', 
     pysalt.saltspec.specrectify.specrectify),
    ('specreduce', 'saltspec$specreduce.par', 
     pysalt.saltspec.specreduce.specreduce),
    ('specselfid', 'saltspec$specselfid.par', 
     pysalt.saltspec.specselfid.specselfid),
    ('specsens', 'saltspec$specsens.par', 
     pysalt.saltspec.specsens.specsens),
    ('specsky', 'saltspec$specsky.par', 
     pysalt.saltspec.specsky.specsky),
    ('specslitnormalize', 'saltspec$specslitnormalize.par', 
     pysalt.saltspec.specslitnormalize.specslitnormalize),
    ('specslit', 'saltspec$specslit.par', 
     pysalt.saltspec.specslit.specslit),
]
pkg_name = 'saltspec'

pysalt._iraf.install(tasks, pkg_name)
