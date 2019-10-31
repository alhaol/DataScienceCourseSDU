# Data Science Course at SDU

The course/repo is run/maintained by Jakob Hviid <jah@mmmi.sdu.dk> and Fisayo Caleb Sangogboye <fsan@mmmi.sdu.dk>.

## Setup

In the root directory run the following from an administrative terminal:

```bash
docker-compose up -d
addroute.cmd
```

also, add a file to the HDFS setup by attaching to the namenode and running:

```bash
apt update
apt install wget
wget -O alice.txt https://www.gutenberg.org/files/11/11-0.txt
```

A sample of how to connect to spark is provided in example.py

## Credits

This repo consists of several components created by Data Science Europe, but has been restructured into a part of a course run at the University of Southern Denmark.
The repos are as follows

- https://github.com/big-data-europe/docker-hadoop
- https://github.com/big-data-europe/docker-spark
