import tkinter as tk
import tkinter.ttk as ttk
import utils as u
from application import main


class App(tk.Tk):
    def __init__(self, registration=None, file=None):
        super().__init__()
        # Initializing relationships (aggregation)
        self.obj_register = registration
        self.obj_file = file

        # Setting up Initial Things
        self.title("eNGLISH EXCEL")
        self.iconphoto(False, tk.PhotoImage(file="../Pictures/Logo_v1.1.png"))
        # self.state("normal")
        self.geometry("900x600")
        # self.resizable(width=False, height=False)

        # Creating a container
        container = tk.Frame(self, bg="#8AA7A9")
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        # Initialize Frames (add each new frame here)
        self.frames = {}
        self.HomePage = HomePage
        self.LogInPage = LogInPage
        self.SignUpPage = SignUpPage
        # self.MainPage = MainPage

        # Defining Frames and Packing it (add each new frame here to the set)
        for F in {HomePage, LogInPage, SignUpPage}:
            if F == SignUpPage | LogInPage:
                frame = F(self, container, self.obj_register)
            else:
                frame = F(self, container, self.obj_file)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(HomePage)

    def show_frame(self, cont):
        frame = self.frames[cont]
        menubar = u.create_general_menubar(self)
        self.configure(menu=menubar[0])
        frame.tkraise()  # This line will put the frame on front
        frame.focus_set()


class HomePage(tk.Frame):
    def __init__(self, parent, container, registration=None):
        super().__init__(container)
        # parent.state("normal")
        # parent.geometry("900x600")
        # parent.resizable(width=False, height=False)


        # Initializing relationships (aggregation)
        self.obj_register = registration

        # --vars initialization--
        self.parent = parent
        self.file_menu = None
        self.menubar = None
        self.bg_label = None
        self.bgImage = None
        self.signup_button = None
        self.login_button = None
        self.guide_button = None
        self.guest_button = None
        
        # calling functions to create the UI
        self.background_image_func()
        self.login_button_func()
        self.signup_button_func()
        self.guest_button_func()
        self.guide_button_func()

    def background_image_func(self):
        # --background image initialization--
        from PIL import ImageTk, Image
        self.bgImage = ImageTk.PhotoImage(Image.open("../Pictures/Home_Pagev1.jpg"))

        # --set background image label--
        self.bg_label = tk.Label(self, image=self.bgImage)
        self.bg_label.place(x=0, y=0)

    # ----Buttons----
    def login_button_func(self):
        # 1--login--
        self.login_button = tk.Button(self, text='Log in !', bd='3', width=30, font=('Myriad Pro', 12, 'bold'), foreground='white', background='#1aa160', command=lambda: self.parent.show_frame(self.parent.LogInPage))
        self.login_button.place(x=310, y=209)

    def signup_button_func(self):
        # 2--signup--
        self.signup_button = tk.Button(self, text='Sign up !', bd='3', width=30, font=('Myriad Pro', 12, 'bold'), foreground='white', background='#1aa160', command=lambda: self.parent.show_frame(self.parent.SignUpPage))
        self.signup_button.place(x=310, y=275)

    def guide_button_func(self):
        # 3--guide--
        self.guide_button = tk.Button(self, text='Guide !', bd='2', width=14, font=('Myriad Pro', 11, 'bold'), foreground='white', background='#1aa160')
        self.guide_button.place(x=300, y=355)
    
    def guest_button_func(self):
        # 4--guest--
        self.guest_button = tk.Button(self, text='Guest User !', bd='2', width=14, font=('Myriad Pro', 11, 'bold'), foreground='white', background='#1aa160')
        self.guest_button.place(x=465, y=355)


class LogInPage(tk.Frame):
    def __init__(self, parent, container, registration=None):
        super().__init__(container)
        # parent.geometry("900x600")
        # parent.resizable(width=False, height=False)

        # Initializing relationships (aggregation)
        self.obj_register = obj_reg

        # --vars initialization--
        self.parent = parent
        self.forgot_password = None
        self.signup_button = None
        self.login_button = None
        self.password_entry = None
        self.email_entry = None
        self.bg_label = None
        self.bgImage = None
        self.file_menu = None

        # calling functions to create the UI
        self.background_image_func()
        self.email_entry_func()
        self.password_entry_func()
        self.login_button_func()
        self.signup_button_func()
        self.forgot_password_button_func()

    def background_image_func(self):
        # --background image initialization--
        from PIL import ImageTk, Image
        self.bgImage = ImageTk.PhotoImage(Image.open("../Pictures/Login_Page_v1.jpg"))
        # --set background image label--
        self.bg_label = tk.Label(self, image=self.bgImage)
        self.bg_label.place(x=0, y=0)

    # ----Entries----
    def email_entry_func(self):
        # 1--email entry--
        self.email_entry = tk.Entry(self, bd='2', width=30, font=('Myriad Pro', 12, 'bold'), foreground='#1aa160', background='white')
        self.email_entry.insert(0, "Email Address")
        self.email_entry.bind("<FocusIn>", lambda e: self.email_entry.delete(0, tk.END) if (self.email_entry.get() == "Email Address") else 0)
        self.email_entry.bind("<FocusOut>", lambda e: (self.email_entry.insert(0, 'Email Address') if (self.email_entry.get() == "") else 0))
        self.email_entry.bind("<KeyRelease>", lambda e: u.validate_e(self.obj_register, self.email_entry))
        self.email_entry.place(x=310, y=210)

    def password_entry_func(self):
        # 2--password entry--
        self.password_entry = tk.Entry(self, bd='2', width=30, font=('Myriad Pro', 12, 'bold'), foreground='#1aa160', background='white')
        self.password_entry.insert(0, "Password")
        self.password_entry.bind("<FocusIn>", lambda e: (self.password_entry.delete(0, tk.END), u.show(self.password_entry)) if (self.password_entry.get() == "Password") else 0)
        self.password_entry.bind("<FocusOut>",lambda e: (self.password_entry.insert(0, "Password" if (self.password_entry.get() == "") else ""), u.show(self.password_entry) if (self.password_entry.get() == "Password") else u.hide(self.password_entry))) if (self.password_entry.get() == "" or "Password") else u.hide(self.password_entry)
        self.password_entry.bind('<KeyRelease>', lambda e: (self.password_entry.configure(show="*") if (self.password_entry.get() != "Password" and self.password_entry.get() != "") else self.password_entry.configure(show=""), u.validate_p(self.obj_register, self.password_entry)))
        u.prevent_copy_paste(self.password_entry)
        self.password_entry.place(x=310, y=260)

    # ----Buttons----
    def login_button_func(self):
        # 3--login--
        self.login_button = tk.Button(self, text='Log in !', bd='2', width=13, font=('Myriad Pro', 11, 'bold'), foreground='white', background='#1aa160')
        self.login_button.configure(command=lambda: u.login_helper(self, self.obj_register))
        self.login_button.place(x=314, y=310)

    def signup_button_func(self):
        # 4--signup--
        self.signup_button = tk.Button(self, text='Sign up !', bd='2', width=13, font=('Myriad Pro', 11, 'bold'), foreground='white', background='#1aa160', command=lambda: self.parent.show_frame(self.parent.SignUpPage))
        self.signup_button.place(x=464, y=310)

    def forgot_password_button_func(self):
        # 5--forgot_password--
        self.forgot_password = tk.Button(self, text='Forgot password?', width=15, bg="white", fg="blue", bd="0", font=('Myriad Pro', 8, 'bold'), foreground='#1aa160')
        self.forgot_password.place(x=330, y=345)


class SignUpPage(tk.Frame):
    def __init__(self, parent, container, registration=None):
        super().__init__(container)
        # parent.geometry("900x600")
        # parent.resizable(width=False, height=False)

        # Initializing relationships (aggregation)
        self.obj_register = registration

        # --vars initialization--
        self.parent = parent

        self.bg_label = None
        self.bgImage = None
        self.file_menu = None
        self.first_name = None
        self.second_name = None
        self.email_entry = None
        self.password_entry = None
        self.password_confirm = None
        # Buttons
        self.forgot_password = None
        self.login_button = None
        self.signup_button = None
        # self.email = tk.StringVar(value="Empty")  # not used
        # self.password = tk.StringVar(value="Empty")  # not used
        # self.passwordConfirmation = tk.StringVar(value="Empty")  # not used

        # calling functions to create the UI
        self.background_image_func()
        self.first_name_entry_func()
        self.second_name_entry_func()
        self.email_entry_func()
        self.password_entry_func()
        self.password_confirmation_entry_func()
        self.signup_button_func()
        self.login_button_func()
        self.forgot_password_button_func()

    # we will organize our constructor in shape of functions
    def background_image_func(self):
        # --background image initialization--
        from PIL import ImageTk, Image
        self.bgImage = ImageTk.PhotoImage(Image.open("../Pictures/Signin_Page_v1.jpg"))

        # --set background image label--
        self.bg_label = tk.Label(self, image=self.bgImage)
        self.bg_label.place(x=0, y=0)

    # ----Entries----
    def first_name_entry_func(self):
        # 1--first name--
        self.first_name = tk.Entry(self, bd='2', width=31, font=('Myriad Pro', 12, 'bold'), foreground='#1aa160', background='white')
        self.first_name.insert(0, "First Name")
        self.first_name.bind("<FocusIn>", lambda e: self.first_name.delete(0, tk.END) if (self.first_name.get() == "First Name") else 0)
        self.first_name.bind("<FocusOut>", lambda e: (self.first_name.insert(0, 'First Name') if (self.first_name.get() == "") else 0))
        self.first_name.bind("<KeyRelease>", lambda e: u.validate_fname(self.obj_register, self.first_name))
        self.first_name.place(x=310, y=225)

    def second_name_entry_func(self):
        # 2--second name--
        self.second_name = tk.Entry(self, bd='2', width=31, font=('Myriad Pro', 12, 'bold'), foreground='#1aa160', background='white')
        self.second_name.insert(0, "Last Name")
        self.second_name.bind("<FocusIn>", lambda e: self.second_name.delete(0, tk.END) if (self.second_name.get() == "Last Name") else 0)
        self.second_name.bind("<FocusOut>", lambda e: (self.second_name.insert(0, 'Last Name') if (self.second_name.get() == "") else 0))
        self.second_name.bind("<KeyRelease>", lambda e: u.validate_lname(self.obj_register, self.second_name))

        self.second_name.place(x=310, y=275)

    def email_entry_func(self):
        # 3--email entry--
        self.email_entry = tk.Entry(self, bd='2', width=31, font=('Myriad Pro', 12, 'bold'), foreground='#1aa160', background='white')
        self.email_entry.insert(0, "Email Address")
        self.email_entry.bind("<FocusIn>", lambda e: self.email_entry.delete(0, tk.END) if (self.email_entry.get() == "Email Address") else 0)
        self.email_entry.bind("<FocusOut>", lambda e: (self.email_entry.insert(0, 'Email Address') if (self.email_entry.get() == "") else 0))
        self.email_entry.bind("<KeyRelease>", lambda e: u.validate_e(self.obj_register, self.email_entry))
        self.email_entry.place(x=310, y=325)

    def password_entry_func(self):
        # 4--password entry--
        # ! First letter is visible until release !
        self.password_entry = tk.Entry(self, bd='2', width=31, font=('Myriad Pro', 12, 'bold'), foreground='#1aa160', background='white')
        self.password_entry.insert(0, "Password")

        self.password_entry.bind("<FocusIn>", lambda e: (self.password_entry.delete(0, tk.END), u.show(self.password_entry)) if (self.password_entry.get() == "Password") else 0)
        self.password_entry.bind("<FocusOut>", lambda e: ( self.password_entry.insert(0, "Password" if (self.password_entry.get() == "") else ""), u.show(self.password_entry) if (self.password_entry.get() == "Password") else u.hide(self.password_entry))) if (self.password_entry.get() == "" or "Password") else u.hide(self.password_entry)
        self.password_entry.bind('<KeyRelease>', lambda e: (self.password_entry.configure(show="*") if (self.password_entry.get() != "Password" and self.password_entry.get() != "") else self.password_entry.configure(show=""), u.validate_p(self.obj_register, self.password_entry)))
        u.prevent_copy_paste(self.password_entry)
        self.password_entry.place(x=310, y=375)

    def password_confirmation_entry_func(self):
        # 5--password confirmation--
        self.password_confirm = tk.Entry(self, bd='2', width=31, font=('Myriad Pro', 12, 'bold'), foreground='#1aa160', background='white')
        self.password_confirm.insert(0, "Confirm Password")
        self.password_confirm.bind("<FocusIn>", lambda e: (self.password_confirm.delete(0, tk.END), u.show(self.password_confirm)) if (self.password_confirm.get() == "Confirm Password") else 0)
        self.password_confirm.bind("<FocusOut>", lambda e: (self.password_confirm.insert(0, "Confirm Password" if (self.password_confirm.get() == "") else ""), u.show(self.password_confirm) if (self.password_confirm.get() == "Confirm Password") else u.hide(self.password_confirm)) if (self.password_confirm.get() == "" or "Password") else u.hide(self.password_confirm))
        self.password_confirm.bind('<KeyRelease>', lambda e: (self.password_confirm.configure(show="*") if ( self.password_confirm.get() != "Confirm Password" and self.password_confirm.get() != "") else self.password_confirm.configure(show=""), u.validate_pc(self.obj_register, self.password_entry, self.password_confirm)))
        u.prevent_copy_paste(self.password_confirm)
        self.password_confirm.place(x=310, y=425)

    # --Buttons--
    def signup_button_func(self):
        # 6--signup button--
        self.signup_button = tk.Button(self, text='Sign up !', bd='2', width=31, font=('Myriad Pro', 11, 'bold'), foreground='white', background='#1aa160')
        self.signup_button.configure(command=lambda: u.signup_helper(self, self.obj_register))
        self.signup_button.place(x=308, y=472)

    def login_button_func(self):
        # 7--login button--
        self.login_button = tk.Button(self, text='Log in !', bd='2', width=25, font=('Myriad Pro', 10, 'bold'), foreground='white', background='#1aa160', command=lambda: self.parent.show_frame(self.parent.LogInPage))
        self.login_button.place(x=348, y=510)

    def forgot_password_button_func(self):
        # 8--forgot_password button--
        self.forgot_password = tk.Button(self, text='Forgot password?', width=15, bg="white", bd="0", font=('Myriad Pro', 8, 'bold'), foreground='#1aa160')
        self.forgot_password.place(x=405, y=550)


if __name__ == "__main__":
    obj_reg = main.Registration()
    obj_file = main.File()
    app = App(registration=obj_reg, file=obj_file)
    app.mainloop()
