## 2026-06-30 - ChessAiBot V0.1A Engineering Foundation

Today I started the initial engineering foundation for ChessAiBot.

The main focus was not chess logic yet, but setting up the project as a local-first enterprise-style Python software system. I created the basic project structure, including `src/`, `tests/`, `scripts/`, `documents/`, `notes/`, and `.github/workflows/`.

I added initial configuration files such as `pyproject.toml`, `requirements.txt`, `requirements-dev.txt`, `Makefile`, and `docker-compose.yml`. I also added basic config and utility modules for settings, logging, exceptions, and timing.

GitHub Actions was added for the test workflow. The first CI run had issues: the workflow initially did not run jobs correctly, then failed because `requirements.txt` was misspelled. After fixing the dependency file name and adding a minimal pytest smoke test, the test workflow became stable.

Current result:

- Project structure is created.
- Python dependency files are prepared.
- Basic settings and utility modules exist.
- Pytest can collect and run the initial smoke test.
- Local test result: `1 passed`.
- GitHub Actions test workflow is now ready for the next stage.

——————————————————————————————————————————————————————————————
# Start

docker compose up -d

# Check status

docker compose ps

# Run tests

docker compose exec app python -m pytest

# Enter the container

docker compose exec app bash

# Stop and keep the database

docker compose down

# Build and start the full environment

docker compose up -d --build

# Check container status

docker compose ps

# View application logs

docker compose logs app

# View MySQL logs

docker compose logs mysql

# Run tests inside the application container

docker compose exec app python -m pytest

# Enter the application container

docker compose exec app bash

# Restart the environment

docker compose down
docker compose up -d --build

# Stop the environment and keep database data

docker compose down
——————————————————————————————————————————————————————————————


## 2026-07-17 - ChessAiBot V0.1B–V0.1C Local Environment Completion

The V0.1B–V0.1C development stage focused on completing and stabilizing the full local development environment for ChessAiBot.

The main difficulty during this stage was setting up the local Docker and MySQL environment. The initial setup did not run smoothly because some required configuration files and settings were incomplete or incorrectly structured. This caused several startup and validation errors before the application could connect to the database successfully.

One of the main issues came from the `docker-compose.yml` configuration. The MySQL `healthcheck` section was not defined as a valid YAML mapping, which caused Docker Compose validation to fail before any containers could start. After correcting the YAML structure and reviewing the related environment variables, ports, database credentials, and service dependencies, Docker Compose was able to build and start the full environment correctly.

The environment was then tested through repeated container rebuilds, startup checks, database initialization, and Python test execution. The application container and MySQL container can now run together, and the Python application is able to use the local database environment as expected.

Current result:

- Docker Compose configuration is valid.
- The Python application image can be built successfully.
- The MySQL container starts and initializes correctly.
- The application and database containers can run together.
- Database connection settings are correctly configured.
- Environment variables and local ports are aligned.
- Basic tests and environment checks run successfully.
- The environment remains stable after container restarts and rebuilds.
- The project is ready to begin the main Python code foundation and chess logic development.

This stage also showed that environment errors do not always come from the application code itself. Missing files, invalid YAML structure, incorrect environment variables, port mappings, and service startup order can all prevent a local system from running correctly. Reading terminal output carefully and checking each layer separately made it possible to identify and resolve these issues.

The core direction of ChessAiBot remains unchanged. It is still a local-first Python application using Docker and MySQL for local engineering support. It is not being developed as a WebApp, SaaS platform, cloud service, or online chess room system.

The V0.1A–V0.1C engineering environment is now complete, so the next stage can focus on the Python-based code architecture, chess board representation, legal move handling, AI algorithms, testing, logging, benchmarks, and result reports.
