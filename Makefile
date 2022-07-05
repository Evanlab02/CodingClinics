all:
	make build
	make coverage
	make test
	make clean

build:
	@echo "Creating Exectuable ..."
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

coverage:
	@echo "Running Coverage on code base tests..."
	@sleep 1
	@coverage run -m unittest discover -s testing/ -p "test_*.py"
	@coverage report 
	@rm .coverage

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

requirements:
	@echo "Installing requirements..."
	@sleep 1
	@pip install -r files/requirements.txt
	@echo "Installed requirements"
	@sleep 1

update:
	@echo "Updating PIP..."
	@sleep 1
	@python -m pip install --upgrade pip
	@echo "Updated PIP"
	@sleep 1
