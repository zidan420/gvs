import argparse
import os

def delete_files():
	for file_name in file_list:
		os.remove(file_name)
	os.remove('logo.txt')

def return_logo():
	with open('logo.txt', encoding='utf-8') as f:
		return f.read()

def combine_file_columnwise():
	with open('logo.txt', 'w', encoding='utf-8') as writer:
		readers = [open(file_name, encoding='utf-8') for file_name in file_list]
		for lines in zip(*readers):
			print(' '.join([line.rstrip('\n') for line in lines]), file=writer)

def store_diagram(character, diagram):
	for i in range(200):
		file_name = character + str(i) + '.txt'
		file_exists = os.path.isfile(file_name)
		if not file_exists:
			file_list.append(file_name)
			break
	
	with open(file_name, 'w', encoding='utf-8') as f:
		f.write(diagram)

# {space * 6}----{space * 6}
#      / -- \     
#     / /  \ \    
#    /  ----  \   
#   /  ------  \  
#  /_/        \_\ 

def draw_a():
	diagram = rf"""░█████╗░ 
██╔══██╗
███████║
██╔══██║
██║░░██║
╚═╝░░╚═╝
"""
	store_diagram('a', diagram)

def draw_b():
	diagram = rf"""██████╗░
██╔══██╗
██████╦╝
██╔══██╗
██████╦╝
╚═════╝░
"""
	store_diagram('b', diagram)

def draw_c():
	diagram = rf"""░█████╗░
██╔══██╗
██║░░╚═╝
██║░░██╗
╚█████╔╝
░╚════╝░
"""
	store_diagram('c', diagram)

def draw_d():
	diagram = rf"""██████╗░
██╔══██╗
██║░░██║
██║░░██║
██████╔╝
╚═════╝░
"""
	store_diagram('d', diagram)

def draw_e():
	diagram = rf"""███████╗
██╔════╝
█████╗░░
██╔══╝░░
███████╗
╚══════╝
"""
	store_diagram('e', diagram)

def draw_f():
	diagram = rf"""███████╗
██╔════╝
█████╗░░
██╔══╝░░
██║░░░░░
╚═╝░░░░░
"""
	store_diagram('f', diagram)

def draw_g():
	diagram = rf"""░██████╗░
██╔════╝░
██║░░██╗░
██║░░╚██╗
╚██████╔╝
░╚═════╝░
"""
	store_diagram('g', diagram)

def draw_h():
	diagram = rf"""██╗░░██╗
██║░░██║
███████║
██╔══██║
██║░░██║
╚═╝░░╚═╝
"""
	store_diagram('h', diagram)

def draw_i():
	diagram = rf"""██╗
██║
██║
██║
██║
╚═╝
"""
	store_diagram('i', diagram)

def draw_j():
	diagram = rf"""░░░░░██╗
░░░░░██║
░░░░░██║
██╗░░██║
╚█████╔╝
░╚════╝░
"""
	store_diagram('j', diagram)

def draw_k():
	diagram = rf"""██╗░░██╗
██║░██╔╝
█████═╝░
██╔═██╗░
██║░╚██╗
╚═╝░░╚═╝
"""
	store_diagram('k', diagram)

def draw_l():
	diagram = rf"""██╗░░░░░
██║░░░░░
██║░░░░░
██║░░░░░
███████╗
╚══════╝
"""
	store_diagram('l', diagram)

def draw_m():
	diagram = rf"""███╗░░░███╗
████╗░████║
██╔████╔██║
██║╚██╔╝██║
██║░╚═╝░██║
╚═╝░░░░░╚═╝
"""
	store_diagram('m', diagram)

def draw_n():
	diagram = rf"""███╗░░██╗
████╗░██║
██╔██╗██║
██║╚████║
██║░╚███║
╚═╝░░╚══╝
"""
	store_diagram('n', diagram)

def draw_o():
	diagram = rf"""░█████╗░
██╔══██╗
██║░░██║
██║░░██║
╚█████╔╝
░╚════╝░
"""
	store_diagram('o', diagram)

def draw_p():
	diagram = rf"""██████╗░
██╔══██╗
██████╔╝
██╔═══╝░
██║░░░░░
╚═╝░░░░░
"""
	store_diagram('p', diagram)

def draw_q():
	diagram = rf"""░██████╗░
██╔═══██╗
██║██╗██║
╚██████╔╝
░╚═██╔═╝░
░░░╚═╝░░░
"""
	store_diagram('q', diagram)

def draw_r():
	diagram = rf"""██████╗░
██╔══██╗
██████╔╝
██╔══██╗
██║░░██║
╚═╝░░╚═╝
"""
	store_diagram('r', diagram)

def draw_s():
	diagram = rf"""░██████╗
██╔════╝
╚█████╗░
░╚═══██╗
██████╔╝
╚═════╝░
"""
	store_diagram('s', diagram)

def draw_t():
	diagram = rf"""████████╗
╚══██╔══╝
░░░██║░░░
░░░██║░░░
░░░██║░░░
░░░╚═╝░░░
"""
	store_diagram('t', diagram)

def draw_u():
	diagram = rf"""██╗░░░██╗
██║░░░██║
██║░░░██║
██║░░░██║
╚██████╔╝
░╚═════╝░
"""
	store_diagram('u', diagram)

def draw_v():
	diagram = rf"""██╗░░░██╗
██║░░░██║
╚██╗░██╔╝
░╚████╔╝░
░░╚██╔╝░░
░░░╚═╝░░░
"""
	store_diagram('v', diagram)

def draw_w():
	diagram = rf"""░██╗░░░░░░░██╗
░██║░░██╗░░██║
░╚██╗████╗██╔╝
░░████╔═████║░
░░╚██╔╝░╚██╔╝░
░░░╚═╝░░░╚═╝░░
"""
	store_diagram('w', diagram)

def draw_x():
	diagram = rf"""██╗░░██╗
╚██╗██╔╝
░╚███╔╝░
░██╔██╗░
██╔╝╚██╗
╚═╝░░╚═╝
"""
	store_diagram('x', diagram)

def draw_y():
	diagram = rf"""██╗░░░██╗
╚██╗░██╔╝
░╚████╔╝░
░░╚██╔╝░░
░░░██║░░░
░░░╚═╝░░░
"""
	store_diagram('y', diagram)

def draw_z():
	diagram = rf"""███████╗
╚════██║
░░███╔═╝
██╔══╝░░
███████╗
╚══════╝
"""
	store_diagram('z', diagram)

def banner(text):
	global file_list
	file_list = []
	text_length = len(text)
	for character in text:
		if character == 'a' or character == 'A':
			draw_a()
		if character == 'b' or character == 'B':
			draw_b()
		if character == 'c' or character == 'C':
			draw_c()
		if character == 'd' or character == 'D':
			draw_d()
		if character == 'e' or character == 'E':
			draw_e()
		if character == 'f' or character == 'F':
			draw_f()
		if character == 'g' or character == 'G':
			draw_g()
		if character == 'h' or character == 'H':
			draw_h()
		if character == 'i' or character == 'I':
			draw_i()
		if character == 'j' or character == 'J':
			draw_j()
		if character == 'k' or character == 'K':
			draw_k()
		if character == 'l' or character == 'L':
			draw_l()
		if character == 'm' or character == 'M':
			draw_m()
		if character == 'n' or character == 'N':
			draw_n()
		if character == 'o' or character == 'O':
			draw_o()
		if character == 'p' or character == 'P':
			draw_p()
		if character == 'q' or character == 'Q':
			draw_q()
		if character == 'r' or character == 'R':
			draw_r()
		if character == 's' or character == 'S':
			draw_s()
		if character == 't' or character == 'T':
			draw_t()
		if character == 'u' or character == 'U':
			draw_u()
		if character == 'v' or character == 'V':
			draw_v()
		if character == 'w' or character == 'X':
			draw_w()
		if character == 'x' or character == 'X':
			draw_x()
		if character == 'y' or character == 'Y':
			draw_y()
		if character == 'z' or character == 'Z':
			draw_z()
	combine_file_columnwise()
	logo = return_logo()
	delete_files()
	return logo

def main():
	parser = argparse.ArgumentParser()
	parser.add_argument('-t', '--text', help="Text to be used as banner")
	args = parser.parse_args()
	text = args.text

	if text == None:
		parser.print_help()
		exit()

	logo = banner(text)
	print(logo)

if __name__ == '__main__':
	main()