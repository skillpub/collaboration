import paramiko
import time
import re
import threading
import warnings
warnings.filterwarnings(action='ignore',module='.*paramiko.*')

class SSH:
    def __init__(self):
        self.host = ""
        self.username = ""
        self.password = ""
        #self.SSHKEY = "../.ssh/my_key"
        self.shell = None
        self.client = None
    
    def callback(*arg, **kw):
        return
    
    def connect(self, host, port=22, username=None, password=None, callback=None, timeout=5):
        self.host = host
        self.port = port
        self.username = username
        self.password = password
        if callable(callback): self.callback = callback
        self.timeout = timeout
        try:
            self.client = paramiko.SSHClient()
            self.client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            self.client.connect(hostname=self.host, port=self.port, username=self.username, password=self.password, timeout=self.timeout)
            self.shell = self.client.invoke_shell()
            if self.callback is not None:
                self.ssh_recv = self.ShellRecv(self.shell, self.callback)
                self.ssh_recv.start()
            return(0)
        except Exception as e:
            self.callback(str(e))
            return(1)
    
    def cmd(self, command):
        if len(command) == 0: return(0)
        command += "\n"
        try:
            self.shell.send(command)
            return(0)
        except Exception as e:
            self.callback(str(e))
            return(1)
        
    def close(self):
        try:
            self.client.close()
            return(0)
        except Exception as e:
            self.callback(str(e))
            return(1)
        
    def is_connected(self):
        try:
            return(not self.shell.closed)
        except Exception as e:
            self.callback(str(e))
            return(False)
        
    class ShellRecv(threading.Thread):    
        def __init__(self, shell, callback):
            threading.Thread.__init__(self)
            self.shell = shell
            self.callback = callback
            self.loop_delay = 1
            self.daemon = True

        def run(self):
            while True:
                if self.shell.closed : break
                time.sleep(self.loop_delay)
                if self.shell.recv_ready():
                    data = self.shell.recv(65535)
                    self.callback(data.decode())
