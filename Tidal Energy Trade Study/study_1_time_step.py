"""
Created on Tue Oct 27 12:23:22 2020

@author: jeff
"""

# This script contains calculations pertaining to possibilities of
# installation for tidal energy infrastructure in Northeastern region of the
# United States.  It includes potential power-production and economic analyses.

import numpy as np
import matplotlib.pyplot as plt

rho = 1000    # density of water [kg/m^3]
g = 9.81      # acceleration due to gravity [m/s^2]

A = 10      # area of interest, [mi^2]
A = A*5280**2/3.281**2   # [mi^2] -> [ft^2] -> [m^2]

# tidal range info
    # https://upload.wikimedia.org/wikipedia/commons/5/5e/M2_tidal_constituent.jpg
z0  = 100           # tidal range [cm]
z0  = z0/100        # [cm] -> [m]
t_T  = 6.2          # time period between hi & lo tide [hrs]  NOTE: _T refers to natural Tidal cycle
t_T  = t_T*60**2    # [hrs] -> [s]

# define geometry of system
# assuming small vertical hole
#   https://www.engineeringtoolbox.com/flow-liquid-water-tank-d_1753.html
#   h1 = H, h2 = h  (in figure)
l = 1                       # length of hole [m]
h = 0.6                     # height of hole [m]
A = h*l                     # hole area [m^2]
h1 = z0 - h/2               # height between center of hole and top of water
h2 = h/2                    # height between center of hole and floor
h_checc_is_z = h1+h2

## P0 = rho*g*z  # calculate hydrostatic pressure at lo tide due to difference in height [N/m^2]
#V   = A*z0     # volume of water [m^3]
#m   = rho*V   # mass of water [kg]
#pe  = m*g*z0   # potential energy of water [J]
#P   = pe/t_T    # very, very rough estimate of power produced during one tide [J/s] [W]
#P   = P/1000**2  # [W] -> [MW]

#Cv = 0.97      # velocity coeff
#Cd = 1         # discharge coeff

#v = Cv*(2*g*h1)**0.5         # outlet velocity of water [m/s]
#dV_dt = Cd*A*(2*g*h1)**0.5   # volume flow rate [m^3/s]
#F = rho*dV_dt*v              # reaction force

# generate diagram
x = [0,0,1,1]
y = [0,z0,0,z0]
plt.plot(x,y,'ro')
plt.plot(x[1],h,'co')
plt.plot(x[1],0,'co')
plt.title('Diagram')
plt.xlabel('(arbitrary length scale)')
plt.ylabel('Height [m]')
plt.show()


# time begins at hi tide
dt     = 120          # time increment [s]
steps  = t_T/dt    # number of time steps
steps  = int(steps)   # convert from type float to integer
dz_dt_T  = z0/t_T     # rate of change in tide over time [m/s]

t   = [0]
z   = [z0]
z_T = [z0]
V   = [A*z0]
m   = [rho*A*z0]  # m = rho*V
pe  = [rho*A*z0*g*z0]  # pe = m*g*z0
P   = [pe/dt/1000**2]  # [MW]


for i in range(steps):
    #print(i)
    t.append(dt*i)
    z_T.append
    
    
    
    
    
    
    