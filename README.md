# Rail-Meter-TX
Rail Meter Transmitter is intended to send DTSU666 data to InfluxDB using Modbus through python.

This project was made for my use case. I commented out some parameters I do not intend to use, so they don't take unnecessary space on my InfluxDB.

The file `app/DTSU666_2019.py` holds the addresses for my device (manufactured in 2020) found on the device manual `dtsu666_series_2019.pdf`. I found that the same models fabricated before can have different addresses (like 2016 for example).

Feel free to fork this project and modify it to yourself.

# Usage

You can run this script directly with a python interpreter or as a Docker container.

If you choose to run **just using python** (on a embedded system) you need to:
- clone repo `git clone https://github.com/onvrb/Rail-Meter-TX` (and enter project with `cd Rail-Meter-TX`)
- setup a venv (recommended) `python3 -m venv venv` and enter `source venv/bin/activate`
- install the requirements `pip3 install -r requirements.txt` 
- setup the environments on your host, or hard-code it into the `app/run.py`
- run script `python3 app/run.py`

## or

Using Docker:

- Create a `docker-compose.yml` file:
- Change the environments to suit your needs and run.

```yml
---
version: '3'
services:
  rail-meter-tx:
    container_name: rail-meter-tx
    image: ghcr.io/onvrb/rail-meter-tx:main
    environment:
      - DEV_PATH='/dev/ttyUSB0'     # optional - do not change unless you know what you're doing
      - DEV_SLAVE_ADDR=1            # optional
      - DEV_BAUDRATE=9600           # optional
      - DEV_BYTESIZE=8              # optional
      - DEV_STOPBITS=1              # optional
      - DEV_TIMEOUT=1               # optional
      - DRY_RUN=0                   # optional
      - URL=http://localhost:8086
      - PORT=80
      - TOKEN="XXXX"
      - ORG="org"
      - BUCKET="bucket-name"
      - MEASUREMENT="measurement"
      - TAGS="tags"
      - READ_FREQ=10                # optional
    devices:
      - /dev/ttyUSB0:/dev/ttyUSB0
    restart: unless-stopped
```
- Optional values assumes the default written in this example
- You can check the USB device path you just plugged in running `dmesg | tail`
