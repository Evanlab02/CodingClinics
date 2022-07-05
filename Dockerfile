FROM ubuntu:latest

RUN apt-get update
RUN apt-get -y install python3.10
RUN apt-get -y install python3-pip
RUN apt-get -y install make

COPY . .

RUN python -m pip install --upgrade pip
RUN pip install -r files/requirements.txt

ENTRYPOINT ["python", "code_clinic.py"]
