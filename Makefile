run:
	sh simulator.sh

dockrun-cent:
	docker-compose -f docker-compose.yml -f centralised.yml up

dockbuild-cent:
	docker-compose -f docker-compose.yml -f centralised.yml up --build

dockdown-cent:
	docker-compose -f docker-compose.yml -f centralised.yml down -v --remove-orphans

dockrun-clust:
	docker-compose -f docker-compose.yml -f clustered.yml up

dockbuild-clust:
	docker-compose -f docker-compose.yml -f clustered.yml up --build

dockdown-clust:
	docker-compose -f docker-compose.yml -f clustered.yml down -v --remove-orphans

dockrun-dist:
	docker-compose -f docker-compose.yml -f distributed.yml up

dockbuild-dist:
	docker-compose -f docker-compose.yml -f distributed.yml up --build

dockdown-dist:
	docker-compose -f docker-compose.yml -f distributed.yml down -v --remove-orphans