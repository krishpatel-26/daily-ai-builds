# Dynamics

The reference model is an idealized planar, Earth-centered two-body gravitational system. Units: position km, velocity km/s, time seconds. Acceleration is `-mu*r/|r|^3`. Integrate with explicit fourth-order Runge–Kutta using bounded time steps. Circular initial states use `v=sqrt(mu/r)`. The display is illustrative and is not a faithful orbit plot.
