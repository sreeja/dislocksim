This is a simulator to measure performance of distributed locks.

# Architecture
The structure of the simulator is divided into layers:
- Network Layer
- Application Layer
- Lock service

## Network Layer
Ideally, this layer simply requires the following as an input:
- Latency matrix
Since the automation is yet to be implemented, the latency is to be simulated using scripts.

## Application Layer
This layer requires a json file containing the execution time for each operation in ms.

## Lock service
Lock service needs configuration for each lock. 
- Lock type: Mutex or shared/exclusive
- Granularity: Navigating the granularity matrix (Given the conflicts, construct a granularity matrix. To start with, it is given manually.)
- Lock placement: centralized, clustered and distributed. 
