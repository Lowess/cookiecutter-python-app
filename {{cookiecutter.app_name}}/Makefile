### Local developement

.PHONY: dev tests lint checkstyle coverage docs

FORCE=

run:
ifeq ($(FORCE),)
	docker-compose -f docker/docker-compose.yml up
else
	docker-compose -f docker/docker-compose.yml build --no-cache
	docker-compose -f docker/docker-compose.yml up
endif

dev:
	@echo ⚙️ Setting up dev environment and dependencies...
	pip install -r requirements.txt
	pip install -e '.[dev]'
	@echo ⚙️ Setting up pre-commit hooks...
	pre-commit install
	pre-commit install --hook-type commit-msg

tests:
	$(MAKE) lint
	$(MAKE) checkstyle
	$(MAKE) coverage

lint:
	@echo 💠 Linting code...
	tox -e lint

checkstyle:
	@echo ✅ Validating checkstyle...
	tox -e checkstyle

coverage:
	@echo 🔍️  Run test coverage...
	tox -e coverage

docs:
	@echo 📚 Generate documentation using sphinx...
	tox -e docs
