#!/usr/bin/env python3

import argparse
import os
import sys
import yaml

def create_netplan_config(iface_id, auto_start, ip_address, gateway, dns):
    config = {
        "network": {
            "version": 2,
            "renderer": "networkd",
            "ethernets": {
                iface_id: {
                    "dhcp4": True
                }
            }
        }
    }

    if not auto_start:
        config["network"]["ethernets"][iface_id]["optional"] = True

    if ip_address and gateway and dns:
        config["network"]["ethernets"][iface_id]["dhcp4"] = False
        config["network"]["ethernets"][iface_id]["addresses"] = [ip_address]
        config["network"]["ethernets"][iface_id]["gateway4"] = gateway
        config["network"]["ethernets"][iface_id]["nameservers"] = {"addresses": dns}

    return config

def write_netplan_config(config, output_file):
    with open(output_file, 'w') as f:
        yaml.dump(config, f, default_flow_style=False)

def main():
    parser = argparse.ArgumentParser(description="Configure a network interface on a Linux machine.")
    parser.add_argument("iface_id", help="Interface ID (e.g., eth0, ens3, etc.)")
    parser.add_argument("--auto-start", action="store_true", help="Enable auto-start for the interface")
    parser.add_argument("--ip-address", help="IP address and prefix (e.g., 192.168.1.10/24)")
    parser.add_argument("--gateway", help="Gateway IP address")
    parser.add_argument("--dns", nargs='+', help="DNS server IP addresses")

    args = parser.parse_args()

    if (args.ip_address and not (args.gateway and args.dns)) or (args.gateway and not (args.ip_address and args.dns)) or (args.dns and not (args.ip_address and args.gateway)):
        print("Error: If you provide IP address, gateway, and DNS information, all three values must be specified.")
        sys.exit(1)

    config = create_netplan_config(args.iface_id, args.auto_start, args.ip_address, args.gateway, args.dns)
    output_file = f"/etc/netplan/{args.iface_id}.yaml"
    write_netplan_config(config, output_file)
    os.system(f"netplan apply")

if __name__ == "__main__":
    main()
