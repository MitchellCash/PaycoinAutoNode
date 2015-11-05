#!/bin/bash
echo "### Changing to paycoind directory"
cd ~
echo "### Stopping Paycoin Server"
./paycoind stop
echo "### Changing to home directory"
cd ~
echo "### Updating centOS"
sudo yum update -y
sudo yum upgrade -y
sudo yum install python-pip -y
yum install httpd -y
sudo chkconfig --levels 235 httpd on
echo "### Allow ports 80, 8999 and save iptables"
sudo iptables -A INPUT -p tcp -m tcp --dport 80 -j ACCEPT
sudo iptables -A INPUT -p tcp -m tcp --dport 8999 -j ACCEPT
sudo iptables-save
echo "### Installing python-bitcoinrpc"
sudo pip install python-bitcoinrpc
echo "### Changing to paycoind directory"
cd ~
echo "### Starting Paycoin Server"
./paycoind
echo "### Changing to home directory"
cd ~
echo "### IN 15 SECONDS PLEASE WRITE DOWN YOUR RPCUSER AND RPCPASSWORD AND PRESS CTRL+X (WE WILL NEED THESE SOON)"
sleep 15
cd .paycoin
nano paycoin.conf
echo "### Changing to home directory"
cd ~
echo "### Downloading the Web Interface"
mkdir ~/WebInterface/
cd ~/WebInterface/
wget -O osversion.py https://raw.githubusercontent.com/sk00t3r/PaycoinAutoNode/master/osversion.py
wget -O cpu.py https://raw.githubusercontent.com/sk00t3r/PaycoinAutoNode/master/cpu.py
wget -O server_uptime.py https://raw.githubusercontent.com/sk00t3r/PaycoinAutoNode/master/server_uptime.py
wget -O WebInterface.py https://raw.githubusercontent.com/sk00t3r/PaycoinAutoNode/master/WebInterface.py
echo "### IN 15 SECONDS CONFIGURE WEBINTERFACE.PY WITH RPC_USER, RPC_PASS, NODE_LOCATION, NODE_NAME, NODE_IP, DONATION_XPY_ADDR AND EXIT (DON’T FORGET TO SAVE)"
sleep 15
nano WebInterface.py
echo "### Installing the Web Interface"
sudo python WebInterface.py
echo "### Changing to home directory"
cd ~
echo "### Scheduling Cron Job to run WebInterface.py every 5 minutes"
(crontab -l ; echo "*/5 * * * * sudo python ~/WebInterface/WebInterface.py")| crontab -
echo "### System will now reboot"
reboot
