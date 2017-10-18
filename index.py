import json
import sys
import urllib.request

src = 'https://api.darksky.net/forecast/' + \
    sys.argv[2] + '/' + sys.argv[1] + '?exclude=currently'

with urllib.request.urlopen(src) as forecast_raw:

    report = ''
    show = 12

    forecast = json.loads(forecast_raw.read())
    hourly_data = forecast['hourly']['data']
    count = 0
    for hda in hourly_data[:show]:
        if count % 4 == 0:
            report += '#[bg=' + sys.argv[3] + '] '
        count += 1
        if 'Sunny' in hda['summary']:
            report += '#[bg=colour255] '
            continue
        if 'Clear' in hda['summary']:
            report += '#[bg=colour251] '
            continue
        if 'Partly Cloudy' in hda['summary']:
            report += '#[bg=colour246] '
            continue
        if 'Mostly Cloudy' in hda['summary']:
            report += '#[bg=colour242] '  # 242
            continue
        if 'Overcast' in hda['summary']:
            report += '#[bg=colour237] '  # 237
            continue
        if 'Drizzle' in hda['summary']:
            report += '#[bg=colour32] '
            continue
        if 'Light Rain' in hda['summary']:
            report += '#[bg=colour25] '
            continue
        if 'Rain' in hda['summary']:
            report += '#[bg=colour20] '
            continue
        if 'Heavy Rain' in hda['summary']:
            report += '#[bg=colour18] '
            continue
        if 'Humid' in hda['summary']:
            report += '#[bg=colour214] '
            continue
        # Unmatched summary
        report += '#[bg=colour196] '

    report += '#[bg=' + sys.argv[3] + ']'
    print(report)
