#!/usr/bin/zsh

source ./.venv/bin/activate
python3 autoclicker.py

echo -e "\b\e[3;35mPROCESS KILLED"
deactivate