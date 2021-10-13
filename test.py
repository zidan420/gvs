import subprocess

output = subprocess.run(['curl','https://gitlab.com/','--head'], shell=True, capture_output=True)
print(output.stdout.decode())