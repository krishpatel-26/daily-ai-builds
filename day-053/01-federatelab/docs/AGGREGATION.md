# Aggregation methods

FedAvg: arithmetic mean of equally weighted client updates. Coordinate median: independently take the median per model coordinate. Coordinate trimmed mean: sort each coordinate, remove the two largest and two smallest values, and mean the remainder. These do not represent all federated methods and have no universal adversarial guarantees. Client updates are not weighted by dataset size because all shards have equal cardinality in the demo.
