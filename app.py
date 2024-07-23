"""
service_monitor - Monitor of all running services on local server
Author: piszczke
kontakt@piszczke.pl
https://github.com/piszczke/services_monitor
"""

# service_monitor.py
import subprocess
import json
from tabulate import tabulate

def load_services_to_monitor(filename='services_to_monitor.json'):
    with open(filename, 'r') as file:
        data = json.load(file)
    return data['services']

def get_service_status():
    # Run the systemctl command to get the status of all services
    result = subprocess.run(['systemctl', 'list-units', '--type=service', '--all'], stdout=subprocess.PIPE)
    output = result.stdout.decode('utf-8')

    # Parse the output
    lines = output.splitlines()
    services = []
    for line in lines:
        if 'loaded' in line or 'not-found' in line:
            parts = line.split(None, 4)
            if len(parts) >= 4:
                name = parts[0]
                load = parts[1]
                active = parts[2]
                sub = parts[3]
                description = parts[4] if len(parts) == 5 else ""
                services.append([name, load, active, sub, description])
    
    return services

def filter_services(services, services_to_monitor):
    filtered_services = [service for service in services if service[0] in services_to_monitor]
    return filtered_services

def print_service_status():
    services_to_monitor = load_services_to_monitor()
    services = get_service_status()
    filtered_services = filter_services(services, services_to_monitor)
    headers = ["Service", "Load", "Active", "Sub", "Description"]
    table = tabulate(filtered_services, headers, tablefmt="pretty")
    print(table)

if __name__ == "__main__":
    print_service_status()
