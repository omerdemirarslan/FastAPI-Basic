### MakeFile
up-build:
	docker-compose up --build

up:
	docker-compose up -d

down:
	docker-compose down

build:
	docker-compose build

run:
	/usr/bin/python3 main.py --debug=True --reload=True

logs:
	docker-compose logs -f
