# Day 013 — Robotics Fleet Diagnostic Copilot

A browser-based telemetry inspection prototype inspired by ROS 2 mobile-robot sensor debugging.

## Features
- Load synthetic multi-sensor telemetry or import CSV.
- Validate rows using timestamp, sensor, and numeric value columns.
- Detect inter-sample gaps against a configurable expected interval.
- Flag potential numeric spikes using median absolute deviation.
- View per-sensor summaries and a time-ordered trace.
- Export a JSON diagnostic report or Markdown summary.
- All analysis happens locally in the browser.

## Run
Open index.html in a modern browser. No build step, server, or API key is required.

## CSV format
Required headers: timestamp,sensor,value. Example row: 2026-10-18T08:00:00.000Z,imu_yaw_rate,0.05

Timestamps must be parseable date-times. Values must be numeric. Rows with invalid values are skipped.

## Heuristic details
A stream gap is recorded when the adjacent timestamp difference exceeds 1.5 times the configured expected interval. Potential spikes use the median and median absolute deviation, scaled by 1.4826. Streams with zero median absolute deviation cannot produce this spike score in the current implementation.

## Limitations
One global interval and spike threshold are used across every sensor. Real robotics systems need per-sensor rates, units, timestamp synchronization checks, physically meaningful ranges, and evaluation against labeled fault data. Events are candidates, not confirmed hardware faults. This tool does not connect to a live ROS graph, actuate hardware, or repair robots.