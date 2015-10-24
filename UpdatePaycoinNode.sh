#!/bin/bash
echo "### Changing to paycoind directory"
cd ~
echo "### Stopping Paycoin Server"
./paycoind stop
echo "### Changing to home directory"
cd ~
echo "### Downloading Paycoin Core 0.3.2.0"
wget https://github.com/PaycoinFoundation/paycoin/releases/download/v0.3.2.0/linux64.zip
echo "### Installing Paycoin Core 0.3.2.0"
rm -f -r paycoind
unzip linux64.zip
rm -f -r linux64.zip
rm -f -r paycoin-qt
echo "### System will now reboot"
reboot