FROM ubuntu

RUN apt-get update

RUN apt-get install nodejs -y npm

RUN apt-get install -y npm

RUN npm install -g npm

RUN npm install -g mountebank

RUN apt-get install -y curl

HEALTHCHECK --interval=30s --timeout=30s CMD curl -f http://localhost:8888/actuator/health || exit 1

EXPOSE 8888

CMD mb 





