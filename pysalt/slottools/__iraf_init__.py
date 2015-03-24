#
# Import script to make all python commands accessible from pyraf/IRAF
#
# Changelog:
# 
# 2015-03-23: Ralf Kotulla
#             First release
#

import pysalt._iraf
import pysalt.slottools

tasks = [
    ('slotback', 'slottools$slotback.par', 
     pysalt.slottools.slotback.slotback),
    ('slotmerge', 'slottools$slotmerge.par', 
     pysalt.slottools.slotmerge.slotmerge),
    ('slotphot', 'slottools$slotphot.par', 
     pysalt.slottools.slotphot.slotphot),
    ('slotpreview', 'slottools$slotpreview.par', 
     pysalt.slottools.slotpreview.slotpreview),
    ('slotreadtimefix', 'slottools$slotreadtimefix.par', 
     pysalt.slottools.slotreadtimefix.slotreadtimefix),
    ('slotutcfix', 'slottools$slotutcfix.par', 
     pysalt.slottools.slotutcfix.slotutcfix),
    ('slotview', 'slottools$slotview.par', 
     pysalt.slottools.slotview.slotview),
]
pkg_name = 'slottools'

pysalt._iraf.install(tasks, pkg_name)
