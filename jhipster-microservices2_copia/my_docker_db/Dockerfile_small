FROM python:3

ADD servermongo.py /

RUN pip3 install git+https://github.com/Luke2691/mongo-mockup-db

RUN pip install pyshark

RUN pip install pprintpp

COPY docker-entrypoint.sh /usr/local/bin/
RUN ln -s usr/local/bin/docker-entrypoint.sh /entrypoint.sh # backwards compat
ENTRYPOINT ["docker-entrypoint.sh"]

EXPOSE 37379

CMD ["python3", "-u", "servermongo.py"]





