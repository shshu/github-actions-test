install:
	python3 -m pip install --upgrade pip &&\
		python3 -m pip install -r ./requirements.txt

lint:
	python3 -m pylint --disable=R,C ./src

format: 
	python3 -m black .

test:
	python3 -m pytest -vvvs src/tests/