#!/bin/bash
version=$(curl -s https://api.github.com/repos/PaycoinFoundation/Paycoin/releases/latest | grep 'tag_' | cut -d\" -f4)
latest=$(curl -s https://api.github.com/repos/PaycoinFoundation/Paycoin/releases/latest | grep 'browser_' | cut -d\" -f4 | grep 'linux64.zip')
echo "### Changing to paycoind directory"
cd ~
echo "### Stopping Paycoin Server"
./paycoind stop
echo "### Changing to home directory"
cd ~
echo "### Downloading Paycoin Core ${version}"
echo $latest
#curl -O $latest
curl -# -C - -L -k -o linux64.zip $latest
echo "### Installing Paycoin Core ${version}"
rm -f -r paycoind
unzip linux64.zip
rm -f -r linux64.zip
rm -f -r paycoin-qt
echo "### System will now reboot"
reboot
