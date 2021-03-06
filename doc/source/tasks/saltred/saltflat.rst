.. _saltflat:

********
saltflat
********


Name
====

saltflat -- Flatfield correct SALT images

Usage
=====

saltflat images outimages outpref flatimage (minflat) (clobber)  (logfile) (verbose)

Parameters
==========


*images*
    String. List of input images including, if necessary, absolute or
    relative paths to the data. Data can be provided as a comma-separated
    list, or a string with a wildcard (e.g. 'images=S20061210*.fits'), or
    a foreign file containing an ascii list of image filenames. For ascii
    list option, the filename containing the list must be provided
    preceded by a '@' character, e.g. 'images=@listoffiles.lis'.

*outimage*
    String. A list of images. Data can be provided as a comma-separated
    list, or a string with a wildcard (e.g. 'outimages=rS20061210*.fits'), or
    a foreign file containing an ascii list of image filenames. For ascii
    list option, the filename containing the list must be provided
    preceded by a '@' character, e.g. 'outimages=@listoffiles.lis'. This list
    must be of the same size as the images argument list.

*outpref*
    String. If the outpref string is non-zero in length and contains
    characters other than a blank space, it will override any value of the
    outimages argument. Output file names will use the name list provided
    in the images argument, but adding a prefix to the basename of
    each  output file defined by outpref. An absolute or relative directory
    path can be included in the prefix, e.g. 'outpref=/Volumes/data/p'.

*flatimage*
    String.  File to use for flatfielding the data.  This file should
    be the same format and size of the input data.   The file will be
    normalized by the task prior to applying to the data.

*minflat*
    Real.  Minimum value for the flatfield image.  Any pixels above
    this value will be replaces with this value.

*clobber*
    Hidden boolean. If set to 'yes' files contained within the outpath
    directory will be overwritten by newly created files of the same
    name.

*logfile*
    String. Name of an ascii file for storing log and error messages
    written by the task. The file may be new, or messages can also be
    appended to a pre-existing file.

*(verbose)*
    Boolean. If verbose=n, log messages will be suppressed.

Description
===========

SALTFLAT corrects a SALT image for flatflied variations.

The task reads in the flatfield image, flatimage.  The flatimage will have
any bad pixels below the minflat value replace by the minflat value.  Then,
the image will be normalized by its mean.

After normalizing the flatimage, SALTFLAT will divide flatimage
into each of the images supplied here.   If the images have variance
frames, SALTFLAt will also propogate the errors through to the variance
frames.

If the users wishes to only correct for pixel to pixel variations
or illumination corrections, these images can be applied here
but the flatimage would have to be prepared prior to running this
task.



Examples
========

1. To flat field correct a SALT image::

    --> saltflat images='@images.lis' outimages='' outpref='f'
    flatimage='FLAT.fits' minflat=1 clobber='yes'
    logfile='salt.log' verbose='yes'

Time and disk requirements
==========================

Individual unbinned full frame RSS image files can be 112MB in size. It is
recommended to use workstations with a minimum of 512MB RAM. On a
linux machine with 2.8 Ghz processor and 2 Gb of RAM, one 2051x2051 image can
be processed in 0.31 sec.

Bugs and limitations
====================

SALTFLAT will only correct by the image given to it and no other process
is applied to the data. SALTFLAT will not check to make sure that the
data are the right type, but will blindly apply the correction.

Send feedback and bug reports to salthelp@saao.ac.za

See also
========

 :ref:`saltclean` :ref:`saltslot`