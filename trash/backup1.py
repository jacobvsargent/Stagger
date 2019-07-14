from selenium import webdriver
from selenium.webdriver.support.ui import Select
from tkinter import *

import sys
import time

#create the root
gui = Tk()

#for my ego
gui.title("STAGGER V A1.0")
Label(gui, text="STAGGER: VERSION ALPHA 0.0").pack()
Label(gui, text="Created by: Jacob Sargent").pack()

#breathing room
Label(gui, text="").pack()
Label(gui, text="").pack()
Label(gui, text="").pack()

#create all the fields and their entry entities
Label(gui, text="Enter your name:").pack()
name = StringVar()
name_l = Entry(gui, textvariable = name)
name_l.pack()

Label(gui, text="Enter your university:").pack()
uni = StringVar()
uni_l = Entry(gui, textvariable = uni)
uni_l.pack()

Label(gui, text="Enter your LinkedIn Email Address:").pack()
li_un = StringVar()
li_un_l = Entry(gui, textvariable = li_un)
li_un_l.pack()

Label(gui, text="Enter your LinkedIn Password:").pack()
li_pw = StringVar()
li_pw_l = Entry(gui, textvariable = li_pw)
li_pw_l.pack()

Label(gui, text="Enter your TFACT (OKTA) Email:").pack()
okta_un = StringVar()
okta_un_l = Entry(gui, textvariable = okta_un)
okta_un_l.pack()

Label(gui, text="Enter your TFACT (OKTA) Password:").pack()
okta_pw = StringVar()
okta_pw_l = Entry(gui, textvariable = okta_pw)
okta_pw_l.pack()

Label(gui, text="How many people would you like to source?").pack()
num_to_source = StringVar()
num_to_source_l = Entry(gui, textvariable = num_to_source)
num_to_source_l.pack()

Label(gui, text="From what graduating year would you like to source?").pack()
grad_year = StringVar()
grad_year_l = Entry(gui, textvariable = grad_year)
grad_year_l.pack()

#breathing room
Label(gui, text="").pack()

relevant_input = []

def begin():
	test_label.configure(text = "Collecting user input...")

	global relevant_input
	relevant_input = [name.get(), uni.get(), li_un.get(), li_pw.get(), okta_un.get(), okta_pw.get(), num_to_source.get(), grad_year.get()]

def test():
	test_label.configure(text = relevant_input[0])

run_button = Button(gui, text="Run Program", command=begin)
run_button.pack()

test_button = Button(gui, text="Test!", command=test)
test_button.pack()

test_label = Label(gui, text="Waiting for input...")
test_label.pack()

print("Loop begun.")

gui.mainloop()













#time_begin = time.asctime(time.gmtime())



"""
	number_to_source = #user input

	url_list = collect_urls()

	info_dict = []
	updated_dict = []
	csv_link = ""

	for each_url in url_list:
		info_dict = collect_info(each_url)
		updated_dict = update_info()
		csv_link = export_to_csv(updated_dict)

	do_next_item = True
	profile_counter = 0


	while (do_next_item and profile_counter < number_to_source):
		do_next_item = False
		enter_profile(profile_counter)
		profile_counter++

	write_diagnostics_file()
"""





