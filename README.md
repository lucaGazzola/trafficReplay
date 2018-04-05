# TrafficReplay

A simple environment to replay the interaction between microservices that run on docker containers

### Prerequisites

jdk8 `apt install default-jdk`

git `apt install git`

docker - docker-compose `apt install docker`

tshark `apt install tshark`

nodejs - npm (https://askubuntu.com/questions/594656/how-to-install-the-latest-versions-of-nodejs-and-npm) 

yarn (https://yarnpkg.com/lang/en/docs/install/#linux-tab)

jhipster (installation instructions under "Install jHipster 4": https://developer.okta.com/blog/2017/06/20/develop-microservices-with-jhipster) 

python 3

python libs:

pyshark 

`apt install python3-pip`

`pip3 install pyshark`

## Getting Started

We will use a sample microservice application build with the jHipster framework. (more information here: http://www.jhipster.tech/docker-hub/)

First clone the jHipster docker hub project somewhere with:

  `git clone https://github.com/jhipster/jhipster-docker-hub`
  
you can run the 3 microservices (registry, gateway, bank account) with:

  `docker-compose -f jhipster-sample-microservices/prod/prod.yml up`
  
you should now be able to access the application at `localhost:8080`, you can also see the jhipster registry at `localhost:8761`
  
## Capturing traffic

Open another terminal and run `brctl show`. you should see a bridge interface with 5 docker container running on it ( registry, gateway, gateway database, bank account, bank account database).

now run `tcpdump -i interface -w capture.pcap` where `interface` is the name of the interface where the container are running.

You can now use the application normally (add bank accounts for example) while the traffic between containers is captured in the `capture.pcap` file.


## Replaying traffic

You can use the scripts in this repository to replay the captured traffic in the `capture.pcap` file. The current version can only send traffic to the bank account microservice, which runs on port 8081.

first run the script `split.sh` to split a single capture file in streams:

  `./split.sh capture.pcap streamsDirectory`
  
in `streamsDirectory` you now have the single-stream capture files.

to generate a python replay script for each capture file use:

  `./generate_replay_scripts.sh streamsDirectory`
  
This will use `pyshark_test.py` to generate a replay script for each capture file in `streamsDirectory`. However, only the replay scripts for the streams that contain traffic with the microservice which run on 8081 will work.

You can now replay the traffic (if the microservice application is running) by going into `streamsDirectory` and launching:

  `python3 stream-X.cap_replay.py`
  
## Issues

#TODO
at line `91` in `pyshark_test` the string `packet.http.file_data` sometimes presents escaped unicode characters `\xa` : need to handle this case
  
