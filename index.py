import json
import sys
import urllib.request
import os
import configparser

HOME = os.environ['HOME']
CFG_FILE = HOME + '/.tmux-darksky'

DEFAULTS = """
[general]
hours = 12
location = 14.5833,120.9667

[colors]
BG = 235
UNSET = 196
Sunny = 255
Clear = 251
Partly Cloudy = 246
Mostly Cloudy = 242
Overcast = 237
Drizzle = 32
Light Rain = 25
Rain = 20
Heavy Rain = 18
Humid = 214
"""


config = configparser.ConfigParser()
config.read_string(DEFAULTS)
config.read(CFG_FILE)

print(config.sections())

src = 'https://api.darksky.net/forecast/' + \
    config['general']['key'] + '/' + \
    config['general']['location'] + '?exclude=currently'

with urllib.request.urlopen(src) as forecast_raw:

    report = ''
    show = int(config['general']['hours'])

    forecast = json.loads(forecast_raw.read())
    hourly_data = forecast['hourly']['data']
    count = 0
    for hda in hourly_data[:show]:
        if count % 4 == 0:
            report += '#[bg=' + config['colors']['BG'] + '] '
        count += 1

        match = list(filter(lambda v: v[0] in hda['summary'],
                            config['colors'].items()))

        if match:
            report += '#[bg=colour' + match[0][1] + '] '
            continue
        else:
            # Unmatched summary
            report += '#[bg=' + config['colors']['UNSET'] + '] '

    report += '#[bg=' + config['colors']['BG'] + ']'
    print(report)
