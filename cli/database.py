import pickle
from pathlib import Path
class Database:
    def __init__(self):
         self.file_path = Path(__file__).resolve().parent / "students.data"

         if not self.file_path.exists():
                           self.file_path.touch()

    def save_to_file(self, students): # other team members can call Db.save_to_file(students)   
         with open(self.file_path, "wb") as file: #wb=write binary
          pickle.dump(students, file) 

    def read_from_file(self):
        try:
           with open(self.file_path, "rb") as file: #rb=read binary
                  students = pickle.load (file)
           return students
        except EOFError: #handle empty file
           return[]
    def update_file(self, students):
          self.save_to_file(students)
    def delete_from_file(self):
          self.save_to_file([])
         


    