# Temp imports, we should move it later to __init__.py
import datetime
import re
import pymysql
from openpyxl import *


# Class object application as provided in the design
class Application:
    def __init__(self, user):
        self.__appVersion = 'v 1.00'
        self.__lastUpdate = '2022-12-13'
        self.prevFiles = dict()
        # Initiating relationships (composition)
        self.obj_guide = Guide()
        self.obj_file = File()
        # Initiating relationships (aggregation)
        self.obj_user = user

    # # @property
    # def appVersion(self):
    #     return self.__appVersion
    #
    # # @appVersion.setter
    # def appVersion(self, version) -> int:
    #     self.__appVersion = version
    #     return 0
    #
    # # @property
    # def lastUpdate(self) -> datetime:
    #     return self.__lastUpdate
    #
    # # @lastUpdate.setter
    # def lastUpdate(self, last_date) -> int:
    #     self.__lastUpdate = last_date
    #     return 0

    def files(self):
        return self.prevFiles

    def addFile(self, filename, location) -> int:
        self.prevFiles[filename] = location
        return 0


# Class object user as provided in the design
class User:
    def __init__(self):
        self.userFirstName = str()
        self.userLastName = str()
        self.userEmail = str()


    # # @property
    # def userFirstName(self):
    #     return self.userFirstName
    #
    # # @userFirstName.setter
    # def userFirstName(self, firstname) -> 0:
    #     self.userFirstName = firstname
    #     return 0
    #
    # # @property
    # def userLastName(self):
    #     return self.userLastName
    #
    # # @userLastName.setter
    # def userLastName(self, lastname) -> 0:
    #     self.userLastName = lastname
    #     return 0


# Class object guide as provided in the design
class Guide:  # postponed for later iteration
    def __init__(self):
        pass


# Class object file as provided in the design
class File:  # postponed for later iteration
    def __init__(self):
        self.fileName = None
        self.fileLocation = None
        self.fileSaved = None
        self.progressSaved = None
        self.backubFile = None
        self.new_file = False
        self.wb = None
        self.ws = None

    def upload_file(self):
        self.wb = load_workbook(filename=self.fileName)
        self.ws = self.wb.active
        return self.ws

    def save_file(self):
        self.ws.save("D:\Current_Projects\English_Excel_Project\Python_Codes\saved.xlsx")

    def new_file(self):
        self.wb = Workbook()
        dest_filename = 'new_book.xlsx'
        self.ws = self.wb.active
        self.ws.title = "new worksheet"

        return self.ws

    def save_file(self):
        self.wb.save(filename=self.fileName)


class Registration:

    def __init__(self):
        # Initiating relationships (composition)
        self.obj_User = User()
        # db related
        self.connection = None
        self.mycursor = None
        # entries
        self.firstname = str()
        self.lastname = str()
        self.userEmail = str()
        self.__userPassword = str()
        # validation related
        self.passwordValidated = False
        self.passwordConfirmed = False
        self.emailValidated = False
        self.allValidated = (self.passwordValidated and self.passwordConfirmed and self.emailValidated)
        self.loginMatched = False
        # misc
        self.guestUser = False
        self.EMAIL_REGEX = "^[A-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$"
        self.PASS_REGEX = "^(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9]).{8,}$"

    # # @property
    # def passwordValidated(self):
    #     return self.passwordValidated
    #
    # # @passwordValidated.setter
    # def passwordValidated(self, value):
    #     self.passwordValidated = value
    #
    # # @property
    # def passwordConfirmed(self):
    #     return self.passwordConfirmed
    #
    # # @passwordConfirmed.setter
    # def passwordConfirmed(self, value):
    #     self.passwordConfirmed = value
    #
    # # @property
    # def emailValidated(self):
    #     return self.emailValidated
    #
    # # @emailValidated.setter
    # def emailValidated(self, value):
    #     self.emailValidated = value
    #
    # # @property
    # def allValidated(self):
    #     return self.allValidated
    #
    # # @allValidated.setter
    # def allValidated(self, value):
    #     self.allValidated = value
    #
    # # @property
    # def userEmail(self):
    #     return self.userEmail
    #
    # # @userEmail.setter
    # def userEmail(self, email) -> 0:
    #     self.userEmail = email
    #     return 0
    #
    # # @property
    # def userPassword(self):
    #     return self.__userPassword
    #
    # # @userPassword.setter
    # def userPassword(self, password) -> 0:
    #     self.__userPassword = password
    #     return 0

    def validateFName(self, fname):
        match = (len(fname) < 50)
        try:
            if match:
                self.firstname = fname
                return 1
            else:
                self.firstname = 'error'
                return False
        except BaseException as e:
            print(e, "||validateFName function||")
            return -1

    def validateLName(self, lname):
        match = (len(lname) < 50)
        try:
            if match:
                self.lastname = lname
                return 1
            else:
                self.lastname = "error"
                return False
        except BaseException as e:
            print(e, "||validateLName function||")
            return -1

    def validateEmail(self, email) -> bool or int:
        # The match function validated text must be from the beginning of the string, which make the validation more ...
        # ... strict as we wish
        match = re.match(self.EMAIL_REGEX, email)  # returns class type if matched, and None if not matched
        try:
            if match:
                self.emailValidated = True
                self.userEmail = email
                return 1
            else:
                self.emailValidated = False
                self.userEmail = email
                return False
        except BaseException as e:
            print(e, "||validateEmail function||")
            return -1

        # Here we shall validate the uniqueness of the email in the sql server
        pass  # postponed for later iteration

    def validatePassword(self, password):
        # The match function validated text must be from the beginning of the string, which make the validation more ...
        # ... strict as we wish
        match = re.match(self.PASS_REGEX, password)  # returns class type if matched, and None if not matched
        try:
            if match:
                self.passwordValidated = True
                self.__userPassword = password
                return 1
            else:
                self.passwordValidated = False
                self.__userPassword = password
                return False
        except BaseException as e:
            print(e, "||validatePassword function||")
            return -1

    def confirmPassword(self, password, confirmation_password) -> bool | int:
        # This function match the password confirmation field with the password field
        # This is done directly with no foreigner modules, to make sure it is strict
        match = (password == confirmation_password)  # returns class type if matched, and None if not matched
        try:
            if match:
                self.passwordConfirmed = True
                self.__userPassword = password
                return 1
            else:
                self.passwordConfirmed = False
                self.__userPassword = password
                return False
        except BaseException as e:
            print(e, "||validatePassword function||")
            return -1

    def matchLoginCredentials(self):  # postponed for later iteration
        if self.emailValidated and self.passwordValidated and self.passwordConfirmed:
            self.allValidated = True
            return True
        else:
            self.allValidated = 0
            return 0

    def default_values(self):
        try:
            # db related
            self.connection = None
            self.mycursor = None
            # entries
            self.firstname = None
            self.lastname = None
            self.userEmail = None
            self.__userPassword = None
            # validation related
            self.passwordValidated = False
            self.passwordConfirmed = False
            self.emailValidated = False
            self.allValidated = (self.passwordValidated and self.passwordConfirmed and self.emailValidated)
            self.loginMatched = False
            # misc
            self.guestUser = False
        except BaseException as e:
            print("||default_values method||", e)

    def db_connect(self):
        # Make connection
        try:
            self.connection = pymysql.connect(host="127.0.0.1", port=3306, user="root", database='english_excel')
            self.mycursor = self.connection.cursor()
            self.mycursor.execute(""" 
            CREATE TABLE if not exists users (
              `id` int NOT NULL AUTO_INCREMENT,
              `fname` varchar(50) DEFAULT NULL,
              `lname` varchar(50) DEFAULT NULL,
              `email` varchar(100) DEFAULT NULL,
              `pass` varchar(100) DEFAULT NULL,
              PRIMARY KEY (`id`)
            ) """)
            self.connection.commit()

            return 1
        except BaseException as e:
            print("||db_connect method||", e)
            return -1

    def login(self):  # postponed for later iteration
        try:
            # Check connection / make sure it is connected
            self.db_connect()
            # -Make sure the email is already in the database-
            email_exists = self.mycursor.execute(f"SELECT email FROM users WHERE email = '{self.userEmail}';")
            if email_exists == 1:
                self.mycursor.execute(f"SELECT pass FROM users WHERE email = '{self.userEmail}';")
                temp_password = self.mycursor.fetchall()[0][0]
                if self.__userPassword == temp_password:
                    self.obj_User.userFirstName = self.firstname
                    self.obj_User.userLastName = self.lastname
                    self.obj_User.userEmail = self.userEmail
                    self.default_values()
                    self.guestUser = False
                    return 1
                else:
                    # Not as we wish
                    return 0
            elif email_exists == 0:
                # code says email doesn't exist
                return -2
            elif email_exists > 1:
                # code says there are multiple rows with the same email
                return -3

        except BaseException as e:
            return -1

    def signup(self):  # postponed for later iteration
        try:
            # Check connection / make sure it is connected
            self.db_connect()
            # -Make sure the email is not already in the database-
            if self.mycursor.execute(f"SELECT email FROM users WHERE email = '{self.userEmail}';") > 0:
                return -1
            # ---Add the data to the database---
            self.mycursor.execute(f"""
            INSERT INTO users
            VALUES (0, '{self.firstname}', '{self.lastname}', '{self.userEmail}', '{self.__userPassword}');
            """)
            self.connection.commit()
        except BaseException as e:
            return 0

        return 1


if __name__ == "__main__":
    obj = Registration()
