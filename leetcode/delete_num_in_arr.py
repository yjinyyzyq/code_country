# coding:utf-8
# 把当前拍摄的可以用于识别的图片发送给服务器识别程序，直接进行识别。
import paramiko
user = "guowenjia"
ips = "120.26.81.70"
password = "........."
port = 22

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
local_file = "/"
remote_file = "/home/guowenjia/lottery_reco/1.jpg"
ssh.connect(ips, port, user, password)
a = ssh.exec_command("date")
stdin, stdout, stderr = a
print(stdout.read())
sftp = paramiko.SFTPClient.from_transport(ssh.get_transport())
sftp = ssh.open_sftp()
sftp.put(local_file, remote_file)
print("success")

