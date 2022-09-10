#!/usr/bin/zsh

### </> BUILD SCRIPT </> ###

### Use this script to build an executable version of the autoclicker
### Make sure to run inside root folder
## Run with $ source build.zsh

### </> VERSION NUMBER </> ###
VERSION="1.2"

#create virtual environment
print $fg_bold[blue] "Build initiated for v${VERSION}\n ================================================================="
print $fg_bold[blue] 'Creating build environment\n ================================================================='

### =>> MAC SYSTEMS <<= ###
if [[ "$OSTYPE" == "darwin"* ]]; then
    python3 -m venv .buildvenv
    source ./.buildvenv/bin/activate
### =>> MAC SYSTEMS <<= ###

### =>> WINDOWS SYSTEMS <<= ###
elif [[ "$OSTYPE" == "msys" || "$OSTYPE" == "cygwin" ]]; then
    python -m venv .buildvenv
    source ./.venv/Scripts/activate
### =>> WINDOWS SYSTEMS <<= ###

else
    echo "ERROR: Unknown system"
fi

print $fg_bold[blue] 'Installing packages\n ================================================================='
#install pyinstaller and create executable
pip install -q -r requirements.txt
print $fg_bold[magenta] 'Building executable\n ================================================================='
pyinstaller --onefile autoclicker.py

#delete virtual environment
deactivate
rm -r .buildvenv

print $fg[yellow] 'Cleaning stuff up\n ================================================================='
#cp executable and delete build files
cp dist/autoclicker .
rm -r build
rm -r dist
rm autoclicker.spec

print $fg_bold[green] "Process completed: Autoclicker version ${VERSION} installed"