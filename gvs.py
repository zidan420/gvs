#!/usr/bin/python3
import scanner
from bs4 import BeautifulSoup
import argparse
import banner
import sys
import os

#gvs --> Generic Vulnerability Scanner

# http://192.168.0.199/dvwa/
# http://192.168.0.199/dvwa/logout.php
# gvs.py -u admin -p password -iF ignore.txt -t http://192.168.0.199/dvwa/

def main():
	parser = argparse.ArgumentParser()
	parser.add_argument('-u', '--username', help="Specify the Username or Email")
	parser.add_argument('-p', '--password', help="Specify the Password")
	parser.add_argument('-t', '--target', help="Specify the Target URL")
	parser.add_argument('-o', '--output', action="store_true", help="Output to a File")
	parser.add_argument('-iF', '--ignore', help="Write the links in a File to ignore")
	args = parser.parse_args()
	username = args.username
	password = args.password
	target_url = args.target
	ignore_links_file = args.ignore
	ouput_boolean = args.output

	if target_url == None:
		parser.print_help()
		exit()

	vuln_banner = banner.banner('gvs')
	print(f'\n{vuln_banner}')

	links_to_ignore = []
	if ignore_links_file != None:
		with open(ignore_links_file) as file:
			for link in file:
				links_to_ignore.append(link)

	vuln_scanner = scanner.Scanner(target_url, links_to_ignore)

	# parse_html = BeautifulSoup(vuln_scanner.session.get(target_url).content.decode(), features="html.parser")
	# input_list = parse_html.findAll('input')
	# for input in input_list:
	# 	input_name = input.get('name')
	# 	if input_name == "user_token":
	# 		session_token = input.get('value')
	# 		break
	# headers = {'Referer': target_url}
	# data_dict = {"username" : username, "password" : password, "Login" : "submit", "user_token" : session_token}
	# vuln_scanner.session.cookies.set('security', 'medium', domain='192.168.0.199', path='/dvwa')
	
	# vuln_scanner.session.post("http://192.168.0.199/dvwa/login.php", data=data_dict, headers=headers)

	if ouput_boolean:
		url = target_url.split('//')[1]
		domain = url.split('/')[0]
		octet_list = domain.split('.')
		if len(octet_list) == 3:
			output_file = octet_list[1]
		elif len(octet_list) == 2:
			output_file = octet_list[0]
		
		for i in range(200):
			file_name = output_file + str(i) + '.txt'
			file_exists = os.path.isfile(file_name)
			if not file_exists:
				break
		original_stdout = sys.stdout
		sys.stdout = open(file_name, 'w', encoding="utf-8")

	vuln_scanner.crawl()
	vuln_scanner.recon()
	vuln_scanner.run_scanner()
	
	if ouput_boolean:
		sys.stdout.close()
		sys.stdout = original_stdout
		print('Results are saved in --> ' + file_name)


if __name__ == '__main__':
	try:
		main()
	except KeyboardInterrupt:
		exit()