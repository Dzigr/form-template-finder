req:
	poetry export --without-hashes --format=requirements.txt > requirements.txt

env:
	cp .env.template .env

lint:
	poetry run ruff .

prepare: env req
	docker-compose build

start:
	docker-compose up -d
	
stop:
	docker-compose down

test:
	docker-compose -f docker-compose.test.yml up --build

clean:
	docker-compose down --remove-orphans