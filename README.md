# services_monitor
Monitor of all running services on local server 

## Install 

Dependence 

```bash
pip install tabulate colorama
git clone https://github.com/piszczke/services_monitor.git
cd services_monitor
```

## Run the script

for services from the list
```bash
watch -n 10 python3 app.py -l
```

for all services
```bash
watch -n 10 python3 app.py -a
```

## sample output
![sample_output](sample.png)
