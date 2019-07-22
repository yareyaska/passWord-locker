import unittest
from locker import Password

class Testlocker(unittest.TestCase):
	"""docstring for ClassName"""
	def setUp(self):
	      	self.new_person = Password("yu","234")
#testing for user name and password
	def test_init(self):
	     	self.assertEqual(self.new_person.username,"yu")
	     	self.assertEqual(self.new_person.Password,"234")
#testing for save 
	def test_savePassword(self): 
	         self.new_person.savePassword()   
	         self.assertEqual(len(Password.my_list),1) 	
	         #testing for delete
	def test_deletePassword(self): 
	        self.new_person.savePassword()
	        self.new_person.deletePassword()
	        self.assertEqual(len(Password.my_list),0)

if __name__ == '__main__':
			unittest.main()	