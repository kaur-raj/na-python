import paramiko #imported Paramiko library

#initialized variables.
ip = '192.168.2.110'
username = 'csrv'
password = 'cisco1234'

#created Paramiko SSHClient object
remote_conn_pre=paramiko.SSHClient()
remote_conn_pre.set_missing_host_key_policy(paramiko.AutoAddPolicy()) #automatically adding SSH host key
remote_conn_pre.connect(ip, port=22, username=username, password=password, look_for_keys=False, allow_agent=False)


