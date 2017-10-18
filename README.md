# tmux-darksky

![](https://user-images.githubusercontent.com/1647347/31725286-8c6ebc2c-b456-11e7-8e14-84b77f447e57.png)

Each block is an hour.

Colors are currently hardcoded, soon this'll be editable through a dotfile in yaml, as well as the API and location details.

### Installation

Requires: `python3`

Add your location and Dark Sky API key:

```
set -g @darksky_lon_lat "14.5833,120.9667"
set -g @darksky_api_key "0a6a8952082439b11cdbcXXXXXXXXX"
```

Add the plugin via tpm:

```
set -g @plugin 'hmngwy/tmux-darksky'
```

