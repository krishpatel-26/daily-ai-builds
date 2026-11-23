# EmbodiedBench — Grounded Robot Task Planning & Recovery Laboratory

**Day 049/365 · Research Build 02**

A deterministic symbolic robot manipulator operates in a discrete warehouse world with shelves, objects and destination zones. A strict natural-language-like command grammar is compiled to typed tasks; an A* planner routes between object pickup and delivery; a policy gate validates every action; and a dynamically introduced obstacle triggers online route replanning.

## Run

Python 3.11+, zero third-party dependencies:

```bash
python -m embodiedbench.server
python -m unittest discover -s tests -v
```

Open `http://127.0.0.1:4203`. JSON: `GET /api/report?policy=nearest&fault=true&limit=200`.

## Features

- Verified command parsing and known-object/known-zone grounding.
- A* obstacle-aware route search and nearest vs ordered task scheduling.
- Pick/move/place state transitions with explicit gripper and battery constraints.
- Dynamic obstacle injection and automatic route replanning.
- Auditable step-by-step simulation timeline with interactive playback.
- Policy and fault-injection scenario comparisons.

## Limits

Not a real embodied foundation model, VLA, manipulation controller, real physics simulator, motion planner or safety-rated robot stack. Objects have no mass/geometry, and collision constraints are discrete cells. Do not use to control physical equipment. Real adoption would require ROS 2/Gazebo simulation, hardware validation and independent safety engineering.
