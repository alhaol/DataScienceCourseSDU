docker build . -t flume:latest 

docker run --rm -it --ip 172.200.0.245 --hostname flume --network hadoop flume:latest 