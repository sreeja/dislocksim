docker exec -it locker-paris tc qdisc add dev eth0 root handle 1: prio bands 16 priomap 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0

docker exec -it locker-paris tc qdisc add dev eth0 parent 1:2 handle 2: netem delay 121ms
docker exec -it locker-paris tc qdisc add dev eth0 parent 1:3 handle 3: netem delay 126ms
docker exec -it locker-paris tc qdisc add dev eth0 parent 1:4 handle 4: netem delay 76ms
docker exec -it locker-paris tc qdisc add dev eth0 parent 1:5 handle 5: netem delay 37ms

docker exec -it locker-paris tc filter add dev eth0 parent 1:0 protocol ip u32 match ip dst 172.20.0.16 flowid 1:2
docker exec -it locker-paris tc filter add dev eth0 parent 1:0 protocol ip u32 match ip dst 172.20.0.17 flowid 1:3
docker exec -it locker-paris tc filter add dev eth0 parent 1:0 protocol ip u32 match ip dst 172.20.0.18 flowid 1:4
docker exec -it locker-paris tc filter add dev eth0 parent 1:0 protocol ip u32 match ip dst 172.20.0.19 flowid 1:5

docker exec -it locker-tokyo tc qdisc add dev eth0 root handle 1: prio bands 16 priomap 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0

docker exec -it locker-tokyo tc qdisc add dev eth0 parent 1:2 handle 2: netem delay 121ms
docker exec -it locker-tokyo tc qdisc add dev eth0 parent 1:3 handle 3: netem delay 38ms
docker exec -it locker-tokyo tc qdisc add dev eth0 parent 1:4 handle 4: netem delay 181ms
docker exec -it locker-tokyo tc qdisc add dev eth0 parent 1:5 handle 5: netem delay 102ms

docker exec -it locker-tokyo tc filter add dev eth0 parent 1:0 protocol ip u32 match ip dst 172.20.0.15 flowid 1:2
docker exec -it locker-tokyo tc filter add dev eth0 parent 1:0 protocol ip u32 match ip dst 172.20.0.5 flowid 1:2
docker exec -it locker-tokyo tc filter add dev eth0 parent 1:0 protocol ip u32 match ip dst 172.20.0.17 flowid 1:3
docker exec -it locker-tokyo tc filter add dev eth0 parent 1:0 protocol ip u32 match ip dst 172.20.0.18 flowid 1:4
docker exec -it locker-tokyo tc filter add dev eth0 parent 1:0 protocol ip u32 match ip dst 172.20.0.19 flowid 1:5

docker exec -it locker-singapore tc qdisc add dev eth0 root handle 1: prio bands 16 priomap 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0

docker exec -it locker-singapore tc qdisc add dev eth0 parent 1:2 handle 2: netem delay 38ms
docker exec -it locker-singapore tc qdisc add dev eth0 parent 1:3 handle 3: netem delay 126ms
docker exec -it locker-singapore tc qdisc add dev eth0 parent 1:4 handle 4: netem delay 157ms
docker exec -it locker-singapore tc qdisc add dev eth0 parent 1:5 handle 5: netem delay 126ms

docker exec -it locker-singapore tc filter add dev eth0 parent 1:0 protocol ip u32 match ip dst 172.20.0.16 flowid 1:2
docker exec -it locker-singapore tc filter add dev eth0 parent 1:0 protocol ip u32 match ip dst 172.20.0.15 flowid 1:3
docker exec -it locker-singapore tc filter add dev eth0 parent 1:0 protocol ip u32 match ip dst 172.20.0.5 flowid 1:3
docker exec -it locker-singapore tc filter add dev eth0 parent 1:0 protocol ip u32 match ip dst 172.20.0.18 flowid 1:4
docker exec -it locker-singapore tc filter add dev eth0 parent 1:0 protocol ip u32 match ip dst 172.20.0.19 flowid 1:5

docker exec -it locker-capetown tc qdisc add dev eth0 root handle 1: prio bands 16 priomap 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0

docker exec -it locker-capetown tc qdisc add dev eth0 parent 1:2 handle 2: netem delay 181ms
docker exec -it locker-capetown tc qdisc add dev eth0 parent 1:3 handle 3: netem delay 157ms
docker exec -it locker-capetown tc qdisc add dev eth0 parent 1:4 handle 4: netem delay 76ms
docker exec -it locker-capetown tc qdisc add dev eth0 parent 1:5 handle 5: netem delay 107ms

docker exec -it locker-capetown tc filter add dev eth0 parent 1:0 protocol ip u32 match ip dst 172.20.0.16 flowid 1:2
docker exec -it locker-capetown tc filter add dev eth0 parent 1:0 protocol ip u32 match ip dst 172.20.0.17 flowid 1:3
docker exec -it locker-capetown tc filter add dev eth0 parent 1:0 protocol ip u32 match ip dst 172.20.0.15 flowid 1:4
docker exec -it locker-capetown tc filter add dev eth0 parent 1:0 protocol ip u32 match ip dst 172.20.0.5 flowid 1:4
docker exec -it locker-capetown tc filter add dev eth0 parent 1:0 protocol ip u32 match ip dst 172.20.0.19 flowid 1:5

docker exec -it locker-newyork tc qdisc add dev eth0 root handle 1: prio bands 16 priomap 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0

docker exec -it locker-newyork tc qdisc add dev eth0 parent 1:2 handle 2: netem delay 102ms
docker exec -it locker-newyork tc qdisc add dev eth0 parent 1:3 handle 3: netem delay 126ms
docker exec -it locker-newyork tc qdisc add dev eth0 parent 1:4 handle 4: netem delay 107ms
docker exec -it locker-newyork tc qdisc add dev eth0 parent 1:5 handle 5: netem delay 37ms

docker exec -it locker-newyork tc filter add dev eth0 parent 1:0 protocol ip u32 match ip dst 172.20.0.16 flowid 1:2
docker exec -it locker-newyork tc filter add dev eth0 parent 1:0 protocol ip u32 match ip dst 172.20.0.17 flowid 1:3
docker exec -it locker-newyork tc filter add dev eth0 parent 1:0 protocol ip u32 match ip dst 172.20.0.18 flowid 1:4
docker exec -it locker-newyork tc filter add dev eth0 parent 1:0 protocol ip u32 match ip dst 172.20.0.15 flowid 1:5
docker exec -it locker-newyork tc filter add dev eth0 parent 1:0 protocol ip u32 match ip dst 172.20.0.5 flowid 1:5

docker exec -it zoo-paris tc qdisc add dev eth0 root handle 1: prio bands 16 priomap 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0

docker exec -it zoo-paris tc qdisc add dev eth0 parent 1:2 handle 2: netem delay 121ms
docker exec -it zoo-paris tc qdisc add dev eth0 parent 1:3 handle 3: netem delay 126ms
docker exec -it zoo-paris tc qdisc add dev eth0 parent 1:4 handle 4: netem delay 76ms
docker exec -it zoo-paris tc qdisc add dev eth0 parent 1:5 handle 5: netem delay 37ms

docker exec -it zoo-paris tc filter add dev eth0 parent 1:0 protocol ip u32 match ip dst 172.20.0.16 flowid 1:2
docker exec -it zoo-paris tc filter add dev eth0 parent 1:0 protocol ip u32 match ip dst 172.20.0.17 flowid 1:3
docker exec -it zoo-paris tc filter add dev eth0 parent 1:0 protocol ip u32 match ip dst 172.20.0.18 flowid 1:4
docker exec -it zoo-paris tc filter add dev eth0 parent 1:0 protocol ip u32 match ip dst 172.20.0.19 flowid 1:5

docker exec -it locker-paris ping -c 4 locker-tokyo
docker exec -it locker-paris ping -c 4 locker-singapore
docker exec -it locker-paris ping -c 4 locker-capetown
docker exec -it locker-paris ping -c 4 locker-newyork
docker exec -it locker-paris ping -c 4 zoo-paris

docker exec -it locker-tokyo ping -c 4 locker-paris
docker exec -it locker-tokyo ping -c 4 locker-singapore
docker exec -it locker-tokyo ping -c 4 locker-capetown
docker exec -it locker-tokyo ping -c 4 locker-newyork
docker exec -it locker-tokyo ping -c 4 zoo-paris

docker exec -it locker-singapore ping -c 4 locker-tokyo
docker exec -it locker-singapore ping -c 4 locker-paris
docker exec -it locker-singapore ping -c 4 locker-capetown
docker exec -it locker-singapore ping -c 4 locker-newyork
docker exec -it locker-singapore ping -c 4 zoo-paris

docker exec -it locker-capetown ping -c 4 locker-tokyo
docker exec -it locker-capetown ping -c 4 locker-singapore
docker exec -it locker-capetown ping -c 4 locker-paris
docker exec -it locker-capetown ping -c 4 locker-newyork
docker exec -it locker-capetown ping -c 4 zoo-paris

docker exec -it locker-newyork ping -c 4 locker-tokyo
docker exec -it locker-newyork ping -c 4 locker-singapore
docker exec -it locker-newyork ping -c 4 locker-capetown
docker exec -it locker-newyork ping -c 4 locker-paris
docker exec -it locker-newyork ping -c 4 zoo-paris

docker exec -it zoo-paris ping -c 4 locker-tokyo
docker exec -it zoo-paris ping -c 4 locker-singapore
docker exec -it zoo-paris ping -c 4 locker-capetown
docker exec -it zoo-paris ping -c 4 locker-newyork
docker exec -it zoo-paris ping -c 4 locker-paris