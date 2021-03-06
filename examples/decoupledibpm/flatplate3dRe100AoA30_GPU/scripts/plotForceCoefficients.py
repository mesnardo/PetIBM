"""
Post-processes the force coefficients from a PetIBM simulation.
"""

import pathlib
import numpy
from matplotlib import pyplot


# Set up root directory.
simu_dir = pathlib.Path(__file__).absolute().parents[1]

# Get the force coefficients.
filepath = simu_dir / 'forces-0.txt'
with open(filepath, 'r') as infile:
    t, cd, cl = numpy.loadtxt(infile, dtype=numpy.float64,
                              unpack=True, usecols=(0, 1, 2))

# Compute the time-averaged force coefficients.
# Get the min/max values of the lift coefficient.
limits = (15.0, 20.0)
mask = numpy.where(numpy.logical_and(t >= limits[0], t <= limits[1]))
cd_mean, cl_mean = cd[mask].mean(), cl[mask].mean()
cl_min, cl_max = cl[mask].min(), cl[mask].max()
print('<Cd> = {:0.4f}'.format(cd_mean))
print('<Cl> = {:0.4f} ([{:0.4f}, {:0.4f}])'.format(cl_mean, cl_min, cl_max))

pyplot.rc('font', family='serif', size=16)

# Plots the figure.
fig, ax = pyplot.subplots(nrows=2, figsize=(10.0, 6.0), sharex=True)
ax[0].grid()
ax[0].set_ylabel('Drag coefficient')
ax[0].plot(t, cd)
ax[0].set_ylim(0.6, 1.2)
ax[1].grid()
ax[1].set_xlabel('Non-dimensional time')
ax[1].set_ylabel('Lift coefficient')
ax[1].plot(t, cl)
ax[1].set_xlim(0.0, 20.0)
ax[1].set_ylim(0.6, 1.2)
fig.tight_layout()

pyplot.show()

# Save figure.
fig_dir = simu_dir / 'figures'
fig_dir.mkdir(parents=True, exist_ok=True)
filepath = fig_dir / 'forceCoefficients.png'
fig.savefig(str(filepath), dpi=300)
