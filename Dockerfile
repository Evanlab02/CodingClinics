FROM ubuntu:latest

RUN apt-get update
RUN apt-get install python3-pip

COPY . .

RUN python -m pip install --upgrade pip
RUN pip install -r files/requirements.txt

ENTRYPOINT ["python", "code_clinic.py"]
