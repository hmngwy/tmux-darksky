import json
import sys
import urllib.request
import os
import configparser

HOME = os.environ['HOME']
CFG_FILE = HOME + '/.tmux-darksky'

DEFAULTS = """
[general]
space_every = 4
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

src = 'https://api.darksky.net/forecast/' + \
    config['general']['key'] + '/' + \
    config['general']['location']

with urllib.request.urlopen(src) as forecast_raw:

    report = ''
    count = 0
    show = int(config['general']['hours'])
    space_every = int(config['general']['space_every'])

    forecast = json.loads(forecast_raw.read())
    hourly_data = [forecast['currently']] + \
        forecast['hourly']['data'][1:show - 1]
    print(forecast['currently'])

    for hda in hourly_data:
        # Spacers
        if count % space_every == 0:
            report += '#[bg=colour' + config['colors']['BG'] + '] '
        count += 1

        match = list(filter(lambda v: v[0] in hda['summary'],
                            config['colors'].items()))

        if match:
            report += '#[bg=colour' + match[0][1] + '] '
            continue
        else:
            # Unmatched summary
            report += '#[bg=colour' + config['colors']['UNSET'] + '] '

    report += '#[bg=colour' + config['colors']['BG'] + ']'
    print(report)
