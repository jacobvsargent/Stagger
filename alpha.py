from selenium import webdriver
from selenium.webdriver.support.ui import Select
from tkinter import *

import sys
import time
import csv

#create the root
gui = Tk()

#for my ego
gui.title("STAGGER V A0.0")
Label(gui, text="STAGGER: VERSION ALPHA 0.0").pack()
Label(gui, text="Created by: Jacob Sargent").pack()

#breathing room
Label(gui, text="--------------------------------------------------------------------").pack()

#create all the fields and their entry entities
n1 = Label(gui, text="Enter your name:")
n1.pack()
name = StringVar()
name_l = Entry(gui, textvariable = name)
name_l.pack()

n2 = Label(gui, text="Enter your university:")
n2.pack()
uni = StringVar()
uni_l = Entry(gui, textvariable = uni)
uni_l.pack()

#n3 = Label(gui, text="Enter your LinkedIn Email Address:")
#n3.pack()
#li_un = StringVar()
#li_un_l = Entry(gui, textvariable = li_un)
#li_un_l.pack()

#n4 = Label(gui, text="Enter your LinkedIn Password:")
#n4.pack()
#li_pw = StringVar()
#li_pw_l = Entry(gui, textvariable = li_pw)
#li_pw_l.pack()

#Label(gui, text="Enter your TFACT (OKTA) Email:").pack()
#okta_un = StringVar()
#okta_un_l = Entry(gui, textvariable = okta_un)
#okta_un_l.pack()

#Label(gui, text="Enter your TFACT (OKTA) Password:").pack()
#okta_pw = StringVar()
#okta_pw_l = Entry(gui, textvariable = okta_pw)
#okta_pw_l.pack()

#n5 = Label(gui, text="How many people would you like to source?")
#n5.pack()
#num_to_source = StringVar()
#num_to_source_l = Entry(gui, textvariable = num_to_source)
#num_to_source_l.pack()

n6 = Label(gui, text="From what graduating year would you like to source?")
n6.pack()
grad_year = StringVar()
grad_year_l = Entry(gui, textvariable = grad_year)
grad_year_l.pack()

#breathing room
Label(gui, text="").pack()

#this is the user input
relevant_input = []

#add chromedriver to environmental variables in sys
path = "C:\\Stagger\\chromedriver.exe"
sys.path.append(path)
driver = webdriver.Chrome(path)

#soak up the inputs in the entry fields, clear them, and store them into relevant_input
def collect_input():
	global relevant_input
	relevant_input = [name.get(), uni.get(), "jacobvsargent@gmail.com", "OceanMan420", "okta_un.get()", "okta_pw.get()", "num_to_source.get()", grad_year.get()]

	name_l.delete(0, END)
	uni_l.delete(0, END)
	#li_un_l.delete(0, END)
	#li_pw_l.delete(0, END)
	#okta_un_l.delete(0, END)
	#okta_pw_l.delete(0, END)
	#num_to_source_l.delete(0, END)
	grad_year_l.delete(0, END)

	test_label.configure(text = "User input successfully collected, " + relevant_input[0])
	print("Input has been collected!")
	
	n1.pack_forget()
	name_l.pack_forget()
	n2.pack_forget()
	grad_year_l.pack_forget()
	#n3.pack_forget()
	#num_to_source_l.pack_forget()
	#n4.pack_forget()
	#n5.pack_forget()
	#li_un_l.pack_forget()
	#li_pw_l.pack_forget()
	uni_l.pack_forget()
	n6.pack_forget()


"""
#fake definition
def collect_input():
	global relevant_input
	relevant_input = ["Jacob", "Clemson University", "jacobvsargent@gmail.com", "OceanMan420", "---", "---", "50", "2021"]
	test_label.configure(text = "Input process bypassed.")
"""

hitlist = [""]


def collect_urls():

	sign_in_link = "https://www.linkedin.com/login"

	#connect link to driver and scrape full html data from website
	driver.get(sign_in_link)

	time.sleep(2)


	#log in
	username = driver.find_element_by_id("username")
	username.clear()
	username.send_keys(relevant_input[2])
	password = driver.find_element_by_id("password")
	password.clear()
	password.send_keys(relevant_input[3])
	password.submit()

	time.sleep(2)

	print("Signed in to LinkedIn.")

	uni_url = "https://www.linkedin.com/school/" + relevant_input[1].lower().replace(" ", "-") + "/people/"
	
	driver.get(uni_url)

	print("Reaching University Page.")

	time.sleep(2)

	driver.find_element_by_id("people-search-year-start").send_keys(relevant_input[7])
	time.sleep(1)
	driver.find_element_by_id("people-search-year-end").send_keys(relevant_input[7])
	driver.find_element_by_id("people-search-year-start").send_keys("")
	time.sleep(1)

	current_count = 0

	print("Scrolling begun.")

	#auto-scroller
	scroller = 0
	for x in range(2):
		driver.execute_script("window.scrollTo(0," + str(scroller) + ")")
		time.sleep(0.1)
		scroller += 500

	print("Scrolling complete.")

	time.sleep(5)

	print("Scraping URL data.")

	raw_links = driver.find_elements_by_tag_name("a")

	global hitlist
	skip = False

	for link in raw_links:
		link_text = link.get_attribute("href")
		if (len(link_text) > 29):
			if (link_text[25:27] == "in" and skip == False):
				hitlist.append(link_text.strip())
				skip = True
			elif (link_text[25:27] == "in"):
				skip = False

	time.sleep(2)

	hitlist.remove("")

	time.sleep(2)

	for i in range(0, 6):
		hitlist.pop(0)

	test_label.configure(text = "Hitlist created of length " + str(len(hitlist)) + ".")
	print("Created hitlist of length: " + str(len(hitlist)))





"""
#fake definition
def collect_urls():
	global hitlist
	test_urls = ["https://www.linkedin.com/in/allison-mclane-81b3b3149/"]
	hitlist = test_urls

	sign_in_link = "https://www.linkedin.com/login"
	driver.get(sign_in_link)

	time.sleep(1)

	#log in
	username = driver.find_element_by_id("username")
	username.clear()
	username.send_keys("jacobvsargent@gmail.com")
	password = driver.find_element_by_id("password")
	password.clear()
	password.send_keys("OceanMan420")
	password.submit()

	test_label.configure(text="Url Collection Process Bypassed, Logged in to LinkedIn")
"""

def strip_info(arg1):
	dp = ["NIX", "NIX", "NIX", "NIX", "NIX", "NIX", "NIX"]

	driver.get(arg1)

	time.sleep(1)

	driver.refresh()

	scroller = 0
	for x in range(10):
		driver.execute_script("window.scrollTo(0," + str(scroller) + ")")
		time.sleep(0.2)
		scroller += 500
	driver.execute_script("window.scrollTo(0,0)")

	time.sleep(1)

	possible_uni = []
	possible_mse = []

	start_looking = False
	headings_a = driver.find_elements_by_tag_name("a")
	for x in headings_a:
		start_looking = True
		if (start_looking):
			if ("connection" in x.text or len(x.text) < 24 or "followers" in x.text or "comment" in x.text or "endorse" in x.text or "Endorse" in x.text):
				pass
			elif ("See more" in x.text or "See all" in x.text or "LinkedIn" in x.text or "Manage your account" in x.text):
				pass
			elif ("Governor's School" in x.text or "High School" in x.text):
				pass

			if (("University" in x.text or "College" in x.text or "School" in x.text)):
				possible_uni.append(x.text)
			elif ("Field Of Study" in x.text):
				possible_uni.append(x.text)

			if ("Intern" in x.text and "Company Name" in x.text):
				possible_mse.append(x.text)
				if ("International Baccalaureate" in x.text or "Degree Name" in x.text):
					possible_mse.remove(x.text)
			elif (("President" in x.text or "Chair" in x.text or "Editor" in x.text or "Founder" in x.text or "Research" in x.text) and "Company Name" in x.text):
				possible_mse.append(x.text)
			elif (("Director" in x.text or "Chief" in x.text or "Volunteer" in x.text or "Manager" in x.text) and "Company Name" in x.text):
				possible_mse.append(x.text)
			else:
				pass



	if (len(possible_uni) > 1):
		for pos in possible_uni:
			if (not "Field Of Study" in pos):
				possible_uni.remove(pos)
	if (len(possible_uni) > 1):
		for pos in possible_uni:
			if (not "Field Of Study" in pos):
				possible_uni.remove(pos)
	if (len(possible_uni) > 1):
		for pos in possible_uni:
			if (not relevant_input[1] in pos):
				possible_uni.remove(pos)
	if (len(possible_uni) > 1):
		for pos in possible_uni:
			if ("Company Name" in x.text):
				possible_uni.remove(pos)

	if (len(possible_uni) > 0 and "Field Of Study" in possible_uni[0]):
		major_index_start = possible_uni[0].index("Field Of Study") + 15
		m_i_temp1= len(possible_uni[0])
		m_i_temp2= len(possible_uni[0])

		if ("Dates" in possible_uni[0]):
			m_i_temp1 = possible_uni[0].index("Dates")
			#print("Date index found: " + str(m_i_temp1))
		if ("Grade" in possible_uni[0]):
			m_i_temp2 = possible_uni[0].index("Grade")
			#print("Grade index found: " + str(m_i_temp2))

		major_index_end = min(m_i_temp1, m_i_temp2) - 1

		major_text = possible_uni[0][major_index_start:major_index_end]
		#print("SHOULD BE MAJOR: \n" + major_text)
	else:
		major_text = "NIX"


	if (len(possible_mse) > 1):
		for pos in possible_mse:
			if (not "Company Name" in x.text):
				possible_mse.remove(pos)

	if (len(possible_mse) > 1):
		for pos in possible_mse:
			if ("Volunteer" in x.text and len(possible_mse) > 1):
				possible_mse.remove(pos)



	#for pos in possible_mse:
	#	print("SHOULD BE AN INTERNSHIP OR EXPERIENCE: " + pos)
	if (len(possible_mse) > 0):
		mse_comp_index = possible_mse[0].index("Company Name")
		mse_name_text = possible_mse[0][0:mse_comp_index-1]
		#print("SHOULD BE MSE NAME: " + mse_name_text)

		mse_date_index = possible_mse[0].index("Date")
		mse_comp_text = possible_mse[0][mse_comp_index+13:mse_date_index-1]
		#print("SHOULD BE MSE COMPANY: " + mse_comp_text)

		mse_start_text = possible_mse[0][mse_date_index+15:mse_date_index+23]
		#print("SHOULD BE MSE START DATE: " + mse_start_text)
		if ("Voluntee" in possible_mse[0]):
			mse_start_text = possible_mse[0][mse_date_index+18:mse_date_index+26]
	else:
		mse_comp_text = "NIX"
		mse_start_text = "NIX"
		mse_name_text = 'NIX'


	name_index = 0
	#adds full name
	headings_li = driver.find_elements_by_tag_name("li")
	if ("connection" in headings_li[16].text):
		name_index = 12
	else:
		name_index = 16
	print("Name added to file: " + headings_li[name_index].text)
	dp[0] = headings_li[name_index].text

	#adds url
	print("LinkedIn URL added to file: " +  arg1)
	dp[1] = arg1

	#adds uni
	print("University added to file: " + relevant_input[1])
	dp[2] = relevant_input[1]

	#adds major
	print("Major added to file: " + major_text)
	dp[3] = major_text

	#adds mse name
	print("MSE Name added to file: " + mse_name_text)
	dp[4] = mse_name_text

	#adds mse start date
	print("MSE Start Date added to file: " + mse_start_text)
	dp[5] = mse_start_text

	#adds mse company
	print("MSE Company added to file: " + mse_comp_text)
	dp[6] = mse_comp_text

	return dp


"""
#fake definition
def strip_info(arg1):
	dp = ["Jacob Sargent", "www.linkedin.com", "Clemson University", "Marketing", "Tech Intern", "May 2016", "Samsung Co."]
	test_label.configure(text = "Info stripping bypassed.")
	return dp
"""

def clean_info(arg1):
	cleandp = []

	for x in arg1:
		cleandp.append(x)

	first_space_name = arg1[0].index(" ")
	first_name = arg1[0][0:first_space_name]
	last_name = arg1[0][first_space_name+1:]
	second_space = 0

	if(" " in last_name):
		second_space = last_name.index(" ")
		last_name = last_name[second_space+1:]


	cleandp.pop(0)
	cleandp.insert(0, last_name)
	cleandp.insert(0, first_name)

	print("Should be full, combined name: " + first_name + " + " + last_name + ". Getting email...")

	driver.get("https://my.clemson.edu/#/directory")

	time.sleep(2)

	searcher = driver.find_element_by_id("dojox_mobile_TextBox_0")
	searcher.clear()
	searcher.send_keys(first_name + " " + last_name)

	time.sleep(2)

	test_p_list = driver.find_elements_by_tag_name("p")

	if (len(test_p_list) > 0):
		test_p = test_p_list[0].text
		if ("(" in test_p):
			par = [test_p.index("(")+1, test_p.index(")")]
			temp_email = test_p[par[0]:par[1]] + "@clemson.edu"
			print("Email found: " + temp_email)
		else:
			temp_email = "NIX"
			print("Email not found.")
	else:
		temp_email = "NIX"
		print("Email not found.")


	cleandp.append(temp_email)

	return cleandp


li_info = []
cleaned_info = []

def scrape_li():
	hitcount = 0
	total_counted = 0
	nix_check = False
	for hit in hitlist:
		nix_check = False
		print("Successful Profiles: " + str(hitcount) + " / Total Profiles: " + str(total_counted) + ". This URL = " + hit)
		hit_info = strip_info(hit)
		for h in hit_info:
			if (h=="NIX"):
				nix_check = True
		if (nix_check == False):
			li_info.append(hit_info)
			hitcount+=1
			total_counted += 1
			print("Profile entered successfully. \n")
		else:
			print("Profile has been nixxed. \n")
			total_counted += 1

	print("Length of dirty info: " + str(len(li_info)))

	test_label.configure(text = "Scraping complete.")

def fix_up():
	for packet in li_info:
		cleaned_info.append(clean_info(packet))

	test_label.configure(text = "Cleaning complete.")

def dupe_killer():
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
	time.sleep(3)

	#cleaned_info.append(["Allison", "McLane", "x", "x", "x", "x", "x", "x", "akmclan@clemson.edu"])
	#cleaned_info.append(["Jacob", "Sargent", "x", "x", "x", "x", "x", "x", "sargen4@clemson.edu"])
	#cleaned_info.append(["Top", "Lee", "x", "x", "x", "x", "x", "x", "tflee@clemson.edu"])

	print("Checking for duplicates...")

	for person in cleaned_info:
		if (person[6] == "NIX" or len(person[8]) < 7):
			pass
		else:
			email_a = person[8]
			email_b = person[8][0:person[8].index("@")] + '@g.clemson.edu'
			print("Checking duplicates for: " + email_a)

			input_box = driver.find_element_by_id("phSearchInput")

			input_box.send_keys(email_a)
			input_box.submit()
			time.sleep(.5)

			td_list = driver.find_elements_by_tag_name("td")

			act_amt = 0
			act_in_1 = 0
			do_i_exit = False
			#check for accounts
			for td in td_list:
				if "Accounts" in td.text:
					act_in_1 = td.text.index("(")
					act_amt = int(td.text[act_in_1+1:act_in_1+2])
					print("Amount of accounts found in TFACT: " + str(act_amt))
					do_i_exit = True

				if (do_i_exit):
					break

			check_b = False

			if (act_amt > 0):
				person[0] = "NIX"
				print("DUPLICATE FOUND, NIXXED")
			else:
				check_b = True

			time.sleep(.2)

			if (check_b):
				input_box = driver.find_element_by_id("phSearchInput")

				input_box.send_keys(email_b)
				input_box.submit()
				time.sleep(.5)

				td_list = driver.find_elements_by_tag_name("td")


				act_amt = 0
				act_in_1 = 0
				do_i_exit = False
				#check for accounts
				for td in td_list:
					if "Accounts" in td.text:
						act_in_1 = td.text.index("(")
						act_amt = int(td.text[act_in_1+1:act_in_1+2])
						print("Should be amount of accounts: " + str(act_amt))
						do_i_exit = True

					if (do_i_exit):
						break

				if (act_amt > 0):
					person[0] = "NIX"
					print("DUPLICATE FOUND, NIXXED")
	time.sleep(1)
	print("Duplicate process complete.")
	test_label.configure(text = "Duplicates found and nixxed.")

good_profiles = 0

def write_to_csv():
	global good_profiles

	print("Attempting to write CSV File.")

	good_profiles = 0
	path_name = ""
	path_name += relevant_input[1] + "_" + relevant_input[7] + ".csv"
	path_name = path_name.replace(" ", "_")
	path_name = path_name.lower()

	with open(path_name, 'w+', newline = "") as csvFile:
		writer = csv.writer(csvFile)
		writer.writerow(['First Name', 'Last Name', 'LinkedIn URL', 'University', 'Major', 'MSE Title', 'MSE Start', 'MSE Company', 'Email'])
		for entry in cleaned_info:
			exit_me = False
			for i in entry:
				if (i == "NIX" or i == "connections"):
					exit_me = True
			if (not exit_me):
				writer.writerow(entry)
				good_profiles += 1
	print("CSV File Successfully Created.")
	test_label.configure(text = "CSV File Created.")


def swoop():
	global good_profiles
	
	time_begin = time.asctime(time.localtime())
	ticks_begin = time.time()
	print("PROCESS BEGUN AT: " + time_begin)

	collect_input()
	time.sleep(1)
	collect_urls()
	time.sleep(1)
	scrape_li()
	time.sleep(1)
	fix_up()
	time.sleep(1)
	dupe_killer()
	time.sleep(1)
	write_to_csv()

	time_end = time.asctime(time.localtime())
	ticks_end = time.time()
	time_elapsed = str(int((ticks_end - ticks_begin) / 60))

	print("")
	print("")

	print("PROCESS COMPLETE.")
	print("PROCESS BEGUN AT: " + time_begin)
	print("PROCESS ENDED AT: " + time_end)
	print("MINUTES ELAPSED: " + time_elapsed + "\n")

	print("PROFILES SCRAPED: " + str(len(hitlist)))
	print("COMPLETE PROFILES BUILT: " + str(good_profiles))

	print("Thank you for using Stagger!")

	driver.close()



 
#inputs_button = Button(gui, text="Collect Inputs", command=collect_input)
#inputs_button.pack()

#urls_button = Button(gui, text="Collect Hitlist", command=collect_urls)
#urls_button.pack()

#li_button = Button(gui, text="Scrape from LinkedIn", command=scrape_li)
#li_button.pack()

#fix_button = Button(gui, text="Clean and Do Emails", command=fix_up)
#fix_button.pack()

#dupe_button = Button(gui, text="Kill Dupes", command=dupe_killer)
#dupe_button.pack()

#csv_button = Button(gui, text="Write CSV", command=write_to_csv)
#csv_button.pack()

big_button = Button(gui, text="SWOOP.", command=swoop)
big_button.pack()


test_label = Label(gui, text="Push Button After Entering Inputs!")
test_label.pack()


print("Process begun.")

gui.mainloop()










"""

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





