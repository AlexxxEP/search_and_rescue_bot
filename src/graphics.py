#!/usr/bin/env python3
# ---  ---  ---  ---  ---
# file name:         graphics.py
# description :		 collection of graphical assets
#					 for console echo and prints
#
# author:            Alexandre EANG
# created on:        2023 12 22
# last updated:      2023 12 24
# updated by:        Alexandre EANG
# comment :          * Created file
# 				 	 * Added 2 logo variants
#					 * Added console clear
# ---  ---   ---  ---  ---  ---
print("# importing {}".format(__name__))



# ---  IMPORTS  ---  ---  ---  ---
# ---  ---   ---  ---  ---  ---
from time import sleep
import json
# import threading

# ---  DECLARATIONS  ---
# --- CONSTANTS / CONFIG
PERIPH =[]
SYS =[]
module_init = False

gui_drawrobot = True

# --- GRAPHIC RESSOURCES 
loading_flag = True

# --- GRAPHIC RESSOURCES 
ansicolor={
	"style" : {
		'reset'	:	'0',
		'italic':	'1'
	},
	"textcolor" : {
		'reset'	:	'0',
		'black'	:   '30',
		'green':   '32',
		'blue'	:	'34',
		'cyan'	:	'36'
	},
	"bgcolor" : {
		'reset'	:	'0',
		'red'	:	'42',
		'blue'	:	'44',
		'cyan'	:	'46',
		'yellow':	'48'
	}
}


d_lw=[
	# --- line 1
	{
		'n' :(
				'                  ' ,
				''
			),
		'd'	:(
				'                  ' ,
				'    \\\\  \\\\  \\\\'
			),
		'r'	:(
				'    //  //  //    ' ,
				''
			)
	},
	# --- line 2
	{
		'n' 	:(
						'                  ' ,
						''
					 ),
		'd'	:(
						'                  ' ,
						'     ))  ))  ))'
					 ),
		'r'	:(
						'   ((  ((  ((     ' ,
						''
					 )
	},
	# --- line 3
	{
		'n' 	:(
						'                  ' ,
						''
					 ),
		'd'	:(
						'                  ' ,
						'     //  //  // '
					 ),
		'r'	:(
						'    \\\\  \\\\  \\\\    ' ,
						''
					 )
	},
]
d_rw=[
	# --- line 1
	{
		'n' :(
				'                  ' ,
				'  ___'
			),
		'd'	:(
				'                  ' ,
				'  __\\\\  \\\\  \\\\'
			),
		'r'	:(
				'    //  //  //    ' ,
				''
			)
	},
	# --- line 2
	{
		'n' 	:(
						'                  ' ,
						''
					 ),
		'd'	:(
						'                  ' ,
						'  ))  ))'
					 ),
		'r'	:(
						'   ((  ((  ((     ' ,
						''
					 )
	},
	# --- line 3
	{
		'n' 	:(
						'                  ' ,
						''
					 ),
		'd'	:(
						'                  ' ,
						' //  // '
					 ),
		'r'	:(
						'    \\\\  \\\\  \\\\    ' ,
						''
					 )
	},
]
d_clw=[
	# --- line 1
	{
		'n' :('  _____________'),
		'c' :('    __________'),
		'o' :('  //──────/')
	},
	# --- line 2
	{
		'n' :('  //────────────\\\\'),
		'c' :('   / ────  ──── \\'),
		'o' :('  //')
	},
	# --- line 3
	{
		'n' :('||'),
		'c' :(' //            \\\\'),
		'o' :('||')
	},
	# --- line 4
	{
		'n' :('||'),
		'c' :('//             ||'),
		'o' :('||')
	},
	# --- line 5
	{
		'n' :(' ||'),
		'c' :(' \\\\	         //'),
		'o' :(' ||')
	},
	# --- line 6
	{
		'n' :('||'),
		'c' :(' \\\\_      ____//'),
		'o' :('||')
	},
	# --- line 7
	{
		'n' :(' \\\\____________//'),
		'c' :('   \\\\____─────'),
		'o' :(' \\\\')
	},
	# --- line 8
	{
		'n' :('      ───────────'),
		'c' :(''),
		'o' :('     \\\\______')
	},
	# --- line 9
	{
		'n' :(''),
		'c' :(''),
		'o' :('    ──────\\')
	},
	# --- line 10
	{
		'n' :(''),
		'c' :('    ||'),
		'o' :('')
	},
	# --- line 11
	{
		'n' :(''),
		'c' :('    ╠╣'),
		'o' :('')
	},
	# --- line 12
	{
		'n' :(''),
		'c' :('    ||'),
		'o' :('')
	},
]
# ---  ---  ---  ---  ---  ---



# ---  FUNCTION DEFINITION  ---
def init(*args):
	"""
	init
	"""
	global PERIPH
	global SYS
	global module_init
	global gui_drawrobot

	try:
		PERIPH = args[0]
		module_init = True
	except:
		print("\n\t>>> Failed to call PERIPH from {}".format(__name__))
		return 1
	try:
		SYS = args[1]
		gui_drawrobot = SYS["gui_drawrobot"]
	except:
		print("\n\t>>> Failed to call SYS from {}".format(__name__))
		return 1
	return



def CLEAR_CONSOLE(n=50):
	for k in range(n):
		print("\n")
	return


def echo(text, text_color='reset', bg_color='reset', text_style='reset'):
	"""
	"""
	# global ansicolor
	end="`\033[0;0;0m"
	styling = "\033["

	try:
		styling += ansicolor["style"][text_style]
	except:
		styling += ansicolor["style"]['reset']
	styling += ';'
	try:
		styling += ansicolor["textcolor"][text_color]
	except:
		styling += ansicolor["textcolor"]['reset']
	styling += ';'
	try:
		styling += ansicolor["bgcolor"][bg_color]
	except:
		styling += ansicolor["bgcolor"]['reset']
	styling += 'm'

	print(styling+text+end)
	return


def loading_animation(arg='',length=8, timeout=500):
	counter = 0
	global loading_flag
	loading_flag=True
	brk_request = False

	bar = []
	for k in range(length):
		bar.append('-')
	donebar =''
	for k in range(length):
		donebar += " "
	errorbar =''
	for k in range(length):
		errorbar += "="

	while True:
		counter += 1*length
		if (counter > timeout):
			print("||\033[0;0;41m"+errorbar+"\033[0;0;0m||Error.")
			print("\n\t>>> TIMED OUT")
			return

		for k in range(0,length):
			string=''
			bar[k] = '\033[1;30;46m \033[0;0;0m'
			for j in range(0,length):
				string += bar[j]
			CLEAR_CONSOLE(5)
			print("||"+string+"\033[0;0;0m||"+arg)
			sleep(0.01)
			if (loading_flag!=True): brk_request= True
		if brk_request: break

		for k in range(0,length):
			string=''
			bar[k] = '\033[1;37;40m-\033[0;0;0m'
			for j in range(0,length):
				string += bar[j]
			CLEAR_CONSOLE(5)
			print("||"+string+"\033[0;0;0m||"+arg)
			sleep(0.01)
			if (loading_flag!=True): brk_request= True
		if brk_request: break

		for k in range(0,length):
			string=''
			bar[k] = '\033[1;30;46m \033[0;0;0m'
			for j in range(0,length):
				string += bar[length-j-1]
			CLEAR_CONSOLE(5)
			print("||"+string+"\033[0;0;0m||"+arg)
			sleep(0.01)
			if (loading_flag!=True): brk_request= True
		if brk_request: break

		for k in range(0,length):
			string=''
			bar[k] = '\033[0;0;0m-\033[0;0;0m'
			for j in range(0,length):
				string += bar[length-j-1]
			CLEAR_CONSOLE(5)
			print("||"+string+"\033[0;0;0m||"+arg)
			sleep(0.01)
			if (loading_flag!=True): brk_request= True
		if brk_request: break

	CLEAR_CONSOLE(5)	
	print("||\033[0;0;42m"+donebar+"\033[0;0;0m||Done.")
	return

def TECHNOBOTS_LOGO(style='slant'):
	if (style == 'slant'):
		print("______________________________________________________________")
		print("  ____________________  ____  ______  __    ____  ___________")
		print(" /_  __/ ____/ ____/ / / / | / / __ \\/ /_  / __ \\/_  __/ ___/")
		print("  / / / __/ / /   / /_/ /  |/ / / / / __ \\/ / / / / /  \\__ \\ ")
		print(" / / / /___/ /___/ __  / /|  / /_/ / /_/ / /_/ / / /  ___/ / ")
		print("/_/ /_____/\\____/_/ /_/_/ |_/\\____/_____/\\____/ /_/  /____/  ")
		print("______________________________________________________________")
		
	if (style == 'left slant'):
		print("  _________  _______   ________  ___  ___  ________   ________  ________  ________  _________  ________      ")
		print(" |\\___   ___\\\\   ___\\ |\\   ____\\|\\  \\|\\  \\|\\   ___  \\|\\   __  \\|\\   __  \\|\\   __  \\|\\___   ___\\\\   ____\\     ")
		print(" \\|___ \\  \\_| \\  \\__| \\ \\  \\___|\\ \\  \\\\\\  \\ \\  \\\\ \\  \\ \\  \\|\\  \\ \\  \\|\\ /_ \\  \\|\\  \\|___ \\  \\_| \\  \\___|_    ")
		print("      \\ \\  \\ \\ \\   ___\\\\ \\  \\    \\ \\   __  \\ \\  \\\\ \\  \\ \\  \\\\\\  \\ \\   __  \\ \\  \\\\\\  \\   \\ \\  \\ \\ \\_____  \\   ")
		print("       \\ \\  \\ \\ \\  \\__|_\\ \\  \\____\\ \\  \\ \\  \\ \\  \\\\ \\  \\ \\  \\\\\\  \\ \\  \\|\\  \\ \\  \\\\\\  \\   \\ \\  \\ \\|____|\\  \\  ")
		print("        \\ \\__\\ \\ \\______\\\\ \\_______\\ \\__\\ \\__\\ \\__\\\\ \\__\\ \\_______\\ \\_______\\ \\_______\\   \\ \\__\\  ____\\_\\  \\ ")
		print("         \\|__|  \\|_______|\\|_______|\\|__|\\|__|\\|__| \\|__|\\|_______|\\|_______|\\|_______|    \\|__| |\\_________\\")
		print("                                                                                                 \\|_________|")
	return

def ROBOT(lw_status='n' , rw_status='n', clw_status='n'):
	

	lws=lw_status
	rws=rw_status
	clws=clw_status

	# SYNTAX FOR PYTHON 3.6+
	
	# print(f"{d_lw[0][lws][0]} |▓▓▓▓▓▓▓▓▓\\      {d_lw[0][lws][1]}")
	# print(f"{d_lw[1][lws][0]}||▓▓▓▓▓▓▓▓▓▓|\\    {d_lw[1][lws][1]}")
	# print(f"{d_lw[2][lws][0]} \\____..____\\|   {d_lw[2][lws][1]}")
	# print(f" _______________________||____     _____          {d_clw[0][clws]}")
	# print(f"|▓[             ▓▓▓▓▓▓▓▓▓▓▓▓▓▓|\\  |▓▓   |        {d_clw[1][clws]}")
	# print(f"|▓[             ▓|          |▓||  |▓▓___|    ___  {d_clw[2][clws]}")
	# print(f"|▓[             ▓|          |▓|| |▓_________/  [) {d_clw[3][clws]}")
	# print(f"|▓[       ^     ▓|          |▓|| |▓     ▓▓▓▓|__[) ====___    {d_clw [9][clws]}")
	# print(f"|▓[     < □ >   ▓|          |▓|| |▓     ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓    {d_clw[10][clws]}")
	# print(f"|▓[       v     ▓|          |▓|| |▓_____▓▓▓▓|  [) ====	     {d_clw[11][clws]}")
	# print(f"|▓[             ▓|          |▓|| |▓         \\__[){d_clw[4][clws]}")
	# print(f"|▓[             ▓|__________|▓|| |▓               {d_clw[5][clws]}")
	# print(f"|▓[_____________▓▓▓▓▓▓▓▓▓▓▓▓▓▓||                  {d_clw[6][clws]}")
	# print(f"\\_\\____________________.._____\\|               {d_clw[7][clws]}")
	# print(f"     \\____||           ||                        {d_clw[8][clws]}")
	# print(f"{d_rw[0][rws][0]}  |▓▓▓▓▓▓▓▓▓\\     {d_rw[0][rws][1]}")
	# print(f"{d_rw[1][rws][0]} ||▓▓▓▓▓▓▓▓▓▓|\\   <[▓▓▓| {d_rw[1][rws][1]}")
	# print(f"{d_rw[2][rws][0]}  \\__________\\|   <[▓▓▓| {d_rw[2][rws][1]}")
	# print('')

	# SYNTAX FOR PYTHON 3.5.4
	
	print("{} |▓▓▓▓▓▓▓▓▓\\      {}".format(d_lw[0][lws][0],d_lw[0][lws][1]))
	print("{}||▓▓▓▓▓▓▓▓▓▓|\\    {}".format(d_lw[1][lws][0],d_lw[1][lws][1]))
	print("{} \\____..____\\|   {}".format(d_lw[2][lws][0],d_lw[2][lws][1]))
	print(" _______________________||____     _____          {}".format(d_clw[0][clws]))
	print("|▓[             ▓▓▓▓▓▓▓▓▓▓▓▓▓▓|\\  |▓▓   |        {}".format(d_clw[1][clws]))
	print("|▓[             ▓|          |▓||  |▓▓___|    ___  {}".format(d_clw[2][clws]))
	print("|▓[             ▓|          |▓|| |▓_________/  [) {}".format(d_clw[3][clws]))
	print("|▓[       ^     ▓|          |▓|| |▓     ▓▓▓▓|__[) ====___    {}".format(d_clw [9][clws]))
	print("|▓[     < □ >   ▓|          |▓|| |▓     ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓    {}".format(d_clw[10][clws]))
	print("|▓[       v     ▓|          |▓|| |▓_____▓▓▓▓|  [) ====	     {}".format(d_clw[11][clws]))
	print("|▓[             ▓|          |▓|| |▓         \\__[){}".format(d_clw[4][clws]))
	print("|▓[             ▓|__________|▓|| |▓               {}".format(d_clw[5][clws]))
	print("|▓[_____________▓▓▓▓▓▓▓▓▓▓▓▓▓▓||                  {}".format(d_clw[6][clws]))
	print("\\_\\____________________.._____\\|               {}".format(d_clw[7][clws]))
	print("     \\____||           ||                        {}".format(d_clw[8][clws]))
	print("{}  |▓▓▓▓▓▓▓▓▓\\     {}".format(d_rw[0][rws][0],d_rw[0][rws][1]))
	print("{} ||▓▓▓▓▓▓▓▓▓▓|\\   <[▓▓▓| {}".format(d_rw[1][rws][0],d_rw[1][rws][1]))
	print("{}  \\__________\\|   <[▓▓▓| {}".format(d_rw[2][rws][0],d_rw[2][rws][1]))
	print('')
	return

	# COLOR HIGHLIGHT TOOL
	# --- --- --- --- ---
	# def print_format_table():
	#     """
	#     prints table of formatted text format options
	#     """
	#     for style in range(8):
	#         for fg in range(30,38):
	#             s1 = ''
	#             for bg in range(40,48):
	#                 format = ';'.join([str(style), str(fg), str(bg)])
	#                 s1 += '\x1b[%sm %s \x1b[0m' % (format, format)
	#             print(s1)
	#         print('\n')
	# print_format_table()

	# WRAPPER FOR ROBOT DISLAY
	# --- --- --- --- ---
	# def DisplayRobot_WPR():
	# global lws
	# global rws
	# global clws
	# while (DisplayRobot == True):
	# 	CLEAR_CONSOLE(30)
	# 	ROBOT(lws,rws,clws)
	# 	sleep(0.3)
	# return

def blinker():
	global PERIPH
	global activate
	global end
	global stopack
	global gui_drawrobot
	if gui_drawrobot == False:
		return


	pos_left = PERIPH["wheels"].left_motor.position
	pos_right = PERIPH["wheels"].right_motor.position
	old_pos_left = pos_left
	old_pos_right = pos_right

	old_old_lw_status = 'n'
	old_lw_status = 'n'
	lw_status = 'n'
	old_old_rw_status = 'n'
	old_rw_status = 'n'
	rw_status = 'n'

	new_lw_status = 'n'
	old_new_lw_status = 'n'
	new_rw_status = 'n'
	old_new_rw_status = 'n'

	poller = 0
	poll = 100

	while end != True:
		if activate !=True:
			stopack = True
			continue
		stopack = False

		sleep = 0.5
		poller +=1
		if poller == poll:
			poller = 0
		else:
			continue

		old_pos_left = pos_left
		old_pos_right = pos_right
		pos_left=PERIPH["wheels"].left_motor.position
		pos_right=PERIPH["wheels"].right_motor.position


		old_old_lw_status = old_lw_status
		old_old_rw_status = old_rw_status
		old_lw_status = lw_status
		old_rw_status = rw_status

		if (old_pos_left < pos_left):
			lw_status = 'd'
		elif (old_pos_left > pos_left):
			lw_status = 'r'
		elif (old_pos_left == pos_left):
			lw_status = 'n'

		if (old_pos_right < pos_right):
			rw_status = 'd'
		elif (old_pos_right > pos_right):
			rw_status = 'r'
		elif (old_pos_right == pos_right):
			rw_status = 'n'

		clw_status = 'n'

		if (lw_status == old_lw_status):
			if (old_lw_status == old_old_lw_status):
				if (rw_status == old_rw_status):
					if( old_rw_status == old_old_rw_status):	
						CLEAR_CONSOLE(10)
						ROBOT(lw_status, rw_status, clw_status)
		

	# CLEAR_CONSOLE(10)
	# ROBOT('n','n','n')
	return
# ---  ---  ---  ---  ---  ---  ---



# ---  CODE START  ---

# loading_animation('# Importing {}'.format(__name__), 16)