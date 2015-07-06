#!/usr/bin/python
from bitcoinrpc.authproxy import AuthServiceProxy
import time

www_file = "/var/www/html/index.html"
rpc_user = ""
rpc_pass = ""
node_location = ""
node_name = ""
node_ip = ""
donation_xpy_addr = ""

access = AuthServiceProxy("http://" + rpc_user + ":" + rpc_pass + "@127.0.0.1:8999")
info = access.getinfo()

ff = open(www_file, 'w')


ff.write("<!DOCTYPE html>")
ff.write("<html lang='en-us'>")
ff.write("<head>")
ff.write("<meta charset='utf-8'>")
ff.write("<title>Paycoin Node Status</title>")
ff.write("<link href='http://fonts.googleapis.com/css?family=Exo+2:300,400' rel='stylesheet' type='text/css'>")
ff.write("<style type='text/css'> ")
ff.write("</style>")
ff.write("</head>")
ff.write("<body>")

ff.write("<link href='http://fonts.googleapis.com/css?family=Exo+2:300,400' rel='stylesheet' type='text/css'>")
ff.write("<style>")

ff.write("/* Eric Meyer's Reset CSS v2.0 - http://cssreset.com */")
ff.write("html,body,div,span,applet,object,iframe,h1,h2,h3,h4,h5,h6,p,blockquote,pre,a,abbr,acronym,address,big,cite,code,del,dfn,em,img,ins,kbd,q,s,samp,small,strike,strong,sub,sup,tt,var,b,u,i,center,dl,dt,dd,ol,ul,li,fieldset,form,label,legend,table,caption,tbody,tfoot,thead,tr,th,td,article,aside,canvas,details,embed,figure,figcaption,footer,header,hgroup,menu,nav,output,ruby,section,summary,time,mark,audio,video{border:0;font-size:100%;font:inherit;vertical-align:baseline;margin:0;padding:0}article,aside,details,figcaption,figure,footer,header,hgroup,menu,nav,section{display:block}body{line-height:1}ol,ul{list-style:none}blockquote,q{quotes:none}blockquote:before,blockquote:after,q:before,q:after{content:none}table{border-collapse:collapse;border-spacing:0}")

ff.write("html,body{height:100%;}")
ff.write("body{")
ff.write("color: #444;")
ff.write("background: url(https://dl.dropboxusercontent.com/u/37902134/PaycoinNodeBackground.png) no-repeat; background-size: 100%")
ff.write("}")

ff.write("#wrap{")
ff.write("background-color: rgba(255, 255, 255, 0.6);")
ff.write("width: 100%;")
ff.write("height: 100%;")
ff.write("line-height: 1.4;")
ff.write("font-size: 24px;")
ff.write("font-family: 'Exo 2', sans-serif;")
ff.write("}")

ff.write("h3{")
ff.write("font-weight: 300;")
ff.write("}")

ff.write("h1{")
ff.write("font-weight: 400;")
ff.write("margin-bottom: 15px;")
ff.write("}")
ff.write("</style>")
ff.write("<div id='wrap'>")
ff.write("<h1>Paycoin Node: " + node_ip + ":8998<br \></h1>")
ff.write("<h3>")

ff.write("Last Update: " + time.strftime("%l:%M:%S %p (%z %Z) on %-d %b %Y") + "<br \>\n")
ff.write("Connections: " + str(info['connections']) + "<br \>\n")
ff.write("Blocks: " + str(info['blocks']) + "<br \>\n")
ff.write("Difficulty: " + str(info['difficulty']) + "<br \>\n")

ff.write("Location: " + node_location + "<br />")
ff.write("Node created by " + node_name + "<br />")
ff.write("Donate: <a href='https://ledger.paycoin.com/address/" + donation_xpy_addr + "'>")
ff.write(donation_xpy_addr + "</a>")
ff.write("</h3>")

ff.write("<img src='http://qrfree.kaywa.com/?l=1&amp;s=4&amp;d=" + donation_xpy_addr + "' alt='QRCode'>")
ff.write("</div>")
ff.write("</body></html>")

ff.close()