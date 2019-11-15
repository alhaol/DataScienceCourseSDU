docker build . -t consumer:latest 
docker run --rm --ip 172.200.1.240 --hostname consumer --network kafkaNetwork consumer:latest