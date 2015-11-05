#!/bin/bash
echo "### Change to home directory"
cd ~
echo "### Installing sudo"
yum install sudo -y
echo "### Updating centOS"
sudo yum update -y
sudo yum upgrade -y
sudo yum install unzip -y
yum install cronie -y
echo "### Allow ports 22, 8998 and save iptables"
sudo iptables -A INPUT -p tcp -m tcp --dport 22 -j ACCEPT
sudo iptables -A INPUT -p tcp -m tcp --dport 8998 -j ACCEPT
sudo iptables-save
echo "### Creating Swap File"
dd if=/dev/zero of=/swapfile bs=1M count=1024
echo "/swapfile swap swap defaults 0 0" >> /etc/fstab
#sudo ./create_swap.sh 4096
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
echo "### Downloading Paycoin Core 0.3.2.0"
wget https://github.com/PaycoinFoundation/paycoin/releases/download/v0.3.2.0/linux64.zip
echo "### Installing Paycoin Core 0.3.2.0"
unzip linux64.zip
rm -f -r linux64.zip
rm -f -r paycoin-qt
echo "### Scheduling Cron Job to run Paycoin Core on boot"
(crontab -l ; echo "@reboot ~/./paycoind")| crontab -
echo "### System will now reboot"
reboot
