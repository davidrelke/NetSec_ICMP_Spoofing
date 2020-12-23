from scapy.all import *
from scapy.layers.inet import IP, ICMP, Ether


def icmp_monitor_callback(package):
    if package[ICMP].type == 8:
        request_dst = package[IP].dst
        request_src = package[IP].src

        reply_package = IP(dst=request_src, src=request_dst)/ICMP(type=0, id=package[ICMP].id, seq=package[ICMP].seq)/Raw(load=package[ICMP].payload)

        sr(reply_package, timeout=0)
        print(f"Sniffed ICMP request from source {request_src} to destination {request_dst}")
        print(f"Send ICMP response. from {request_dst} to {request_src}")


if __name__ == '__main__':
    sniff(prn=icmp_monitor_callback, filter="icmp", store=0)
