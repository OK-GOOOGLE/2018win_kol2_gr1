#Banking simulator. Write a code in python that simulates the banking system. 
#The program should:
# - be able to create new banks
# - store client information in banks
# - allow for cash input and withdrawal
# - allow for money transfer from client to client
#If you can thing of any other features, you can add them.
#This code shoud be runnable with 'python kol1.py'.
#You don't need to use user input, just show me in the script that the structure of your code works.
#If you have spare time you can implement: Command Line Interface, some kind of data storage, or even multiprocessing.
#Do your best, show off with good, clean, well structured code - this is more important than number of features.
#After you finish, be sure to UPLOAD this (add, commit, push) to the remote repository.
#Make intelligent use of pythons syntactic sugar (overloading, iterators, generators, etc)
#Most of all: CREATE GOOD, RELIABLE, READABLE CODE.
#The goal of this task is for you to SHOW YOUR BEST python programming skills.
#Impress everyone with your skills, show off with your code.
#
#Your program must be runnable with command "python task.py".
#Show some usecases of your library in the code (print some things)
#Good Luck


class Bank:
    def __init__(self, *args):
        self.bank_Name = args[0]
        self.clients = {}

    def add_client(self, client_name, amount):
    	if client_name in self.clients.keys:
    		print("There is already a client with sach name.")
    		return
        self.clients.setdefault(client_name, amount)

    def transfer(self, sender, recipient, recipient_bank, amount):
        self.clients[sender] -= amount
        recipient_bank.clients[sender] += amount

    def remove_client(self, client_name):
    	if client_name in self.clients.keys:
	    	del self.clients[client_name]

	def __str__(self):
		result = "Bank Name: {}. \n Clients: \n".format(self.bank_Name)
		return result

		


bank1 = Bank("bank1")
bank2 = Bank("bank2")

bank1.add_client("client1", 200)


print(bank1)


