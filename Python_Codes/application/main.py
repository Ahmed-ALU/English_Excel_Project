# Temp imports, we should move it later to __init__.py
import datetime
import re


# Class object application as provided in the design
class Application:
    def __init__(self):
        self.__appVersion = str()
        self.__lastUpdate = datetime
        self.prevFiles = dict()

    def getVersion(self):
        return self.__appVersion

    def __setVersion(self, version) -> int:
        self.__appVersion = version
        return 0

    def getLastUpdate(self) -> datetime:
        return self.__lastUpdate

    def __setLastUpdate(self, last_date) -> int:
        self.__lastUpdate = last_date
        return 0

    def getfiles(self):
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
        self.__userPassword = str()
        self.guestUser = True
        self.loginMatched = bool()
        self.EMAIL_REGEX = "^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$"
        self.PASS_REGEX = "^(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9])(?=.*?[#?!@$%^&*-]).{8,}$"

    def getUserFirstName(self):
        return self.userFirstName

    def __setUserFirstName(self, firstname) -> 0:
        self.userFirstName = firstname
        return 0

    def getUserLastName(self):
        return self.userLastName

    def __setUserLastName(self, lastname) -> 0:
        self.userLastName = lastname
        return 0

    def getUserEmail(self):
        return self.userEmail

    def __setUserEmail(self, email) -> 0:
        self.userEmail = email
        return 0

    def __getUserPassword(self):
        return self.__userPassword

    def __setUserPassword(self, password) -> 0:
        self.__userPassword = password
        return 0

    def matchLoginCredentials(self):  # postponed for later iteration
        pass

    def validateEmail(self, email) -> bool or int:
        # The match function validated text must be from the beginning of the string, which make the validation more ...
        # ... strict as we wish
        match = re.match(self.EMAIL_REGEX, email)  # returns class type if matched, and None if not matched
        try:
            if match:
                return True
            else:
                return False
        except BaseException as e:
            print(e, "||validateEmail function||")
            return -1

        # Here we shall validate the uniqueness of the email in the sql server
        pass  # postponed for later iteration

    def __validatePassword(self, password):
        # The match function validated text must be from the beginning of the string, which make the validation more ...
        # ... strict as we wish
        match = re.match(self.PASS_REGEX, password)  # returns class type if matched, and None if not matched
        try:
            if match:
                return True
            else:
                return False
        except BaseException as e:
            print(e, "||validatePassword function||")
            return -1

    def logIn(self):  # postponed for later iteration
        pass

    def signUp(self):  # postponed for later iteration
        pass


# Class object guide as provided in the design
class Guide:  # postponed for later iteration
    def __init__(self):
        pass


# Class object file as provided in the design
class File:  # postponed for later iteration
    def __init__(self):
        pass
