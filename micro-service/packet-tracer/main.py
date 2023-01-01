import pyshark

ip_list = ['127.0.0.1']

capture = pyshark.LiveCapture(interface='Wi-Fi',display_filter='tcp.port==443 or tcp.port==80 or tcp.port==8000')
for packet in capture.sniff_continuously(packet_count=0):
    # print(type(str(packet['ip'].dst)))
    dst_ip = str(packet['ip'].dst )
    src_ip = str(packet['ip'].src )

    if dst_ip in ip_list or src_ip in ip_list:
        print( 'Just arrived:',packet['ip'].dst ,'- src : ' ,packet['ip'].src)
        print(packet.tcp.srcport ,'-->' , packet.tcp.dstport)
    # print(packet)