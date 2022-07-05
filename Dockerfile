FROM ubuntu:latest

RUN apt-get update
RUN apt-get install python3

ADD dist/code_clinic src/code_clinic

RUN chmod +X src/code_clinic

WORKDIR /src
CMD ["code_clinic", "help"]