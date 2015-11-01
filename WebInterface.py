#!/usr/bin/python
from bitcoinrpc.authproxy import AuthServiceProxy
import time

rpc_user = ""
rpc_pass = ""
node_location = ""
node_name = ""
donation_xpy_addr = ""

access = AuthServiceProxy("http://" + rpc_user + ":" + rpc_pass + "@127.0.0.1:8999")
info = access.getinfo()

www_file = "/var/www/html/index.html"
node_ip = str(info['ip'])

ff = open(www_file, 'w')

ff.write("<!DOCTYPE html>")
ff.write("<html lang='en'>")
ff.write("<head>")
ff.write("<meta charset='utf-8'>")
ff.write("<title>Paycoin Node Status</title>")
ff.write("<link href='https://fonts.googleapis.com/css?family=Open+Sans:400,300,600,700|Source+Sans+Pro:400,300,600,700' rel='stylesheet' type='text/css'>")
ff.write("<style type='text/css'> ")
ff.write("</style>")
ff.write("</head>")
ff.write("<body>")

ff.write("<style>")

ff.write("/* Eric Meyer's Reset CSS v2.0 - http://cssreset.com */")
ff.write("html,body,div,span,applet,object,iframe,h1,h2,h3,h4,h5,h6,p,blockquote,pre,a,abbr,acronym,address,big,cite,code,del,dfn,em,img,ins,kbd,q,s,samp,small,strike,strong,sub,sup,tt,var,b,u,i,center,dl,dt,dd,ol,ul,li,fieldset,form,label,legend,table,caption,tbody,tfoot,thead,tr,th,td,article,aside,canvas,details,embed,figure,figcaption,footer,header,hgroup,menu,nav,output,ruby,section,summary,time,mark,audio,video{border:0;font-size:100%;font:inherit;vertical-align:baseline;margin:0;padding:0}article,aside,details,figcaption,figure,footer,header,hgroup,menu,nav,section{display:block}body{line-height:1}ol,ul{list-style:none}blockquote,q{quotes:none}blockquote:before,blockquote:after,q:before,q:after{content:none}table{border-collapse:collapse;border-spacing:0}")

ff.write("html,body{height:100%;}")

ff.write("body{")
ff.write("color: #333;")
ff.write("-moz-osx-font-smoothing: grayscale;")
ff.write("font-feature-settings: 'liga', 'kern';")
ff.write("text-rendering: optimizelegibility;")
ff.write("background: url(https://dl.dropboxusercontent.com/u/37902134/PaycoinNodeBackgroundv2.png) no-repeat; background-size: 100%")
ff.write("}")

ff.write("a{")
ff.write("color: #08c;")
ff.write("}")

ff.write("a:visited, a:link, a:active {")
ff.write("text-decoration: none;")
ff.write("}")

ff.write("#wrap{")
ff.write("background-color: rgba(255, 255, 255, 0.6);")
ff.write("width: 100%;")
ff.write("height: 100%;")
ff.write("line-height: 1.4;")
ff.write("font-size: 24px;")
ff.write("font-family: 'Source Sans Pro','Open Sans','Helvetica Neue','Helvetica','Arial',sans-serif;")
ff.write("}")

ff.write("h3{")
ff.write("font-size: 21px;")
ff.write("font-weight: 200;")
ff.write("letter-spacing: -0.01em;")
ff.write("line-height: 1.14286;")
ff.write("margin-bottom: 18px;")
ff.write("}")

ff.write("h1{")
ff.write("color: #08c;")
ff.write("font-size: 42px;")
ff.write("font-weight: 200;")
ff.write("letter-spacing: -0.01em;")
ff.write("line-height: 1.14286;")
ff.write("margin-bottom: 18px;")
ff.write("}")
ff.write("</style>")

ff.write("<div id='wrap'>")
ff.write("<h1>Paycoin Node: " + node_ip + ":8998<br \></h1>")

ff.write("<h3>")
ff.write("Last Updated: " + time.strftime("%l:%M:%S %p (%z %Z) on %-d %b %Y") + "<br \>\n")
ff.write("Node Version: " + str(info['version']) + "<br \>\n")
ff.write("Protocol Version: " + str(info['protocolversion']) + "<br \>\n")
ff.write("Connections: " + str(info['connections']) + "<br \>\n")
ff.write("Blocks: " + str(info['blocks']) + "<br \>\n")
ff.write("Location: " + node_location + "<br />")
ff.write("Node created by " + node_name + "<br />")
ff.write("Donate: <a href='https://ledger.paycoin.com/address/" + donation_xpy_addr + "'>")
ff.write(donation_xpy_addr + "</a>")
ff.write("</h3>")

ff.write("<img src='http://qrfree.kaywa.com/?l=1&amp;s=4&amp;d=" + donation_xpy_addr + "' alt='QRCode'>")
ff.write("</div>")
ff.write("</body></html>")

ff.close()
