# 2D lid-driven cavity flow at Re=5000

Run the example:

```
mpiexec -np 4 petibm-navierstokes -options_left -log_view ascii:stdout.txt
```

The simulation completes in about 16 minutes when using 4 processes
(Intel(R) Core(TM) i7-3770 CPU @ 3.40GHz).

Plot the centerline velocity components and compare with the numerical results
from Ghia et al. (1982):

```
python scripts/plotCenterlineVelocities.py
```

The plot is saved in the sub-folder `figures` of the simulation directory.
