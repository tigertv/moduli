.PHONY: run clean

run: main.py
	python ./main.py
run3: main.py
	python3 ./main.py
clean:
	rm -rf *.pyc
	find . -name "*.pyc" -type f -delete
	find . -name "__pycache__" -type d -delete
