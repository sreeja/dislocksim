run:
	docker-compose up

run-build:
	docker-compose up --build

down:
	docker-compose down -v --remove-orphans
