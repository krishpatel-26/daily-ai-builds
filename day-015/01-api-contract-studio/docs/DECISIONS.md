# Design decisions

Browser-only processing keeps the first version easy to run and avoids transmitting customer payloads.

A documented schema subset makes behavior inspectable; production should use a maintained validator.

A heuristic diff highlights common changes but cannot prove compatibility.

Case generation creates reproducible examples without credentials or a live API.