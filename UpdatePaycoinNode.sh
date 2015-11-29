#!/bin/bash
set -e

version=$(curl -s https://api.github.com/repos/PaycoinFoundation/Paycoin/releases/latest | grep 'tag_' | cut -d\" -f4 | sed 's/\v//g')
latest=$(curl -s https://api.github.com/repos/PaycoinFoundation/Paycoin/releases/latest | grep 'browser_' | cut -d\" -f4 | grep 'linux64.zip')

while getopts ":frhv" opt; do
  case $opt in
    f)
      FORCE=1
      ;;
    r)
      REBOOT=1
      ;;
    h)
      echo "-f                     Stop and force update Paycoin"
      echo "-r                     Reboot without prompting for interaction"
      echo "-v                     Show latest available version"
      exit 0
      ;;
    v)
      echo "### The latest is available version is v${version}"
      exit 0
      ;;
    \?)
      echo "Invalid option: -$OPTARG" >&2
      exit 1
      ;;
    :)
      echo "Option -$OPTARG requires an argument." >&2
      exit 2
      ;;
  esac
done

echo "### Changing to paycoind directory"
cd ~

xpy_version=$(./paycoind getinfo | grep '"version"' | cut -d\" -f4 | sed 's/\v//g' )
# Check we are running the same version; otherwise; update

if [ ! -z $FORCE ]
then
    echo "### The latest available version is v${version}"
    echo "### Stopping Paycoin server"
    ./paycoind stop
else
    if [[ "${xpy_version}" == "" ]]
    then
        echo "### Paycoin server not running, Unable to check version"
        echo "### The latest is available version is v${version}"
    else 
        if [[ "${version}" == "${xpy_version}" ]]
        then
            echo "### You are already running the latest version: v${version}"
            echo "### Exiting updater script."
            exit 1
        else
            echo "### You are running Paycoin Core v#{xpy_version}"
            echo "### The latest available version is v${version}"
            echo "### Stopping Paycoin server"
            ./paycoind stop
        fi
    fi
fi

echo "### Downloading Paycoin Core ${version}"
curl -# -C - -L -k -o linux64.zip $latest
echo "### Installing Paycoin Core ${version}"
rm -f -r paycoind
unzip linux64.zip
rm -f -r linux64.zip
rm -f -r paycoin-qt

echo "### We recommend a system reboot to finish installation"
if [ ! -z $REBOOT ]
then
    # Reboot The System
    echo "### System will reboot in 5 seconds"
    sleep 5
    reboot
else
    read -p "### Would you like to reboot your system? " -n 1 -r
    echo    # Create new Line
    if [[ $REPLY =~ ^[Yy]$ ]]
    then
        # Reboot The System
        echo "### System will reboot in 5 seconds"
        sleep 5
        reboot
    else
        echo "### Please reboot your system for these changes to take effect"
    fi
fi
