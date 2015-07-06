#!/bin/bash
echo "### Change to home directory"
cd ~
echo "### Update Ubuntu"
sudo apt-get update -y
sudo apt-get upgrade -y
sudo apt-get dist-upgrade -y
sudo apt-get install software-properties-common python-software-properties unzip ufw -y
echo "### Allow ports 22, 8998 and enable The Uncomplicated Firewall"
sudo ufw allow 22/tcp
sudo ufw allow 8998/tcp
sudo ufw --force enable
echo "### Creating Swap File"
dd if=/dev/zero of=/swapfile bs=1M count=1024 ; mkswap /swapfile ; swapon /swapfile
echo "/swapfile swap swap defaults 0 0" >> /etc/fstab
echo "### Creating paycoin.conf"
mkdir ~/.paycoin/
config=".paycoin/paycoin.conf"
touch $config
echo "server=1" > $config
echo "daemon=1" >> $config
echo "maxconnections=125" >> $config
echo "disablewallet=1" >> $config
randUser=`< /dev/urandom tr -dc A-Za-z0-9 | head -c30`
randPass=`< /dev/urandom tr -dc A-Za-z0-9 | head -c30`
echo "rpcuser=$randUser" >> $config
echo "rpcpassword=$randPass" >> $config
echo "### Downloading Paycoin Core 0.3.0.2"
wget https://github.com/PaycoinFoundation/paycoin/releases/download/v0.3.0.2/linux64.zip
echo "### Installing Paycoin Core 0.3.0.2"
unzip linux64.zip
rm -f -r linux64.zip
rm -f -r paycoin-qt
echo "### Scheduling Cron Job to run Paycoin Core on boot"
(crontab -l ; echo "@reboot ~/./paycoind")| crontab -
echo "### System will now reboot"
reboot