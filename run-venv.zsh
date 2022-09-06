#!/usr/bin/zsh

### Use this script to run in the terminal ###
### if you're using a virtual environment ###

DIR=$(dirname "$0")
# echo "$DIR" --> returns ~/.../.../Autoclicker

#activate venv
source $DIR/.venv/bin/activate
python3 $DIR/autoclicker.py

#on autoclicker being killed deactivate venv
deactivate