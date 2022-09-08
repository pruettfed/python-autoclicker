#!/usr/bin/zsh

### Use this script to run in the terminal ###
### if you're using a virtual environment ###

### =>> MAC SYSTEMS <<= ###
if [[ "$OSTYPE" == "darwin"* ]]; then
    DIR="$(dirname $0)"
    
    #activate venv
    source "$DIR"/.venv/bin/activate
    python3 "$DIR"/autoclicker.py
### =>> MAC SYSTEMS <<= ###

### =>> WINDOWS SYSTEMS <<= ###
elif [[ "$OSTYPE" == "msys" || "$OSTYPE" == "cygwin" ]]; then
    DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
    
    #activate venv
    source "$DIR"/.venv/Scripts/activate
    python "$DIR"/autoclicker.py
### =>> WINDOWS SYSTEMS <<= ###

else
    echo "ERROR: Unknown system"
fi


#on autoclicker being killed deactivate venv
deactivate