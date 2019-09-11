'''connects via ssh to servers'''
import paramiko
import time
import sys
sys.path.insert(0, '../modules')
from sshlib import SSH

commands = ["help", "boot log", "cli"]
servers = ["us01"]

USERNAME = "nasahelper"
SSHKEY = "../.ssh/nasahelper-ssh-key"

NAME2IP_LIST = {"us01" : "XXX.XXX.XXX.XXX"}
                
argv = ' '.join(sys.argv)

command = next((command for command in commands if command in argv), None)
server = next((server for server in servers if server in argv), None)

def ssh_print(s):
    print(s)

if command is None: 
    print("tell me what to do, one of these commands - {}".format(', '.join(commands)))
    sys.exit()
    
if command == "help":
    help_str = '''to get boot logs text me "ssh boot log <server>"\nto open command line interface text me "ssh cli <server>"\navailable servers: {}\n'''.format(', '.join(servers))
    print(help_str)
    sys.exit()
    
if server is None: 
    print("specify the server, one of these - {}".format(', '.join(servers)))
    sys.exit()
    
if command == "boot log":
    
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(hostname=NAME2IP_LIST[server], username=USERNAME, key_filename=SSHKEY)

    shell = client.invoke_shell()
    time.sleep(2.0)
    data = shell.recv(65000)
    
    cmd = 'sudo cat /var/log/boot.log\n'
    shell.send(cmd)
    time.sleep(0.2)
    data = shell.recv(65000).decode()
    
    client.close()
    
    print({server+"_boot.log" : data})
    
if command == "cli":
    
    ssh = SSH()
    
    print("connecting ..., close it as usual - exit or smth like that")
    
    res = ssh.connect(host=NAME2IP_LIST[server], username=USERNAME, key_filename=SSHKEY, callback=ssh_print)

    if res == 1:
        print("can't connect")
        sys.exit()

    while ssh.is_connected():
        if (ssh.cmd(input())) != 0 : break 
        time.sleep(2)

