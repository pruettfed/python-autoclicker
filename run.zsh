#!/usr/bin/zsh

DIR=$(dirname "$0")
# echo "$DIR" --> returns ~/.../.../Autoclicker

#activate venv
source $DIR/.venv/bin/activate
python3 $DIR/autoclicker.py

#on autoclicker being killed deactivate venv
echo -e "\b\e[3;35mPROCESS FINISHED"
deactivate