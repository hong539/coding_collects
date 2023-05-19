import os
import re

# BASE = '/root/devops'
BASE = '.'

IP_PATTERN = '\.'.join(['(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)'] * 4)

def process_file(filename):
    ips = []
    with open(filename, 'r') as f:
        for line in f.readlines():
            cur_ips = re.findall(IP_PATTERN, line)

            # tuple -> 'x.x.x.x'
            for cur_ip in cur_ips:
                ips.append('.'.join(cur_ip))
    return ips

def process_directory(base):
    ip_addresses = []

    for root, directories, filenames in os.walk(base):
        for filename in filenames:
            full_filename = os.path.join(root, filename)
            new_addresses = process_file(full_filename)
            ip_addresses.extend(new_addresses)

    return ip_addresses

def solution():
    ip_addresses = process_directory(BASE)
    ip_addresses = list(set(ip_addresses))
    ip_addresses.sort()

    for address in ip_addresses:
        print(address)

solution()
# lexicographical order?
# if setting BASE = '.'
# then run python analyzingIpAddresses.py
# out put
# lol
# 0.0.0.0
# 06.5.76.35
# 127.0.0.1
# 127.0.49.1
# 127.98.0.1
# 128.128.4.11
# 128.68.4.11
# 128.96.107.55
# 128.99.107.55
# 128.99.58.55
# 15.128.4.65
# 26.56.4.23
# 74.0.65.76
# 77.255.255.254