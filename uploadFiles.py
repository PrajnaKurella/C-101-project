#import dropbox, os
import dropbox
import os 
from dropbox.files import WriteMode

class TransferData:
    #initalize dropbox
    def __init__(self, access_token):
        self.access_token = access_token

    def upload_file(self, file_from, file_to):
        dbx = dropbox.Dropbox(self.access_token)
    #getting filename and then setting its path
        for root, dirs, files in os.walk(file_from):
            for fileName in files:
                local_path = os.path.join(root, fileName)

                relative_path = os.path.relpath(local_path, file_from)
                dropbox_path = os.path.join(file_to, relative_path)
                #using write mode
                with open(local_path, 'rb') as file: #file is just the var name 
                    dbx.files_upload(file.read(), dropbox_path, mode = WriteMode('overwrite'))
                    
def main(): #whatever you want to be executed on the user side 
    access_token = 'sl.BVprVmjerg-220ZIjMQ-6fuRqEz9ZIZKUmJ5eta-alqW4WRhJEAWY-R-uxbI4XQCLHJk5qGDYYq8gx2jkLV_DpJVkbl3ojSJpvKxIl6gVU4gsmqEwKv7nyzxakDTfnFNoIO5Ya8'
    transferData = TransferData(access_token)

    file_from = input("Enter the file path to transfer: ")
    file_to = input("enter the full path to upload to dropbox: ")  

    transferData.upload_file(file_from, file_to)
    print("file moved.")

main()