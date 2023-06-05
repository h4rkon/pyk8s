test: check
	CI/test.sh

watch: check
	CI/watch.sh

init:
	CI/init.sh

check:
	CI/check.sh

coverage: check
	CI/coverage.sh

build: coverage
	CI/build.sh

run:
	uvicorn python_boilerplate.main:app --reload

clean:
	CI/clean.sh