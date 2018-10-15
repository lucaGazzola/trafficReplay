FROM python:3

ADD readoperations.py /

ADD readop.sh /

ADD MongoTrafficReplay MongoTrafficReplay

RUN pip3 install git+https://github.com/Luke2691/mongo-mockup-db

RUN pip install pyshark

RUN pip install pprintpp

RUN pip3 install pymongo

CMD ./readop.sh MongoTrafficReplay/reports/Test/





