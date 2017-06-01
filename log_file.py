import sys
import os
import time

#to create folders and files for a new project
def create_project(projectName):
	os.mkdir(projectName)
	os.chdir(projectName)
	f = open('descriptif.txt', 'w')
	f = open('logs.txt', 'w')

#to write the description file for a project
def write_description(date, projectName,typeProjet, language, nbParticipants, estimatedTime, loc, nbBugs):
	fichier = open("descriptif.txt", "a")
	fichier.write("\ndate: "+date)
	fichier.write("\nproject name: "+projectName)
	fichier.write("\nproject type: "+typeProjet)
	fichier.write("\nlanguage "+language)
	fichier.write("\nnumber of participants "+nbParticipants)
	fichier.write("\nestimated time "+estimatedTime)
	fichier.write("\nlines of code "+loc)
	fichier.write("\nnumber of bugs "+nbBugs)
	fichier.close()

#to write a new log entry
def write_log(date, typeOfEntry, bugType, description, solution):
	fichier = open("logs.txt", "a")
	fichier.write(date+" "+typeOfEntry+" "+bugType+" "+description+" "+solution)
	fichier.write("\n")
	fichier.close()

#to read an entry
def read_project(projectName, fileName):
	os.chdir(projectName)
	fichier = open(fileName, "r")
	print (fichier.read())
	fichier.close()

S = ''
while S != 'exit':
	print ('To create a new project tape NP')
	print ('To read the content of a project tape RP')
	print ('To edit the content of a project tape EP')
	choix = input('tape your request: ')
	if choix == "NP":
		projectName = input('Project name: ')
		date = time.strftime('%d/%m/%y %H:%M', time.localtime())
		typeProjet = input('Project type: ')
		language = input('Project language: ')
		nbParticipants = input('Number of participants: ')
		estimatedTime = input('Estimated time: ')
		loc = input('Lines of code: ')
		nbBugs = input('Number of bugs: ')
		create_project(projectName)
		write_description(date, projectName, typeProjet, language, nbParticipants, estimatedTime, loc, nbBugs)
	elif choix == "RP":
		projectName = input('tape the name of the folder you want to open: ')
		fileName = input('tape the name of the file you want to read: ')
		read_project(projectName, fileName)
	elif choix == "EP":
		projectName = ''
		projectName = input('tape the name of your project: ')
		os.chdir(projectName)
		Q = ''
		while Q != "exit":
			typeOfEntry = input('type of entry (description DESC or bug BUG): ')
			date = time.strftime('%d/%m/%y %H:%M', time.localtime())
			typeOfEntry = input('type of entry (description DESC or bug BUG): ')
			bugType = input('tYPE OF bug (NONE (if not a bug), critical, blocking, not_blocking, help_data_needed, not_critical, critical_not_blocking): ')
			description = input('description: ')
			solution = input('solution: ')
			write_log(date, typeOfEntry, bugType, description, solution)
			Q = input('to exit tape exit else enter: ')
			if Q == 'exit':
				os.chdir('../')

	S = input('to exit tape exit to go back to menu tape enter: ')




