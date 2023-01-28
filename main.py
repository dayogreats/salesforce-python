# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

from simple_salesforce import Salesforce, SalesforceLogin
import json
import pandas as pd

info = json.load(open('userlogin.json'))

username = info['username']
password = info['password']
security_token = info['security_token']
domain = 'login'


#     OPTION 1 CONNECT TO SALESFORCE WITH PYTHON USING SIMPLE_SALESFORCE MODULE

class SalesforceConnectors:
    def __init__(self, username, password, security_token, domain=domain):
        self.username = username
        self.password = password
        self.security_token = security_token

        self.sf = Salesforce(self.username, password, security_token)
        # print(self.sf)
        metadata_org = self.sf.describe()

        # print(metadata_org.keys()) # odict_keys(['encoding', 'maxBatchSize', 'sobjects'])
        # print(metadata_org['encoding'])
        # print(metadata_org['maxBatchSize'])
        # print(metadata_org['sobjects'])
        df_sobjects = pd.DataFrame(metadata_org['sobjects'])
        # print(df_sobjects)
        df_sobjects.to_csv('metadata info.csv', index=False)

        # session_id, instance = SalesforceLogin(self, username, password, security_token, domain=domain)
        # sfx = Salesforce(instance_url=instance, session_id=session_id)
        # print(sfx)

    def get_account(self):
        # Now you can make API calls, for example:
        sql = "SELECT Id, Name FROM Account LIMIT 10"
        accs = self.sf.query(sql)
        # dir(self.sf)

        # extra data to csv
        account = self.sf.account
        account_metadata = account.describe()

        # load to dataframe
        df_account_metadata = pd.DataFrame(account_metadata.get('fields'))
        df_account_metadata.to_csv('account object field metada.csv', index=False)

        return accs

    def create_contact(self, lastname, email):
        # Now you can make API calls, for example:
        sql = {'LastName': lastname, 'Email': email}
        # sql = {'LastName': 'barry', 'Email': "brarry@email.com"}
        contact = self.sf.Contact.create(sql)
        print(contact)
        contact_id = contact.get('id')  # method 1
        # contact_id = contact['id']  # method 2
        print(f'Contact ID: {contact_id} was created')

        return contact_id

    def get_all_contacts(self):
        sql = "SELECT Id, Name, Email, Account.Id FROM Contact"
        contacts = self.sf.query(sql)
        print(contacts)
        print("All contacts  printed")
        return contacts

    def get_one_contact_id(self, id):
        one_contact = self.sf.Contact.get(f'{id}')
        print(one_contact['Id'])
        print(f"{one_contact['Id']}  contact with id returned ")
        return one_contact['Id']

    def get_custom_contact(self, custom_obj, num):
        contact = self.sf.Contact.get_by_custom_id(custom_obj=custom_obj, num=num)
        print(contact)
        return contact

    def update_contact(self, id, lastname, firstname):
        contact = self.sf.Contact.update(f'{id}', {'LastName': f'{lastname}', 'FirstName': f'{firstname}'})
        # 0038c00002lEzgsAAC
        return contact

    def delete_contact(self, id):
        contact = self.sf.Contact.delete(f'{id}')
        # 0038c00002lEzgsAAC
        return contact


# MAIN PROGRAM METHOD CALL
def main():
    # Use a breakpoint in the code line below to debug your script
    sim = SalesforceConnectors(username=username, password=password, security_token=security_token)
    sim.get_account()
    # sim.create_contact('dora', 'dora@gmail.com')
    sim.get_all_contacts()
    sim.get_one_contact_id('0038c00002lEzgsAAC')
    # sim.update_contact()
    # sim.delete_contact()

    # API CALL BY BEATBOX
    # bt = BeatboxConnector(username=username, password=password, security_token=security_token)
    # bt.account_query()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
