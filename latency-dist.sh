docker exec -it paris tc qdisc add dev eth0 root handle 1: prio bands 16 priomap 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0

docker exec -it paris tc qdisc add dev eth0 parent 1:2 handle 2: netem delay 121ms
docker exec -it paris tc qdisc add dev eth0 parent 1:3 handle 3: netem delay 126ms
docker exec -it paris tc qdisc add dev eth0 parent 1:4 handle 4: netem delay 76ms
docker exec -it paris tc qdisc add dev eth0 parent 1:5 handle 5: netem delay 37ms

docker exec -it paris tc filter add dev eth0 parent 1:0 protocol ip u32 match ip dst 172.20.0.206 flowid 1:2
docker exec -it paris tc filter add dev eth0 parent 1:0 protocol ip u32 match ip dst 172.20.0.207 flowid 1:3
docker exec -it paris tc filter add dev eth0 parent 1:0 protocol ip u32 match ip dst 172.20.0.208 flowid 1:4
docker exec -it paris tc filter add dev eth0 parent 1:0 protocol ip u32 match ip dst 172.20.0.209 flowid 1:5

docker exec -it paris tc filter add dev eth0 parent 1:0 protocol ip u32 match ip dst 172.20.0.26 flowid 1:2
docker exec -it paris tc filter add dev eth0 parent 1:0 protocol ip u32 match ip dst 172.20.0.27 flowid 1:3
docker exec -it paris tc filter add dev eth0 parent 1:0 protocol ip u32 match ip dst 172.20.0.28 flowid 1:4
docker exec -it paris tc filter add dev eth0 parent 1:0 protocol ip u32 match ip dst 172.20.0.29 flowid 1:5

docker exec -it tokyo tc qdisc add dev eth0 root handle 1: prio bands 16 priomap 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0

docker exec -it tokyo tc qdisc add dev eth0 parent 1:2 handle 2: netem delay 121ms
docker exec -it tokyo tc qdisc add dev eth0 parent 1:3 handle 3: netem delay 38ms
docker exec -it tokyo tc qdisc add dev eth0 parent 1:4 handle 4: netem delay 181ms
docker exec -it tokyo tc qdisc add dev eth0 parent 1:5 handle 5: netem delay 102ms

docker exec -it tokyo tc filter add dev eth0 parent 1:0 protocol ip u32 match ip dst 172.20.0.205 flowid 1:2
docker exec -it tokyo tc filter add dev eth0 parent 1:0 protocol ip u32 match ip dst 172.20.0.207 flowid 1:3
docker exec -it tokyo tc filter add dev eth0 parent 1:0 protocol ip u32 match ip dst 172.20.0.208 flowid 1:4
docker exec -it tokyo tc filter add dev eth0 parent 1:0 protocol ip u32 match ip dst 172.20.0.209 flowid 1:5

docker exec -it tokyo tc filter add dev eth0 parent 1:0 protocol ip u32 match ip dst 172.20.0.25 flowid 1:2
docker exec -it tokyo tc filter add dev eth0 parent 1:0 protocol ip u32 match ip dst 172.20.0.27 flowid 1:3
docker exec -it tokyo tc filter add dev eth0 parent 1:0 protocol ip u32 match ip dst 172.20.0.28 flowid 1:4
docker exec -it tokyo tc filter add dev eth0 parent 1:0 protocol ip u32 match ip dst 172.20.0.29 flowid 1:5

docker exec -it singapore tc qdisc add dev eth0 root handle 1: prio bands 16 priomap 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0

docker exec -it singapore tc qdisc add dev eth0 parent 1:2 handle 2: netem delay 126ms
docker exec -it singapore tc qdisc add dev eth0 parent 1:3 handle 3: netem delay 38ms
docker exec -it singapore tc qdisc add dev eth0 parent 1:4 handle 4: netem delay 157ms
docker exec -it singapore tc qdisc add dev eth0 parent 1:5 handle 5: netem delay 126ms

docker exec -it singapore tc filter add dev eth0 parent 1:0 protocol ip u32 match ip dst 172.20.0.205 flowid 1:2
docker exec -it singapore tc filter add dev eth0 parent 1:0 protocol ip u32 match ip dst 172.20.0.206 flowid 1:3
docker exec -it singapore tc filter add dev eth0 parent 1:0 protocol ip u32 match ip dst 172.20.0.208 flowid 1:4
docker exec -it singapore tc filter add dev eth0 parent 1:0 protocol ip u32 match ip dst 172.20.0.209 flowid 1:5

docker exec -it singapore tc filter add dev eth0 parent 1:0 protocol ip u32 match ip dst 172.20.0.25 flowid 1:2
docker exec -it singapore tc filter add dev eth0 parent 1:0 protocol ip u32 match ip dst 172.20.0.26 flowid 1:3
docker exec -it singapore tc filter add dev eth0 parent 1:0 protocol ip u32 match ip dst 172.20.0.28 flowid 1:4
docker exec -it singapore tc filter add dev eth0 parent 1:0 protocol ip u32 match ip dst 172.20.0.29 flowid 1:5

docker exec -it capetown tc qdisc add dev eth0 root handle 1: prio bands 16 priomap 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0

docker exec -it capetown tc qdisc add dev eth0 parent 1:2 handle 2: netem delay 76ms
docker exec -it capetown tc qdisc add dev eth0 parent 1:3 handle 3: netem delay 181ms
docker exec -it capetown tc qdisc add dev eth0 parent 1:4 handle 4: netem delay 157ms
docker exec -it capetown tc qdisc add dev eth0 parent 1:5 handle 5: netem delay 107ms

docker exec -it capetown tc filter add dev eth0 parent 1:0 protocol ip u32 match ip dst 172.20.0.205 flowid 1:2
docker exec -it capetown tc filter add dev eth0 parent 1:0 protocol ip u32 match ip dst 172.20.0.206 flowid 1:3
docker exec -it capetown tc filter add dev eth0 parent 1:0 protocol ip u32 match ip dst 172.20.0.207 flowid 1:4
docker exec -it capetown tc filter add dev eth0 parent 1:0 protocol ip u32 match ip dst 172.20.0.209 flowid 1:5

docker exec -it capetown tc filter add dev eth0 parent 1:0 protocol ip u32 match ip dst 172.20.0.25 flowid 1:2
docker exec -it capetown tc filter add dev eth0 parent 1:0 protocol ip u32 match ip dst 172.20.0.26 flowid 1:3
docker exec -it capetown tc filter add dev eth0 parent 1:0 protocol ip u32 match ip dst 172.20.0.27 flowid 1:4
docker exec -it capetown tc filter add dev eth0 parent 1:0 protocol ip u32 match ip dst 172.20.0.29 flowid 1:5

docker exec -it newyork tc qdisc add dev eth0 root handle 1: prio bands 16 priomap 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0

docker exec -it newyork tc qdisc add dev eth0 parent 1:2 handle 2: netem delay 37ms
docker exec -it newyork tc qdisc add dev eth0 parent 1:3 handle 3: netem delay 102ms
docker exec -it newyork tc qdisc add dev eth0 parent 1:4 handle 4: netem delay 126ms
docker exec -it newyork tc qdisc add dev eth0 parent 1:5 handle 5: netem delay 107ms

docker exec -it newyork tc filter add dev eth0 parent 1:0 protocol ip u32 match ip dst 172.20.0.205 flowid 1:2
docker exec -it newyork tc filter add dev eth0 parent 1:0 protocol ip u32 match ip dst 172.20.0.206 flowid 1:3
docker exec -it newyork tc filter add dev eth0 parent 1:0 protocol ip u32 match ip dst 172.20.0.207 flowid 1:4
docker exec -it newyork tc filter add dev eth0 parent 1:0 protocol ip u32 match ip dst 172.20.0.208 flowid 1:5

docker exec -it newyork tc filter add dev eth0 parent 1:0 protocol ip u32 match ip dst 172.20.0.25 flowid 1:2
docker exec -it newyork tc filter add dev eth0 parent 1:0 protocol ip u32 match ip dst 172.20.0.26 flowid 1:3
docker exec -it newyork tc filter add dev eth0 parent 1:0 protocol ip u32 match ip dst 172.20.0.27 flowid 1:4
docker exec -it newyork tc filter add dev eth0 parent 1:0 protocol ip u32 match ip dst 172.20.0.28 flowid 1:5

docker exec -it zoo-paris-dist tc qdisc add dev eth0 root handle 1: prio bands 16 priomap 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0

docker exec -it zoo-paris-dist tc qdisc add dev eth0 parent 1:2 handle 2: netem delay 121ms
docker exec -it zoo-paris-dist tc qdisc add dev eth0 parent 1:3 handle 3: netem delay 126ms
docker exec -it zoo-paris-dist tc qdisc add dev eth0 parent 1:4 handle 4: netem delay 76ms
docker exec -it zoo-paris-dist tc qdisc add dev eth0 parent 1:5 handle 5: netem delay 37ms

docker exec -it zoo-paris-dist tc filter add dev eth0 parent 1:0 protocol ip u32 match ip dst 172.20.0.206 flowid 1:2
docker exec -it zoo-paris-dist tc filter add dev eth0 parent 1:0 protocol ip u32 match ip dst 172.20.0.207 flowid 1:3
docker exec -it zoo-paris-dist tc filter add dev eth0 parent 1:0 protocol ip u32 match ip dst 172.20.0.208 flowid 1:4
docker exec -it zoo-paris-dist tc filter add dev eth0 parent 1:0 protocol ip u32 match ip dst 172.20.0.209 flowid 1:5

docker exec -it zoo-paris-dist tc filter add dev eth0 parent 1:0 protocol ip u32 match ip dst 172.20.0.26 flowid 1:2
docker exec -it zoo-paris-dist tc filter add dev eth0 parent 1:0 protocol ip u32 match ip dst 172.20.0.27 flowid 1:3
docker exec -it zoo-paris-dist tc filter add dev eth0 parent 1:0 protocol ip u32 match ip dst 172.20.0.28 flowid 1:4
docker exec -it zoo-paris-dist tc filter add dev eth0 parent 1:0 protocol ip u32 match ip dst 172.20.0.29 flowid 1:5

docker exec -it zoo-tokyo-dist tc qdisc add dev eth0 root handle 1: prio bands 16 priomap 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0

docker exec -it zoo-tokyo-dist tc qdisc add dev eth0 parent 1:2 handle 2: netem delay 121ms
docker exec -it zoo-tokyo-dist tc qdisc add dev eth0 parent 1:3 handle 3: netem delay 38ms
docker exec -it zoo-tokyo-dist tc qdisc add dev eth0 parent 1:4 handle 4: netem delay 181ms
docker exec -it zoo-tokyo-dist tc qdisc add dev eth0 parent 1:5 handle 5: netem delay 102ms

docker exec -it zoo-tokyo-dist tc filter add dev eth0 parent 1:0 protocol ip u32 match ip dst 172.20.0.205 flowid 1:2
docker exec -it zoo-tokyo-dist tc filter add dev eth0 parent 1:0 protocol ip u32 match ip dst 172.20.0.207 flowid 1:3
docker exec -it zoo-tokyo-dist tc filter add dev eth0 parent 1:0 protocol ip u32 match ip dst 172.20.0.208 flowid 1:4
docker exec -it zoo-tokyo-dist tc filter add dev eth0 parent 1:0 protocol ip u32 match ip dst 172.20.0.209 flowid 1:5

docker exec -it zoo-tokyo-dist tc filter add dev eth0 parent 1:0 protocol ip u32 match ip dst 172.20.0.25 flowid 1:2
docker exec -it zoo-tokyo-dist tc filter add dev eth0 parent 1:0 protocol ip u32 match ip dst 172.20.0.27 flowid 1:3
docker exec -it zoo-tokyo-dist tc filter add dev eth0 parent 1:0 protocol ip u32 match ip dst 172.20.0.28 flowid 1:4
docker exec -it zoo-tokyo-dist tc filter add dev eth0 parent 1:0 protocol ip u32 match ip dst 172.20.0.29 flowid 1:5

docker exec -it zoo-singapore-dist tc qdisc add dev eth0 root handle 1: prio bands 16 priomap 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0

docker exec -it zoo-singapore-dist tc qdisc add dev eth0 parent 1:2 handle 2: netem delay 126ms
docker exec -it zoo-singapore-dist tc qdisc add dev eth0 parent 1:3 handle 3: netem delay 38ms
docker exec -it zoo-singapore-dist tc qdisc add dev eth0 parent 1:4 handle 4: netem delay 157ms
docker exec -it zoo-singapore-dist tc qdisc add dev eth0 parent 1:5 handle 5: netem delay 126ms

docker exec -it zoo-singapore-dist tc filter add dev eth0 parent 1:0 protocol ip u32 match ip dst 172.20.0.205 flowid 1:2
docker exec -it zoo-singapore-dist tc filter add dev eth0 parent 1:0 protocol ip u32 match ip dst 172.20.0.206 flowid 1:3
docker exec -it zoo-singapore-dist tc filter add dev eth0 parent 1:0 protocol ip u32 match ip dst 172.20.0.208 flowid 1:4
docker exec -it zoo-singapore-dist tc filter add dev eth0 parent 1:0 protocol ip u32 match ip dst 172.20.0.209 flowid 1:5

docker exec -it zoo-singapore-dist tc filter add dev eth0 parent 1:0 protocol ip u32 match ip dst 172.20.0.25 flowid 1:2
docker exec -it zoo-singapore-dist tc filter add dev eth0 parent 1:0 protocol ip u32 match ip dst 172.20.0.26 flowid 1:3
docker exec -it zoo-singapore-dist tc filter add dev eth0 parent 1:0 protocol ip u32 match ip dst 172.20.0.28 flowid 1:4
docker exec -it zoo-singapore-dist tc filter add dev eth0 parent 1:0 protocol ip u32 match ip dst 172.20.0.29 flowid 1:5

docker exec -it zoo-capetown-dist tc qdisc add dev eth0 root handle 1: prio bands 16 priomap 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0

docker exec -it zoo-capetown-dist tc qdisc add dev eth0 parent 1:2 handle 2: netem delay 76ms
docker exec -it zoo-capetown-dist tc qdisc add dev eth0 parent 1:3 handle 3: netem delay 181ms
docker exec -it zoo-capetown-dist tc qdisc add dev eth0 parent 1:4 handle 4: netem delay 157ms
docker exec -it zoo-capetown-dist tc qdisc add dev eth0 parent 1:5 handle 5: netem delay 107ms

docker exec -it zoo-capetown-dist tc filter add dev eth0 parent 1:0 protocol ip u32 match ip dst 172.20.0.205 flowid 1:2
docker exec -it zoo-capetown-dist tc filter add dev eth0 parent 1:0 protocol ip u32 match ip dst 172.20.0.206 flowid 1:3
docker exec -it zoo-capetown-dist tc filter add dev eth0 parent 1:0 protocol ip u32 match ip dst 172.20.0.207 flowid 1:4
docker exec -it zoo-capetown-dist tc filter add dev eth0 parent 1:0 protocol ip u32 match ip dst 172.20.0.209 flowid 1:5

docker exec -it zoo-capetown-dist tc filter add dev eth0 parent 1:0 protocol ip u32 match ip dst 172.20.0.25 flowid 1:2
docker exec -it zoo-capetown-dist tc filter add dev eth0 parent 1:0 protocol ip u32 match ip dst 172.20.0.26 flowid 1:3
docker exec -it zoo-capetown-dist tc filter add dev eth0 parent 1:0 protocol ip u32 match ip dst 172.20.0.27 flowid 1:4
docker exec -it zoo-capetown-dist tc filter add dev eth0 parent 1:0 protocol ip u32 match ip dst 172.20.0.29 flowid 1:5

docker exec -it zoo-newyork-dist tc qdisc add dev eth0 root handle 1: prio bands 16 priomap 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0

docker exec -it zoo-newyork-dist tc qdisc add dev eth0 parent 1:2 handle 2: netem delay 37ms
docker exec -it zoo-newyork-dist tc qdisc add dev eth0 parent 1:3 handle 3: netem delay 102ms
docker exec -it zoo-newyork-dist tc qdisc add dev eth0 parent 1:4 handle 4: netem delay 126ms
docker exec -it zoo-newyork-dist tc qdisc add dev eth0 parent 1:5 handle 5: netem delay 107ms

docker exec -it zoo-newyork-dist tc filter add dev eth0 parent 1:0 protocol ip u32 match ip dst 172.20.0.205 flowid 1:2
docker exec -it zoo-newyork-dist tc filter add dev eth0 parent 1:0 protocol ip u32 match ip dst 172.20.0.206 flowid 1:3
docker exec -it zoo-newyork-dist tc filter add dev eth0 parent 1:0 protocol ip u32 match ip dst 172.20.0.207 flowid 1:4
docker exec -it zoo-newyork-dist tc filter add dev eth0 parent 1:0 protocol ip u32 match ip dst 172.20.0.208 flowid 1:5

docker exec -it zoo-newyork-dist tc filter add dev eth0 parent 1:0 protocol ip u32 match ip dst 172.20.0.25 flowid 1:2
docker exec -it zoo-newyork-dist tc filter add dev eth0 parent 1:0 protocol ip u32 match ip dst 172.20.0.26 flowid 1:3
docker exec -it zoo-newyork-dist tc filter add dev eth0 parent 1:0 protocol ip u32 match ip dst 172.20.0.27 flowid 1:4
docker exec -it zoo-newyork-dist tc filter add dev eth0 parent 1:0 protocol ip u32 match ip dst 172.20.0.28 flowid 1:5