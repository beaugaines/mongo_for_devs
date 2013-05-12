#!/bin/bash
mkdir -p /home/sircharles/rs1 /home/sircharles/rs2 /home/sircharles/rs3
mongod --replSet m101 --logpath "1.log" --dbpath /home/sircharles/data/rs1 --port 27018 --smallfiles --fork
mongod --replSet m101 --logpath "2.log" --dbpath /home/sircharles/data/rs2 --port 27019 --smallfiles --fork
mongod --replSet m101 --logpath "3.log" --dbpath /home/sircharles/data/rs3 --port 27020 --smallfiles --fork
