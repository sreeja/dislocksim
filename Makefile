run:
	sh simulator.sh

dockrun-cent:
	docker-compose -f docker-compose.centralised.yml up

dockbuild-cent:
	docker-compose -f docker-compose.centralised.yml up --build

dockdown-cent:
	docker-compose -f docker-compose.centralised.yml down -v --remove-orphans

dockrun-clust:
	docker-compose -f docker-compose.clustered.yml up

dockbuild-clust:
	docker-compose -f docker-compose.clustered.yml up --build

dockdown-clust:
	docker-compose -f docker-compose.clustered.yml down -v --remove-orphans

dockrun-dist:
	docker-compose -f docker-compose.distributed.yml up

dockbuild-dist:
	docker-compose -f docker-compose.distributed.yml up --build

dockdown-dist:
	docker-compose -f docker-compose.distributed.yml down -v --remove-orphans