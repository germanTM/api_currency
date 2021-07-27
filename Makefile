clean:##clean project temp data
	find . -type f -name '*.pyc' -delete
	find . -type f -name '*.log' -delete

install:##install dependencies requirements
	pip3 install -r requirements.txt

tests:##start tests
	python3 -m unittest

run:## run the docker container
	@docker-compose run --service-ports --rm apicurrency || true

stop: ## stop Docker containers without removing them
	@docker-compose stop

rebuild: ## rebuild base Docker images
	@docker-compose down --remove-orphans
	@docker-compose build --no-cache
	

all:##first initialization of the project
	make clean
	make install 
	make tests 
	make run