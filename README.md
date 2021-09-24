# **Pyng Scan**
Ping scanner written in Python, using Scapy.

## **Installation**

1. Make sure you have Scapy installed
```
sudo apt install python3-scapy
```

2. Then `git clone` this repository and run main.py
## **The Problem**
```
$ nmap -sn 192.168.0.69
Starting Nmap 7.80 ( https://nmap.org ) at 2021-09-23 14:55 CEST
Note: Host seems down. If it is really up, but blocking our ping probes, try -Pn
Nmap done: 1 IP address (0 hosts up) scanned in 3.00 seconds

$ ping 192.168.0.69
PING 192.168.0.69 (192.168.0.69) 56(84) bytes of data.
64 bytes from 192.168.0.69: icmp_seq=1 ttl=126 time=0.744 ms
64 bytes from 192.168.0.69: icmp_seq=2 ttl=126 time=0.686 ms
64 bytes from 192.168.0.69: icmp_seq=3 ttl=126 time=0.740 ms
```

## **The Solution**
```
$ sudo python3 main.py 192.168.178.50/29 --timeout 4
192.168.178.49 is down or ICMP is blocked
192.168.178.50 is down or ICMP is blocked
192.168.178.51 is down or ICMP is blocked
192.168.178.52 is up (0.00010s latency).
192.168.178.53 is up (0.00026s latency).
192.168.178.54 is down or ICMP is blocked
```