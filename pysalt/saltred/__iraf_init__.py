#
# Import script to make all python commands accessible from pyraf/IRAF
#
# Changelog:
# 
# 2015-03-23: Ralf Kotulla
#             First release
#

import pysalt._iraf
import pysalt.saltred

tasks = [
    ('saltbias',     'saltred@saltbias.par',     pysalt.saltred.saltbias.saltbias),
    ('saltclean',    'saltred@saltclean.par',    pysalt.saltred.saltclean.saltclean),
    ('salt2iraf',    'saltred@salt2iraf.par',    pysalt.saltred.salt2iraf.salt2iraf),
    ('saltgain',     'saltred@saltgain.par',     pysalt.saltred.saltgain.saltgain),
    ('saltflat',     'saltred@saltflat.par',     pysalt.saltred.saltflat.saltflat),
    ('saltillum',    'saltred@saltillum.par',    pysalt.saltred.saltillum.saltillum),
    ('saltcombine',  'saltred@saltcombine.par',  pysalt.saltred.saltcombine.saltcombine),
    ('saltmosaic',   'saltred@saltmosaic.par',   pysalt.saltred.saltmosaic.saltmosaic),
    ('saltobslog',   'saltred@saltobslog.par',   pysalt.saltred.saltobslog.saltobslog),
    ('saltslot',     'saltred@saltslot.par',     pysalt.saltred.saltslot.saltslot),
    ('saltxtalk',    'saltred@saltxtalk.par',    pysalt.saltred.saltxtalk.saltxtalk),
    ('saltprepare',  'saltred@saltprepare.par',  pysalt.saltred.saltprepare.saltprepare),
    ('saltheadtime', 'saltred@saltheadtime.par', pysalt.saltred.saltheadtime.saltheadtime),
    ('saltarith',    'saltred@saltarith.par',    pysalt.saltred.saltarith.saltarith),
]
pkg_name = 'saltred'

pysalt._iraf.install(tasks, pkg_name)
