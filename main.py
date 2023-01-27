# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

from simple_salesforce import Salesforce, SalesforceLogin
import json

import requests
# import pandas as pd
from io import StringIO

info = json.load(open('userlogin.json'))

username = info['username']
password = info['password']
security_token = info['security_token']

domain = 'login'


#     OPTION 1 CONNECT TO SALESFORCE WITH PYTHON USING SIMPLE_SALESFORCE MODULE

class SalesforceConnectors:
    def __init__(self, username, password, security_token, domain=domain):
        # self.sf = None
        self.username = username
        self.password = password
        self.security_token = security_token

        self.sf = Salesforce(self.username, password, security_token)
        # print(self.sf)
        metadata_org = self.sf.describe()

        print(metadata_org.keys()) #odict_keys(['encoding', 'maxBatchSize', 'sobjects'])
        # print(metadata_org['encoding'])
        # print(metadata_org['maxBatchSize'])
        print(metadata_org['sobjects'])


        # session_id, instance = SalesforceLogin(self, username, password, security_token, domain=domain)
        # sfx = Salesforce(instance_url=instance, session_id=session_id)
        # print(sfx)

    def get_account(self):
        # Now you can make API calls, for example:
        sql = "SELECT Id, Name FROM Account LIMIT 10"
        accounts = self.sf.query(sql)
        # print("Simple_Saleforce module print salesforce account details")
        # dir(self.sf)

        # for account in accounts:
        #     print(account)

        return accounts

    def create_contact(self):
        # Now you can make API calls, for example:
        sql = {'LastName': 'Smith', 'Email': "smith@email.com"}
        contact = self.sf.Contact.create(sql)
        print("contact created")
        print(contact)
        return contact

    def get_contact(self, contact_obj):
        # Now you can make API calls, for example:
        contact = self.sf.Contact.get(f'{contact_obj}')
        print(contact)
        return contact

    def get_custom_contact(self, custom_obj, num):
        contact = self.sf.Contact.get_by_custom_id(custom_obj=custom_obj, num=num)
        print(contact)
        return contact

    def update_contact(self):
        contact = self.sf.Contact.update('003e0000003GuNXAA0', {'LastName': 'Jones', 'FirstName': 'John'})
        return contact

    def delete_contact(self):
        contact = self.sf.Contact.delete('003e0000003GuNXAA0')
        return contact


#     OPTION 2 CONNECT TO SALESFORCE WITH PYTHON USING BEATBOX MODULE


# from beatbox import PythonClient
# from beatbox import PythonClient
#
#
# class BeatboxConnector:
#     def __int__(self, username, password, security_token):
#         self.username = username
#         self.password = password
#         self.security_token = security_token
#
#         # Connect to Salesforce
#         self.sf = PythonClient()
#         self.ctn = self.sf.login(username=username, password=password, security_token=security_token)
#         # self.sf = Salesforce(username=username, password=password, security_token=security_toke)
#
#     # Now you can make API calls, for example:
#     def account_query(self):
#         sql = "SELECT Id, Name FROM Account LIMIT 10"
#         result = self.sf.query(sql)
#
#         print("Beatbox print salesforce account details")
#         print(result)


# MAIN PROGRAM METHOD CALL
def main():
    # Use a breakpoint in the code line below to debug your script
    sim = SalesforceConnectors(username=username, password=password, security_token=security_token)
    sim.get_account()
    # sim.create_contact()
    # sim.get_contact(0038c00003A8c9EAAR)
    # sim.update_contact()
    # sim.delete_contact()

    # API CALL BY BEATBOX
    # bt = BeatboxConnector(username=username, password=password, security_token=security_token)
    # bt.account_query()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
