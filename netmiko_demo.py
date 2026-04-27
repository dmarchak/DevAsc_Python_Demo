#! /usr/bin/env python3

"""Demonstrate using Netmiko to connect to a network device."""

from netmiko import ConnectHandler

# Define the device parameters
device = {
    "device_type": "cisco_ios",
    "host": "192.168.0.11",
    "username": "cisco",
    "password": "cisco",
}

# Establish a connection to the device
with ConnectHandler(**device) as net_connect:
    # Send a command to the device and print the output
    output = net_connect.send_command("show running-config")
    print(output)

# Send configuration commands to the device
with ConnectHandler(**device) as net_connect:
    config_commands = ["interface Loopback0", "description Configured by Netmiko"]
    output = net_connect.send_config_set(config_commands)
    print(output)
