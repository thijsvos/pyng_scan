#!/usr/bin/python3

import sys
import argparse
from scapy.all import IP, ICMP, sr1, sr
import ipaddress
import os
import traceback
import contextlib

parser = argparse.ArgumentParser(description='Simple Python application to ping targets.')
parser.add_argument('target', help='Targets (e.g. 192.168.4.20 or 192.168.69.0/24')
parser.add_argument('--timeout', type=int, help='Ping timeout in seconds', default=1)
arguments = parser.parse_args()

ping_targets = arguments.target
timeout = arguments.timeout

if timeout < 1:
    raise argparse.ArgumentTypeError("Minimum timeout is 1 second.")

def run_ping(targets):
    for ip in [str(ip) for ip in ipaddress.ip_network(targets, False).hosts()]:
        # print(ip)
        icmp = IP(dst=ip)/ICMP()
        answers, unanswers = sr(icmp,timeout=int(timeout), verbose=0)

        if len(answers) == 0:
            print(f"{ip} is down or ICMP is blocked")
        else:
            rx = answers[0][1]
            tx = answers[0][0]
            delta_time = rx.time-tx.sent_time
            print(f"{ip} is up ({delta_time:.5f}s latency).")

def main():
    try:
        run_ping(ping_targets)
    except KeyboardInterrupt:
        sys.exit(1)
    
main()
