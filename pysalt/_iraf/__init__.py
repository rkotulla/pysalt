

from pyraf import iraf
from pyraf.iraf import pysalt



def install(tasks, pkg_name):

    for task in tasks:
        taskname, par, fct = task
        exec("import %s" % (taskname))

        if not iraf.deftask(taskname):
            parfile = iraf.osfn(par)
            t = iraf.IrafTaskFactory(
                taskname=taskname,
                value=parfile,
                function=fct, 
                pkgname=pkg_name)
