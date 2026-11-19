# SwarmGrid — Multi-Robot Coordination Research Lab
Day 046/365, project 2. Grid-world simulation with multi-robot task allocation, A* paths, reservation-based conflict avoidance and performance benchmarks.

Python 3.11+, standard library only. Run `python -m swarmgrid.server` then open http://127.0.0.1:4197. Tests: `python -m unittest discover -s tests -v`.

Research demo only: discrete grid, synchronous moves, synthetic tasks, no real robot control, no ROS 2, no safety certification. The planner is not complete MAPF/CBS and cannot guarantee a solution for every multi-robot scenario.
