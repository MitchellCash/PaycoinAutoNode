# PaycoinAutoNode
Script to run, ideally just after setting up a new server or VPS, to automatically setup paycoind and have it start on boot together with an optional Apache web interface.

To set up on Ubuntu/Debian:

cd /opt

apt-get install git -y

wget https://raw.githubusercontent.com/sk00t3r/PaycoinAutoNode/master/DeployPaycoinNode.sh

wget https://raw.githubusercontent.com/sk00t3r/PaycoinAutoNode/master/DeployWebInterface.sh

chmod 755 DeployPaycoinNode.sh

chmod 755 DeployWebInterface.sh

./DeployPaycoinNode.sh

*****System will Reboot*****

cd /opt

./DeployWebInterface.sh

*****Follow On Screen Instrcutions*****
