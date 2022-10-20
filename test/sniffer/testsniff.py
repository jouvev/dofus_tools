import pyshark
import time

cap = pyshark.LiveCapture(interface='Ethernet',bpf_filter=f'tcp src port 5555 and len > 10')

def R(p):
    t = p.sniff_timestamp
    print("time : ",time.time()-float(t))

cap.apply_on_packets(R)

print("STOP")