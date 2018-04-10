
# NOTE !! you need to clear data.dat file after each program run.
# Otherwise, it will try to add already existing client and will throw an exception.
# but program can correctly read json files with respective structure. Start_session() is responsible for that.

import json
from collections import defaultdict
from os import stat
banks = defaultdict(dict)


# read data from file and keep it in dictionary Banks
def session_start():
    global banks
    with open("data.dat", "r") as file:
        if stat("data.dat").st_size < 2:
            banks = {}
            return
        banks = json.load(file)
        file.close()


def session_finish():
    global banks
    with open("data.dat", "w") as file:
        json.dump(banks, file, indent=3)
        file.close()


# (string, ((), (), (), ..) ) -- tuple of tuples: ("client", sum)
def add_bank(name, *clients_and_sums):
    global banks
    if name in banks.keys():
        raise Exception(f'''a bank with "{name}" name already exists''')
    # for i,k in clients_and_sums:
    #     print(i, k)

    banks[name] = {i: k for i, k in clients_and_sums}


# (string, string, int)
def add_client(bank, client, amount):
    global banks
    if client in banks[bank].keys():
        raise Exception(f'''a "{client}" is already a client of the "{client}" bank''')
    banks[bank][client] = amount


#           (string, string,      string,    string,         int   )
def transfer(payer, payer_bank, payee, payee_bank, amount):
    global banks

    if payer_bank not in banks.keys() or payer not in banks[payer_bank].keys():
        print("There is no such bank or payer in the database. Interrupting transaction.")
        return
    if payee_bank not in banks.keys() or payee not in banks[payee_bank].keys():
        print("There is no such bank or payee in the database. Interrupting transaction.")
        return
    if banks[payer_bank][payer] < amount:
        print("no funds available. Interrupting transaction.")
        return

    provision = 1
    if payer_bank != payee_bank:
        provision = 0.95
    banks[payer_bank][payer] -= amount
    banks[payee_bank][payee] += amount * provision


# (string, string)
def remove_client(bank, client):
    global banks
    if client not in banks[bank].keys():
        print("can not find such a client")
        return

    del banks[bank][client]


# (string, string, int)
def income_payment(bank, client, sum):
    if bank not in banks.keys() or client not in banks[bank].keys():
        print("There is no such bank or client in the database. Interrupting transaction.")
        return
    banks[bank][client] += sum


# (string, string, int)
def cashing(bank, client, sum):
    if bank not in banks.keys() or client not in banks[bank].keys():
        print("There is no such bank or client in the database. Interrupting transaction.")
        return
    if banks[bank][client] < sum:
        print("No funds available. Interrupting transaction.")
        return

    banks[bank][client] -= sum


print(banks)
session_start()
# banks = {} #############

add_bank("bank1", ("client1", 100), ("client2", 100))
add_bank("bank2", ("client1", 200), ("client2", 200))
add_bank("bank3", ("client1", 300), ("client2", 300))

add_client("bank1", "client3", 100)

transfer("client1", "bank2", "client2", "bank1", 100)
remove_client("bank3", "client2")
income_payment("bank3", "client1", 50)
cashing("bank3", "client1", 30)
print(banks)

session_finish()
