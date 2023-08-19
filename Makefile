install:
	python3 -m pip install --upgrade pip &&\
		python3 -m pip install -r ./requirements.txt

lint:
	pylint --disable=R,C ./src ./tests

format: 
	black .

test:
	python3 -m pytest -vvvs tests/