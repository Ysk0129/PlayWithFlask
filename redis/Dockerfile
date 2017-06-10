FROM centos:7.3.1611
ADD . /work
WORKDIR /work
EXPOSE 6379

RUN yum -y update
RUN yum -y install epel-release
RUN yum -y install redis

RUN sed -i -e "s/daemonize no/daemonize yes/g" /etc/redis.conf
CMD bash -c "redis-server /etc/redis.conf && cat evaluation_dictionary.txt | redis-cli --pipe --raw && /bin/bash"
