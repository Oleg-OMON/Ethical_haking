import subprocess

set_up = 'sudo ip link set dev eth0 up'
set_down = 'sudo ip link set dev eth0 down'
eth_info = 'sudo macchanger -s eth0'
random_mac = 'sudo macchanger -r eth0'


def new_mac_address():

    subprocess.call(set_down, shell=True)
    my_mac = subprocess.call(eth_info, shell=True)
    print(my_mac)
    subprocess.call(random_mac, shell=True)
    subprocess.call(set_up, shell=True)


new_mac_address()