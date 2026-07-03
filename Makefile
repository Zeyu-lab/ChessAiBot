.PHONY: install test test-db db-up db-down db-reset db-logs db-shell db-check backend-check tools-up

install:
	python -m pip install -r requirements.txt -r requirements-dev.txt

test:
	PYTHONPATH=src pytest tests/unit

test-db:
	PYTHONPATH=src pytest tests/integration -m integration

db-up:
	docker compose up -d mysql

db-down:
	docker compose down

db-reset:
	docker compose down -v
	docker compose up -d mysql

db-logs:
	docker compose logs -f mysql

db-shell:
	docker compose exec mysql sh -lc 'mysql -u"$$MYSQL_USER" -p"$$MYSQL_PASSWORD" "$$MYSQL_DATABASE"'

db-check:
	PYTHONPATH=src python scripts/check_db.py

backend-check:
	docker compose run --rm backend

tools-up:
	docker compose --profile tools up -d