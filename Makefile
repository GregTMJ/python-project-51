install:
	poetry install

build:
	poetry build

publish:
	poetry publish --dry-run

package-install:
	python -m pip install --force-reinstall dist/*.whl

lint:
	poetry run flake8 page_loader

test:
	poetry run pytest tests

test-coverage:
	poetry run pytest --cov=page_loader --cov-report xml tests

page_loader:
	poetry run page-loader