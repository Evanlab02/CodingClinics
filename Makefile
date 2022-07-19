all:
	@echo "Checking"
	@sleep 5
	@make check
	@echo "Graph"
	@sleep 5
	@make graph
	@echo "Updating"
	@sleep 5
	@make update
	@echo "Verifying"
	@sleep 5
	@make verify 
	@echo "Coverage"
	@sleep 5
	@make coverage
	@echo "Testing"
	@sleep 5
	@make test
	@echo "Building"
	@sleep 5
	@make build
	@echo "Installing"
	@sleep 5
	@make install
	@echo "Cleaning"
	@sleep 5
	@make clean


build:
	@echo "Creating Executable ..."
	@sleep 2
	@python3 -m PyInstaller --onefile code_clinic.py
	@echo "Created Exectuable"
	@sleep 2

clean: build
	@echo "Cleaning Up..."
	@sleep 1
	@pipenv clean
	@rm -r build/
	@rm -r dist/
	@rm -r code_clinic.spec
	@echo "Cleaned Up"
	@sleep 1

check:
	@echo "Checking requirements..."
	@sleep 1
	@pipenv check
	@echo "Checked requirements"
	@sleep 1

coverage:
	@echo "Running Coverage on code base tests..."
	@sleep 1
	@coverage run -m unittest discover -s testing/ -p "test_*.py"
	@coverage report 
	@rm .coverage

graph:
	@pipenv graph

install: build
	@echo "-UNSTABLE- Installing code_clinic ..."
	@sleep 1
	@sudo cp dist/code_clinic /usr/local/bin/
	@echo "-UNSTABLE- Installed code_clinic"
	@sleep 1

test:
	@echo "Testing the code base..."
	@sleep 1
	@python3 -m unittest discover -s testing/ -p "test_*.py"

update:
	@echo "Installing requirements..."
	@sleep 1
	@pip install -r files/requirements.txt
	@echo "Installed requirements"
	@sleep 1

update-env:
	@echo "Updating PIP..."
	@sleep 1
	@python -m pip install --upgrade pip
	@echo "Updated PIP"
	@sleep 1
	@echo "PIPENV - Locking..."
	@sleep 1
	@pipenv lock
	@echo "PIPENV - Locked"
	@sleep 1
	@echo "PIPENV - Updating requirements.txt..."
	@sleep 1
	@pipenv lock -r > requirements.txt
	@echo "PIPENV - Updated requirements.txt"
	@sleep 1
	@echo "PIPENV - Syncing..."
	@sleep 1
	@pipenv sync
	@echo "PIPENV - Synced"
	@sleep 1

verify:
	@echo "Verifying..."
	@sleep 1
	@pipenv verify
	@echo "Verified"
	@sleep 1

shell:
	@pipenv shell
