from pymongo import MongoClient
from bson.objectid import ObjectId


class AnimalShelter(object):
    """ CRUD operations for Animal collection in MongoDB """
    def __init__(self, USER, PASS):

        # Hard-coded database details - Edit these values where appropriate
        #     Host and port number are needed to connect with anything on the internet. For common types of traffic, such as loading a web page, the port numbers are standardized. For our application, you will need to verify the port your host is running on.
        HOST = 'nv-desktop-services.apporto.com'
        PORT = 32760
        DB = 'AAC'# The name of the database you are connecting to
        COL = 'animals'# The name of the collection you will be working with
        try:
            # Initialize Connection
            self.client = MongoClient('mongodb://%s:%s@%s:%d' % (USER, PASS, HOST, PORT)) # connect to the host
            self.database = self.client['%s' % (DB)] # Select the database
            self.collection = self.database['%s' % (COL)] # Select the collection.
        
            # Check connection
            self.database.animals.find_one()
        except Exception:
            print("Invalid server or login credentials provided.")

    # This method implements the C in CRUD: CREATE
    #    data_kv_json should be dictionary
    #    Returns a bool: True if the data was successfuly inserted
    def create(self, data_kv_json):
        if data_kv_json is not None:  # If the data exists
            try:
                return self.database.animals.insert_one(data_kv_json).acknowledged# insert the data and return a confirmation
            except Exception:# This happens when there are two duplicate documents
                print("Attempted to create duplicate document. Skipping...")
                return False
        else: # else there's a problem'
            raise Exception("CREATE ERROR: Nothing to create, because data_kv_json parameter is empty")

    # This method implements the R in CRUD: READ
    #    search_key_value should be dictionary
    #    Returns a python list of python dictionaries
    #        Each dictionary in the list is a document
    def read(self, search_key_value):
        if search_key_value is not None:  # if there was a search parameter provided
            # To return a cursor instead of a list:
            # return self.database.animals.find(search_key_value)

            # To return a list instead of a cursor:
            return [doc for doc in self.database.animals.find(search_key_value)]
        else:# else there was a problem
            raise Exception("READ ERROR: Nothing to read, because search_key_value parameter is empty")

    # This method implements the U in CRUD: UPDATE
    #    search_key_value should be dictionary
    #    data_kv_json should be dictionary
    #        The function is additive; if the dictionary contains fields which exist in the document, it updates; else it inserts. It does not remove.
    #    returns the number of documents which were modified (update_one should only return 0 or 1)
    def update_one(self, search_key_value, data_kv_json):
        if (search_key_value is not None) and (data_kv_json is not None):  # if there is both a search value AND a data provided
            return self.database.animals.update_one(search_key_value,{"$set": data_kv_json}).modified_count # update the document and return the number of documents updated
        else: # else there was a provlem
            if (search_key_value is None) and (data_kv_json is not None):
                raise Exception("UPDATE ERROR: Nothing to update, because search_key_value parameter is empty")
            elif (search_key_value is not None) and (data_kv_json is None):
                raise Exception("UPDATE ERROR: Nothing to update, because data_kv_json parameter is empty")
            else:
                raise Exception("UPDATE ERROR: Nothing to update, because search_key_value and data_kv_json parameter are empty")

    # This method implements the U in CRUD: UPDATE
    #    search_key_value should be dictionary
    #    data_kv_json should be dictionary
    #        The function is additive; if the dictionary contains fields which exist in the document, it updates; else it inserts. It does not remove.
    #    returns the number of documents which were modified
    def update_many(self, search_key_value, data_kv_json):
        if (search_key_value is not None) and (data_kv_json is not None):  # if there is both a search parameter AND data provided
            return self.database.animals.update_many(search_key_value,{"$set": data_kv_json}).modified_count # Modify the documents and return the number of documents which were modified
        else: # Else there was a problem
            if (search_key_value is None) and (data_kv_json is not None):
                raise Exception("UPDATE ERROR: Nothing to update, because search_key_value parameter is empty")
            elif (search_key_value is not None) and (data_kv_json is None):
                raise Exception("UPDATE ERROR: Nothing to update, because data_kv_json parameter is empty")
            else:
                raise Exception("UPDATE ERROR: Nothing to update, because search_key_value and data_kv_json parameter are empty")

    # This method implements the D in CRUD: DELETE
    #    search_key_value should be dictionary
    #    returns the number of documents which were deleted (delete_one should only return 0 or 1)
    def delete_one(self, search_key_value):
        if search_key_value is not None:  # if a search parameter was provided
            return self.database.animals.delete_one(search_key_value).deleted_count # Delete the document, if there, and return the number of documents deleted
        else:# Else there was a problem
            raise Exception("DELETE ERROR: Nothing to delete, because search_key_value parameter is empty")

    # This method implements the D in CRUD: DELETE
    #    search_key_value should be dictionary
    #    returns the number of documents which were deleted
    def delete_many(self, search_key_value):
        if search_key_value is not None:  # if there was a search value provided
            return self.database.animals.delete_many(search_key_value).deleted_count # Delete the files and return the number of files deleted
        else: # Else there was a problem
            raise Exception("DELETE ERROR: Nothing to delete, because search_key_value parameter is empty")

