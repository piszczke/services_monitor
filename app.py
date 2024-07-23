"""
service_monitor - Monitor of all running services on local server
Author: piszczke
kontakt@piszczke.pl
https://github.com/piszczke/services_monitor
"""

import subprocess
from tabulate import tabulate

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

def print_service_status():
    services = get_service_status()
    headers = ["Service", "Load", "Active", "Sub", "Description"]
    table = tabulate(services, headers, tablefmt="pretty")
    print(table)

if __name__ == "__main__":
    print_service_status()