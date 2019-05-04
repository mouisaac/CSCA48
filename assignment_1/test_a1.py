import unittest
import pep8
# import hijack
import phonebook as a1

# no need to import, only the filename
PEP8_CHECK_FILES = [a1.__file__]


def build_node_list(name_list: list):
    head = tail = curr = None
    for i, d in enumerate(name_list):
        c = a1.Contact(surname=d['surname'] if d.get('surname', None) else None,
                       name=d['name'] if d.get('name', None) else None,
                       cp=d['cp'] if d.get('cp', None) else None,
                       hp=d['hp'] if d.get('hp', None) else None,
                       wp=d['wp'] if d.get('wp', None) else None,
                       email=d['email'] if d.get('email', None) else None,
                       ha=d['ha'] if d.get('ha', None) else None,
                       fav=d['fav'] if d.get('fav', False) else False)
        node = a1.Node(c)
        if i == 0:
            head = tail = curr = node
        else:
            curr.set_next(node)
            tail = curr = node
    return head, tail, len(name_list)


def compare_phonebooks(expect: a1.PhoneBook, actual: a1.PhoneBook) -> bool:
    exp_curr = expect.get_head()
    act_curr = actual.get_head()
    identical = True
    while identical and exp_curr:
        if act_curr and exp_curr.get_element() != act_curr.get_element():
            identical = False
        else:
            exp_curr = exp_curr.get_next()
            act_curr = act_curr.get_next()
    if act_curr:
        identical = False
    return identical


class TestContact(unittest.TestCase):

    def test_init_cp(self):
        c = a1.Contact(surname='world', name='hello', cp='647-000-1000')
        self.assertIsNotNone(c, 'Failed to create Contact with name, surname and cell phone')

    def test_init_hp(self):
        c = a1.Contact(surname='world', name='hello', hp='647-000-1000')
        self.assertIsNotNone(c, 'Failed to create Contact with name, surname and home phone')

    def test_init_wp(self):
        c = a1.Contact(surname='world', name='hello', wp='647-000-1000')
        self.assertIsNotNone(c, 'Failed to create Contact with name, surname and work phone')

    def test_no_name_exception(self):
        self.assertRaises(a1.MissingNameException, a1.Contact, cp='647-000-1000')

    def test_no_phone_exception(self):
        self.assertRaises(a1.MissingPhoneNumberException, a1.Contact, name='hello', surname='world')

    def test_phone_and_name(self):
        c = a1.Contact(name='hello', cp='647-000-1000')
        self.assertIsNotNone(c, 'Failed to create Contact with name and cell phone')
        c = a1.Contact(name='hello', hp='647-000-2000')
        self.assertIsNotNone(c, 'Failed to create Contact with name and home phone')
        c = a1.Contact(name='hello', wp='647-000-3000')
        self.assertIsNotNone(c, 'Failed to create Contact with name and work phone')

    def test_phone_and_surname(self):
        c = a1.Contact(surname='world', cp='647-000-1000')
        self.assertIsNotNone(c, 'Failed to create Contact with surname and cell phone')
        c = a1.Contact(surname='world', hp='647-000-2000')
        self.assertIsNotNone(c, 'Failed to create Contact with surname and home phone')
        c = a1.Contact(surname='world', wp='647-000-3000')
        self.assertIsNotNone(c, 'Failed to create Contact with surname and work phone')

    def test_all_arguments(self):
        c = a1.Contact(surname='world', name='hello', cp='647-000-1000', hp='647-000-2000', wp='647-000-3000',
                       email='test@email.com', ha='1 Infinite loop', fav=True)
        self.assertIsNotNone(c, 'Failed to create Contact with fulfilled arguments')

    def test_contact_inheritance(self):
        self.assertFalse(issubclass(a1.Node, a1.Contact), 'Contact should not be the subclass of Node')
        self.assertFalse(issubclass(a1.Contact, a1.Node), 'Node should not be the subclass of Contact')


class _TestPhoneBook(unittest.TestCase):

    def setUp(self):
        self.pb_expect = a1.PhoneBook()
        self.pb_actual = a1.PhoneBook()


class TestPhoneBookBasic(_TestPhoneBook):

    def test_init(self):
        self.assertIsNone(self.pb_actual.get_head(), 'Failed to create new Phone book with empty contacts')
        self.assertIsNone(self.pb_actual.get_tail(), 'Failed to create new Phone book with empty contacts')
        self.assertEqual(0, self.pb_actual.size(), 'Failed to create new Phone book with empty contacts')

    def test_init_with_contact(self):
        c = a1.Contact(surname='Alex', cp='647-000-1000')
        pb = a1.PhoneBook(c)
        self.assertEqual(c, pb.get_head().get_element(), 'Failed to create new Phone book with only one contact')
        self.assertEqual(c, pb.get_tail().get_element(), 'Failed to create new Phone book with only one contact')
        self.assertEqual(1, pb.size(), 'Failed to create new Phone book with only one contact')

    def test_phonebook_inheritance(self):
        self.assertTrue(issubclass(a1.PhoneBook, a1.SingleLinkedList),
                        'PhoneBook should be the subclass of SingleLinkedList')
        self.assertFalse(issubclass(a1.SingleLinkedList, a1.PhoneBook),
                         'SingleLinkedList should not be the subclass of PhoneBook')


class TestPhoneBookAdd(_TestPhoneBook):

    def test_add_to_empty_phonebook(self):
        c = a1.Contact(surname='Alan', name='Dino', cp='285-000-0010')
        self.pb_actual.add(c)
        self.assertEqual(c, self.pb_actual.get_head().get_element(),
                         'Failed to add one contact. Head node is different')
        self.assertEqual(c, self.pb_actual.get_tail().get_element(),
                         'Failed to add one contact. Tail node is different')
        self.assertEqual(1, self.pb_actual.size(), 'Failed to add one contact. Size is different')

    def test_add_to_head(self):
        names_exp = [{'surname': 'Alan', 'name': 'Ted', 'cp': '345-790-0001'},
                     {'surname': 'Bell', 'name': 'John', 'wp': '437-000-1000'},
                     {'surname': 'Dean', 'name': 'Allan', 'wp': '519-100-2345'}]
        names_act = [{'surname': 'Bell', 'name': 'John', 'wp': '437-000-1000'},
                     {'surname': 'Dean', 'name': 'Allan', 'wp': '519-100-2345'}]
        head, tail, size = build_node_list(names_exp)
        self.pb_expect._set_list(head, tail, size)
        head, tail, size = build_node_list(names_act)
        self.pb_actual._set_list(head, tail, size)

        self.pb_actual.add(a1.Contact(surname='Alan', name='Ted', cp='345-790-0001'))
        self.assertTrue(compare_phonebooks(self.pb_expect, self.pb_actual), 'Phone books are not the same')

    def test_add_to_tail(self):
        names_exp = [{'surname': 'Bell', 'name': 'John', 'wp': '437-000-1000'},
                     {'surname': 'Dean', 'name': 'Allan', 'wp': '519-100-2345'},
                     {'surname': 'George', 'name': 'Brown', 'hp': '209-613-7600'}]
        names_act = [{'surname': 'Bell', 'name': 'John', 'wp': '437-000-1000'},
                     {'surname': 'Dean', 'name': 'Allan', 'wp': '519-100-2345'}]
        head, tail, size = build_node_list(names_exp)
        self.pb_expect._set_list(head, tail, size)
        head, tail, size = build_node_list(names_act)
        self.pb_actual._set_list(head, tail, size)

        self.pb_actual.add(a1.Contact(surname='George', name='Brown', hp='209-613-7600'))
        self.assertTrue(compare_phonebooks(self.pb_expect, self.pb_actual), 'Phone books are not the same')

    def test_add_to_body(self):
        names_exp = [{'surname': 'Bell', 'name': 'John', 'wp': '437-000-1000'},
                     {'surname': 'Dean', 'name': 'Allan', 'wp': '519-100-2345'},
                     {'surname': 'George', 'name': 'Brown', 'hp': '209-613-7600'}]
        names_act = [{'surname': 'Bell', 'name': 'John', 'wp': '437-000-1000'},
                     {'surname': 'George', 'name': 'Brown', 'hp': '209-613-7600'}]
        head, tail, size = build_node_list(names_exp)
        self.pb_expect._set_list(head, tail, size)
        head, tail, size = build_node_list(names_act)
        self.pb_actual._set_list(head, tail, size)

        self.pb_actual.add(a1.Contact(surname='Dean', name='Allan', wp='519-100-2345'))
        self.assertTrue(compare_phonebooks(self.pb_expect, self.pb_actual), 'Phone books are not the same')

    def test_add_contact_no_surname(self):
        names_exp = [{'name': 'Allan', 'wp': '519-100-2345'},
                     {'surname': 'Bell', 'name': 'John', 'wp': '437-000-1000'},
                     {'surname': 'George', 'name': 'Brown', 'hp': '209-613-7600'}]
        names_act = [{'surname': 'Bell', 'name': 'John', 'wp': '437-000-1000'},
                     {'surname': 'George', 'name': 'Brown', 'hp': '209-613-7600'}]
        head, tail, size = build_node_list(names_exp)
        self.pb_expect._set_list(head, tail, size)
        head, tail, size = build_node_list(names_act)
        self.pb_actual._set_list(head, tail, size)

        self.pb_actual.add(a1.Contact(name='Allan', wp='519-100-2345'))
        self.assertTrue(compare_phonebooks(self.pb_expect, self.pb_actual), 'Phone books are not the same')

    def test_add_same_surname(self):
        names_exp = [{'surname': 'Bell', 'name': 'John', 'wp': '437-000-1000'},
                     {'surname': 'bELL', 'name': 'bROWN', 'hp': '209-613-7600'}]
        names_act = [{'surname': 'Bell', 'name': 'John', 'wp': '437-000-1000'}]
        head, tail, size = build_node_list(names_exp)
        self.pb_expect._set_list(head, tail, size)
        head, tail, size = build_node_list(names_act)
        self.pb_actual._set_list(head, tail, size)

        self.pb_actual.add(a1.Contact(surname='bELL', name='bROWN', hp='209-613-7600'))
        self.assertTrue(compare_phonebooks(self.pb_expect, self.pb_actual), 'Phone books are not the same')

    def test_add_same_name_no_surname(self):
        names_exp = [{'name': 'Edward', 'wp': '437-000-1000'},
                     {'name': 'edwARD', 'hp': '209-613-7600'}]
        names_act = [{'name': 'Edward', 'wp': '437-000-1000'}]
        head, tail, size = build_node_list(names_exp)
        self.pb_expect._set_list(head, tail, size)
        head, tail, size = build_node_list(names_act)
        self.pb_actual._set_list(head, tail, size)

        self.pb_actual.add(a1.Contact(name='edwARD', hp='209-613-7600'))
        self.assertTrue(compare_phonebooks(self.pb_expect, self.pb_actual), 'Phone books are not the same')


class TestPhoneBookRemove(_TestPhoneBook):

    def test_remove_head(self):
        names_exp = [{'surname': 'Amber', 'name': 'Yeti', 'hp': '209-613-7600'},
                     {'surname': 'Markus', 'name': 'Word', 'cp': '647-000-1100'}]
        names_act = [{'surname': 'Albert', 'name': 'Edward', 'wp': '437-000-1000'},
                     {'surname': 'Amber', 'name': 'Yeti', 'hp': '209-613-7600'},
                     {'surname': 'Markus', 'name': 'Word', 'cp': '647-000-1100'}]
        head, tail, size = build_node_list(names_exp)
        self.pb_expect._set_list(head, tail, size)
        head, tail, size = build_node_list(names_act)
        self.pb_actual._set_list(head, tail, size)

        c = a1.Contact(surname='Albert', name='Edward', wp='437-000-1000')
        actual = self.pb_actual.remove(c)
        self.assertEqual(c, actual, 'Failed to remove from phone book')
        self.assertEqual(2, self.pb_actual.size(), 'Size incorrect after remove')

    def test_remove_tail(self):
        names_exp = [{'surname': 'Albert', 'name': 'Edward', 'wp': '437-000-1000'},
                     {'surname': 'Amber', 'name': 'Yeti', 'hp': '209-613-7600'}]
        names_act = [{'surname': 'Albert', 'name': 'Edward', 'wp': '437-000-1000'},
                     {'surname': 'Amber', 'name': 'Yeti', 'hp': '209-613-7600'},
                     {'surname': 'Markus', 'name': 'Word', 'cp': '647-000-1100'}]
        head, tail, size = build_node_list(names_exp)
        self.pb_expect._set_list(head, tail, size)
        head, tail, size = build_node_list(names_act)
        self.pb_actual._set_list(head, tail, size)

        c = a1.Contact(surname='Markus', name='Word', cp='647-000-1100')
        actual = self.pb_actual.remove(c)
        self.assertEqual(c, actual, 'Failed to remove from phone book')
        self.assertEqual(2, self.pb_actual.size(), 'Size incorrect after remove')

    def test_remove_body(self):
        names_exp = [{'surname': 'Albert', 'name': 'Edward', 'wp': '437-000-1000'},
                     {'surname': 'Markus', 'name': 'Word', 'cp': '647-000-1100'}]
        names_act = [{'surname': 'Albert', 'name': 'Edward', 'wp': '437-000-1000'},
                     {'surname': 'Amber', 'name': 'Yeti', 'hp': '209-613-7600'},
                     {'surname': 'Markus', 'name': 'Word', 'cp': '647-000-1100'}]
        head, tail, size = build_node_list(names_exp)
        self.pb_expect._set_list(head, tail, size)
        head, tail, size = build_node_list(names_act)
        self.pb_actual._set_list(head, tail, size)

        c = a1.Contact(surname='Amber', name='Yeti', hp='209-613-7600')
        actual = self.pb_actual.remove(c)
        self.assertEqual(c, actual, 'Failed to remove from phone book')
        self.assertEqual(2, self.pb_actual.size(), 'Size incorrect after remove')

    def test_remove_not_exist(self):
        names_exp = [{'surname': 'Albert', 'name': 'Edward', 'wp': '437-000-1000'},
                     {'surname': 'Amber', 'name': 'Yeti', 'hp': '209-613-7600'},
                     {'surname': 'Markus', 'name': 'Word', 'cp': '647-000-1100'}]
        names_act = [{'surname': 'Albert', 'name': 'Edward', 'wp': '437-000-1000'},
                     {'surname': 'Amber', 'name': 'Yeti', 'hp': '209-613-7600'},
                     {'surname': 'Markus', 'name': 'Word', 'cp': '647-000-1100'}]
        head, tail, size = build_node_list(names_exp)
        self.pb_expect._set_list(head, tail, size)
        head, tail, size = build_node_list(names_act)
        self.pb_actual._set_list(head, tail, size)

        c = a1.Contact(surname='Chan', name='Edward', hp='519-008-2345')
        actual = self.pb_actual.remove(c)
        self.assertIsNone(actual, 'Contact does not exist in the phone book')
        self.assertEqual(3, self.pb_actual.size(), 'Size incorrect after remove')


class TestPhoneBookShowFavList(_TestPhoneBook):

    def test_return_type(self):
        names = [{'surname': 'Bell', 'name': 'John', 'hp': '437-000-1000', 'ha': '1 Loop Dr.'},
                 {'surname': 'Kiwi', 'name': 'Frank', 'cp': '437-222-1890', 'ha': '10 Infinite Loop Dr.'}]
        head, tail, size = build_node_list(names)
        self.pb_actual._set_list(head, tail, size)

        actual = self.pb_actual.show_fav_list()
        self.assertTrue(isinstance(actual, list), 'Incorrect return type.')

    def test_no_fav_contact(self):
        names = [{'surname': 'Bell', 'name': 'John', 'hp': '437-000-1000', 'ha': '1 Loop Dr.'},
                 {'surname': 'Kiwi', 'name': 'Frank', 'cp': '437-222-1890', 'ha': '10 Infinite Loop Dr.'}]
        head, tail, size = build_node_list(names)
        self.pb_actual._set_list(head, tail, size)

        actual = self.pb_actual.show_fav_list()
        self.assertEqual([], actual, 'Phone book has no favourite contact')

    def test_multiple_fav_contacts(self):
        names = [{'surname': 'Bell', 'name': 'John', 'hp': '437-000-1000', 'ha': '1 Loop Dr.'},
                 {'surname': 'Kiwi', 'name': 'Frank', 'cp': '437-222-1890', 'ha': '10 Infinite Loop Dr.', 'fav': True},
                 {'surname': 'Larry', 'name': 'Sans', 'wp': '616-000-8501', 'fav': True},
                 {'surname': 'Op', 'name': 'Erica', 'hp': '522-354-1890', 'email': 'oe@test.com', 'ha': '13 Infinite Loop Dr.'}]
        head, tail, size = build_node_list(names)
        self.pb_actual._set_list(head, tail, size)

        actual = self.pb_actual.show_fav_list()
        self.assertEqual(['Kiwi', 'Larry'], actual, 'Incorrect result')

    def test_no_surname_fav_contacts(self):
        names = [{'name': 'John', 'hp': '437-000-1000', 'ha': '1 Loop Dr.', 'fav': True},
                 {'surname': 'Kiwi', 'name': 'Frank', 'cp': '437-222-1890', 'ha': '10 Infinite Loop Dr.'},
                 {'surname': 'Larry', 'name': 'Sans', 'wp': '616-000-8501', 'fav': True},
                 {'surname': 'Op', 'name': 'Erica', 'hp': '522-354-1890', 'email': 'oe@test.com', 'ha': '13 Infinite Loop Dr.'}]
        head, tail, size = build_node_list(names)
        self.pb_actual._set_list(head, tail, size)

        actual = self.pb_actual.show_fav_list()
        self.assertEqual(['John', 'Larry'], actual, 'Incorrect result')


class TestPhoneBookTorontoPhone(_TestPhoneBook):

    def test_all_416(self):
        names = [{'name': 'John', 'hp': '416-000-1000', 'ha': '1 Loop Dr.', 'fav': True},
                 {'surname': 'Kiwi', 'name': 'Frank', 'cp': '416-222-1890', 'ha': '10 Infinite Loop Dr.'},
                 {'surname': 'Larry', 'name': 'Sans', 'wp': '416-000-8501', 'fav': True},
                 {'surname': 'Op', 'name': 'Erica', 'hp': '416-354-1890', 'email': 'oe@test.com', 'ha': '13 Infinite Loop Dr.'}]
        names_416 = [{'name': 'John', 'hp': '416-000-1000', 'ha': '1 Loop Dr.', 'fav': True},
                     {'surname': 'Kiwi', 'name': 'Frank', 'cp': '416-222-1890', 'ha': '10 Infinite Loop Dr.'},
                     {'surname': 'Larry', 'name': 'Sans', 'wp': '416-000-8501', 'fav': True},
                     {'surname': 'Op', 'name': 'Erica', 'hp': '416-354-1890', 'email': 'oe@test.com', 'ha': '13 Infinite Loop Dr.'}]
        names_647 = []
        head, tail, size = build_node_list(names)
        self.pb_actual._set_list(head, tail, size)
        pb_416, pb_647 = a1.PhoneBook(), a1.PhoneBook()
        head, tail, size = build_node_list(names_416)
        pb_416._set_list(head, tail, size)
        head, tail, size = build_node_list(names_647)
        pb_647._set_list(head, tail, size)

        actual_416, actual_647 = self.pb_actual.toronto_phone()
        self.assertTrue(compare_phonebooks(pb_416, actual_416), 'Phone book content not the same')
        self.assertTrue(compare_phonebooks(pb_647, actual_647), 'Phone book content not the same')

    def test_all_647(self):
        names = [{'name': 'John', 'hp': '647-000-1000', 'ha': '1 Loop Dr.', 'fav': True},
                 {'surname': 'Kiwi', 'name': 'Frank', 'cp': '647-222-1890', 'ha': '10 Infinite Loop Dr.'},
                 {'surname': 'Larry', 'name': 'Sans', 'wp': '647-000-8501', 'fav': True},
                 {'surname': 'Op', 'name': 'Erica', 'hp': '647-354-1890', 'email': 'oe@test.com', 'ha': '13 Infinite Loop Dr.'}]
        names_416 = []
        names_647 = [{'name': 'John', 'hp': '647-000-1000', 'ha': '1 Loop Dr.', 'fav': True},
                     {'surname': 'Kiwi', 'name': 'Frank', 'cp': '647-222-1890', 'ha': '10 Infinite Loop Dr.'},
                     {'surname': 'Larry', 'name': 'Sans', 'wp': '647-000-8501', 'fav': True},
                     {'surname': 'Op', 'name': 'Erica', 'hp': '647-354-1890', 'email': 'oe@test.com', 'ha': '13 Infinite Loop Dr.'}]
        head, tail, size = build_node_list(names)
        self.pb_actual._set_list(head, tail, size)
        pb_416, pb_647 = a1.PhoneBook(), a1.PhoneBook()
        head, tail, size = build_node_list(names_416)
        pb_416._set_list(head, tail, size)
        head, tail, size = build_node_list(names_647)
        pb_647._set_list(head, tail, size)

        actual_416, actual_647 = self.pb_actual.toronto_phone()
        self.assertTrue(compare_phonebooks(pb_416, actual_416), 'Phone book content not the same')
        self.assertTrue(compare_phonebooks(pb_647, actual_647), 'Phone book content not the same')

    def test_both_toronto_and_non_toronto_phone_numbers(self):
        names = [{'name': 'John', 'hp': '647-000-1000', 'ha': '1 Loop Dr.', 'fav': True},
                 {'surname': 'Kiwi', 'name': 'Frank', 'cp': '416-222-1890', 'ha': '10 Infinite Loop Dr.'},
                 {'surname': 'Larry', 'name': 'Sans', 'wp': '800-000-8501', 'fav': True},
                 {'surname': 'Op', 'name': 'Erica', 'hp': '512-354-1890', 'email': 'oe@test.com', 'ha': '13 Infinite Loop Dr.'}]
        names_416 = [{'surname': 'Kiwi', 'name': 'Frank', 'cp': '416-222-1890', 'ha': '10 Infinite Loop Dr.'}]
        names_647 = [{'name': 'John', 'hp': '647-000-1000', 'ha': '1 Loop Dr.', 'fav': True}]
        head, tail, size = build_node_list(names)
        self.pb_actual._set_list(head, tail, size)
        pb_416, pb_647 = a1.PhoneBook(), a1.PhoneBook()
        head, tail, size = build_node_list(names_416)
        pb_416._set_list(head, tail, size)
        head, tail, size = build_node_list(names_647)
        pb_647._set_list(head, tail, size)

        actual_416, actual_647 = self.pb_actual.toronto_phone()
        self.assertTrue(compare_phonebooks(pb_416, actual_416), 'Phone book content not the same')
        self.assertTrue(compare_phonebooks(pb_647, actual_647), 'Phone book content not the same')


class TestPhoneBookReversedPhoneBook(_TestPhoneBook):

    def test_return_type(self):
        names = [{'surname': 'Bell', 'name': 'John', 'hp': '437-000-1000', 'ha': '1 Loop Dr.'},
                 {'surname': 'Kiwi', 'name': 'Frank', 'cp': '437-222-1890', 'ha': '10 Infinite Loop Dr.'}]
        head, tail, size = build_node_list(names)
        self.pb_actual._set_list(head, tail, size)

        actual = self.pb_actual.reversed_phonebook()
        self.assertTrue(isinstance(actual, a1.PhoneBook), 'Incorrect return type.')

    def test_reverse(self):
        names_exp = [{'surname': 'Op', 'name': 'Erica', 'hp': '522-354-1890', 'email': 'oe@test.com', 'ha': '13 Infinite Loop Dr.'},
                     {'surname': 'Larry', 'name': 'Sans', 'wp': '616-000-8501', 'fav': True},
                     {'surname': 'Kiwi', 'name': 'Frank', 'cp': '437-222-1890', 'ha': '10 Infinite Loop Dr.'},
                     {'name': 'John', 'hp': '437-000-1000', 'ha': '1 Loop Dr.', 'fav': True}]
        names_act = [{'name': 'John', 'hp': '437-000-1000', 'ha': '1 Loop Dr.', 'fav': True},
                     {'surname': 'Kiwi', 'name': 'Frank', 'cp': '437-222-1890', 'ha': '10 Infinite Loop Dr.'},
                     {'surname': 'Larry', 'name': 'Sans', 'wp': '616-000-8501', 'fav': True},
                     {'surname': 'Op', 'name': 'Erica', 'hp': '522-354-1890', 'email': 'oe@test.com', 'ha': '13 Infinite Loop Dr.'}]
        head, tail, size = build_node_list(names_exp)
        self.pb_expect._set_list(head, tail, size)
        head, tail, size = build_node_list(names_act)
        self.pb_actual._set_list(head, tail, size)

        actual = self.pb_actual.reversed_phonebook()
        self.assertTrue(compare_phonebooks(self.pb_expect, actual), 'Rearranged phone books are not the same')


class TestPhoneBookSyncPhoneBook(_TestPhoneBook):

    def test_return_type(self):
        names_exp = [{'surname': 'Kiwi', 'name': 'Frank', 'cp': '437-222-1890', 'wp': '800-222-1890'}]
        names_act = [{'surname': 'Kiwi', 'name': 'Frank', 'wp': '800-222-1890'}]
        names_to_sync = [{'surname': 'Kiwi', 'name': 'Frank', 'cp': '437-222-1890'}]
        head, tail, size = build_node_list(names_exp)
        self.pb_expect._set_list(head, tail, size)
        head, tail, size = build_node_list(names_act)
        self.pb_actual._set_list(head, tail, size)
        pb_sync = a1.PhoneBook()
        head, tail, size = build_node_list(names_to_sync)
        pb_sync._set_list(head, tail, size)

        actual = self.pb_actual.sync_phonebook(pb_sync)
        self.assertIsNone(actual, 'Incorrect return type')

    def test_sync_contact_same_person(self):
        names_exp = [{'surname': 'Kiwi', 'name': 'Frank', 'cp': '437-222-1890', 'wp': '800-222-1890'},
                     {'surname': 'Kiwi', 'name': 'Frank', 'hp': '115-885-1287'}]
        names_act = [{'surname': 'Kiwi', 'name': 'Frank', 'cp': '437-222-1890', 'wp': '800-222-1890'}]
        names_to_sync = [{'surname': 'Kiwi', 'name': 'Frank', 'hp': '115-885-1287'}]
        head, tail, size = build_node_list(names_exp)
        self.pb_expect._set_list(head, tail, size)
        head, tail, size = build_node_list(names_act)
        self.pb_actual._set_list(head, tail, size)
        pb_sync = a1.PhoneBook()
        head, tail, size = build_node_list(names_to_sync)
        pb_sync._set_list(head, tail, size)

        self.pb_actual.sync_phonebook(pb_sync)
        self.assertTrue(compare_phonebooks(self.pb_expect, self.pb_actual), 'Failed to sync 2 phone books with 1 same person contact')

    def test_sync_contact_different_people(self):
        names_exp = [{'surname': 'Kiwi', 'name': 'Frank', 'wp': '800-222-1890'},
                     {'surname': 'Larry', 'name': 'Sans', 'hp': '616-000-8501', 'fav': True}]
        names_act = [{'surname': 'Kiwi', 'name': 'Frank', 'wp': '800-222-1890'}]
        names_to_sync = [{'surname': 'Larry', 'name': 'Sans', 'hp': '616-000-8501', 'fav': True}]
        head, tail, size = build_node_list(names_exp)
        self.pb_expect._set_list(head, tail, size)
        head, tail, size = build_node_list(names_act)
        self.pb_actual._set_list(head, tail, size)
        pb_sync = a1.PhoneBook()
        head, tail, size = build_node_list(names_to_sync)
        pb_sync._set_list(head, tail, size)

        self.pb_actual.sync_phonebook(pb_sync)
        self.assertTrue(compare_phonebooks(self.pb_expect, self.pb_actual), 'Failed to sync 2 phone books with 2 different people contact')

    def test_sync_1_new_1_existing_contact(self):
        names_exp = [{'surname': 'Kiwi', 'name': 'Frank', 'wp': '800-222-1890'},
                     {'surname': 'Kiwi', 'name': 'Frank', 'cp': '437-222-1890', 'wp': '800-222-1890'},
                     {'surname': 'Larry', 'name': 'Sans', 'hp': '616-000-8501', 'fav': True}]
        names_act = [{'surname': 'Kiwi', 'name': 'Frank', 'wp': '800-222-1890'}]
        names_to_sync = [{'surname': 'Kiwi', 'name': 'Frank', 'cp': '437-222-1890', 'wp': '800-222-1890'},
                         {'surname': 'Larry', 'name': 'Sans', 'hp': '616-000-8501', 'fav': True}]
        head, tail, size = build_node_list(names_exp)
        self.pb_expect._set_list(head, tail, size)
        head, tail, size = build_node_list(names_act)
        self.pb_actual._set_list(head, tail, size)
        pb_sync = a1.PhoneBook()
        head, tail, size = build_node_list(names_to_sync)
        pb_sync._set_list(head, tail, size)

        self.pb_actual.sync_phonebook(pb_sync)
        self.assertTrue(compare_phonebooks(self.pb_expect, self.pb_actual), 'Failed to sync 2 phone books with 2 different people contact')

    def test_sync_same_name_different_info(self):
        names_exp = [{'surname': 'Kiwi', 'name': 'Frank', 'cp': '437-222-1890', 'wp': '599-133-1890'},
                     {'surname': 'Kiwi', 'name': 'Frank', 'hp': '616-000-8501', 'wp': '800-221-2384', 'fav': True}]
        names_act = [{'surname': 'Kiwi', 'name': 'Frank', 'cp': '437-222-1890'}]
        names_to_sync = [{'surname': 'Kiwi', 'name': 'Frank', 'cp': '437-222-1890', 'wp': '599-133-1890'},
                         {'surname': 'Kiwi', 'name': 'Frank', 'hp': '616-000-8501', 'wp': '800-221-2384', 'fav': True}]
        head, tail, size = build_node_list(names_exp)
        self.pb_expect._set_list(head, tail, size)
        head, tail, size = build_node_list(names_act)
        self.pb_actual._set_list(head, tail, size)
        pb_sync = a1.PhoneBook()
        head, tail, size = build_node_list(names_to_sync)
        pb_sync._set_list(head, tail, size)

        self.pb_actual.sync_phonebook(pb_sync)
        self.assertTrue(compare_phonebooks(self.pb_expect, self.pb_actual), 'Failed to sync 2 phone books with 2 different people contact')


class TestPhoneBookGroupRemove(_TestPhoneBook):

    def test_group_remove(self):
        names_exp = [{'surname': 'Kiwi', 'name': 'Frank', 'cp': '437-222-1890', 'ha': '10 Infinite Loop Dr.'},
                     {'surname': 'Op', 'name': 'Erica', 'hp': '522-354-1890', 'email': 'oe@test.com', 'ha': '13 Infinite Loop Dr.'}]
        names_act = [{'name': 'John', 'hp': '437-000-1000', 'fav': True},
                     {'surname': 'Kiwi', 'name': 'Frank', 'cp': '437-222-1890', 'ha': '10 Infinite Loop Dr.'},
                     {'surname': 'Larry', 'name': 'Sans', 'wp': '616-000-8501', 'fav': True},
                     {'surname': 'Op', 'name': 'Erica', 'hp': '522-354-1890', 'email': 'oe@test.com', 'ha': '13 Infinite Loop Dr.'}]
        head, tail, size = build_node_list(names_exp)
        self.pb_expect._set_list(head, tail, size)
        head, tail, size = build_node_list(names_act)
        self.pb_actual._set_list(head, tail, size)

        c1 = a1.Contact(name='John', hp='437-000-1000', fav=True)
        c2 = a1.Contact(surname='Larry', name='Sans', wp='616-000-8501', fav=True)
        self.pb_actual.group_remove([c1, c2])
        self.assertTrue(compare_phonebooks(self.pb_expect, self.pb_actual), 'Rearranged phone books are not the same')


class TestPhoneBookGetSublist(_TestPhoneBook):

    def test_return_type(self):
        names = [{'surname': 'Bell', 'name': 'John', 'hp': '437-000-1000', 'ha': '1 Loop Dr.'}]
        head, tail, size = build_node_list(names)
        self.pb_actual._set_list(head, tail, size)

        actual = self.pb_actual.get_sublist('B')
        self.assertTrue(isinstance(actual, a1.PhoneBook), 'Incorrect return type.')

    def test_sublist_no_contacts(self):
        names = [{'surname': 'Bell', 'name': 'John', 'hp': '437-000-1000', 'ha': '1 Loop Dr.'}]
        head, tail, size = build_node_list(names)
        self.pb_actual._set_list(head, tail, size)

        actual = self.pb_actual.get_sublist('A')
        self.assertEqual(0, actual.size(), 'Sublist does not contain any contact')

    def test_sublist_multiple_contacts(self):
        names = [{'surname': 'Arron', 'name': 'Ben', 'hp': '416-200-3000', 'ha': '1 Loop Dr.'},
                 {'surname': 'Bell', 'name': 'John', 'hp': '437-000-1000', 'ha': '10 Infinite Loop Dr.'},
                 {'surname': 'Ben', 'name': 'Andrew', 'hp': '416-200-3000', 'ha': '1 Loop Dr.'}]
        head, tail, size = build_node_list(names)
        self.pb_actual._set_list(head, tail, size)

        actual = self.pb_actual.get_sublist('B')
        self.assertEqual(2, actual.size(), 'Sublist contains 2 contacts')
        c1 = a1.Contact(surname='Bell', name='John', hp='437-000-1000', ha='10 Infinite Loop Dr.')
        c2 = a1.Contact(surname='Ben', name='Andrew', hp='416-200-3000', ha='1 Loop Dr.')
        self.assertEqual(c1, actual.get_head().get_element(), 'First Contact not the same.')
        self.assertEqual(c2, actual.get_tail().get_element(), 'Second Contact not the same.')


class TestPhoneBookGetHousemate(_TestPhoneBook):

    def test_return_type(self):
        names = [{'surname': 'Bell', 'name': 'John', 'hp': '437-000-1000', 'ha': '1 Loop Dr.'},
                 {'surname': 'Bell', 'name': 'Kati', 'hp': '437-000-1000', 'ha': '1 Loop Dr.'}]
        head, tail, size = build_node_list(names)
        self.pb_actual._set_list(head, tail, size)

        actual = self.pb_actual.get_housemate('437-000-1000')
        self.assertTrue(isinstance(actual, a1.PhoneBook), 'Incorrect return type.')

    def test_get_no_housemate(self):
        names = [{'surname': 'Bell', 'name': 'John', 'hp': '437-000-1000', 'ha': '1 Loop Dr.'},
                 {'surname': 'Chan', 'name': 'Joshua', 'hp': '647-100-2000', 'ha': '2 Loop Dr.'}]
        head, tail, size = build_node_list(names)
        self.pb_actual._set_list(head, tail, size)

        actual = self.pb_actual.get_housemate('416-111-2222')
        self.assertEqual(0, actual.size(), 'No one share the same phone number.')

    def test_get_one_housemate(self):
        names = [{'surname': 'Bell', 'name': 'John', 'hp': '437-000-1000', 'ha': '1 Loop Dr.'},
                 {'surname': 'Chan', 'name': 'Joshua', 'hp': '647-100-2000', 'ha': '20 Loop Dr.'}]
        head, tail, size = build_node_list(names)
        self.pb_actual._set_list(head, tail, size)

        actual = self.pb_actual.get_housemate('437-000-1000')
        self.assertEqual(1, actual.size(), 'Only one person share this phone number.')
        c = a1.Contact(surname='Bell', name='John', hp='437-000-1000', ha='1 Loop Dr.')
        self.assertEqual(c, actual.get_head().get_element(), 'Contact not the same.')

    def test_get_multiple_housemates(self):
        names = [{'surname': 'Arron', 'name': 'Ben', 'hp': '416-200-3000', 'ha': '1 Loop Dr.'},
                 {'surname': 'Bell', 'name': 'John', 'hp': '437-000-1000', 'ha': '10 Infinite Loop Dr.'},
                 {'surname': 'Chan', 'name': 'Joshua', 'hp': '416-200-3000', 'ha': '1 Loop Dr.'}]
        head, tail, size = build_node_list(names)
        self.pb_actual._set_list(head, tail, size)

        actual = self.pb_actual.get_housemate('416-200-3000')
        self.assertEqual(2, actual.size(), 'Two people share this phone number.')
        c1 = a1.Contact(surname='Arron', name='Ben', hp='416-200-3000', ha='1 Loop Dr.')
        c2 = a1.Contact(surname='Chan', name='Joshua', hp='416-200-3000', ha='1 Loop Dr.')
        self.assertEqual(c1, actual.get_head().get_element(), 'First Contact not the same.')
        self.assertEqual(c2, actual.get_tail().get_element(), 'Second Contact not the same.')


class TestPhoneBookRearrangePhoneBook(_TestPhoneBook):

    def test_return_type(self):
        names = [{'surname': 'Bell', 'name': 'John', 'hp': '437-000-1000'},
                 {'surname': 'Chan', 'name': 'Anderson', 'wp': '647-811-0002', 'fav': True}]
        head, tail, size = build_node_list(names)
        self.pb_actual._set_list(head, tail, size)

        actual = self.pb_actual.rearrange_phonebook()
        self.assertIsNone(actual, 'Incorrect return type.')

    def test_no_fav_contacts(self):
        names_exp = [{'surname': 'Bell', 'name': 'John', 'hp': '437-000-1000'},
                     {'surname': 'Chan', 'name': 'Anderson', 'wp': '647-811-0002'}]
        names_act = [{'surname': 'Bell', 'name': 'John', 'hp': '437-000-1000'},
                     {'surname': 'Chan', 'name': 'Anderson', 'wp': '647-811-0002'}]
        head, tail, size = build_node_list(names_exp)
        self.pb_expect._set_list(head, tail, size)
        head, tail, size = build_node_list(names_act)
        self.pb_actual._set_list(head, tail, size)

        self.pb_actual.rearrange_phonebook()
        self.assertTrue(compare_phonebooks(self.pb_expect, self.pb_actual), 'Rearranged phone books are not the same')

    def test_all_fav_contacts(self):
        names_exp = [{'surname': 'Bell', 'name': 'John', 'hp': '437-000-1000', 'fav': True},
                     {'surname': 'Chan', 'name': 'Anderson', 'wp': '647-811-0002', 'fav': True}]
        names_act = [{'surname': 'Bell', 'name': 'John', 'hp': '437-000-1000', 'fav': True},
                     {'surname': 'Chan', 'name': 'Anderson', 'wp': '647-811-0002', 'fav': True}]
        head, tail, size = build_node_list(names_exp)
        self.pb_expect._set_list(head, tail, size)
        head, tail, size = build_node_list(names_act)
        self.pb_actual._set_list(head, tail, size)

        self.pb_actual.rearrange_phonebook()
        self.assertTrue(compare_phonebooks(self.pb_expect, self.pb_actual), 'Rearranged phone books are not the same')

    def test_rearrange_fav_contacts(self):
        names_exp = [{'surname': 'Chan', 'name': 'Anderson', 'wp': '647-811-0002', 'fav': True},
                     {'surname': 'Wish', 'name': 'Kristin', 'cp': '519-088-0002', 'fav': True},
                     {'surname': 'Bell', 'name': 'John', 'hp': '437-000-1000'}]
        names_act = [{'surname': 'Bell', 'name': 'John', 'hp': '437-000-1000'},
                     {'surname': 'Chan', 'name': 'Anderson', 'wp': '647-811-0002', 'fav': True},
                     {'surname': 'Wish', 'name': 'Kristin', 'cp': '519-088-0002', 'fav': True}]
        head, tail, size = build_node_list(names_exp)
        self.pb_expect._set_list(head, tail, size)
        head, tail, size = build_node_list(names_act)
        self.pb_actual._set_list(head, tail, size)

        self.pb_actual.rearrange_phonebook()
        self.assertTrue(compare_phonebooks(self.pb_expect, self.pb_actual), 'Rearranged phone books are not the same')


class TestPEP8(unittest.TestCase):

    def test_pep8(self):
        pep8style = pep8.StyleGuide(quiet=True,
                                    ignore=('E121', 'E123', 'E126', 'E133',
                                            'E211', 'E226', 'E241', 'E242', 'E704', 'W503'))
        result = pep8style.check_files(PEP8_CHECK_FILES)

        report_output = "Found code style errors (and warnings):"
        for code in result.messages:
            message = result.messages[code]
            count = result.counters[code]
            report_output += "\n" + code + ": " + message + " (" + str(count) + ")"

        self.assertEqual(result.total_errors, 0, report_output)


# hijack module, detect any restricted calls. Terminated test if detected
# hijack.hijack(a1)

if __name__ == "__main__":
    unittest.main(exit=False, verbosity=2)
