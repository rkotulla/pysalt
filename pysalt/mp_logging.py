#!/usr/bin/env python

"""

This module contains all routines to configure and start the multi-processing
safe logging. All log output is queued, and handled in sequence by a separate
logging process.

"""


import sys
import numpy
import os
import pyfits
import datetime
import scipy
import scipy.stats
import math
import scipy.spatial
import itertools
import logging

import time
import Queue
import threading
import multiprocessing
import traceback

#from podi_definitions import *
#from podi_commandline import *
#import podi_sitesetup as sitesetup


from random import choice, random
import time

LEVELS = [logging.DEBUG, logging.INFO, logging.WARNING,
          logging.ERROR, logging.CRITICAL]

LOGGERS = ['a.b.c', 'd.e.f']

MESSAGES = [
    'Random message #1',
    'Random message #2',
    'Random message #3',
]

################################################################################
#
# Testing code goes here
#
################################################################################



# This is the worker process top-level loop, which just logs ten events with
# random intervening delays before terminating.
# The print messages are just so you know it's doing something!
def test_worker_process(log_setup):

    name = multiprocessing.current_process().name
    print('Worker started xxx: %s' % name)
    podi_logger_setup(log_setup)

    #logger = podi_getlogger(name, log_setup)
    for i in range(10):
        time.sleep(random())
        # print "in worker ."
        logger = logging.getLogger(choice(LOGGERS))
        level = choice(LEVELS)
        message = "msg %d: %s" % (i+1, choice(MESSAGES))
        # print message
        logger.log(level, message)
    print('Worker finished: %s' % name)




# The worker configuration is done at the start of the worker process run.
# Note that on Windows you can't rely on fork semantics, so each process
# will run the logging configuration code when it starts.
def log_slave_setup(queue):
    h = QueueHandler(queue) # Just the one handler needed
    root = logging.getLogger()
    root.addHandler(h)
    root.setLevel(logging.DEBUG) # send all messages, for demo; no other level or filter logic applied.




def log_master_setup():
    root = logging.getLogger()
    # h = logging.handlers.RotatingFileHandler('/tmp/mptest.log', 'a', 300, 10)
    try:
        h = logging.StreamHandler(stream=sys.stdout)
    except TypeError:
        h = logging.StreamHandler(strm=sys.stdout)
    except:
        raise
    f = logging.Formatter('%(asctime)s %(processName)-10s %(name)s %(levelname)-8s %(message)s')
    h.setFormatter(f)
    root.addHandler(h)




PPA_PROGRESS_LEVEL = 19


################################################################################
#
# Real code below
#
################################################################################



class QueueHandler(logging.Handler):
    """
    This is a logging handler which sends events to a multiprocessing queue.
    
    """

    def __init__(self, queue):
        """
        Initialise an instance, using the passed queue.
        """
        logging.Handler.__init__(self)

        #import os
        #print "\n\n\n\n Setting up logging, in Process ",os.getpid(),"XXX\n\n\n\n"

        self.queue = queue
        self.msgcount = 0

    def flush(self):
        pass

    def emit(self, record):

        """
        Emit a record.

        Writes the LogRecord to the queue.
        """
        self.msgcount += 1
        #sys.stdout.write("Current msg count: %d\n" % (self.msgcount))
        #sys.stdout.flush()

        # print "emitting 1 entry,",self.msgcount,"so far"
        try:
            #print "before adding one to queue",self.queue.qsize()
            #print "adding log entry to queue",self.msgcount, self.format(record)
            self.queue.put_nowait(record)
            #print "after adding one queue",self.queue.qsize()
        except (KeyboardInterrupt, SystemExit):
            raise
        except:
            sys.stdout.write("OOppsie!\n")
            sys.stdout.flush()
            self.handleError(record)






def log_master(queue, options):
    """

    This is the main process that handles all log output. 

    Each log-entry is received via the queue that's being fed by all
    sub-processes, and then forwarded to other log-handlers.

    """

    # print "starting logging!"

    import sys
    root = logging.getLogger()
    try:
        h = logging.NullHandler() #StreamHandler(stream=sys.stdout)
        f = logging.Formatter('%(asctime)s %(processName)-10s %(name)s %(levelname)-8s %(message)s')
        h.setFormatter(f)
        root.addHandler(h)
    except AttributeError:
        # This happens in older Python versions that don't have a NULLHandler
        pass
    except:
        raise

    root.propagate = False

    enable_debug = False
    debug_logger = root
    if (True):

        debug_filename = "debug.log"
        try:
            open_mode = "a" 
            debugfile = open(debug_filename, open_mode)
            enable_debug = True
            print >>debugfile, " ".join(sys.argv)
            
            # print 'activating debug output'

            debug_logger = logging.getLogger('debug')
            # debug_logger = logging.getLogger()
            try:
                h = logging.StreamHandler(stream=debugfile)
            except TypeError:
                h = logging.StreamHandler(strm=debugfile)
            except:
                raise
            f = logging.Formatter('%(asctime)s -- %(levelname)-8s [ %(filename)30s : %(lineno)4s - %(funcName)30s() in %(processName)-12s] %(name)30s :: %(message)s')
            h.setFormatter(f)
            debug_logger.addHandler(h)
            debug_logger.propagate=False
        except:
            print "#@#@#@#@#@# Unable to write to debug file: %s" % (debug_filename)
            print "#@#@#@#@#@# Routing all debug output to stderr"
            debug_logger = logging.getLogger('debug')
            try:
                h = logging.StreamHandler(stream=sys.stderr)
            except TypeError:
                h = logging.StreamHandler(strm=sys.stderr)
            except:
                raise
            f = logging.Formatter('%(asctime)s -- %(levelname)-8s [ %(filename)30s : %(lineno)4s - %(funcName)30s() in %(processName)-12s] %(name)30s :: %(message)s')
            h.setFormatter(f)
            debug_logger.addHandler(h)
            debug_logger.propagate=False
            
            pass

    #
    # Create a handler for all output that also goes into the display
    #
    info = logging.getLogger('info')
    
    # set format for the terminal output
    try:
        h = logging.StreamHandler(stream=sys.stdout)
    except TypeError:
        h = logging.StreamHandler(strm=sys.stdout)
    except:
        raise
    # Add some specials to make sure we are always writing to a clean line
    f = logging.Formatter('\r\x1b[2K%(name)s: %(message)s')
    # f = logging.Formatter('%(name)s: %(message)s')
    h.setFormatter(f)
    info.addHandler(h)
    
    # 
    # Also write all info/warning/error messages to the logfile
    #
    infolog_file = open("quickreduce.log", "w")
    try:
        h = logging.StreamHandler(stream=infolog_file)
    except TypeError:
        h = logging.StreamHandler(strm=infolog_file)
    except:
        raise
    f = logging.Formatter('%(asctime)s %(processName)-10s %(name)s %(levelname)-8s %(message)s')
    h.setFormatter(f)
    info.addHandler(h)
    info.propagate = False
            
    #
    # Check if we can connect to a RabbitMQ server
    #
    enable_pika = False
    
    msg_received = 0
    while True:
        try:
            try:
                record = queue.get()
            except KeyboardInterrupt, SystemExit:
                record = None
            except:
                raise

            if (record == None): 
                break

            msg_received += 1
            # Add some logic here

            #print "record-level:",record.levelno, record.levelname, msg_received

            if (enable_debug):
                #print "handling at debug level", record.msg
                debug_logger.handle(record)

            if ((record.levelno > logging.DEBUG) and
                (record.levelno <= logging.INFO) ):
                info.handle(record)
                #print "handling at info level"
            elif (record.levelno > logging.INFO):
                # logger = logging.getLogger(record.name)
                # print "msg",msg_received," --> ",record.msg
                
                #print "handling at root level"
                info.handle(record) # No level or filter logic applied - just do it!

            #print "done with record.\n"

            #
            # only sent select message via Pika, and only if Pika has been 
            # initialized successfully
            #
             
            queue.task_done()
        except (KeyboardInterrupt, SystemExit):
            raise
        except:
            import sys, traceback
            print >> sys.stderr, 'Whoops! Problem:'
            traceback.print_exc(file=sys.stderr)

    if (enable_debug):
        print >>debugfile, "done with logging, closing file"
        debugfile.close()




def podi_log_master_start(options):
    """
    
    This function creates the logging sub-process that handles all log output.

    This function also prepares the necessary information so we can activate the
    multiprocessing-safe logging in all sub-processes

    """

    queue = multiprocessing.JoinableQueue()
    listener = multiprocessing.Process(target=log_master,
                                kwargs={"queue": queue,
                                        "options": options}
                            )
    listener.start()

    worker_setup = {"queue": queue,
                  "configurer": log_slave_setup}
    
    log_master_info = {"queue": queue,
                       "listener": listener
                   }

    # Also start a logger for the main process
    podi_logger_setup(worker_setup)

    return log_master_info, worker_setup


def podi_log_master_quit(log_master_info):
    """
    Shutdown the logging process
    """

    log_master_info['queue'].put_nowait(None)
    try:
        log_master_info['listener'].join()
    except (KeyboardInterrupt, SystemExit):
        pass

    return


def podi_logger_setup(setup):
    """
    This function re-directs all logging output to the logging queue that feeds
    the logging subprocess.
    """
    
    if (setup == None):
        return
        # handler = logging.StreamHandler(sys.stdout)
    else:
        handler = QueueHandler(setup['queue'])

    # import sys
    # handler = logging.StreamHandler(stream=sys.stdout)
    logger = logging.getLogger()

    for h in logger.handlers:
        logger.removeHandler(h)

    logger.setLevel(logging.DEBUG)

    f = logging.Formatter('MYLOGGER = %(asctime)s %(processName)-10s %(name)s %(levelname)-8s %(message)s')
    handler.setFormatter(f)
    
    logger.addHandler(handler)
    logger.propagate = True

    logger.debug("Started logging for process %s" % (multiprocessing.current_process().name))

    return


def log_exception(name=None):

    etype, error, stackpos = sys.exc_info()

    exception_string = ["\n",
                        "=========== EXCEPTION ==============",
                        "etype: %s" % (str(etype)),
                        "error: %s" % (str(error)),
                        "stackpos: %s" % (str(stackpos)),
                        "---\n",
                        traceback.format_exc(),
                        "--- end\n"
    ]
    logger = logging.getLogger(name)
    logger.critical("\n".join(exception_string))
    return


def log_platform_debug_data():
    logger = logging.getLogger("PLATFORM")
    try:
        import platform
        logger.debug("Python version: %s" % (str(platform.python_version())))
        logger.debug("Python compiler: %s" % (str(platform.python_compiler())))
        logger.debug("Python build: %s" % (str(platform.python_build())))

        logger.debug("OS version: %s" % (str(platform.platform())))

        logger.debug("OS uname: %s" % (" ".join(platform.uname())))
        logger.debug("OS system: %s" % (str(platform.system())))
        logger.debug("OS node: %s" % (str(platform.node())))
        logger.debug("OS release: %s" % (str(platform.release())))
        logger.debug("OS version: %s" % (str(platform.version())))
        logger.debug("OS machine: %s" % (str(platform.machine())))
        logger.debug("OS processor: %s" % (str(platform.processor())))

        logger.debug("interpreter: %s" % (" ".join(platform.architecture())))
    except:
        logger.debug("OS info not available, missing package platform")
        pass

    try:
        import socket
        logger.debug("Socket hostname: %s" % (socket.gethostname()))
    except:
        logger.debug("socket info not available, missing package socket")
        pass

    try:
        import getpass
        logger.debug("username: %s" % (getpass.getuser()))
    except:
        logger.debug("username not available, missing package getpass")
        pass
        
    return


def setup_logging(options=None):

    if (options == None):
        options = {}

    # Setup everything we need for logging
    log_master_info, log_setup = podi_log_master_start(options)
    options['log_setup'] = log_setup
    options['log_master_info'] = log_master_info

    log_platform_debug_data()

    return options
    
def shutdown_logging(options):
    podi_log_master_quit(options['log_master_info'])
    return




# def podi_getlogger(name, setup):

#     if (setup == None):
#         handler = logging.StreamHandler(sys.stdout)
#     else:
#         handler = QueueHandler(setup['queue'])

#     logger = logging.getLogger(name)
#     logger.addHandler(handler)
#     logger.setLevel(logging.DEBUG) # send all messages, for demo; no other level or filter logic applied.
#     logger.propagate = False

#     return logger


if __name__ == "__main__":
    pass
