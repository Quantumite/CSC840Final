# CSC840 Final

## General Information

***

- Author: Austin Norby
- Date: 11/22/2020
- Description: This presentation covers examples of malware that use Non-application layer protocols for communication.
- YouTube Link: TODO

## Why You Should Care

***
  Malware can be difficult to find, track, and conquer normally, but it can be more difficult when the authors choose the communication protocol to be non-standard, or specifically non-application layer. This could mean that the malware is communicating via unstructured TCP or UDP packets. This could also mean that the malware uses a custom structure that will be harder to analyze because its possible that it's never been seen before.  

  Some examples that have been seen in the wild are communication via ICMP, the session layer protocol, Socket Secure (SOCKS), and even raw sockets. These kind of communications are less likely to be caught by automated network intrusion applications and require additional analysis to fully understand the capabilities of the malware.

## Three Main Ideas

***

  1. Malware is not required to use an application-layer protocol like DNS, or HTTP(S).
  2. Non-Application Layer C2 Communications are not just theoretical capabilities.
  3. It is easy to build a proof-of-concept that communicates using these Non-Application Layer protocols.

## Future Direction

***

One possible avenue for further research to mitigate this malware capability:  

- Artificial Intelligence/Machine Learning applied to network communications to classify network activity.  

Other options for prevention and detection include:

- Strict firewall rules that control the destination, and/or source, ports for all communications.
- Prevent usage of common Non-Application Layer Protocols on the network.
- Signature-based detection of known capabilities.

## Related Topics

***

- Encrypted Malware Communication
- C2 Communication
- ICMP, Socks, UDP protocols
- Network Anomaly Detection

## Additional Resources

***

  1. [MITRE ATT&CK (Non-Application Layer Protocol)](https://attack.mitre.org/techniques/T1095/)
  2. [Operation DoubleTap - Fireeye](https://www.fireeye.com/blog/threat-research/2014/11/operation_doubletap.html)
  3. [Crimson - Proofpoint](https://www.proofpoint.com/sites/default/files/proofpoint-operation-transparent-tribe-threat-insight-en.pdf)
  4. [Derusbi - Fidelis Cybersecurity](https://paper.seebug.org/papers/APT/APT_CyberCriminal_Campagin/2016/2016.02.29.Turbo_Campaign_Derusbi/TA_Fidelis_Turbo_1602_0.pdf)
  5. [Standard Non-Application Layer Protocol - Corelight](https://www.corelight.com/mitre-attack/c2/t1095-standard-non-application-layer-protocol/)
  6. [ICMP C2 Standard Non-Application Layer Protocol - Praetorian](https://www.praetorian.com/blog/icmp-c2-standard-non-application-layer-protocol-mitre-attack-t1095)
  7. [Phoreal - FireEye](https://www.fireeye.com/blog/threat-research/2017/05/cyber-espionage-apt32.html)
  8. [TSCookie - JPCERT](https://blogs.jpcert.or.jp/en/2019/09/tscookie-loader.html)
  9. [BUBBLEWRAP - FireEye](https://www.fireeye.com/blog/threat-research/2015/11/china-based-threat.html)
  10. [Scapy - ReadTheDocs](https://scapy.readthedocs.io)
