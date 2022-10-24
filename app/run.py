import serial
import minimalmodbus
from os import environ
from time import time, sleep, strftime
from datetime import datetime
from influxdb_client import InfluxDBClient, Point, WritePrecision
from influxdb_client.client.write_api import SYNCHRONOUS

from DTSU666_2019 import dict

dev_location = environ.get('DEV_PATH', '/dev/ttyUSB0')
dev_slave_addr = environ.get('DEV_SLAVE_ADDR', 1)

# setup device
rs485 = minimalmodbus.Instrument(dev_location, dev_slave_addr)
rs485.serial.baudrate = environ.get('DEV_BAUDRATE', 9600)
rs485.serial.bytesize = environ.get('DEV_BYTESIZE', 8)
rs485.serial.parity   = serial.PARITY_NONE
rs485.serial.stopbits = environ.get('DEV_STOPBITS', 1)
rs485.serial.timeout  = environ.get('DEV_TIMEOUT', 1)

# good practice
rs485.clear_buffers_before_each_transaction = True

# influxdb envs
url = environ.get('URL')
port = environ.get('PORT')
token = environ.get('TOKEN')
org = environ.get('ORG')
bucket = environ.get('BUCKET')
measurement = environ.get('MEASUREMENT')
tags = environ.get('TAGS')
schema = measurement + tags

read_freq = environ.get('READ_FREQ', 10)

debug = environ.get('DEBUG', False)

printed_stats_today = False
read_error_session = 0
read_error_this_week = 0
write_error_session = 0
write_error_this_week = 0
start = True

def timed_print(my_input):
    print(f'{strftime("%Y-%m-%d, %H:%M:%S")}:', my_input)

while True:
    payload = []
    for param in dict:
        try:
            value = rs485.read_float(dict[param]['address'])    # read value
            value = value * dict[param]['multiplier']           # scale value
            value = round(value, dict[param]['decimals'])       # fix decimal
        except Exception as e:
            value = 0
            read_error_session += 1
            read_error_this_week += 1
            # date
            timed_print(f'Error reading {param}: {e}')
        payload.append(f"{measurement},{tags} {param}={value}")  # create payload

    if debug:
        print(payload)
        quit()

    try:
        with InfluxDBClient(url=url, port=443, token=token, org=org, ssl=True) as client:
            write_api = client.write_api(write_options=SYNCHRONOUS)

            write_api.write(bucket, org, payload) # send payload
    except Exception as e:
        write_error_session += 1
        write_error_this_week += 1
        timed_print(f'Error writing to InfluxDB: {e}')

    # print stats once every monday
    if datetime.today().weekday() == 1:
        printed_stats_today=False

    if datetime.today().weekday() == 0 and printed_stats_today==False:
        timed_print('Stats')
        print('Errors last 7 days:')
        print(f'read: {read_error_this_week}')
        print(f'write: {write_error_this_week}')
        print('Errors this session (total):')
        print(f'read: {read_error_session}')
        print(f'write: {write_error_session}')
        read_error_this_week = 0
        write_error_this_week = 0
        printed_stats_today = True

    # health check first run
    if start:
        if read_error_session > 0 or write_error_session > 0:
            timed_print('Error upon first loop, quitting')
            quit()
        timed_print('Service started and successfully sent first payload')
        print(f'Sending data every {read_freq} seconds')
        start=False

    sleep(read_freq)
