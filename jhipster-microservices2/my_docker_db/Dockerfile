FROM python:3

ADD servermongo.py /

EXPOSE 27017/tcp

RUN pip3 install git+https://github.com/ajdavis/mongo-mockup-db

RUN pip install pyshark

RUN pip install pprintpp

CMD [ "python3", "-u", "servermongo.py" ]





