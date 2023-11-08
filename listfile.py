import subprocess

command = "ls -la" 
#can type he cmt you want to execute in shell Like windows , linux kernel , Mac
subprocess.Popen(command,shell =True)