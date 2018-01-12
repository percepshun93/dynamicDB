#First thing to do is read the csv files and store them in separate data structures so that they can be put into the database
#without issue

import csv
import pymysql

database = pymysql.connect('localhost','root','root','db_proj')

crs = database.cursor()

#crs.execute('show databases;')

'''Create the tables for: 1. Survey details, 2. Field IDs 3. Field Information 4. Customer info like customer ids, emails, questions recieved, answers given
									4. Emails and their IDS'''

crs.execute('DROP TABLE IF EXISTS  survey_details')
crs.execute('DROP TABLE IF EXISTS  respondent_details')
crs.execute('DROP TABLE IF EXISTS  field_values')
crs.execute('DROP TABLE IF EXISTS  field_iden')

query_string_field_iden = '''CREATE TABLE field_iden( ID INT UNSIGNED AUTO_INCREMENT,
																	Field_1 VARCHAR(50) NOT NULL,
																	Field_2 VARCHAR(50) NOT NULL,
																	Field_3 VARCHAR(50) NOT NULL,
																	Field_4 VARCHAR(50) NOT NULL,
																	Field_5 VARCHAR(50) NOT NULL,
																	Field_6 VARCHAR(50) NOT NULL,
																	Field_7 VARCHAR(50) NOT NULL,
																	Field_8 VARCHAR(50) NOT NULL,
																	Field_9 VARCHAR(50) NOT NULL,
																	Field_10 VARCHAR(50) NOT NULL,
																	Field_11 VARCHAR(50) NOT NULL,
																	Field_12 VARCHAR(50) NOT NULL,
																	PRIMARY KEY(ID)
																	);'''

#print (query_string_field_iden)
crs.execute(query_string_field_iden)

query_string_survey_details = '''CREATE TABLE survey_details (SURVEY_ID INT UNSIGNED AUTO_INCREMENT,
																	COMPANY_ID INT UNSIGNED NOT NULL,
																	COMPANY_NAME VARCHAR(50) NOT NULL,
																	DATE_CREATED DATETIME NOT NULL,
																	FIELD_IDEN_ID INT UNSIGNED AUTO_INCREMENT,
																	FOREIGN KEY(FIELD_IDEN_ID) REFERENCES field_iden(ID),
																	PRIMARY KEY(SURVEY_ID)
																	);'''

#print (query_string_survey_details)
crs.execute(query_string_survey_details)

query_string_field_values = '''CREATE TABLE field_values ( ID INT UNSIGNED AUTO_INCREMENT,
																		VALUE_ID INT UNSIGNED NOT NULL,
																		VALUE_1 VARCHAR(50) NOT NULL,
																		VALUE_2 VARCHAR(50) NOT NULL,
																		VALUE_3 VARCHAR(50) NOT NULL,
																		VALUE_4 VARCHAR(50) NOT NULL,
																		VALUE_5 VARCHAR(50) NOT NULL,
																		VALUE_6 VARCHAR(50) NOT NULL,
																		VALUE_7 VARCHAR(50) NOT NULL,
																		VALUE_8 VARCHAR(50) NOT NULL,
																		VALUE_9 VARCHAR(50) NOT NULL,
																		VALUE_10 VARCHAR(50) NOT NULL,
																		VALUE_11 VARCHAR(50) NOT NULL,
																		VALUE_12 VARCHAR(50) NOT NULL,
																		FOREIGN KEY(VALUE_ID) REFERENCES field_iden(ID),
																		PRIMARY KEY(ID)
																	);'''

#print (query_string_field_values)
crs.execute(query_string_field_values)


query_string_respondent_details = '''CREATE TABLE respondent_details ( ID INT UNSIGNED AUTO_INCREMENT,
																		Email VARCHAR(50) NOT NULL,
																		ANSWER TINYINT NOT NULL,
																		Value_ID INT UNSIGNED NOT NULL,
																		FOREIGN KEY(VALUE_ID) REFERENCES field_values(ID),
																		PRIMARY KEY(ID)
																	);'''

#print (query_string_respondent_details)
crs.execute(query_string_respondent_details)

#----------------------------------------------------------------------------------------------------------------
class SQLClass:
	'''This is a class for all sql commands'''
	def __init__(self,comp_id=0,comp_name='',emailFile='',queryFile=''):
		self.self = self
		self.emailFile = emailFile
		self.queryFile = queryFile
		self.comp_id = comp_id
		self.comp_name = comp_name

	def insertvalue(self):
		with open(self.queryFile,'r') as file:
			questions_list = []
			fileReader = csv.reader(file,delimiter=',')
			for row in fileReader:
				for x in row:
					questions_list.append(x)
				break

		query_input_field_iden = "INSERT INTO field_iden values(NULL,'%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s');" %(questions_list[1],questions_list[2],questions_list[3],questions_list[4],questions_list[5],questions_list[6],questions_list[7],questions_list[8],questions_list[9],questions_list[10],questions_list[11],questions_list[12])
		crs.execute(query_input_field_iden)
		database.commit()
		#print(query_input_field_iden)


		with open(self.queryFile,'r') as newfile:
			newlist = []
			newfileReader = csv.reader(newfile, delimiter = ',')
			for x in newfileReader:
				newlist.append(x)
		newlist = newlist[1:]

		count = 0
		while count<len(newlist):

			query_string_fields = "INSERT INTO field_values VALUES(%s,%d,'%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s');" %(newlist[count][0],1,newlist[count][1],newlist[count][2],newlist[count][3],newlist[count][4],newlist[count][5],newlist[count][6],newlist[count][7],newlist[count][8],newlist[count][9],newlist[count][10],newlist[count][11],newlist[count][12])
			crs.execute(query_string_fields)
			database.commit()
			count += 1
			#print(count)
			#print(query_string_fields)

	def updateSurvey(self):
		query_string_survey_id = "INSERT INTO survey_details VALUES(NULL,%d,'%s',now(),NULL)" %(self.comp_id,self.comp_name)
		crs.execute(query_string_survey_id)
		databse.commit()

	def uploadAnswer(self):
		with open(self.emailFile,'r') as file:
			email_list = []
			fileReader = csv.reader(file,delimiter = ',')
			for row in fileReader:
				email_list.append(row[1])
		email_list = email_list[1:]

		query_string_response = "INSERT INTO respondent_details VALUES(NULL,'%s',%d,)"
		crs.execute(query_string_response)
		databse.commit()

	def display(self):
		pass
#-----------------------------------------------------------------------------------------------

# FIRSTLY ASK: Do you want to create a survey or take a survey?
#1. Create a survey -> Use existing database or create new database?
#2. Take a survey -> Select company id or name -> Question by question give answers, store those answers and then display
# For creation of survey, drop existing tables, create new ones, with new questions.
#So the first time this code is run you have to create a new survey


while True:
	opt00 = int(input('''Do you want to:
						1. Create a survey
						2. Take an existing Survey

						Enter your Option: '''))

	if opt00 == 1:
		print ('You are now creating a survey!')
		opt = int(input('''Enter an Option:
	 					1. Enter Survey details
						2. Upload CSV files to Database
						3. Exit

						Option: '''))

		if opt==1:
			myObj = SQLClass()
			print("Enter Company Details:"))
			myObj.comp_id = input("1. Enter Company ID: ")
			myObj.comp_name = input("2. Enter Company Name: ")
			myObj.updateSurvey()

		if opt==2:
			myObj = SQLClass()
			print('Enter CSV Filenames (with the .csv extension)')
			myObj.queryFile = input('Enter filename for Survey Questions: ')
			myObj.emailFile = input('Enter filename for Emails: ')

		if opt==3:
			continue
		else:
			print('enter a valid option')
			continue




	if opt00 == 2:
		print('you are now taking an existing survey')
		opt01 = int(input('''Enter an Option:
	 					1. Choose survey
						2. Exit

						Option: '''))


		if opt01 == 1:
			crs.execute("SELECT survey_details.`SURVEY_ID`, survey_details.`COMPANY_NAME` FROM survey_details")
			data = crs.fetchone()
			print(data)
			opt02 = int(input('Enter ID of Survey you want to take: '))
			print('Questions are: \n')
			crs.execute("SELECT * FROM field_values WHERE  ")

	else:
		print('Enter a valid option')
		continue

myObj = SQLClass()
myObj.queryFile = input('Enter filename for Survey: ')
myObj.emailFile = input('Enter filename for emails: ')
myObj.insertvalue()
