

class contact:
    phone_dictionary = []

    def __init__(self,name,phone):
        self.name = name
        self.number = phone
        contact.phone_dictionary.append(self)

    def display_contact(self):
        return f"Name:\t{self.name}\t Phone Number:\t{self.number}"


    @classmethod
    def display_all_contacts(cls):
        if len(cls.phone_dictionary)==0:
            print('No contact number found in the Directory')
        else:
            print("All contacts from the Directory!! =>")
            for contacts in cls.phone_dictionary:
                print(contacts.display_contact())

    @classmethod
    def search_contact(cls, search_name):
        for contact in cls.phone_dictionary:
            if contact.name.lower() == search_name.lower():
                return contact.number

        return f"No contact found for {search_name}"

    @staticmethod
    def valiadate_phone_number(number):
        if len(number) >= 10 and   number.isdigit():
            return True
        else:
            return False

n_contacts = int(input('Enter number of contacts you want to add:\t'))
for i in range(n_contacts):
    name = input('Enter Name:\t')
    phone = input('Enter Phone Number:\t')
    if contact.valiadate_phone_number(phone):
        contact(name,phone)#.phone_dictionary.append(phone)
    else:
        print(f"invalid phone number {name} , phone number should be between 10 and 10 digits")

#
# c1 = contact('RAM',12657565454)
# c2 = contact('aman',3432124243)
# c3 = contact('Krishna',2342097827)
# c4 = contact('mohan',4567654534)
# c5 = contact('say am',1276876544)
# c6 = contact('read',1224354565)
# c7 = contact('hema',1324356787)
# c8 = contact('anshu',9865345676)
# c9 = contact('mohan',8765456787)
# c10 = contact('gopal',9867865456)
# c11 = contact('radhika',9876543456)
# c12 = contact('roopa',3456788987)
# c13 = contact('aditya',6787656567)
# c14 = contact('suryanshu',8765678765)
# c15 = contact('gopal',6545354657)
# c16 = contact('maya',4342125434)
# c17 = contact('mahak',1324122423)
# c18 = contact('himani',2323234323)
# c19 = contact('mohni',7586425310)
# c20 = contact('divyanshu',4050607080)
# c21 = contact('Dipanshu',2010203040)
# c22 = contact('manan',1205487877)
# c23 = contact('vivek',7845794615)
# c24 = contact('kamal',1293847566)
# c25 = contact('raman',1029382828)
# c26 = contact('chetan',2345409687)
# c27 = contact('mohit',1324354656)
# c28 = contact('sohit',1029384758)
# c29 = contact('cherry',6574839201)
# c30 = contact('subham',1029384757)
# c31 = contact('bhawna',1029384756)
# c32 = contact('rohit',1224354657)
# c33 = contact('dipanshu',3428374536)
# c34 = contact('merry',2354393484)
# c35 = contact('komal',2989019828)
#   contact.display_all_contacts()
# # alaways check your code if you are wright but also one time check your code
# print(contact.search_contact("komal"))
# print(contact.search_contact("MOHAN"))
# print(contact.search_contact("madanmohn"))
#
# contact.display_all_contacts()
print(contact.display_all_contacts)
print("======================================")
contact.display_all_contacts()
print("======================================")
