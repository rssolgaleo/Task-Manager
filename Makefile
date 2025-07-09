install:
	uv sync 

migrate:
	uv run python manage.py migrate

collectstatic:
	uv run python manage.py collectstatic --no-input

run:
	uv run python manage.py runserver

render-start:
	gunicorn task_manager.wsgi

build:
	chmod +x ./build.sh
	./build.sh

test:
	pytest

reset_migrations:
	find . -path "*/migrations/*.py" -not -name "__init__.py" -delete
	find . -path "*/migrations/*.pyc" -delete
	python manage.py makemigrations
	python manage.py migrate --fake-initial --noinput