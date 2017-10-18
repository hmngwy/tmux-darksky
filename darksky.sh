get_tmux_option() {
	local option="$1"
	local default_value="$2"
	local option_value="$(tmux show-option -gqv "$option")"
	if [ -z "$option_value" ]; then
		echo "$default_value"
	else
		echo "$option_value"
	fi
}

FILE=/tmp/darksky_cache
CURRENT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
if [ ! -f $FILE ] || test "`find $FILE -mmin +10`"; then
  python3 $CURRENT_DIR/index.py $(get_tmux_option "@darksky_lon_lat") $(get_tmux_option "@darksky_api_key") $(get_tmux_option "status-bg") > $FILE
fi
cat $FILE
