import os

from pymongo import MongoClient
class DatabaseOperations:

    database = collection = client = ''

    # Connection to the local MongoDB
    def db_connect(self):

        try:

            # Database connection string
            self.client = MongoClient('localhost', 27017)

            # Change the DATABASE and COLLECTION name accordingly
            self.database = self.client.Test_DB                              # Database Name: Test_DB

            self.collection = self.database.Test                        # Collection Name: Test

            print('Database Connection Successful')

        except Exception as ex:

            print('Error: {}.\nCannot connect to database.'.format(ex))

    # To close the database connection
    def db_close(self):

        self.client.close()                                         # Closes the database connection

    # To create database/collection and insert data into it
    def db_filepaths(self, inputvalue):

        arr = os.listdir(inputvalue)

        return arr
    def db_insert(self, insert_str, file_name):

        # Convert data to JSON format to insert into database/collection
        insert_data = {'file name': file_name,
                       'file content': insert_str}

        record_id = self.collection.insert_one(insert_data)

        return record_id

    # Convert the content of fle into a single string to store in MongoDB
    @staticmethod
    def file_content(file_path):

        con_str = ''                                             # String variable to store data that is to be inserted

        file_name = r'{}'.format(file_path).replace('\\', '/').split('/').pop()     # To extract the file name

        file_read = open(file_path, 'r')

        for lines in file_read:

            con_str += lines

        return con_str, file_name                           # Returns the concatenated string & the extracted file name

    # Retrieve all records from the database/collection
    def read_all_rec(self):

        return self.collection.find({})

    # Retrieve record from the database/collection by file name
    def read_by_field(self, file_name):

        db_record = self.collection.find({'file name': file_name})          # Extracts the required row from database

        for data_dict in db_record:                                         # Converts the extracted row to dictionary

            return data_dict['file content'].split('\n')                    # Returns the 'file content' string as list
