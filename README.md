Paycoin Auto Node
=================

What is Paycoin Auto Node?
--------------------------

Paycoin Auto Node are a handful of scripts to run, ideally just after setting up
a new server or VPS, to automatically setup paycoind and have it start on boot
together with an optional Apache web interface.

Installation
------------

The `DeployPaycoinNode.sh` and `DeployWebInterface.sh` scripts will install all required libraries and packages needed for the usage of Paycoin Auto Node. Please only run the scripts you intend on using.

Download the scripts onto your server.

### Using Git
```bash
git clone https://github.com/mitchellcash/PaycoinAutoNode.git
```

### Using Wget

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


Usage
-----

Deploy the scripts.

Run the script to deploy the paycoind instance:
```
bash ./DeployPaycoinNode.sh
```

Run the script to update the paycoind instance:
```
bash ./UpdatePaycoinNode.sh
```
Note, this script accepts the following flags
```bash
-h                     Show this message
-f                     Stop and force update Paycoin
-r                     Reboot without prompting for interaction
-v                     Show latest available version
```

You can use the -r and -f flags in conjunction with crontab to schedule automatic reboots and updates.



Run the script to deploy the web interface:
```
bash ./DeployWebInterface.sh
```



Example
-------

If you'd like to see an example of how the web interface looks in production see the [example web interface](http://paycoin.paynodes.io/).
