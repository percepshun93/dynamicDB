# dynamicDB
Dynamic database project for Mahiteor Technologies

This is a dynamic database project in SQL, automated by python. 
This was made for storing information on surveys taken by clients of Mahiteor Technologies.

Survey data was stored in 2 CSV files - one containing the information of the surveys, and the other containing the emails of the people to whom the survey was supposed to be sent to. 

Using python, the respective information was taken from these csv files to be automatically updated to the tables in a database created by the admin.

Since the number of queries or the number of companies who sent information to the client was not known, it would be shortsighted to let python create unique tables for every survey taken. Rather, a relational database was created which linked 4 tables to store survey details, field ids - containing the labels of survey questions, field values - containing the actual questions, and customer answers. 

These relationships are made via foreign key assignments and queries are enabled for the user to find relationships between these tables. 

The entire structure was made on python. The data is also automatically uploaded to the tables once the script is run. A menu based user interfaced was developed for the user so that no back end changes need to be made. 

This is still a work in progress as some changes are being made to the user interface and automation of data entry. 
