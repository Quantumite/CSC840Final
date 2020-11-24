"""
ICMP send data Proof-of-Concept

This PoC was developed for CSC840 Final project to demonstrate
how easy it is for data to be transmitted via ICMP rather than
other standard, or Application-Layer protocols.

@author: Austin Norby (quantumite)

@note: If running on windows, you must install NPCAP driver to
access raw sockets. Link: https://nmap.org/npcap/
"""

from scapy.all import IP, ICMP, send

p = IP(dst="127.0.0.1")/ICMP()/"Hello, world!"
send(p)