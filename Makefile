

format: 
	@echo "Formatting code..."
	@black .
	@isort .

seed:
	@echo "Seeding database..."
	@python -m seeds.seed

migration:
	@echo "Creating new migration..."
	@flask db migrate -m "$(msg)"

migrate:
	@echo "Applying migrations..."
	@flask db upgrade

migrate-down:
	@echo "Rolling back last migration..."
	@flask db downgrade -- -1