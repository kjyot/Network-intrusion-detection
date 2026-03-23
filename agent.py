from scapy.all import sniff, IP
import socket

SERVER_IP = "127.0.0.1"
PORT = 9999

packet_count = {}

def detect_attack(packet):
    if IP in packet:
        src = packet[IP].src
        packet_count[src] = packet_count.get(src, 0) + 1

        print(f"{src} -> count: {packet_count[src]}")

        if packet_count[src] > 5:
            print(f"🚨 Attack detected from {src}")

            try:
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                s.connect((SERVER_IP, PORT))
                s.send(f"Attack from {src}".encode())
                s.close()
            except:
                print ("Server not running")

sniff(prn=detect_attack, store=0)