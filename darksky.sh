FILE=/tmp/darksky_cache
CURRENT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
if [ ! -f $FILE ] || test "`find $FILE -mmin +10`"; then
  python3 $CURRENT_DIR/index.py > $FILE
fi
cat $FILE
