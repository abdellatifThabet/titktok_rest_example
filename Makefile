# this is run only one time to generate the migrations folder
db-init:
	@docker-compose run api flask db init

build:
	@docker-compose build 

db-upgrade:
	@docker-compose up -d db
	@sleep 5
	@docker-compose run api flask db upgrade --directory migrations

db-migrate: build
	@docker-compose run api flask db migrate --directory migrations

run: stop build db-upgrade 
	@docker-compose up --remove-orphans

stop:
	@docker-compose down --remove-orphans