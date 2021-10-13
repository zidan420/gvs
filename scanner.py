#!/usr/bin/python3
import requests
import re
import advance_vuln
from urllib.parse import urljoin
from bs4 import BeautifulSoup
from threading import Thread
# import concurrent.futures

# Tips:
# 1. Class names always start with capital Letter (e.g. Scanner NOT scanner)

class Scanner:
	def __init__(self, url, ignore_links):
		self.session = requests.Session()
		self.target_url = url
		self.links_to_ignore = ignore_links
		self.target_links = []

	def extract_link_from(self, url):
		response = self.session.get(url)
		try:
			response = response.content.decode()
			return re.findall('(?:href=")(.*?)"', response)
		except:
			return []

	def thread_crawl(self, link):
		if self.target_url in link and link not in self.target_links and link not in self.links_to_ignore:
			self.target_links.append(link)
			print(link)
			self.crawl(link)

	def crawl(self, url=None):
		if url == None:
			print("\n###### Crawling Links ######\n")
			url = self.target_url
			self.target_links.append(url)
			print(url)

		threads_list = []
		href_links = self.extract_link_from(url)
		for link in href_links:
			link = urljoin(url, link)

			if "#" in link:
				link = link.split("#")[0]
			
			t = Thread(target=self.thread_crawl, args=(link,))
			t.start()
			threads_list.append(t)

		# wait for all threads to stop
		for x in threads_list:
			x.join()

	def extract_forms(self, url):
		try:
			response = self.session.get(url).content.decode()
			parse_html = BeautifulSoup(response, features="html.parser")
			return parse_html.findAll('form')
		except:
			return []

	def submit_form(self, form, value, url):
		form_action = form.get('action')
		post_url = urljoin(url, form_action)
		form_method = form.get('method')
		input_list = form.findAll('input')
		post_data = {}
		for input in input_list:
			input_name = input.get('name')
			input_type = input.get('type')
			input_value = input.get('value')
			if input_type == "text":
				input_value = value
			if input_type == "password":
				input_value = value
			post_data[input_name] = input_value
		if form_method == "post" or form_method == "POST":
			return self.session.post(post_url, data=post_data)
		elif form_method == "get" or form_method == "GET":
			return self.session.get(post_url, params=post_data)

	def recon(self):
		print("\n###### Gathering Information ######\n")
		self.server_and_language_written_in()
		self.interesting_files()

	def thread_scan(self, link):
		output = ""
		output += f"\n[+] Testing {link}"
		forms_list = self.extract_forms(link)

		for form in forms_list:
			### SQLI VULNERABILITY ###
			# is_form_vulnerable_to_sqli = self.test_sqli_in_forms(form, link)
			# if is_form_vulnerable_to_sqli:
			# 	print("\n\n[***] SQLI discovered in the " + link + " in the following form:")
			# 	print(str(form) + "\n\n")
			### XSS VULNERABILITY ###
			form_vuln_to_xss = self.test_xss_in_forms(form, link)
			if form_vuln_to_xss:
				payload = form_vuln_to_xss
				output += f"\n\n[***] XSS discovered with {payload} in the following form:\n{str(form)}\n"
			### LFI VULNERABILITY ###
			form_vuln_to_lfi = self.test_lfi_in_forms(form, link)
			if form_vuln_to_lfi:
				output += f"\n\n[***] LFI discovered in the following form:\n{str(form)}\n"
		if "=" in link:
			### XSS VULNERABILITY ###
			link_vuln_to_xss = self.test_xss_in_links(link)
			if link_vuln_to_xss:
				payload = link_vuln_to_xss
				output += f"\n\n[***] Discovered XSS with {payload}\n"
			### LFI VULNERABILITY ###
			link_vuln_to_lfi = self.test_lfi_in_links(link)
			if link_vuln_to_lfi:
				output += f"\n\n[***] Discovered LFI with {payload}\n"
			### OPEN URL REDIRECT ###
			url_redirect_vuln = self.open_url_redirect(link)
			if url_redirect_vuln:
				evil_url = url_redirect_vuln
				output += f"\n\n[***] Discovered Open URL Redirect with {evil_url}\n"
		### HOST HEADER INJECTION ###
		host_header_vuln = self.inject_host_header(link)
		if host_header_vuln:
			payload = host_header_vuln
			output += f"\n\n[***] Discovered Host Header Injection with: {payload}\n"
		### OPEN URL REDIRECT ###
		### HTTP Request Smuggler ###
		# smuggler_vuln_boolean = advance_vuln.execute_smuggler(link)
		# if smuggler_vuln_boolean:
		# 	output += f"\n\n[***] Vulnerable to HTTP Request Smuggling\n"
		print(output)

	def run_scanner(self):
		print("\n###### Testing For Vulnerabilities ######\n")
		threads_list = []
		for link in self.target_links:
			thread_skip = False
			ignore_file_link = ['.css', '.pdf', '.js', '.zip', '.ico', '.svg', '.jpg', '.png', '.woff2']
			for file_type in ignore_file_link:
				if file_type in link[-5:]:
					thread_skip = True
			if thread_skip:
				continue
			t = Thread(target=self.thread_scan, args=(link,))
			t.start()
			threads_list.append(t)

		# wait for all threads to stop
		for x in threads_list:
			x.join()

	def server_and_language_written_in(self):
		response = self.session.get(self.target_url)
		for header in response.headers:
			if header == "X-Powered-By":
				print(f"{header}: {response.headers[header]}")
			if header == "Server":
				print(f"{header}: {response.headers[header]}")

	def interesting_files(self):
		file_list = ['robots.txt', 'sitemap.xml', 'sitemap.xml.gz', 'crossdomain.xml', 'phpinfo.php', 'test.php', 'elmah.axd', 'server-status', 'jmx-console/', 'admin-console/', 'web-console/']
		for file in file_list:
			if self.target_url[-1] == '/':
				interesting_file_path = self.target_url + file
			else:
				interesting_file_path = self.target_url + '/' + file
			response = self.session.get(interesting_file_path)
			if response.ok:
				print(f"[+] Interesting File: {interesting_file_path}")

	def test_lfi_in_links(self, url):
		lfi_payload = '& dir #'
		evil_url = url.replace('=', '=' + lfi_payload)
		response = self.session.get(evil_url)
		return '<DIR>' in response.content.decode()

	def test_lfi_in_forms(self, form, url):
		lfi_payload = ' & dir'
		response = self.submit_form(form, lfi_payload, url)
		if response == None:
			return False
		return '<DIR>' in response.content.decode()

	def test_sqli_in_forms(self, form, url):
		sqli_payload = "'or'1'='1'#"
		response = self.submit_form(form, sqli_payload, url)
		if response == None:
			return False
		return sqli_payload in response.content.decode()

	def test_xss_in_links(self, url):
		with open('small_xss_payload.txt', encoding="utf8") as file:
			for xss_payload in file:
				xss_payload = xss_payload.rstrip()
				evil_url = url.replace('=', '=' + xss_payload)
				response = self.session.get(evil_url)
				response = response.content.decode()
				if xss_payload in response:
					return xss_payload
			return False
		# return xss_payload in response.content.decode()

	def test_xss_in_forms(self, form, url):
		with open('small_xss_payload.txt', encoding="utf8") as file:
			# max_lines_in_file = len(file.readlines())
			# num_of_lines_read = 0
			# file.seek(0)
			for xss_payload in file:
				xss_payload = xss_payload.rstrip()
				# print("\r[+] Payload: " + xss_payload, end="")
				# with concurrent.futures.ThreadPoolExecutor() as executor:
				# 	    future = executor.submit(self.submit_form, form, xss_payload, url)
				response = self.submit_form(form, xss_payload, url)
				if response == None:
					return False
				response = response.content.decode()
				if xss_payload in response:
					return xss_payload
				# num_of_lines_read += 1
				# percentage_of_lines_read = int(num_of_lines_read/max_lines_in_file * 100)
				# print('\r\t[+] Percentage Of File Read: ' + str(percentage_of_lines_read) + "%", end='')
			# print('\r' + space, end='')
			return False

	def inject_host_header(self, url):
		payload_list = [{'Host':'www.bing.com'}, {'Host':'www.bing.com', 'X-Forwarded-Host':url}, 
		{'Host':url, 'X-Forwarded-Host':'www.bing.com'}, {'Host':url, 'X-Forwarded-Host':'www.bing.com', 
		'X-Forwarded-Host':'www.bing.com'}]
		for payload in payload_list:
			try:
				response = self.session.get(url, headers=payload)
			except requests.exceptions.ConnectionError:
				continue
			html_parse = BeautifulSoup(response.content, features="html.parser")
			site_title = html_parse.find(text='Bing')
			if site_title:
				return payload
		return False

	def open_url_redirect(self, url):
		with open('small_url_redirect_payload.txt', encoding="utf8") as f:
			for payload in f:
				payload = payload.rstrip()
				evil_url = url.replace('=', '=' + payload + '#')
				response = self.session.get(evil_url)
				html_parse = BeautifulSoup(response.content, features="html.parser")
				site_title = html_parse.find(text='Google')
				if site_title:
					return evil_url
			return False