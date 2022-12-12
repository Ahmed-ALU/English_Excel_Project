# Temp imports, we should move it later to __init__.py
import datetime
import re
import pymysql


# Class object application as provided in the design
class Application:
    def __init__(self, user):
        self.__appVersion = str()
        self.__lastUpdate = datetime
        self.prevFiles = dict()
        # Initiating relationships (composition)
        self.obj_guide = Guide()
        self.obj_file = File()
        # Initiating relationships (aggregation)
        self.obj_user = user

    # @property
    def appVersion(self):
        return self.__appVersion

    # @appVersion.setter
    def appVersion(self, version) -> int:
        self.__appVersion = version
        return 0

    # @property
    def lastUpdate(self) -> datetime:
        return self.__lastUpdate

    # @lastUpdate.setter
    def lastUpdate(self, last_date) -> int:
        self.__lastUpdate = last_date
        return 0

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
        # Initiating relationships (aggregation)

    # @property
    def userFirstName(self):
        return self.userFirstName

    # @userFirstName.setter
    def userFirstName(self, firstname) -> 0:
        self.userFirstName = firstname
        return 0

    # @property
    def userLastName(self):
        return self.userLastName

    # @userLastName.setter
    def userLastName(self, lastname) -> 0:
        self.userLastName = lastname
        return 0


# Class object guide as provided in the design
class Guide:  # postponed for later iteration
    def __init__(self):
        pass


# Class object file as provided in the design
class File:  # postponed for later iteration
    def __init__(self):
        pass


class Registration:

    def __init__(self):
        # Initiating relationships (composition)
        self.obj_User = User()

        self.connection = None
        self.mycursor = None
        self.firstname = str()
        self.lastname = str()
        self.passwordValidated = False
        self.passwordConfirmed = False
        self.emailValidated = False
        self.allValidated = (self.passwordValidated and self.passwordConfirmed and self.emailValidated)
        self.obj_User.userEmail = str()
        self.userEmail = str()
        self.__userPassword = str()
        self.guestUser = True
        self.loginMatched = bool()
        self.EMAIL_REGEX = "^[A-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$"
        self.PASS_REGEX = "^(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9]).{8,}$"

    # @property
    def passwordValidated(self):
        return self.passwordValidated

    # @passwordValidated.setter
    def passwordValidated(self, value):
        self.passwordValidated = value

    # @property
    def passwordConfirmed(self):
        return self.passwordConfirmed

    # @passwordConfirmed.setter
    def passwordConfirmed(self, value):
        self.passwordConfirmed = value

    # @property
    def emailValidated(self):
        return self.emailValidated

    # @emailValidated.setter
    def emailValidated(self, value):
        self.emailValidated = value

    # @property
    def allValidated(self):
        return self.allValidated

    # @allValidated.setter
    def allValidated(self, value):
        self.allValidated = value

    # @property
    def userEmail(self):
        return self.userEmail

    # @userEmail.setter
    def userEmail(self, email) -> 0:
        self.userEmail = email
        return 0

    # @property
    def userPassword(self):
        return self.__userPassword

    # @userPassword.setter
    def userPassword(self, password) -> 0:
        self.__userPassword = password
        return 0

    def validateEmail(self, email) -> bool or int:
        # The match function validated text must be from the beginning of the string, which make the validation more ...
        # ... strict as we wish
        match = re.match(self.EMAIL_REGEX, email)  # returns class type if matched, and None if not matched
        try:
            if match:
                self.emailValidated = True
                self.obj_User.userEmail = email
                return 1
            else:
                self.emailValidated = False
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
                return 1
            else:
                self.passwordValidated = False
                return False
        except BaseException as e:
            print(e, "||validatePassword function||")
            return -1

    def confirmPassword(self, password, confirmation_password) -> bool:
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
                return False
        except BaseException as e:
            print(e, "||validatePassword function||")
            return -1

    def validateFName(self, fname):
        match = (len(fname) < 50)
        try:
            if match:
                self.obj_User.userFirstName = fname
                self.firstname = fname
                return 1
            else:
                self.passwordConfirmed = False
                return False
        except BaseException as e:
            print(e, "||validateFName function||")
            return -1

    def validateLName(self, lname):
        match = (len(lname) < 50)
        try:
            if match:
                self.obj_User.userLastName = lname
                self.lastname = lname
                return 1
            else:
                self.passwordConfirmed = False
                return False
        except BaseException as e:
            print(e, "||validateLName function||")
            return -1

    def matchLoginCredentials(self):  # postponed for later iteration
        if self.emailValidated and self.passwordValidated and self.passwordConfirmed:
            self.allValidated = True
            return True
        else:
            self.allValidated = 0
            return 0

    def login(self):  # postponed for later iteration
        pass

    def db_connect(self):
        # Make connection just in case
        self.connection = pymysql.connect(host="127.0.0.1", port=3306, user="root", database='english_excel')
        self.mycursor = self.connection.cursor()
        # self.mycursor.execute("""CREATE DATABASE if not exists english_excel;""")
        # self.mycursor.execute("Use english_excel;")
        self.mycursor.execute(""" 
        CREATE TABLE if not exists users (
          `id` int NOT NULL AUTO_INCREMENT,
          `fname` varchar(50) DEFAULT NULL,
          `lname` varchar(50) DEFAULT NULL,
          `email` varchar(100) DEFAULT NULL,
          `pass` varchar(100) DEFAULT NULL,
          PRIMARY KEY (`id`)
        ) """)

    def signup(self):  # postponed for later iteration
        # Check connection / make sure it is connected
        self.db_connect()
        # Add the data to the database
        self.firstname =  self.obj_User.userFirstName
        self.lastname = self.obj_User.userLastName
        self.userEmail = self.obj_User.userEmail
        if self.mycursor.execute(f"SELECT email FROM users WHERE email = '{self.obj_User.userEmail}';") > 0:
            return -1
        self.mycursor.execute(f"""
        INSERT INTO users
        VALUES (0, '{self.obj_User.userFirstName}', '{self.obj_User.userLastName}', '{self.obj_User.userEmail}', '{self.__userPassword}');
        """)
        self.connection.commit()

        return 1

    def test(self):
        print("Test")


if __name__ == "__main__":
    obj = Registration()
