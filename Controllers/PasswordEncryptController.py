from Views.PasswordEncryptView import PasswordEncryptView
from Models.PasswordEncryptModel import PasswordEncryptModel

import os

import pikepdf
from pikepdf import Pdf
from pikepdf import _cpphelpers # required for packaging app

class PasswordEncryptController:

    def __init__(self, root):
        self.view = PasswordEncryptView(root, self)
        self.model = PasswordEncryptModel(self.view)

    def add_files(self, file_paths):
        for f in file_paths:
            self.model.add_file(f)

    def remove_files(self, files):
        self.model.remove_files(files)

    def password_protect_files(self, password):
        for file_name in self.model.get_files_for_processing():
            pdf = Pdf.open(file_name)
            pdf.save(os.path.splitext(file_name)[0] + '_pw.pdf', encryption=pikepdf.Encryption(owner=password, user=password, R=4))
            pdf.close()
        self.model.remove_all_files()
