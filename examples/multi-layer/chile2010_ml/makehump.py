"""
Module to create topo and qinit data files for this example.
"""

from __future__ import absolute_import
from clawpack.geoclaw.topotools import Topography
from numpy import *

def maketopo():
    """
    Output topography file for the entire domain
    """
    nxpoints = 201
    nypoints = 201
    xlower = -100.e0
    xupper = 100.e0
    yupper = 100.e0
    ylower = -100.e0
    outfile= "bowl.topotype2"     

    topography = Topography(topo_func=topo)
    topography.x = linspace(xlower,xupper,nxpoints)
    topography.y = linspace(ylower,yupper,nypoints)
    topography.write(outfile, topo_type=2, Z_format="%22.15e")

def makeqinit():
    """
    Create qinit data file
    """
    nxpoints = 101
    nypoints = 101
    xlower = -110.e0
    xupper = -90.e0
    yupper = -50.e0
    ylower = -30.e0
    outfile= "hump.xyz"     

    topography = Topography(topo_func=qinit)
    topography.x = linspace(xlower,xupper,nxpoints)
    topography.y = linspace(ylower,yupper,nypoints)
    topography.write(outfile, topo_type=1)

def topo(x,y):
    """
    Parabolic bowl
    """
    # value of z at origin:  Try zmin = 80 for shoreline or 250 for no shore
    zmin = 80.
    z = 1.e-2*(x**2 + y**2) - zmin
    return z


def qinit(x,y):
    """
    Gaussian hump:
    """
    from numpy import where
    ze = -((x+100e0)**2 + (y+40e0)**2)/10.
    z = where(ze>-10., 2.e0*exp(ze), 0.)
    return z

if __name__=='__main__':
    # maketopo()
    makeqinit()