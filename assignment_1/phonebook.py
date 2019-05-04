from linkedlist import SingleLinkedList
from node import Node
"""
CSCA48 Assignment 1, Summer 2018
I acknowledge that I am aware of University policy on academic integrity as
contained in https://www.utsc.utoronto.ca/aacc/academic-integrity and of the
disciplinary procedures applicable to breaches of such policy as contained
in thttp://academicintegrity.utoronto.ca/key-consequences.

I hereby declare that the code presented here is solely my work and that I
have not received any external help from my peers, nor have I used any
resources not directly supplied by the course in order to complete this
assignment. I have not looked at anyone else's solution, and no one has
looked at mine. I understand that by adding my name to this file, I am
making a formal declaration, and any subsequent discovery of plagiarism
or other academic misconduct could result in a charge of perjury in
addition to other charges under the academic code of conduct of the
University of Toronto Scarborough Campus
Name: Yu-Hsiang, Mou
UtorID: mouyuhsi
Student Number: 1004334669
Date: June 20, 2018
"""


class MissingPhoneNumberException(Exception):
    pass


class MissingNameException(Exception):
    pass


class Contact():
    ''' This class defines a Contact with parameters cp(cell phone), name,
    surname, hp(home phone), wp(work phone), email, ha(home address), and
    fav(favorite or not). Exceptions are raised when the phone number is
    missing (neither kind of phone numbers are provided) or the name is
    missing (first name and last name are not provided).
    '''
    def __init__(self, cp=None, name=None, surname=None, hp=None, wp=None,
                 email=None, ha=None, fav=False):
        '''(Contact, str, str, str, str, str, str, str, bool) -> NoneType
        initializes the attributes of a contact
        REQ: cp/hp/wp has the format "xxx-xxx-xxxx" where x is any single digit
        REQ: name and surname cannot both be None (provide at least one)
        REQ: cp, hp, and wp cannot all be None (require at least one)
        '''
        # Representation Invariant (RI)
        # Contact always has a name and a phone number
        self._cp = cp
        self._name = name
        self._surname = surname
        self._hp = hp
        self._wp = wp
        self._email = email
        self._ha = ha
        self._fav = fav
        # automatically check the required input of the contact upon creating
        self.check_info()

    def check_info(self):
        ''' (Contact) -> NoneType
        raises an exception when no phone number is provided or no name is
        provided (depend on the case)
        '''
        # check by calling the two relevant getter methods
        if self.get_primary_number() is None:
            raise MissingPhoneNumberException

        if self.get_name() is None:
            raise MissingPhoneNumberException

    def get_actual_name(self):
        ''' (Contact) -> str
        returns contact's surname as default, returns name(first name)
        as an alternative when surname is not provided (None if missing both)
        >>> Joanna = Contact('516-765-4393', 'Joanna', 'P', None,\
        '130-201-1943', None, 'ZZ')
        >>> Joanna.get_actual_name()
        'P'
        >>> Gordon = Contact(None, 'GorDoN', None, '242-100-4432', None,\
        None, 'ST')
        >>> Gordon.get_actual_name()
        'GorDoN'
        '''
        # Initiate a variable to store name
        name = None

        # when surname is not provided, the name refers to first name
        if self._surname is None:
            name = self._name

        # otherwise returns surname
        else:
            name = self._surname

        return name

    def get_name(self):
        ''' (Contact) -> str
        returns contact's surname as default, returns name(first name)
        as an alternative when surname is not provided (None if missing both)
        [note: names will be in uppercase]
        >>> Jacqueline = Contact('416-887-7784', 'Jacqueline', 'K', None,\
        '130-201-1943', None, 'SW', True)
        >>> Jacqueline.get_name()
        'K'
        >>> Irene = Contact(None, 'Irene', None, '141-644-711', '122-345-556',\
        None, 'DW', True)
        >>> Irene.get_name()
        'IRENE'
        '''
        # Initiate a variable to store name
        name = None

        # (convert the name into uppercase for comparison purpose)
        # when surname is not provided, the name refers to first name
        if self._surname is None:
            name = self._name.upper()

        # otherwise returns surname (None will remain None if not provided)
        else:
            name = self._surname.upper()

        return name

    def get_list(self):
        ''' (Contact) -> list
        Return a list containing all the contact information 'in order'
        >>> Annie = Contact(None, None, 'Annie', '666-123-1234',\
        '111-222-3333', None, 'A', False)
        >>> Annie.get_list()
        [None, None, 'Annie', '666-123-1234', '111-222-3333', None, 'A', False]
        '''
        return [self._cp, self._name, self._surname, self._hp, self._wp,
                self._email, self._ha, self._fav]

    def get_primary_number(self):
        ''' (Contact) -> str
        Return the primary phone number (which is determined by the order
        cp -> hp -> wp; None is returned if all are missing)
        >>> jessica = Contact(None, 'Jessica', 'C', None, '999-999-9999',\
        None, None, True)
        >>> jessica.get_primary_number()
        '999-999-9999'
        >>> Stephen = Contact('123-456-7890', 'Stephen', 'C', '131-313-1313',\
        '989-387-1763', None, None, True)
        >>> Stephen.get_primary_number()
        '123-456-7890'
        '''
        # Initiate a variable to store phone number
        phone = None

        # check each phone number in order, return the first 'not None' phone
        # number or if not, returns None
        if self._cp is not None:
            phone = self._cp

        elif self._hp is not None:
            phone = self._hp

        elif self._wp is not None:
            phone = self._wp

        return phone

    def merge(self, contact):
        ''' (Contact, Contact) -> NoneType
        Given a contact, merge it with self (update self)
        (uses mainly for contacts that are 'equal')
        >>> Amy = Contact(None, 'Amy', 'T', '416-664-4664', '789-396-1111',\
        None, 'FH', True)
        >>> amy = Contact(None, 'Amy', 'T', '416-664-4664', '609-128-4622',\
        None, 'FH', False)
        >>> Amy.merge(amy)
        >>> print(Amy)
        None, 'Amy', 'T', '416-664-4664', '609-128-4622', None, 'FH', False
        '''
        # update all the info (same thing would be updated to the same thing)
        self._cp = contact.get_cp()
        self._hp = contact.get_hp()
        self._wp = contact.get_wp()
        self._email = contact.get_email()
        self._ha = contact.get_ha()
        self._fav = contact.get_fav()

    def get_cp(self):
        ''' (Contact) -> str
        returns the cell phone number
        >>> David = Contact('222-222-2213', 'David')
        >>> David.get_cp()
        '222-222-2213'
        '''
        return self._cp

    def get_hp(self):
        ''' (Contact) -> str
        returns the home phone number
        >>> Samuel = Contact(None, 'Samuel', None, '901-020-3001')
        >>> Samuel.get_hp()
        '901-020-3001'
        '''
        return self._hp

    def get_wp(self):
        ''' (Contact) -> str
        returns the work phone number
        >>> Nancy = Contact(None, 'Nancy', None, None, '389-123-0000')
        >>> Nancy.get_wp()
        '389-123-0000'
        '''
        return self._wp

    def get_email(self):
        ''' (Contact) -> str
        returns the email address
        >>> Alex = Contact('533-216-3809', 'Alex', None, None, None,\
        'alex@cs.ca')
        >>> Alex.get_email()
        'alex@cs.ca'
        '''
        return self._email

    def get_ha(self):
        ''' (Contact) -> str
        returns the home address
        >>> Brian = Contact('000-584-0027', 'Brian', None, None, None, None,\
        'ABCDEFGHIJKLMOUPQRSTNVWXYZ')
        >>> Brian.get_ha()
        'ABCDEFGHIJKLMOUPQRSTNVWXYZ'
        '''
        return self._ha

    def get_fav(self):
        ''' (Contact) -> bool
        returns a boolean indicating whether it has been marked as favorite or
        not
        >>> Jeffrey = Contact('000-001-0002', 'Jeffrey', None, None, None,\
        None, None, False)
        >>> Jeffrey.get_fav()
        False
        '''
        return self._fav

    def get_primary_type(self):
        ''' (Contact) -> str
        returns a string indicating the type of the primary phone number
        >>> Matthew = Contact( None, 'Matthew', 'Ga', None, '555-199-4977',\
        None, None, False)
        >>> Matthew.get_primary_type()
        'wp'
        '''
        # initiate a variable to store the type
        type = None
        # get the primary phone number
        number = self.get_primary_number()
        # check the 'type' of the number and assign the corresponding string
        if number is not None:
            if number == self._cp:
                type = 'cp'

            elif number == self._hp:
                type = 'hp'

            elif number == self._wp:
                type = 'wp'

        return type

    def __eq__(self, other):
        ''' (Contact, Contact) -> bool
        two contacts are equal if and only if their names are equal and their
        primary phone number are equal (in terms of type and value)
        >>> Isaac = Contact('299-792-4580', 'Isaac', 'Mou', None, None,\
        'csca48@utsc.ca', 'TW', True)
        >>> Smart = Contact('299-792-4580', 'Isaac', 'Mou')
        >>> Isaac == Smart
        True
        '''
        # check the type and value of the names and also primary phone numbers
        if (self.get_list()[1:3] == other.get_list()[1:3] and
                self.get_primary_number() == other.get_primary_number() and
                self.get_primary_type() == self.get_primary_type()):
            # True if and only if the above are simultaneously true
            return True

    def __str__(self):
        ''' (Contact) -> str
        returns a string representation of all the informations of the contact
        in order (separated by comma)
        >>> nana = Contact(None, 'I', 'Love', '100-100-0100', None,\
        'compsci@cms.ca', 'IC', True)
        >>> print(nana)
        None, 'I', 'Love', '100-100-0100', None, 'compsci@cms.ca', 'IC', True
        '''
        return str(self.get_list())[1:-1]


class PhoneBook(SingleLinkedList):
    ''' This class defines a phonebook which can store 'contacts'
    (with their informations). Two contacts are identified to be the same if
    their names and primary phone numbers are the same.
    '''
    def __init__(self, contact=None):
        '''(PhoneBook, SingleLinkedList) -> NoneType
        initializes the attributes of a phonebook
        '''
        # Representation Invariant (RI)
        # PhoneBook contains contact(s) if it is not empty
        SingleLinkedList.__init__(self)
        # _size is non-negative
        # add the first contact during initialization if provided
        if contact is not None:
            self.add(contact)

    def add(self, contact):
        ''' (PhoneBook, Contact) -> NoneType
        Given contact information, add it to the PhoneBook in alphabetical
        order. (orderd by surname, or alternately with first name when surname
        is not provided) [note: character cases do not affect the order]
        >>> Apple = PhoneBook()
        >>> Apple.add(Contact('164-301-0400', 'Isaac', 'N'))
        >>> print(Apple)
        'N'
        '''
        # initiate a variable to store next node
        Next = None
        # get the first contact from the phonebook
        contacts = self.get_head()

        # add the contact to the beginning of the phonebook for arrangement
        self.add_first(contact)

        # if contacts is not None (meaning: phonebook is not empty)
        # then we have to do comparison and possibly arrange the contact
        if contacts is not None:
            # if the order of the contact is 'lower' (compare with the head)
            if contacts.get_element().get_name() < contact.get_name():
                # get the next node
                Next = contacts.get_next()
                # if the next node is None (only one pre-existing contact)
                if Next is None:
                    # remove the contact from the beginning and add it behind
                    # the head
                    self.remove_first()
                    self.add_last(contact)

            elif contacts.get_element() == contact:
                # merge the two contacts (update the original one)
                contact.merge(contacts.get_element())
                # prevent the next loop
                Next = None

        # when the next node is not None, compare the order and 'arrange' the
        # contact when it has 'higher order' than the next node
        while Next is not None:
            if Next.get_element().get_name() > contact.get_name():
                # retrive the original head
                head = self.get_head().get_next()
                # set the link from contact to the next node
                self.get_head().set_next(Next)
                # set the link from contacts node to contact
                contacts.set_next(self.get_head())
                # reassign the head
                self.set_head(head)
                # stop the loop
                Next = None

            elif Next.get_element() == contact:
                # remove the contact that was added at the beginning
                self.remove_first()
                # merge the two contacts (update the original one)
                contact.merge(Next.get_element())
                # stop the loop
                Next = None

            else:
                # move to the next node of the 'next node'
                Next = Next.get_next()
                # remove the contact from the beginning and add it to the back
                # as it has the 'lowest order' compare to all the contacts
                if Next is None:
                    self.remove_first()
                    self.add_last(contact)

                # move to the next node of 'contacts'
                contacts = contacts.get_next()

    def remove(self, contact):
        ''' (PhoneBook, Contact) -> Contact
        Given contact information, remove it from the PhoneBook and then return
        it. Return None if not found.
        >>> Einstein = Contact('187-903-1400', 'Albert')
        >>> Light = PhoneBook(Einstein)
        >>> Light.add(Contact('184-702-1100', 'Thomas'))
        >>> Light.remove(Einstein).get_actual_name()
        'Albert'
        >>> print(Light)
        'Thomas'
        '''
        # get the first node of the phonebook
        contacts = self.get_head()

        # check the first contact if the phonebook is not empty
        if contacts is not None:
            if contacts.get_element() == contact:
                self.remove_first()
                return contact

            Next = contacts.get_next()
            # loop through the phonebook intending to find the specific contact
            while Next is not None:
                if Next.get_element() == contact:
                    contacts.set_next(Next.get_next())
                    # remove the link (point to None)
                    Next.set_next(None)
                    return contact

                # move both contacts and next forward (to the one after them)
                contacts = Next
                Next = contacts.get_next()

        return None

    def show_fav_list(self):
        ''' (PhoneBook) -> list
        Return a list of names that are marked as favorite contact. (include
        surname only; if surname is not provided, then include first name)
        >>> Friend = PhoneBook()
        >>> Friend.add(Contact('010-101-9534', 'Emily', 'Smith', None, None,\
        None, None, True))
        >>> Friend.add(Contact('777-482-0005', 'Jenny', None, None, None,\
        None, None, False))
        >>> Friend.add(Contact('281-199-9945', 'June', None, None, None, None,\
        None, True))
        >>> Friend.show_fav_list()
        ['June', 'Smith']
        '''
        # initiate an empty list to store the names (the favorites)
        fav_list = []
        # get the first contact
        contacts = self.get_head()
        # loop through the whole phonebook
        while contacts is not None:
            # get the contact info
            element = contacts.get_element()

            # check if it is marked as favorite
            if element.get_fav():
                # add the name to the list
                fav_list.append(element.get_actual_name())

            # move to the next contact
            contacts = contacts.get_next()

        return fav_list

    def toronto_phone(self):
        ''' (PhoneBook) -> tuple
        Return a tuple which contains two phonebooks. The first phonebook has
        all the contacts whose primary phone number starts with 416, and the
        second phonebook has all the contacts whose primary phone number starts
        with 647. (Toronto phone number starts with either 416 or 647)
        >>> secret = PhoneBook()
        >>> secret.add(Contact('416-614-1465', 'Dorothy'))
        >>> secret.add(Contact(None, 'Tim', None, '647-467-7466'))
        >>> secret.add(Contact('000-002-0153', 'Eric'))
        >>> secret.add(Contact(None, 'Anny', None, '647-111-3251'))
        >>> toronto = secret.toronto_phone()
        >>> print(toronto[0])
        'Dorothy'
        >>> print(toronto[1])
        'Anny', 'Tim'
        '''
        # initiate two empty phonebooks
        pb_416 = PhoneBook()
        pb_647 = PhoneBook()
        # get the first node of the phonebook
        contacts = self.get_head()
        # loop through the whole phonebook
        while contacts is not None:
            # get the Contact object from the node
            contact = contacts.get_element()
            # check the length of the primary phone number (need at least 3)
            # (convert them all to string in case it was given as integer)
            if len(str(contact.get_primary_number())) > 2:
                # add the 'Toronto contact' to one of the phonebooks if they
                # start with 416 or 647
                if str(contact.get_primary_number())[:3] == '416':
                    pb_416.add(contact)

                elif str(contact.get_primary_number())[:3] == '647':
                    pb_647.add(contact)

            # move to the next node
            contacts = contacts.get_next()

        return (pb_416, pb_647)

    def reversed_phonebook(self):
        ''' (PhoneBook) -> PhoneBook
        Return a phonebook that has been 'reversed' (contacts are listed in
        descending order).
        >>> team = PhoneBook(Contact('936-676-8887', 'Tom'))
        >>> team.add(Contact('099-123-7439', 'Kevin'))
        >>> team.add(Contact(None, 'Max', None, None, '087-678-3318'))
        >>> team.add(Contact(None, 'Gina', None, '000-101-2018'))
        >>> print(team)
        'Gina', 'Kevin', 'Max', 'Tom'
        >>> TEAM = team.reversed_phonebook()
        >>> print(TEAM)
        'Tom', 'Max', 'Kevin', 'Gina'
        '''
        # create an empty phonebook
        order = PhoneBook()

        # get the first node
        contact = self.get_head()

        # add all the contacts from self to the new phonebook one by one
        # (this will ensure that it is getting sorted alphabetically)
        while contact is not None:
            order.add(contact.get_element())
            # get the next contact
            contact = contact.get_next()

        # lastly reverse the phonebook (it will now be sorted from 'Z to A')
        order.reverse()

        return order

    def reverse(self):
        ''' (PhoneBook) -> None
        reverse the order of self (the phonebook)
        >>> normal = PhoneBook(Contact('385-392-3853', 'Ryan'))
        >>> normal.add(Contact('292-788-7394', 'Simon'))
        >>> normal.add(Contact(None, 'Chandler', None, None, '734-758-7779'))
        >>> normal.add(Contact(None, 'Brady', None, '162-147-2112'))
        >>> print(normal)
        'Brady', 'Chandler', 'Ryan', 'Simon'
        >>> normal.reverse()
        >>> print(normal)
        'Simon', 'Ryan', 'Chandler', 'Brady'
        '''
        # initiate a variable to store next node
        next = None
        # get the first node
        contact = self.get_head()
        # store the tail (will be the new head)
        head = self.get_tail()
        # if the phonebook is not empty
        if contact is not None:
            # get the next node
            next = contact.get_next()
            # point the head to None (will become the tail)
            contact.set_next(None)

        # loop through the whole phonebook
        while next is not None:
            # store the 'previous' node (the next node will point to it)
            prev = contact
            # move the current node to next
            contact = next
            # get the next node
            next = contact.get_next()
            # establish the 'reverse' link
            contact.set_next(prev)

        # set the head after reversing all the links
        self.set_head(head)

    def sync_phonebook(self, phonebook):
        ''' (PhoneBook, PhoneBook) -> PhoneBook
        Given a phonebook, merge the current phonebook with it while preserving
        the alphabetical order. Same contact should not appear twice.
        >>> random = PhoneBook(Contact('395-921-1014', 'Leon', 'D'))
        >>> random.add(Contact('093-574-282', 'Emma', 'B'))
        >>> random.add(Contact(None, 'Justin', 'O', '159-201-5832',\
        '087-678-3318'))
        >>> random.add(Contact(None, 'Rudolph', None, '955-453-4492'))
        >>> print(random)
        'B', 'D', 'O', 'Rudolph'
        >>> fortune = PhoneBook(Contact('111-910-475', 'Taylor'))
        >>> fortune.add(Contact('012-370-1989', 'Emma', 'B', '091-234-1109'))
        >>> fortune.add(Contact('395-921-1014', 'Leon', 'D'))
        >>> fortune.add(Contact('334-141-0036', 'Daniel'))
        >>> fortune.add(Contact(None, 'Robert', None, None, '921-578-8033'))
        >>> fortune.add(Contact(None, 'Paul', 'R', '275-613-0686'))
        >>> random.sync_phonebook(fortune)
        >>> print(random)
        'B', 'B', 'D', 'Daniel', 'O', 'R', 'Robert', 'Rudolph', 'Taylor'
        '''
        # get the first contact of the phonebook (not the current one)
        contact = phonebook.get_head()

        # adding every contact to the current phonebook during the loop
        # (same contact will merged to one)
        while contact is not None:
            contacts = contact.get_element()
            self.add(contacts)
            # move to the next contact
            contact = contact.get_next()

    def group_remove(self, remove_list):
        ''' (PhoneBook, list) -> NoneType
        Given a list of contacts, remove them from the phonebook.
        >>> maria = Contact('755-479-5091', 'Maria')
        >>> lisa = Contact('950-883-912', 'Lisa', 'V', '615-452-7730')
        >>> patrick = Contact(None, 'Patrick', None, None, '326-339-2244')
        >>> richard = Contact('080-033-566', 'Richard', 'P', '134-213-3216')
        >>> james = Contact('518-222-842', 'James')
        >>> johnny = Contact(None, 'Johnny', 'W', '275-613-0684')
        >>> group = PhoneBook(maria)
        >>> group.add(lisa)
        >>> group.add(patrick)
        >>> group.add(richard)
        >>> group.add(james)
        >>> group.add(johnny)
        >>> print(group)
        'James', 'Maria', 'P', 'Patrick', 'V', 'W'
        >>> group.group_remove([maria, richard, johnny])
        >>> print(group)
        'James', 'Patrick', 'V'
        '''
        # remove the contact one by one while looping through the list
        for contacts in remove_list:
            self.remove(contacts)

    def get_sublist(self, letter):
        ''' (PhoneBook, str) -> PhoneBook
        Given a letter, return a phonebook that only contains the contacts
        start with that letter. (cases of the letter does not matter)
        REQ: letter should be 'single' (a string of length 1)
        >>> VIP = PhoneBook(Contact('199-999-9991', 'Megan'))
        >>> VIP.add(Contact('379-358-6438', 'Ivy'))
        >>> VIP.add(Contact('827-937-8330', 'Zone', 'I'))
        >>> VIP.add(Contact('887-373-8215', 'Isabella'))
        >>> VIP.add(Contact('737-111-9303', 'Ice'))
        >>> VIP.add(Contact('655-125-0502', 'Olivia', 'A'))
        >>> print(VIP.get_sublist('I'))
        'I', 'Ice', 'Isabella', 'Ivy'
        '''
        # initiate an empty phonebook
        phonebook = PhoneBook()
        # get the first contact
        contact = self.get_head()
        # loop through the whole phonebook
        while contact is not None:
            # check if the name of the contact starts with the specific letter
            if contact.get_element().get_name().startswith(letter.upper()):
                # add the contact to the new phonebook
                phonebook.add(contact.get_element())
            # get the next contact
            contact = contact.get_next()

        return phonebook

    def get_housemate(self, home_phone):
        ''' (PhoneBook, str) -> PhoneBook
        Given a home phone number, return a phonebook which contains all the
        contacts that lives in the same house (having same home phone number).
        >>> town = PhoneBook(Contact(None, 'Megan', None, '246-646-6420',\
        None, None, 'South'))
        >>> town.add(Contact('564-989-1921', 'Sophia', None, '246-646-6420',\
        None, None, 'South'))
        >>> town.add(Contact(None, 'Camila', None, '246-646-6420', None, None,\
        'South'))
        >>> town.add(Contact(None, 'Jacob', None, '135-535-5310', None, None,\
        'North'))
        >>> town.add(Contact(None, 'Ariel', None, '246-646-6420', None, None,\
        'South'))
        >>> town.add(Contact(None, 'Jack', None, '048-848-8400', None, None,\
        'East'))
        >>> town.add(Contact(None, 'Lucas', None, '369-969-9630', None, None,\
        'West'))
        >>> town.add(Contact(None, 'Aya', None, '246-646-6420', None, None,\
        'South'))
        >>> print(town)
        'Ariel', 'Aya', 'Camila', 'Jack', 'Jacob', 'Lucas', 'Megan', 'Sophia'
        >>> print(town.get_housemate('246-646-6420'))
        'Ariel', 'Aya', 'Camila', 'Megan', 'Sophia'
        '''
        # initiate an empty phonebook
        phonebook = PhoneBook()
        # get the first contact
        contact = self.get_head()
        # loop through the whole phonebook
        while contact is not None:
            # check if the contact has the same home phone number
            if contact.get_element().get_hp() == home_phone:
                # add the contact to the new phonebook
                phonebook.add(contact.get_element())
            # get the next contact
            contact = contact.get_next()

        return phonebook

    def rearrange_phonebook(self):
        ''' (PhoneBook) -> NoneType
        Rearange the order of the phonebook. The favorite contacts will be in
        the front, but they still follows their own alphabetical order.
        >>> Class = PhoneBook(Contact(None, 'Mia', None, '291-950-7473', None,\
        None, None, True))
        >>> Class.add(Contact('564-989-1927', 'Eva', None, '481-503-5739',\
        None, None, None, False))
        >>> Class.add(Contact(None, 'Anna', None, '392-116-9527', None, None,\
        None, False))
        >>> Class.add(Contact(None, 'Laura', None, '553-173-1913', None, None,\
        None, True))
        >>> Class.add(Contact(None, 'Aurora', None, '683-587-6821', None,\
        None, None, True))
        >>> Class.add(Contact(None, 'Julia', None, '117-227-3354', None,\
        None, None, False))
        >>> Class.add(Contact(None, 'Tina', None, '667-196-7733', None, None,\
        None, False))
        >>> Class.add(Contact(None, 'Claire', None, '573-693-2941', None,\
        None, None, True))
        >>> print(Class)
        'Anna', 'Aurora', 'Claire', 'Eva', 'Julia', 'Laura', 'Mia', 'Tina'
        >>> Class.rearrange_phonebook()
        >>> print(Class)
        'Aurora', 'Claire', 'Laura', 'Mia', 'Anna', 'Eva', 'Julia', 'Tina'
        '''
        # first restore the alphabetical order of the whole phonebook
        self.rearrange()
        # then extract the favorites and pull them to the front:

        # initiate an empty list to store favorite contacts
        list = []
        # get the first contact
        contact = self.get_head()
        # loop through the whole phonebook
        while contact is not None:
            # get the contact
            contacts = contact.get_element()
            # check if the contact is marked as one of the favorites
            if contacts.get_fav():
                # store this contact (store them in reverse order)
                list.insert(0, contacts)
            # move to the next contact
            contact = contact.get_next()

        # remove all the favorites from the phonebook (will add back after)
        self.group_remove(list)

        # add the contacts back while looping through the list
        for contact in list:
            # add them to the front (this preserves their own order)
            self.add_first(contact)

    def rearrange(self):
        ''' (PhoneBook) -> NoneType
        Rearange the order of the phonebook (in alphabetical order)
        >>> Res = PhoneBook(Contact(None, 'Flora', None, '374-331-0395'))
        >>> Res.add_last(Contact(None, 'Charlotte', None, '533-077-1234'))
        >>> Res.add_first(Contact(None, 'Heather', None, '471-567-8930'))
        >>> Res.add_first(Contact(None, 'Victoria', None, '004-295-0013'))
        >>> Res.add_last(Contact(None, 'Sydney', None, '015-042-8573'))
        >>> Res.add_first(Contact(None, 'Clover', None, '493-222-9038'))
        >>> Res.reverse()
        >>> print(Res)
        'Sydney', 'Charlotte', 'Flora', 'Heather', 'Victoria', 'Clover'
        >>> Res.rearrange()
        >>> print(Res)
        'Charlotte', 'Clover', 'Flora', 'Heather', 'Sydney', 'Victoria'
        '''
        # initiate an empty list to store contacts
        list = []
        # get the first contact
        contact = self.get_head()
        # loop through the whole phonebook
        while contact is not None:
            # get the contact
            contacts = contact.get_element()
            # store this contact
            list.append(contacts)
            # move to the next contact
            contact = contact.get_next()

        # remove all the contacts from the phonebook
        self.group_remove(list)

        # add the contacts back while looping through the list
        for contact in list:
            # this ensure the order
            self.add(contact)

    def __str__(self):
        ''' returns a string representation of the contact names in the
        phonebook in order (separated by comma)
        >>> phonebook = PhoneBook(Contact('136-931-1663', 'Noah', 'P'))
        >>> phonebook.add(Contact('397-586-3334', 'Sebastian', 'Om'))
        >>> phonebook.add(Contact('641-001-0583', 'Daisy', 'C'))
        >>> phonebook.add(Contact('683-332-0357', 'Uter'))
        >>> print(phonebook)
        'C', 'Om', 'P', 'Uter'
        '''
        # get the first contact
        contact = self.get_head()
        # initiate an empty list to store the names
        name_list = []
        # loop through the phonebook
        while contact is not None:
            # add the name to the list and then move to the next contact
            name_list.append(contact.get_element().get_actual_name())
            contact = contact.get_next()

        return str(name_list)[1:-1]
