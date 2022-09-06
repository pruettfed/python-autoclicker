#!/usr/bin/zsh

### Use this script to run in the terminal ###
### if you're using a virtual environment ###

DIR=$(dirname "$0")
# echo "$DIR" --> returns ~/.../.../Autoclicker

### =>> MAC SYSTEMS <<= ###
if [[ "$OSTYPE" == "darwin"* ]]; then
    #activate venv
    source $DIR/.venv/bin/activate
    python3 $DIR/autoclicker.py
### =>> MAC SYSTEMS <<= ###

### =>> WINDOWS SYSTEMS <<= ###
elif [[ "$OSTYPE" == "msys" || "$OSTYPE" == "cygwin" ]]; then
    #activate venv
    source $DIR/.venv/Scripts/activate
    python3.exe $DIR/autoclicker.py
### =>> WINDOWS SYSTEMS <<= ###

else
    echo "ERROR: Unknown system"
fi


#on autoclicker being killed deactivate venv
deactivate