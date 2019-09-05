#!/usr/bin/python3
# coding: utf-8
from redis import Redis

config = {
    'host': '119.3.170.97',
    'port': 6378,
    'db': '9',
    'decode_responses': True
}


rd_client = Redis(**config)

if __name__ == '__main__':
    rd_client.keys('*')