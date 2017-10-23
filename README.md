# tmux-darksky

![](https://user-images.githubusercontent.com/1647347/31725286-8c6ebc2c-b456-11e7-8e14-84b77f447e57.png)

Each block is an hour.

### Installation

Requires: `python3`

Create a configuration file in `$HOME/.tmux-darksky`:

```ini
[general]
hours = 12
location = 14.5833,120.9667
key = your_darksky_api_key
```

Add the plugin via tpm:

```
set -g @plugin 'hmngwy/tmux-darksky'
```

