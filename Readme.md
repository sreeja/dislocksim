This is the repository containing the concurrency control experiments.

# Architecture
The structure of the experimental system is divided into layers:
- Network Layer
- Application Layer
- Lock service
- Workload Layer

## Network Layer
- Latency matrix

## Application Layer
- Application name and version

## Lock service
Lock service needs configuration for each lock. It allows mix between different locking protocols.
- Lock type: Mutex or shared/exclusive
- Granularity: Navigating the granularity matrix (Given the conflicts, construct a granularity matrix. To start with, it is given manually.)
- Lock placement: Starting with centralized vs distributed. Hierarchical to follow.

## Workload
Workload should be parametrized by a matrix giving call frequency of each method at each replica

# Experimental run

## Micro experiment
Start system \\
set configuration \\
run experiment \\
stop system

## Mini experiment
For each workload, do micro experiment

## Experiment
For each lock configuration, do mini experiment

## Entire run
For each application, do experiment