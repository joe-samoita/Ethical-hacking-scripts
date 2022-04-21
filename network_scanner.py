import scapy.all as scapy


def scan(ip):
    arp_request = scapy.ARP(pdst=ip)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_request_broadcast = broadcast / arp_request
    # print(arp_request_broadcast.show())
    answered = scapy.srp(arp_request_broadcast, timeout=1, verbose=False)[0]
    # print(answered.summary())
    print("-----------------------------------------------")
    print("IP\t\t\t MAC")
    print("-----------------------------------------------")
    for element in answered:
        # print(element[1].show())
        print(element[1].psrc + "\t\t" + element[1].hwsrc)


scan("10.0.2.1/24")
