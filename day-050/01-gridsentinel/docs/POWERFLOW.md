# DC power-flow approximation

For an energized line between buses i and j, active flow is approximately `(theta_i - theta_j) / x_ij`, with voltage magnitude assumed 1 p.u. and reactive components omitted. The network susceptance Laplacian is assembled using 1/reactance per line. A slack angle is fixed at zero in each connected island, then reduced equations `B_reduced * theta = P` are solved by partial-pivot elimination. Each island must have balanced generation-load injections. Results are not AC-feasibility or voltage-stability assessments.
