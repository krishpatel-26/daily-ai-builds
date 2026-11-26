# Architecture
Network topology → linear conductance matrix → Gaussian elimination → pressure/pipe-flow forward model → seeded pressure noise → inverse least-squares search over junction candidates → ranked source hypotheses → sensitivity benchmark → read-only API and interactive SVG map.

The same linear solver is reused by the generator and the inverse model; this creates model-matched conditions and can overstate field accuracy.
