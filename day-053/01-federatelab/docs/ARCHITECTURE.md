# Architecture

Nine independently generated synthetic client shards → local SGD over a two-feature logistic model → weight deltas → optional two-client sign-inversion attack → FedAvg, coordinate median or coordinate trimmed mean → round-by-round global model update → independent synthetic holdout scoring → JSON API and interactive dashboard.

All three methods share the same client shards and training batches for a given seed. Only one aggregation rule changes at a time. No external communications occur: this is a single-process simulator.
