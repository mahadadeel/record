##Record Data Structure
#13/9/2020, Mahad Adeel

import datetime as dt

def getNow():
    return dt.datetime.now()

class Record:
    def __init__(self, forename, surname, date_of_birth, gender, CS_student):
        self.__forename = forename.title()
        self.__surname = surname.title()
        try:
            self.__date_of_birth = dt.datetime.strptime(date_of_birth, '%d/%m/%Y').date()
        except:
            print("Date of Birth entered is invalid. Please enter a valid Date of Birth formatted as DD/MM/YYYY.")

        gender = gender.upper()
        if gender not in ('M','F','NB'):
            print("Enter a valid gender from 3 options: Male, Female, Non-Binary")
        else:
            self.__gender = gender

        try:
            CS_student = bool(CS_student)
            self.__CS_student = CS_student
        except:
            print("CS_student entered is invalid. Enter True or False for CS_student.")
        self.__created = getNow().strftime('%d/%m/%Y %H:%M:%S')

    def getForename(self):
        return self.__forename

    def getSurname(self):
        return self.__surname

    def getGender(self):
        return self.__gender

    def isCSstudent(self):
        return self.__CS_student

    def getDateOfBirth(self):
        return self.__date_of_birth

    def getAge(self):
        currentDate = getNow().date()
        difference = (currentDate - self.__date_of_birth).days

        years = difference / 364.25

        return years

        ##Find difference in years, days and months

    def setForename(self):
        self.__forename = input("Enter forename\n").title()

    def setSurname(self):
        self.__surname = input("Enter surname\n").title()

    def setGender(self):
        valid = False
        while not valid:
            try:
                self.__gender = input("Enter gender as M, F, or NB:\n").upper()
                if self.__gender not in ('M','F','NB'):
                    print("Enter a valid gender")
                else:
                    valid = True
            except:
                print("Enter a valid input")

    def setCSstudent(self):
        valid = False
        while not valid:
            try:
                self.__CS_student = (input("Enter CS Student as True or False\n").upper()) == 'TRUE'
                valid = True
            except:
                print("Enter True or False")

    def setDateOfBirth(self):
        valid = False
        while not valid:
            try:
                self.__date_of_birth = dt.datetime.strptime(input("Enter Date of Birth as DD/MM/YYYY\n"),'%d/%m/%Y').date()
                valid = True
            except:
                print("Enter a valid Date of Birth")

    def created(self):
        return self.__created

def getAttributes():
    print(r.getForename())
    print(r.getSurname())
    print(r.getDateOfBirth())
    print(r.getAge())
    print(r.getGender())
    print(r.isCSstudent())
    print(r.created())

r = Record('Mahad','Adeel','06/01/2004','M',CS_student=False)

getAttributes()

r.setForename()
r.setSurname()
r.setDateOfBirth()
r.setGender()
r.setCSstudent()
r.created()

getAttributes()
