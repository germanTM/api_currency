clean:##clean project temp data
	find . -type f -name '*.pyc' -delete
	find . -type f -name '*.log' -delete

install:##install dependencies requirements
	pip3 install -r requirements.txt

tests:##start tests
	python3 -m unittest

run:## run the docker container
	docker run --publish 7000:5000 apicurrency

build:
	docker build -t apicurrency .

all:##first initialization of the project
	make clean
	make install
	make build
	make tests 
	make run