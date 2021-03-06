.. _saltheadtime:

************
saltheadtime
************


Name
====

saltheadtime -- Convert header times to different time systems.

Usage
=====

saltheadtime images (timetype) (writetoheader) (clobber) logfile (verbose) (debug)

Parameters
==========


*images*
    String. List of input images. Data can be provided as a comma-separated
    list, or a string with a wildcard (e.g. 'images=S*.fits'), or
    a foreign file containing an ascii list of image filenames. For ascii
    list option, the filename containing the list must be provided
    preceded by a '@' character, e.g. 'images=@listoffiles.lis'. Conversion
    to HJD and BJD required object positions, so calibration files with
    no target information in the headers should not be used.

*(timetype) [JD(UTC)|JD(TT)|MJD(TT)|HJD(TT)|BJD(TDB)]*
    String. The time system to which the UTC header time(s) from images
    should be converted.  Options include Julian date, referenced to either
    UTC or TT (terrestrial time), Modified Julian date, Heliocentric
    Julian date, and Barycentric Julian Date. Details are below.
    
    JD: Julian Date is the number of days since 01 January 4713 BC. The formula
    used here is from http://scienceworld.wolfram.com/astronomy/JulianDate.html.
    JD(UTC) has time referenced to the coordinated universal timescale,
    which is slightly slower than JD(TT), which has time referenced to Terrestrial time.
    
    UTC vs TT:  Terrestrial time (TT) is based on atomic time (TAI). It is the
    recommended reference timescale by IAU XXIII resolution B.1, so we reference
    all times to it. Many people use JD referenced to coordinated universal time
    (UTC), so we provide that option as well. TT depends on leap seconds, and the
    conversion between UTC, TT, and TAI as a function of date is located at
    ftp://maia.usno.navy.mil/ser7/tai-utc.dat.
    We only use the table back to 1999; therefore, dates prior to 1999 are
    invalid. NOTE: this information *must* be updated when new leap seconds
    are added!
    
    MJD: Modified Julian date (MJD) corresponds to days since midnight on
    17 November 1858, or 2400000.5 JD.  We reference it to Terrestrial Time (TT).
    
    HJD: Heliocentric Julian Date (HJD) is the Julian Date adjusted to the
    center of the Sun. We reference it to Terrestrial Time (TT).
    HJD depends on the JD of the observation (from which we get
    the position of Sun, in terms of the solar longitude and the obliquity of the
    ecliptic), and the object RA and DEC. The intent of HJD is to make a first-order
    accounting of the paralactic time shift between the positions of the Earth
    and the Sun.
    
    The obliquity of the ecliptic calculation we use is from the 2009 Astronomical
    Almanac, pg. C5, ``Low precision formulas for the Sun``. These equations give the
    apparent coordinates of the Sun to a precision of 0.01 degrees and the equation
    of time to 0.01 min between 1950 and 2050.
    
    The longitude of the sun and formula for the distance/time the light must
    travel between the Earth and Sun are from _Observational Astronomy_ by
    D.S Birney, Cambridge Univ. Press, 1991, pages 248-251. (Note that there is a
    typo in the final equation on p251.) This equation is supposedly accurate to
    0.008s, the correction for the Earth's orbital eccentricity; however, the
    obilquity of the ecliptic does have some error as well. Tests with obliquity
    of +/- 0.01 deg show a change in resulting HJD of 0.01s.
    
    BJD: Barycentric JD is relative to the dynamical center-of-mass (``barycenter``)
    of the Solar System. We reference it to Barycentric Dynamical Time (TDB).
    There is not an easy formula to convert between this
    system and others. Here we follow the basic formula from C. Marquardts
    description at http://lheawww.gsfc.nasa.gov/users/craigm/bary/. Rather than
    following that ephemeris interpolation scheme, we use the bulit-in numpy
    interpolation function.
    
    We account for three effects: geometric (geometric time-delay in the Solar
    System), Einstein (relativistic), and Shapiro (photon bending). The output is
    JD(TT)  plus the sum of these corrections. Note that there is NO dispersion time
    correction.  Also, the location is assumed to be the center of the Earth: no
    observatory information is included. Tests with other BJD calculators indicate
    that the accuracy of this function is on the order of 10^(-5) seconds.
    
    Shortly after this code was created, we were directed to a manuscript on
    astro-ph with a nice calculation of BJD for exoplanet observations (Eastman,
    Siverd, and Gaudi,2010; arXiv: 1005.4415v2). A comparison between the equations
    in that paper and in this code is as follows:
    
    Eastman et al.              This code
    ---------------------------------------------------------------
    Romer delay, delta_Rsun     same as ``geometric`` correction
    Clock correction, delta_C   same conversion to TT; ``Einstein`` correction is
    TDB-TT component
    Shaprio delay, delta_Ssun   same as ``Shaprio`` correction
    Einstein delay, delta_Esun  not considered -- is observatory location wrt geocenter
    
    This function requires ephemeris files for the Sun and the Earth.  The
    appropriate files are located in XXdirectory.  The current files, sun.eph and
    earth.eph are valid from 1999 Jan 01 to 2012 Jan 01 (although
    the farther into the future the dates go, the less accurate they will be).
    To generate new files, send the following text (edited to your email address
    and desired dates) to horizons@ssd.jpl.nasa.gov with the word ``job``
    (sans quotes) in the subject line.  The object is altered by the value of
    COMMAND: '10' is the Sun and '399' is the Earth. The ephemeris is
    assumed to be DE405. Note that the ephemerides should NOT be light-time corrected.
    
    !$$SOF (ssd) JPL/Horizons Execution Control VARLIST
    
    !Oct 30,2002
    
    !ftp://ssd.jpl.nasa.gov/pub/ssd/horizons_batch_example.brief
    
    !!+++++++++++++++++++++++++++++++++++++++++++++++++++
    
    !NOTE:First line in this file must start!$$SOF
    
    !Last line in this file must start!$$EOF
    
    !Assigned values should be in quotes
    
    !+++++++++++++++++++++++++++++++++++++++++++++++++++
    
    EMAIL_ADDR='amanda@saao.ac.za'
    
    COMMAND='10'
    
    OBJ_DATA='YES'
    
    MAKE_EPHEM='YES'
    
    TABLE_TYPE='VECTORS'
    
    CENTER='500@0'
    
    REF_PLANE='FRAME'
    
    START_TIME='1999-Jan-01 00:00'
    
    STOP_TIME='2012-Jan-01 00:00'
    
    STEP_SIZE='1 day'
    
    REF_SYSTEM='J2000'
    
    OUT_UNITS='KM-S'
    
    VECT_TABLE='3'
    
    VECT_CORR='NONE'
    
    TIME_ZONE='+00:00'
    
    TIME_DIGITS='FRACSEC'
    
    RANGE_UNITS='AU'
    
    CSV_FORMAT='YES'
    
    VEC_LABELS='NO'
    
    R_T_S_ONLY='NO'
    !$$EOF~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    
    The reply to this message will contain header and footer information as well
    as the ephemerides.  *DELETE* the header and footer information (retaining
    only the lines between $$SOE and $$EOE).  Then save the files in UNIX text
    format as sun.eph and earth.eph in XXdirectory.
    

*(writetoheader)*
    Boolean. If writetoheader='yes' then the new time will be entered
    as a new line(s) in the header(s) of the images. If the keyword
    already exists, the clobber setting determines whether or not it
    will be overwritten. Note that none of the header items from the
    original data file will be overwritten or deleted.  Only dates/times
    specific to this tool are modified.

*(clobber)*
    Boolean. If clobber='yes' and writetoheader='yes', any exisiting
    header keywords and values will be overwritten by the new ones.

*logfile*
    String. Name of an ascii file for storing log and error messages
    written by the task. The file may be new, or messages can also be
    appended to a pre-existing file.

*(verbose)*
    Boolean. If verbose=n, log messages will be suppressed. Currently,
    there are no messages specific to verbose.

Description
===========

saltheadtime reads the UTC header time from salitcam data and converts
it to a different time system.  The original header time, and the new
time, are displayed. If desired, the new time can be written to the
file header with the appropriate keyword and comment.

There are currently five selections for alternative times: Julian Date (UTC),
Julian Date (TT), Modified Julian Date (TT), Heliocentric Julian Date (TT),
and Barycentric Julian Date (TDB).


Examples
========

1. To see the MJD times for all images in the directory::

    --> saltheadtime images=*.fits timetype='MJD(TT)' writetoheader='no'
    logfile='salt.log' verbose='yes' debug='no'

2. To write the HJD time of one file to the header::

    --> saltheadtime images=S200809010002.fits timetype='HJD(TT)'
    writetoheader='yes' logfile='salt.log' verbose='yes' debug='no'

Time and disk requirements
==========================

Disk requirements are negligible since only change is adding one line
to the header. Takes < 0.5 sec per file, including writing to header,
on saltastro (19 May 2010).


Bugs and limitations
====================

Only SALTICAM data have been tested (full frame, FT, and slotmode,
raw and pipeline-reduced).

Send feedback and bug reports to salthelp@saao.ac.za

.endhelp
========

