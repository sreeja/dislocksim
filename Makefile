run:
	sh experiment.sh

dockrun:
	docker-compose up

dockrun-build:
	docker-compose up --build

dockdown:
	docker-compose down -v --remove-orphans