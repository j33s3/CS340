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
			raise Exception("Nothing to save, because data paramter is empty")
	
	#Create method to implement the R in CRUD
	def read(self, query):
		if query is not None:
			cursor = self.collection.find(query)
			return list(cursor)
		else:
			raise Exception("Query parameter is empty")
			return[]
