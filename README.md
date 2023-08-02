# Fetch Rewards: ETL off a SQS Queue
Project demonstrate how to read from SQS and push to postgres in simple way. During the push we make sure that the PII are also ciphered for security compliance

## Objective

1. Read JSON data AWS SQS Queue.
2. Mask the PII fields(device_id and ip)
3. Write each record to a Postgres database.

## Pre-Requisites
1. Docker and Docker compose
2. Python3, Python3-devel and python3-venv
3. python lib psycopg2-binary, awscli-local


## Running the application
1. [Install docker](https://docs.docker.com/engine/install/)
2. [Install docker compose](https://docs.docker.com/compose/install/linux/#install-the-plugin-manually)
3. On the root folder of the project, start the localstack and postgres using docker-compose
	```bash
	docker compose up -d
	```
4. setup python venv and install required modules
	```bash
	python3 -m venv .venv
	source .venv/bin/activate
	pip install -r requirements.txt
	```
5. Run the application
	```bash
		python src/etl.py
	```



## Project Structure

	./
	│
	├── src
	│   ├── __init__.py
	│   ├── config.py
	│   ├── db_handler.py
	│   ├── sqs_handler.py
	│   ├── etl.py
	│   └── masker.py
	├── tests
	│   ├── __init__.py
	│   └── test_etl.py
	│
	├── README.md
	├── requirements.txt
	└── docker-compose.yml

	src/config.py: Common configuration like env variables and maps.
	src/db_handler.py: Handling of postgres ops.
	src/etl.py: Entry point to the python app. Defining how the queue is read and how postgres table is updated.
	src/masker.py: Defines a function to mask PII data in a record.
	tests/test_etl.py: Contains test cases for the ETL process.
	requirements.txt: Specifies the Python packages required to run the application.
	docker-compose.yml: Defines the services (LocalStack and Postgres) that make up the application.



## Troubleshooting
Delete the table
```
docker exec pii_masking-postgres-1 psql -U postgres -c 'drop table user_logins'
```