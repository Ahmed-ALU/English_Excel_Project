from tkinter import *
from tkinter import messagebox


def show(widget):
    widget.configure(show="")


def hide(widget):
    widget.configure(show="*")
    return widget.get()


def prevent_copy_paste(widget):
    widget.bind('<Control-c>', lambda e: 'break')  # disable copy
    widget.bind('<Control-x>', lambda e: 'break')  # disable cut
    widget.bind('<Control-v>', lambda e: 'break')  # disable paste
    widget.bind('<Button-3>', lambda e: 'break')  # disable right-click


def signup_validation(self_obj, obj_reg):
    # obj_reg.useremail
    if obj_reg.matchLoginCredentials():
        try:
            op_id = obj_reg.signup()
            if op_id == 1:
                messagebox.showinfo('Signed up successfully', "Signed up, Log in with the same credentials")
                self_obj.first_name.delete(0, END)
                self_obj.first_name.insert(0, 'First Name')
                self_obj.second_name.delete(0, END)
                self_obj.second_name.insert(0, 'Last Name')
                self_obj.email_entry.delete(0, END)
                self_obj.email_entry.insert(0, 'Last Name')
                self_obj.password_entry.delete(0, END)
                self_obj.password_entry.insert(0, 'Password')
                show(self_obj.password_entry)
                self_obj.password_confirm.delete(0, END)
                self_obj.password_confirm.insert(0, 'Confirm Password')
                show(self_obj.password_confirm)
                # self_obj.parent.LogInPage.email_entry.insert(0, self_obj.obj_register.obj_User.userEmail)
                self_obj.parent.show_frame(self_obj.parent.LogInPage)
            elif op_id == -1:
                messagebox.showinfo('Email Already Exists',
                                    "The email you are using already exists in our database, please try to log in.")
        except BaseException as e:
            messagebox.showinfo('Error connecting to the database', e)

    else:
        messagebox.showinfo('incorrect inputs',
                            "Please Make sure all your inputs are matched and correct and there are no red flags")


def validation_error():
    messagebox.showinfo('Validation Error',
                        "An error happen while validating your inputs, Please try again later or contact the owner if "
                        "it didn't work")


def create_general_menubar(parent):
    menubar = Menu(parent, bd=3, relief=RAISED, activebackground="#80B9DC")
    # File menu
    filemenu = Menu(menubar, tearoff=0, relief=RAISED, activebackground="#026AA9")
    menubar.add_cascade(label="GoTo", menu=filemenu)
    filemenu.add_command(label="Home Page", command=lambda: parent.show_frame(parent.HomePage))
    filemenu.add_command(label="Log in", command=lambda: parent.show_frame(parent.LogInPage))
    filemenu.add_command(label="Sign up", command=lambda: parent.show_frame(parent.SignUpPage))
    filemenu.add_separator()
    filemenu.add_command(label="Exit", command=parent.quit)
    return menubar, filemenu

def validate_fname(obj_register, fname_entry):
    # first name validation
    if fname_entry.get() != "First Name" and fname_entry.get() != "":
        fname_match = obj_register.validateFName(fname_entry.get())
        if fname_match:
            fname_entry.configure(bg='white', fg='#1aa160')
        elif not fname_match:
            fname_entry.configure(bg='red', fg='white')
        elif fname_match == -1:
            validation_error()  # error message
    else:
        fname_entry.configure(bg='white', fg='#1aa160')


def validate_lname(obj_register, lname_entry):

    # Second name validation
    if lname_entry.get() != "Second Name" and lname_entry.get() != "":
        lname_match = obj_register.validateLName(lname_entry.get())
        if lname_match:
            lname_entry.configure(bg='white', fg='#1aa160')
        elif not lname_match:
            lname_entry.configure(bg='red', fg='white')
        elif lname_match == -1:
            validation_error()  # error message
    else:
        lname_entry.configure(bg='white', fg='#1aa160')


def validate_e(obj_register, email_entry):
    if email_entry.get() != "Email Address" and email_entry.get() != "":
        email_match = obj_register.validateEmail(email_entry.get())
        # email validation
        if email_match:
            email_entry.configure(bg='white', fg='#1aa160')
        elif not email_match:
            email_entry.configure(bg='red', fg='white')
        elif email_match == -1:
            validation_error()  # error message
    else:
        email_entry.configure(bg='white', fg='#1aa160')


def validate_p(obj_register, password_entry):
    if password_entry.get() != "Password" and password_entry.get() != "":
        password_match = obj_register.validatePassword(password_entry.get())
        # email validation
        if password_match:
            password_entry.configure(bg='white', fg='#1aa160')
        elif not password_match:
            password_entry.configure(bg='red', fg='white')
        elif password_match == -1:
            validation_error()  # error message
    else:
        password_entry.configure(bg='white', fg='#1aa160')


def validate_pc(obj_register, password_entry, password_confirm):
    if password_confirm.get() != "Confirm Password" and password_confirm.get() != "":
        confirm_match = obj_register.confirmPassword(password_entry.get(), password_confirm.get())
        # email validation
        if confirm_match:
            password_confirm.configure(bg='white', fg='#1aa160')
        elif not confirm_match:
            password_confirm.configure(bg='red', fg='white')
        elif confirm_match == -1:
            validation_error()  # error message
    else:
        password_confirm.configure(bg='white', fg='#1aa160')


def test(wid):
    wid.insert(0, "Hello")