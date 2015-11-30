Paycoin Auto Node
=================

What is Paycoin Auto Node?
--------------------------

Paycoin Auto Node are a handful of scripts to run, ideally just after setting up
a new server or VPS, to automatically setup paycoind and have it start on boot
together with an optional Apache web interface.

Usage
-----

Download the scripts onto your server.

Download the script to deploy the paycoind instance:
```
wget https://raw.githubusercontent.com/mitchellcash/PaycoinAutoNode/master/DeployPaycoinNode.sh
```

Download the script to update the paycoind instance:
```
wget https://raw.githubusercontent.com/mitchellcash/PaycoinAutoNode/master/UpdatePaycoinNode.sh
```

Download the script to deploy the web interface:
```
wget https://raw.githubusercontent.com/mitchellcash/PaycoinAutoNode/master/DeployWebInterface.sh
```

Deploy the scripts.

Run the script to deploy the paycoind instance:
```
bash ./DeployPaycoinNode.sh
```

Run the script to update the paycoind instance:
```
bash ./UpdatePaycoinNode.sh
```

Run the script to deploy the web interface:
```
bash ./DeployWebInterface.sh
```

Example
-------

If you'd like to see an example of how the web interface looks in production see the [example web interface](http://paycoin.paynodes.io/).
