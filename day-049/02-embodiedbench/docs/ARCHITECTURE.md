# Architecture
Strict command grammar → typed goal set → task selection → A* navigation → action guard (move/pick/place) → authoritative world-state mutation → event log and snapshots → browser replay. A dynamic obstacle is injected at a deterministic tick to evaluate replanning.
