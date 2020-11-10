run:
	sh simulator.sh

dockrun:
	docker-compose -f docker-compose.yml up

dockbuild:
	docker-compose -f docker-compose.yml --build

dockdown:
	docker-compose -f docker-compose.yml down -v --remove-orphans
