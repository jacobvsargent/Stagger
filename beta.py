from selenium import webdriver
from selenium.webdriver.support.ui import Select
from tkinter import *

import sys
import time
import csv

#create the root
gui = Tk()

#for my ego
gui.title("STAGGER V B0.0")
Label(gui, text="STAGGER: VERSION BETA 0.0").pack()
Label(gui, text="Created by: Jacob Sargent").pack()

#breathing room
Label(gui, text="----------------------------------------------------------------------").pack()

#breathing room
Label(gui, text="").pack()

test_label = Label(gui, text="Waiting for input...")
test_label.pack()

#this is the user input
relevant_input = []

#big boy
all_profiles = []

#linecounter
linecount = 1

#add chromedriver to environmental variables in sys
path = "C:\\Drivers\\chromedriver.exe"
sys.path.append(path)

def open_tfact():
	global driver
	global test_label
	global read_data
	global all_profiles

	time.sleep(2)

	driver = webdriver.Chrome('C:\\Drivers\\chromedriver.exe')
	sign_in_link = "https://teachforamerica.okta.com/login/login.htm?fromURI=%2Fapp%2FUserHome"
	driver.get(sign_in_link)

	#log in, bypass security question
	username = driver.find_element_by_id("okta-signin-username")
	username.clear()
	username.send_keys("jacobvsargent@gmail.com")
	password = driver.find_element_by_id("okta-signin-password")
	password.clear()
	password.send_keys("cilOW805!@")
	password.submit()
	time.sleep(1.5)
	verify = driver.find_element_by_id("input64")
	verify.clear()
	verify.send_keys("oregon trail")
	verify.submit()
	time.sleep(1)

	#pop over to TFACT
	salesforce = "https://tfact.my.salesforce.com/home/home.jsp"
	driver.get(salesforce)

	time.sleep(1)

	bot_text = ""

	keep_going = True

	with open('clemson_university_2021.csv', 'r') as csvFile:
		read_data = csv.reader(csvFile)
		for x in read_data:
			if (not x[0]=="First Name" and len(x[0])>0):
				all_profiles.append(x)
				print("TESTER: " + x[0])

	test_label.configure(text = "TFACT Opened.")

	tfact_button.pack_forget()


def source_next():
	global linecount
	global keep_going
	global test_label
	global read_data
	global all_profiles
	global driver

	#pop over to RT quick add
	quick_add = "https://tfact--c.na88.visual.force.com/apex/RTPipelinePage?sfdc.tabName=01rF0000000FHDW"
	driver.get(quick_add)
	grad_date = "05/01/2021"

	print("LENGTH OF all_profiles: " + str(len(all_profiles)))


	while (linecount-1 <= len(all_profiles) and keep_going == True):
		person = all_profiles[linecount-1]
		print("Attempting line read: " + str(linecount))
		print(str(linecount) + ": First: " + person[0])

		bot_text = "This entry was created on " + time.ctime() + " by Stagger."

		time.sleep(.2)

		cm_s = Select(driver.find_element_by_id("j_id0:form:block:j_id29:j_id30:label"))
		cm_s.select_by_visible_text('CM Prospect')

		name_s = driver.find_element_by_id("j_id0:form:block:j_id29:j_id36")
		name_s.send_keys(person[0])

		lname_s = driver.find_element_by_id("j_id0:form:block:j_id29:j_id37")
		lname_s.send_keys(person[1])

		rca_s = driver.find_element_by_id("j_id0:form:block:j_id29:j_id38")
		rca_s.send_keys(person[3])

		email_s = driver.find_element_by_id("j_id0:form:block:j_id29:j_id39")
		email_s.send_keys(person[8])

		gender_s = Select(driver.find_element_by_id("j_id0:form:block:j_id29:j_id40"))
		gender_s.select_by_visible_text("Other/Does Not Identify")

		ethnicity_s = Select(driver.find_element_by_id("j_id0:form:block:j_id29:j_id42"))
		ethnicity_s.select_by_visible_text("BG-Unknown")

		linkedin_s = driver.find_element_by_id("j_id0:form:block:j_id29:j_id47")
		linkedin_s.send_keys(person[2])

		signature = driver.find_element_by_id("j_id0:form:block:j_id29:j_id46")
		signature.send_keys(bot_text)

		uni_s = driver.find_element_by_id("j_id0:form:block:edusection:inst")
		uni_s.send_keys(person[3])

		grad_date_s = driver.find_element_by_id("j_id0:form:block:edusection:j_id66:1:j_id67")
		grad_date_s.send_keys(grad_date)

		major_s = Select(driver.find_element_by_id("j_id0:form:block:edusection:j_id66:5:j_id67"))
		try:
			major_s.select_by_visible_text(person[4])
			test_label.configure(text = person[0] + "'s profile has been entered.")

		except:
			print("Major not found.")
			test_label.configure(text = person[0] + "'s profile has been entered. \n No major found for " + person[4] + ".")

		act_s = driver.find_element_by_id("j_id0:form:block:j_id70:emp")
		act_s.send_keys("Other/Misc. Organization")

		mse_start_s = driver.find_element_by_id("j_id0:form:block:j_id70:j_id74:0:j_id75")
		mse_start_s.send_keys(person[6])

		mse_title_s = driver.find_element_by_id("j_id0:form:block:j_id70:j_id74:2:j_id75")
		mse_title_s.send_keys(person[5])

		mse_company_s = driver.find_element_by_id("j_id0:form:block:j_id70:j_id74:3:j_id75")
		mse_company_s.send_keys(person[7])

		mse_role_sig_s = Select(driver.find_element_by_id("j_id0:form:block:j_id70:j_id74:5:j_id75"))
		mse_role_sig_s.select_by_visible_text("Moderate Significance")

		keep_going = False

		linecount += 1

			
def next_person():
	global keep_going
	keep_going = True
	try:
		source_next()
	except:
		test_label.configure(text = "No profiles remaining!")


tfact_button = Button(gui, text="Open TFACT", command=open_tfact)
tfact_button.pack()

continue_button = Button(gui, text="Next Person", command=next_person)
continue_button.pack()



gui.mainloop()