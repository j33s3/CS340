from pymongo import MongoClient
from pymongo.errors import PyMongoError
from bson.objectid import ObjectId

class AnimalShelter(object):
	""" CRUD operations for Animal collection in MongoDB"""
	def __init__(self, user, pwd):
		#Initializing the MongoClient. This helps to
		#access the MonogDB databases and collections.
		#This is hard-wired to use the aac databse, the
		#animals collection, and the aac user
		#Definitions of the connection string variables are
		#unique to the individial Apporto environment
		#
		#you must edit the connection variables below to reflect
		#your own instance of MongoDB
		#
		#Connection variables
		#
		HOST = 'nv-desktop-services.apporto.com'
		PORT = 30884
		DB = 'AAC'
		COL = 'animals'
		#
		# Initialize Connection
		self.client = MongoClient('mongodb://%s:%s@%s:%d' % (user, pwd, HOST, PORT))
		self.database = self.client['%s' % (DB)]
		self.collection = self.database['%s' % (COL)]
		
	# Complete this create method to implement the C for CRUD
	def create(self, data):
		if data is not None:
			self.database.animals.insert_one(data) # data should be dictionary
			return True
		else:
			return False
	
	#Create method to implement the R in CRUD
	def read(self, query):
		if query is not None:
			cursor = self.collection.find(query)
			return list(cursor)
		else:
			raise Exception("Query parameter is empty")
			return[]
	
	# Create method to implement the U in CRUD	
	def update(self, query_filter, update_data, update_many=False):
		if query_filter is not None and update_data is not None: 
			if update_many:
				result = self.collection.update_many(query_filter, {'$set': update_data}) #Update Many
			else: 
				result = self.collection.update_one(query_filter, {'$set': update_data}) #Update One
	
			return result.modified_count
		else:
			raise Exception('Query filter or update data parameter empty')
	
	# Create method to implement the D in CRUD		
	def delete(self, query_filter, delete_many=False):
		if query_filter is not None:
				if delete_many:
					result = self.collection.delete_many(query_filter) #Delete Many
				else:
					result = self.collection.delete_one(query_filter) #Delete One
				return result.deleted_count
		else:
			raise Exception('Query filter parameter empty')
