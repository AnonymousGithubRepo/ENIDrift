from scapy.all import *
import pandas as pd
import numpy as np

file_list = ['20201209.pcap', '20201210.pcap', '20201211.pcap', '20201212.pcap', '20201213.pcap', '20201214.pcap', '20201215.pcap',
             '20201216.pcap', '20201217.pcap', 'zy-20201210.pcap', 'zy-20201211.pcap',
             'zy-20201212.pcap', 'zy-20201213.pcap', 'zy-20201214.pcap', 'zy-20201215.pcap', 'zy-20201216.pcap']

for file in file_list:
    pcap = PcapReader(file)
    dataset = []
    while True:
        try:
            packet = pcap.read_packet()
            IPtype = np.nan
            timestamp = str(packet.time+1)
            framelen = str(len(packet))
            if packet.haslayer(IP):  # IPv4
                srcIP = packet[IP].src
                dstIP = packet[IP].dst
                IPtype = 0
            elif packet.haslayer(IPv6):  # ipv6
                srcIP = packet[IPv6].src
                dstIP = packet[IPv6].dst
                IPtype = 1
            else:
                srcIP = ''
                dstIP = ''

            if packet.haslayer(TCP):
                srcproto = str(packet[TCP].sport)
                dstproto = str(packet[TCP].dport)
            elif packet.haslayer(UDP):
                srcproto = str(packet[UDP].sport)
                dstproto = str(packet[UDP].dport)
            else:
                srcproto = ''
                dstproto = ''

            srcMAC = packet.src
            dstMAC = packet.dst
            if srcproto == '':  # it's a L2/L1 level protocol
                if packet.haslayer(ARP):  # is ARP
                    srcproto = 'arp'
                    dstproto = 'arp'
                    srcIP = packet[ARP].psrc  # src IP (ARP)
                    dstIP = packet[ARP].pdst  # dst IP (ARP)
                    IPtype = 0
                elif packet.haslayer(ICMP):  # is ICMP
                    srcproto = 'icmp'
                    dstproto = 'icmp'
                    IPtype = 0
                elif srcIP + srcproto + dstIP + dstproto == '':  # some other protocol
                    srcIP = packet.src  # src MAC
                    dstIP = packet.dst  # dst MAC
            dataset.append([srcIP, dstIP, srcproto, dstproto, srcMAC, dstMAC, IPtype, framelen, timestamp])
        except:
            dtst = np.mat(dataset)
            dataset_csv = pd.DataFrame(dtst, columns = ['srcIP', 'dstIP', 'srcproto', 'dstproto', 'srcMAC', 'dstMAC', 'IPtype', 'framelen', 'timestamp'])
            dataset_csv.to_csv((file[:-4]+str('csv')), index=False)
            break