# Assignment - 2
# Name - PARMESH YADAV
# Roll No - 2020319

import json


'''
- This is the skeleton code, wherein you have to write the logic for each of the
functions defined below.

- DO NOT modify/delete the given functions. 

- DO NOT import any python libraries, except for the ones already included.

- DO NOT create any global variables in this module.

- DO NOT add print statements anywhere in this module.

- Make sure to return value as specified in the function description.

- Remove the pass statement from the functions when you implement them.
'''


def read_data_from_file(file_path="D:\college\sem 1\ip\Assignment_2\IP_Assignment_2\Final Code\data.json"):
	'''
	**** DO NOT modify this function ****
	Description: Reads the data.json file, and converts it into a dictionary.

	Parameters: 
	- file_path (STRING): The path to the file (with .json extension) which contains the initial database. You can pass the file_path parameter as "data.json".

	Returns:
	- A dictionary containing the data read from the file
	'''
	
	with open(file_path, 'r') as data:
		records = json.load(data)

	return records


def filter_by_first_name(records, first_name):
	'''
	Description: Searches the records to find all persons with the given first name (case-insensitive)

	Parameters:
	- records (LIST): A list of person records (each of which is a dictionary)
	- first_name (STRING): The first name

	Returns:
	- A list of INTEGERS denoting the IDs of the persons with the given first name
		Case 1: No person found => Returns an empty list
		Case 2: At least one person found => Returns a list containing the IDs of all the persons found
	'''
	first_name = first_name.lower()
	first_name = first_name.capitalize()
	f_n = list()
	for i in range(len(records)):
		if records[i]['first_name'] == first_name:
			f_n.append(records[i]['id'])
	return f_n


def filter_by_last_name(records, last_name):
	'''
	Description: Searches the records to find all persons with the given last name (case-insensitive)

	Parameters:
	- records (LIST): A list of person records (each of which is a dictionary)
	- last_name (STRING): The last name

	Returns:
	- A list of INTEGERS denoting the IDs of the persons with the given last name
		Case 1: No person found => Returns an empty list
		Case 2: At least one person found => Returns a list containing the IDs of all the persons found
	'''
	last_name = last_name.lower()
	last_name = last_name.capitalize()
	l_n = list()
	for i in range(len(records)):
		if records[i]['last_name'] == last_name:
			l_n.append(records[i]['id'])
	return l_n


def filter_by_full_name(records, full_name):
	'''
	Description: Searches the records to find all persons with the given full name (case-insensitive)

	Parameters:
	- records (LIST): A list of person records (each of which is a dictionary)
	- full_name (STRING): The full name (a single string with 2 space-separated words, the first name and the last name respectively)

	Returns:
	- A list of INTEGERS denoting the IDs of the persons with the given full name
		Case 1: No person found => Returns an empty list
		Case 2: At least one person found => Returns a list containing the IDs of all the persons found
	'''
	l = full_name.split(' ')
	f_n = l[0]
	l_n = l[1]
	f_n = f_n.lower()
	f_n = f_n.capitalize()
	l_n = l_n.lower()
	l_n = l_n.capitalize()
	fu_n = list()
	for i in range(len(records)):
		if records[i]['last_name'] == l_n:
			if records[i]['first_name'] == f_n:
				fu_n.append(records[i]['id'])
	return fu_n	


def filter_by_age_range(records, min_age, max_age):
	'''
	Description: Searches the records to find all persons whose age lies in the given age range [min_age, max_age]

	Parameters:
	- records (LIST): A list of person records (each of which is a dictionary)
	- min_age (INTEGER): The minimum age (inclusive)
	- max_age (INTEGER): The maximum age (inclusive)

	Note: 0 < min_age <= max_age

	Returns:
	- A list of INTEGERS denoting the IDs of the persons with the given full name
		Case 1: No person found => Returns an empty list
		Case 2: At least one person found => Returns a list containing the IDs of all the persons found
	'''
	a_r = list()
	for i in range(len(records)):
		if min_age >= 0 and min_age <= max_age:
			if records[i]['age'] >= min_age and records[i]['age'] <= max_age:
				a_r.append(records[i]['id'])
	return a_r

def count_by_gender(records):
	'''
	Description: Counts the number of males and females

	Parameters:
	- records (LIST): A list of person records (each of which is a dictionary)

	Returns:
	- A dictionary with the following two key-value pairs:
		KEY        VALUE
		"male"     No of males (INTEGER)
		"female"   No of females (INTEGER)
	'''
	c_m = 0
	c_f = 0
	for i in range(len(records)):
		if records[i]['gender'] == 'male':
			c_m += 1
		elif records[i]['gender'] == 'female':
			c_f += 1
	d = {'male':c_m,'female':c_f}
	return d



def filter_by_address(records, address):
	'''
	Description: Filters the person records whose address matches the given address. 

	Parameters:
	- records (LIST): A list of person records (each of which is a dictionary)
	- address (DICTIONARY): The keys are a subset of { "house_no", "block", "town", "city", "state", "pincode" } (case-insensitive)
		Some examples are:
			Case 1: {} 
				=> All records match this case
			
			Case 2: { "block": "AD", "city": "Delhi" } 
				=> All records where the block is "AD" and the city is "Delhi" (the remaining address fields can be anything)
			
			Case 3: { "house_no": 24, "block": "ABC", "town": "Vaishali", "city": "Ghaziabad", "state": "Uttar Pradesh", "pincode": 110020 }

	Returns:
	- A LIST of DICTIONARIES with the following two key-value pairs:
		KEY            VALUE
		"first_name"   first name (STRING)
		"last_name"    last name (STRING)
	'''
	l = list()
	if address == {}:
		for i in records:
			d = dict()
			f_n = i['first_name']
			l_n = i['last_name']
			d['first_name'] = f_n
			d['last_name'] = l_n
			l.append(d)
		return l
	else:
		for i in address:
			if i == 'block' or i == 'town' or i == 'city' or i == 'state':
				if ' ' not in address[i]:
					address[i] = address[i].lower()
					address[i] = address[i].capitalize()
				else:
					y = ''
					z = address[i].split(' ')
					for x in z:
						x = x.lower()
						x = x.capitalize()
					for x in z:
						y = y + x + ' '
					y = y.rstrip()
					address[i] = y
					
		s = set()
		for i in records:
			for j in address:
				if address[j] == i['address'][j]:
					s.add(i['id'])
				else:
					if len(s) != 0 and i['id'] in s:
						s.remove(i['id'])
					break
		s = list(s)
		s = sorted(s)
		
		for i in s:
			d = dict()
			for j in records:
				if i == j['id']:
					f_n = j['first_name']
					l_n = j['last_name']
					d['first_name'] = f_n
					d['last_name'] = l_n
					l.append(d)
					break
		return l
				





def find_alumni(records, institute_name):
	'''
	Description: Find all the alumni of the given institute name (case-insensitive). 
	
	Note: A person is an alumnus of an institute only if the value of the "ongoing" field for that particular institute is False.

	Parameters:
	- records (LIST): A list of person records (each of which is a dictionary)
	- institute_name (STRING): Name of the institute (case-insensitive)

	Returns:
	- A LIST of DICTIONARIES with the following three key-value pairs:
		KEY            VALUE
		"first_name"   first name (STRING)
		"last_name"    last name (STRING)
		"percentage"   percentage (FLOAT)
	'''
	institute_name = institute_name.upper()
	al = list()
	for i in range(len(records)):
		for j in range(len(records[i]['education'])):
			if institute_name == records[i]['education'][j]['institute']:
				if records[i]['education'][j]['ongoing'] == False:
					d = {'first_name':records[i]['first_name'],'last_name':records[i]['last_name'],'percentage':records[i]['education'][j]['percentage']}
					al.append(d)
	return al


def find_topper_of_each_institute(records):
	'''
	Description: Find topper of each institute

	Parameters:
	- records (LIST): A list of person records (each of which is a dictionary)

	Returns:
	- A DICTIONARY with the institute name (STRING) as the keys and the ID (INTEGER) of the topper of that institute.

	Note: If there are `N` distinct institutes in records, the dictionary will contain `N` key-value pairs. The ongoing status does NOT matter. It is guaranteed that each institute will have exactly one topper.
	'''
	toe_ = dict()
	for i in range(len(records)):
		for j in range(len(records[i]['education'])):
			toe_[records[i]['education'][j]['institute']] = 0
	
	toe = toe_
	for k in toe_:
		maxper = 0.0
		for i in records:
			for j in i['education']:
				if k == j['institute']:
					if j['ongoing'] == False:
						if j['percentage'] >= maxper:
							maxper = j['percentage']
							toe[k] = i['id']
	return toe





def find_blood_donors(records, receiver_person_id):
	'''
	Description: Find all donors who can donate blood to the person with the given receiver ID.

		Note: 
		- Possible blood groups are "A", "B", "AB" and "O".

		Rules:
		BLOOD GROUP      CAN DONATE TO
		A                A, AB
		B                B, AB
		AB               AB
		O                A, B, AB, O

	Parameters:
	- records (LIST): A list of person records (each of which is a dictionary)
	- receiver_person_id (INTEGER): The ID of the donee
		Note: It is guaranteed that exactly one person in records will have the ID as receiver_person_id

	Returns:
	- A DICTIONARY with keys as the IDs of potential donors and values as a list of strings, denoting the contact numbers of the donor
	'''
	bd = dict()
	for i in records:
		if i['id'] == receiver_person_id:
			rbg = i['blood_group'] 
	
	for i in range(len(records)):
		if records[i]['id'] != receiver_person_id:
			if rbg == 'A':
				if records[i]['blood_group'] == 'A' or records[i]['blood_group'] == 'O':
					bd[records[i]['id']] = records[i]['contacts']
			elif rbg == 'B':
				if records[i]['blood_group'] == 'B' or records[i]['blood_group'] == 'O':
					bd[records[i]['id']] = records[i]['contacts']
			elif rbg == 'AB':
				if records[i]['blood_group'] == 'A' or records[i]['blood_group'] == 'O' or records[i]['blood_group'] == 'B' or records[i]['blood_group'] == 'AB':
					bd[records[i]['id']] = records[i]['contacts']
			elif rbg == 'O':
				if records[i]['blood_group'] == 'O':
					bd[records[i]['id']] = records[i]['contacts']
	return bd

			



def get_common_friends(records, list_of_ids):
	'''
	Description: Find the common friends of all the people with the given IDs

	Parameters:
	- records (LIST): A list of person records (each of which is a dictionary)
	- list_of_ids (LIST): A list of IDs (INTEGER) of all the people whose common friends are to be found

	Returns:
	- A LIST of INTEGERS containing the IDs of all the common friends of the specified list of people
	'''
	cf_ = list()
	for i in list_of_ids:
		cf_.append(records[i]['friend_ids'])
	
	for i in range(len(cf_)):
		cf_[i] = set(cf_[i])
	r = cf_[0]	
	for i in range(1,len(cf_)):
		r.intersection_update(cf_[i])
	r = list(r)
	return r






def is_related(records, person_id_1, person_id_2):
	'''
	**** BONUS QUESTION ****
	Description: Check if 2 persons are friends

	Parameters:
	- records (LIST): A list of person records (each of which is a dictionary)
	- person_id_1 (INTEGER): first person ID
	- person_id_2 (INTEGER): second person ID

	Returns:
	- A BOOLEAN denoting if the persons are friends of each other, directly or indirectly (if A knows B, B knows C and C knows D, then A knows B, C and D).
	'''
	for i in range(len(records[person_id_1]['friend_ids'])):
		if records[person_id_1]['friend_ids'][i] == person_id_2:
			return True
			break
	else:
		for i in range(len(records[person_id_1]['friend_ids'])):
			for j in range(len(records[records[person_id_1]['friend_ids'][i]]['friend_ids'])):
				if records[records[person_id_1]['friend_ids'][i]]['friend_ids'][j] == person_id_2:
					return True
					break
		else:
			return False
				
				


def delete_by_id(records, person_id):
	'''
	Description: Given a person ID, this function deletes them from the records. Note that the given person can also be a friend of any other person(s), so also delete the given person ID from other persons friend list. If the person ID is not available in the records, you can ignore that case.

	Parameters:
	- records (LIST): A list of person records (each of which is a dictionary)
	- person_id (INTEGER): The person id
	
	Returns:
	- A LIST of Dictionaries representing all the records (the updated version).
	In case there were no updates, return the original records.
	'''

	for i in records:
		if i['id'] == person_id:
			records.remove(i)
			
	else:
		for i in records:
			if person_id in i['friend_ids']:
				i['friend_ids'].remove(person_id)
	return records


def add_friend(records, person_id, friend_id):
	'''
	Description: Given a person ID and a friend ID, this function makes them friends of each other. If any of the IDs are not available, you can ignore that case.

	Parameters:
	- records (LIST): A list of person records (each of which is a dictionary)
	- person_id (INTEGER): The person id
	- friend_id (INTEGER): The friend id
	
	Returns:
	- A LIST of Dictionaries representing all the records (the updated version).
	In case there were no updates, return the original records.
	'''
	l = list()
	for i in records:
		l.append(i['id'])
	
	if person_id in l and friend_id in l:
		for i in records:	
			if i['id'] == person_id:
				if friend_id not in i['friend_ids']:
					i['friend_ids'].append(friend_id)
			elif i['id'] == friend_id:
				if person_id not in i['friend_ids']:
					i['friend_ids'].append(person_id)
	return records


def remove_friend(records, person_id, friend_id):
	'''
	Description: Given a person ID and a friend ID, this function removes them as friends of each other. If any of the IDs are not available, you can ignore that case.

	Parameters:
	- records (LIST): A list of person records (each of which is a dictionary)
	- person_id (INTEGER): The person id
	- friend_id (INTEGER): The friend id
	
	Returns:
	- A LIST of Dictionaries representing all the records (the updated version).
	In case there were no updates, return the original records.
	'''
	l = list()
	for i in records:
		l.append(i['id'])
	
	if person_id in l and friend_id in l:
		for i in records:
			if i['id'] == person_id:
				if friend_id in i['friend_ids']:
					i['friend_ids'].remove(friend_id)
			elif i['id'] == friend_id:
				if person_id in i['friend_ids']:
					i['friend_ids'].remove(person_id)
	return records
			


def add_education(records, person_id, institute_name, ongoing, percentage):
	'''
	Description: Adds an education record for the person with the given person ID. The education record constitutes of insitute name, the person's percentage and if that education is currently ongoing or not. Please look at the format of an education field from the PDF. If the person ID is not available in the records, you can ignore that case.

	Parameters:
	- records (LIST): A list of person records (each of which is a dictionary)
	- person_id (INTEGER): The person id
	- institute_name (STRING): The institute name (case-insensitive)
	- ongoing (BOOLEAN): The ongoing value representing if the education is currently ongoing or not
	- percentage (FLOAT): The person's score in percentage

	Returns:
	- A LIST of Dictionaries representing all the records (the updated version).
	In case there were no updates, return the original records.
	'''
	institute_name = institute_name.upper()
	l = list()
	for i in records:
		l.append(i['id'])
	
	if person_id in l:
		for i in records:
			if i['id'] == person_id:
				d = dict()
				if ongoing == False:
					d['institute'] = institute_name
					d['ongoing'] = ongoing
					d['percentage'] = percentage
					i['education'].append(d)
				else:
					d['institute'] = institute_name
					d['ongoing'] = ongoing
					i['education'].append(d)
	return records
					





records = read_data_from_file()
#print(records)
#print(len(records))
#print(filter_by_first_name(records,'Isabella'))
#print(filter_by_last_name(records,'Ramirez'))
#print(filter_by_full_name(records,'Isabella Ramirez'))
#print(filter_by_age_range(records,15,18))
#print(count_by_gender(records))
#print(find_alumni(records,'TKRYTU'))
#print(find_topper_of_each_institute(records))
#print(find_blood_donors(records,1))
#print(get_common_friends(records,[0,1,2]))
#print(is_related(records,0,198))
#print(delete_by_id(records,33))
#print(add_friend(records,0,1))
#print(remove_friend(records,0,33))
#print(add_education(records,0,'ABCDEF',True))
#print(filter_by_address(records,{'house_no': 513,'block': 'E','town': 'Gokal Pur','city': 'Siri','state': 'Delhi','pincode': 110011}))
