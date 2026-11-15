# Safety boundaries
Treat model output, player text and retrieved lore as untrusted. Keep state mutation in trusted server code. Reject missing evidence and stale state. Revalidate at execution time.