import os

class PasswordEncryptModel:

    def __init__(self, view):
        self.data = []
        self.view = view

    def add_file(self, file_path):
        
        new_item = {
            'display_name': os.path.splitext(file_path)[0],
            'file_path': file_path
        }
        
        self.data.append(new_item)
        self.view.render_listbox(self.data)

    def remove_files(self, file_idxs):
        for i in file_idxs:
            self.data.pop(i)

        self.view.render_listbox(self.data)

    def get_files_for_processing(self):
        return [d['file_path'] for d in self.data]

    def remove_all_files(self):
        self.data = []
        self.view.render_listbox(self.data)
    