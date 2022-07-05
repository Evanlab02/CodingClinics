FROM ubuntu:latest

RUN apt-get update
RUN apt-get install python3-pip
RUN apt-get install make

COPY . .

RUN python -m pip install --upgrade pip
RUN pip install -r files/requirements.txt

ENTRYPOINT ["python", "code_clinic.py"]
