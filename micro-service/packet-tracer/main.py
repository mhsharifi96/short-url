import pyshark
from api import create_packet_log
from datetime import datetime

packets = []
ip_list = ['127.0.0.1','37.32.14.211']
success_code =200
capture = pyshark.LiveCapture(interface='Wi-Fi',display_filter='tcp.port==443 or tcp.port==80 or tcp.port==8000')
for packet in capture.sniff_continuously():
    # print(type(str(packet['ip'].dst)))
    dst_ip = str(packet['ip'].dst )
    src_ip = str(packet['ip'].src )


    if dst_ip in ip_list or src_ip in ip_list:
        
        if 'http' in packet : 
            print('frame  layer time :',packet.frame_info.time)
          
            if 'response_for_uri' in dir(packet.http):
                if int(packet['http'].response_code) == success_code:
                    
                    print('---------------- response ----------------')
                
                    print(packet['http'].response_code)
                    
                    print('---------------- End response ----------------')
                    
                    create_packet_log({
                                "user_mac":packet['eth'].dst,
                                "user_ip": dst_ip,
                                "time_request": packet['http'].time,
                                "date_request": str(packet['http'].date),
                                "cookie": packet['http'].set_cookie or None
                                })

            else : 
                print('---------------- request ----------------')
                # print(packet['http'].cookie)
                print(packet['http'].request_uri)
                print('---------------- End request ----------------')


           