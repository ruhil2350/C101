import os
import dropbox
from dropbox.files import WriteMode

Class TransferData:
      def __init__(self, access_token):
        self.access_token = access_token

      def upload_file(self,file_fome, file_to):
        dbx = dropbox.Dropbox(self.access_token)

        for root, dirs, files in os.walk(file_from):
          local_path = os.path.join(root, filename)

          relative_path = os.path.relpath(local_path, file_from)
          dropbox_path = os.path.join(file_to, relative_path)

          with open(local_path, 'rb') as f:
            dbx.files_upload(f.read(), dropbox_path, mode=WriteMode('overwrite'))

def main():
      access_token = ''
      transferData = TransferData(access_token)

      file_from = str(input("Enter The file Path to Transfer :- " ))
      file_to = input("Enter the full path to upload :-")

      transferData.upload_file(file_from, file_to)
      print("file has been successfully moved !!")

main()