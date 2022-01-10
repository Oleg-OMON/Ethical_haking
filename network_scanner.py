import scapy.all as scapy


def scan(ip):
    arp_request = scapy.ARP(pdst=ip)
    broadcast = scapy.Ether(dst='ff:ff:ff:ff:ff:ff')
    arp_request_broadcast = broadcast / arp_request
    answered_list = scapy.src(arp_request_broadcast, timeout=1)[0]
    for item in answered_list:
        print(item[1].psrc)
        print(item[1].hwsrc)
        print('#############################')


scan('00.0.0.0/00')
