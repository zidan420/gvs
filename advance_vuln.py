import subprocess
# import os

def execute_smuggler(url):
	# os.chdir('smuggler-master')
	smuggler_output_stdout = subprocess.run(f"py smuggler-master\\smuggler.py -u {url}", shell=True, stdout=subprocess.PIPE)
	smuggler_output = smuggler_output_stdout.stdout.decode()
	# print(smuggler_output)

	return 'CRITICAL' in smuggler_output 	#return true/false

# vuln_or_not = execute_smuggler('ac321fe71edf3fd480e80cc000a8006d.web-security-academy.net')
# print(vuln_or_not)