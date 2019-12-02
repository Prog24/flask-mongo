.PHONY: default status start stop restart build log kill ash

default:
	@cat ./Makefile

status:
	@docker-compose ps

start:
	@docker-compose up -d

stop:
	@docker-compose down

restart:
	@docker-compose restart

build:
	@docker-compose build

logs:
	@docker-compose logs api

kill:
	@docker-compose rm -sf

ash:
	@docker-compose exec api ash