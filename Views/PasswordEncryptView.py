from tkinter import *
from tkinter import simpledialog, messagebox
from tkinter.filedialog import askopenfilenames

class PasswordEncryptView:

    def __init__(self, root, controller):

        self.controller = controller

        self.view_frame = Frame()
        self.listbox_frame = Frame(root, relief='flat', borderwidth=10)
        self.listbox_frame.grid(row=0, column=1, sticky='es')

        self.files_listbox = Listbox(self.listbox_frame, width=100)
        self.files_listbox.pack()

        self.button_frame = Frame(root, relief='flat', borderwidth=10)
        self.button_frame.grid(row=0, column=0, sticky='n')

        self.add_pdf_button = Button(self.button_frame, text='Choose PDFs to encrypt', anchor='n', command=self.choose_files)
        self.add_pdf_button.pack(side=TOP, fill='x')

        self.remove_pdf_button = Button(self.button_frame, text='Remove selected', anchor='n', command=self.remove_files)
        self.remove_pdf_button.pack(side=TOP, fill='x')

        self.password_pdf_button = Button(self.button_frame, text='Password Protect!', anchor='n', command=self.password_protect_files)
        self.password_pdf_button.pack(side=TOP, fill='x')

    def choose_files(self):
        files = askopenfilenames(filetypes=[('PDF Files', '.pdf')])
        self.controller.add_files(files)

    def render_listbox(self, data):
        self.files_listbox.delete(0, END)

        for item in data:
            self.files_listbox.insert(END, item['display_name'])

    def remove_files(self):
        self.controller.remove_files(self.files_listbox.curselection())

    def password_protect_files(self):
        password = self.ask_password()
        if password != None:
            self.controller.password_protect_files(password)

    def ask_password(self):

        password = simpledialog.askstring(title='Password', prompt='Please enter a password:', show="*")
        
        second_password = simpledialog.askstring(title='Confirm Password', prompt='Please confirm password:', show="*")

        if password == second_password:
            return password
        else:
            messagebox.showerror('Error', 'Passwords do not match')
            return None

        