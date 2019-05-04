from Contact import *
from week2_container import *
"""
CSCA48 Assignment 2, Summer 2018
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
Name: Yu-Hsiang Mou
UtorID: mouyuhsi
Student Number: 1004334669
Date: July 26, 2018
"""
MAX_KEY = 3


class MSTNode():
    def __init__(self, key, value):
        ''' (MSTNode, str, Contact) -> NoneType
        Construct an MST node by the given key and value
        REQ: must have a key and value when initialize a MSTNode'''
        self._parent = None
        self._key = []
        self._value = []
        self._child = [None, None, None, None]
        self._key.append(key)
        self._value.append([value])
    # insert your code for MSTNode below this line

    def add(self, contact):
        ''' (self, Contact/list of Contact) -> NoneType
        Given a contact, add it to the node while assuming no overflows
        (if given a list of contact, add them one by one)
        '''
        # if the 'contact' is given as a list of contacts, add each one
        # individually (uses recursion)
        if isinstance(contact, list):
            for C in contact:
                self.add(C)

        # check if contact is of type Contact
        elif isinstance(contact, Contact):
            # get the first letter of the contact's name as the key k
            k = contact.get_name()[0].upper()
            # get the key list
            keys = self._key
            # get the length of the keys
            length = len(keys)
            # get the value list
            values = self._value
            # add the contact to the list that corresponds to the key k
            if k in keys:
                # get the index of the key
                i = keys.index(k)
                # append the contact to the right list indicated by the index
                self.add_value(i, contact)

            else:
                # add the first letter as 'key' and add itself as 'value'
                # when k is not in the key list

                # if k is smaller than the first key, insert k and value to
                # the front (of the corresponding lists)
                if k < keys[0].upper():
                    keys.insert(0, k)
                    values.insert(0, [contact])

                # if there is only one key or k is greater than the first key
                # but smaller than the second key, insert k and value between
                # 'first and second items' (of the corresponding lists)
                elif (length < 2 or keys[0].upper() < k < keys[1].upper()):

                    keys.insert(1, k)
                    values.insert(1, [contact])
                # if there are only two keys or k is greater than the second
                # key but smaller than the third key, insert k and value
                # between the 'second and the third items' (of the
                # corresponding lists)
                elif length < 3 or keys[1].upper() < k < keys[2].upper():
                    keys.insert(2, k)
                    values.insert(2, [contact])

                # if none of the above, then append k and value to the end of
                # the corresponding lists
                else:
                    keys.append(k)
                    values.append([contact])

    def set_child(self, node, index):
        '''  (MSTNode, MSTNode, int) -> NoneType
        Given an index and a node, set the child at that index to be the node.
        REQ: -1 < index < 4
        '''
        self._child[index] = node

    def add_child(self, node):
        ''' (MSTNode, MSTNode) -> NoneType
        Add the node to the child list by replacing the one of the 'None' child
        (this method is used when at least one child is None)
        '''
        # get the child list
        children = self._child
        # check if there is at least one None in the list
        if None in children:
            # get the index of the first None
            index = children.index(None)
            # replace the None with the node
            children.pop(index)
            children.insert(index, node)

    def remove_child(self, index):
        ''' (MSTNode, int) -> NoneType
        Remove the child at the given index
        REQ: -1 < index < 4
        '''
        self._child.pop(index)

    def delete_child(self):
        ''' (MSTNode) -> NoneType
        Delete one None child from the child list
        '''
        # get the child list
        children = self._child
        # check if at least one None is in the list
        if None in children:
            # get the index of the first None
            index = children.index(None)
            # delete it from the list
            children.pop(index)

    def get_child(self):
        ''' (MSTNode) -> list
        Returns the child list
        '''
        return self._child

    def erase_child(self, node):
        ''' (MSTNode, MSTNode) -> NoneType
        'Erase' the child that matches the node (set it back to None)
        '''
        # loop through the child list and 'erase' the one equal to the node
        # (by replacing it with None)
        children = self._child
        for index in range(len(children)):
            if node == children[index]:
                children[index] = None

    def get_value(self):
        ''' (MSTNode) -> list
        Returns the value list
        '''
        return self._value

    def set_value(self, index, v):
        ''' (MSTNode, int, list of contacts) -> NoneType
        Given an index and a value (contact list), sets the value at the index
        REQ: -1 < index < 4
        '''
        self._value[index] = v

    def add_value(self, index, C):
        ''' (MSTNode, int, Contact) -> NoneType
        Given an index and a contact, add the contact to the value list at the
        index and in alphabetical order
        REQ: -1 < index < 4
        '''
        # get the contact list at the index (of the value list)
        value = self._value[index]
        # append the Contact
        value.append(C)
        # sorted the contact list (case-insensitive, sorted by the name)
        value.sort(key=lambda contact: contact.get_name().casefold())

    def get_key(self):
        ''' (MSTNode) -> list
        Returns the key list
        '''
        return self._key

    def set_key(self, index, k):
        ''' (MSTNode, int, int) -> NoneType
        Given an index and a key, sets the key at that index
        REQ: -1 < index < 4
        '''
        self._key[index] = k

    def get_parent(self):
        ''' (MSTNode) -> MSTNode
        Returns the reference to the parent node
        '''
        return self._parent

    def set_parent(self, node):
        ''' (MSTNode, MSTNode) -> NoneType
        Given a node, sets the parent to be that node
        '''
        self._parent = node

    def __eq__(self, mst_node):
        ''' (MSTNode, MSTNode) -> bool
        Returns True if and only if the two nodes containing the same key and
        values, points to the same children, and have the same parent
        '''
        # starts with True, will become False if any one of the conditions is
        # not met (equivalently, any conditions below is met)
        result = True

        # False if the mst_node is not a MSTNode (e.g. None)
        if not isinstance(mst_node, MSTNode):
            result = False
        else:
            # return True if each one of the attributes in self is equal to the
            # one correspond to it in mst_node

            # False if keys or values are not equal
            if not self.equal(mst_node):
                result = False

            # False if their children are not equal
            elif self._child != mst_node.get_child():
                result = False

            # if only one of them is None then it is False
            elif self._parent is None and mst_node.get_parent() is not None:
                result = False

            # check the equality between the parents
            elif self._parent is not None:
                if not self._parent.equal(mst_node.get_parent()):
                    return False

        return result

    def equal(self, mst_node):
        ''' (MSTNode, MSTNode) -> bool
        Returns True if and only if the two nodes contain same keys and values
        '''
        # return False if the mst_node is not a MSTNode (e.g. None)
        # (this comparison will always be False)
        if not isinstance(mst_node, MSTNode):
            return False

        else:
            # get the contact lists inside the value lists
            value1 = self._value
            value2 = mst_node.get_value()
            # get the length of the two value lists
            length1 = len(value1)
            length2 = len(value2)
            # return False if the lengths (or the key lists) are not equal
            if length1 != length2 or self._key != mst_node.get_key():
                return False

            else:
                # initiate two queues to store contacts (one for each node)
                contacts1 = Queue()
                contacts2 = Queue()
                # return False if the lengths of the lists are not equal
                for i in range(length1):
                    if len(value1[i]) != len(value2[i]):
                        return False

                    else:
                        # put all the contacts into the corresponding queues
                        for contact in value1[i]:
                            contacts1.put(contact)

                        for contact in value2[i]:
                            contacts2.put(contact)

                # check the equality between contacts pair by pair while the
                #  queue is not empty (check one as both have equal amount)
                while not contacts1.is_empty():
                    # get the contacts from the queues
                    contact1 = contacts1.get()
                    contact2 = contacts2.get()
                    # get the names and phones of the contacts
                    # (comparison between names are case-insensitive)
                    name1 = contact1.get_name().upper()
                    name2 = contact2.get_name().upper()
                    phone1 = contact1.get_phone()
                    phone2 = contact2.get_phone()
                    # return False if names or phones are not the same
                    if name1 != name2 or phone1 != phone2:
                        return False

        # reaches here means the keys and values are all equal
        return True


class MST():
    def __init__(self, root):
        '''(MST, MSTNode) -> NoneType
        This class represents a Multiway Search Tree'''
        self._root = root
    # insert your code for MST below this line

    def get_root(self):
        ''' (MST) -> MSTNode
        Returns the root of the tree
        '''
        return self._root

    def set_root(self, node):
        ''' (MST, MSTNode) -> NoneType
        Set the _root to be a new node
        '''
        self._root = node

    def search(self, k, v):
        ''' (MST, str, Contact) -> bool
        Given a key k and a value v, return a boolean indicating the presence
        of such entry (corresponding to the given info).
        '''
        # if the root is None, such entry will not exist
        if self._root is None:
            return False

        else:
            # (for comparison purpose, keys are stored in uppercase)
            k = k.upper()
            # get the name and phone number from the contact v
            name1 = v.get_name().upper()
            phone1 = v.get_phone()

            # initiate a queue to store nodes
            q = Queue()
            # put the root into the queue
            q.put(self._root)

            # use while loop to search over the nodes (of the tree)
            while not q.is_empty():
                # get the current node from the queue
                current = q.get()
                # return True if the key and value are present in the node
                if current is not None:
                    # get the key list
                    keys = current.get_key()
                    # check if k is in the list
                    if k in keys or k.lower() in keys:
                        # loop through the value list
                        for value in current.get_value():
                            # return True if the Contact v is 'in the list'
                            # (determine by looping through the value list
                            # and compare the contacts' names and phones)
                            for contact in value:
                                # get the name and phone number of the contact
                                name2 = contact.get_name().upper()
                                phone2 = contact.get_phone()
                                if name1 == name2 and phone1 == phone2:
                                    return True

                    # if the entry is not found (did not return True), then
                    # attempt to find it in the child nodes
                    # (put the right child to the queue)

                    # get the length of the key list
                    length = len(keys)
                    # get the children of the current node
                    nodes = current.get_child()
                    # if k is smaller than the first key, next node should be
                    # the first child of the current node
                    if k < keys[0].upper():
                        # put the 'first child' in the queue
                        q.put(nodes[0])

                    # if there is only one key or k is greater than the first
                    # key but smaller than the second key next node should be
                    # the second child of the current node
                    elif (length < 2 or keys[0].upper() < k < keys[1].upper()):
                        # put the 'second child' in the queue
                        q.put(nodes[1])
                    # if there are only two keys or k is greater than the
                    # second key but smaller than the third key, next node
                    # should be the third child of the current node
                    elif (length < 3 or keys[1].upper() < k < keys[2].upper()):
                        # put 'third child' in the queue
                        q.put(nodes[2])

                    # if none of the above, then next node should be the last
                    # child of the current node
                    else:
                        # put the 'last child' in the queue
                        q.put(nodes[3])

        # reaches here means the search fails
        return False

    def find(self, node, k):
        ''' (MST, MSTNode, str) -> MSTNode
        Given a key k, return the pointer to the node that holds the key k.
        Return None if it is not found. (note: this is a recursive method)
        '''
        # base case: return None when reaching None
        if node is None:
            return None

        else:
            # get the keys and children from the node
            keys = node.get_key()
            # get the length of the key list
            length = len(keys)
            nodes = node.get_child()
            # make k to be uppercased for comparison purpose
            k = k.upper()
            # base case: k is in the key list of the node
            if k in keys or k.lower() in keys:
                result = node

            # if k is smaller than the first key, then recursively find k in
            # the first child of the current node
            elif k < keys[0].upper():
                result = self.find(nodes[0], k)

            # if there is only one key or k is greater than the first key but
            # smaller than the second key, then recursively find k in the
            # second child of the current node
            elif length < 2 or keys[0].upper() < k < keys[1].upper():
                result = self.find(nodes[1], k)

            # if there are only two keys or k is greater than the second key
            # but smaller than the third key, recursively find k in the third
            # child of the current node
            elif length < 3 or keys[1].upper() < k < keys[2].upper():
                result = self.find(nodes[2], k)

            # if none of the above, then recursively find k in the last child
            # of the current node
            else:
                result = self.find(nodes[3], k)

            return result

    def insert(self, k, v):
        ''' (MST, str, Contact) -> NoneType
        Given a key k and a value v, insert an entry with k and v to the tree.
        '''
        # find the node that contains the given key
        node = self.find(self.get_root(), k)
        # check if such node exist
        if node is not None:
            # directly add the entry to the node
            node.add(v)

        else:
            # find the 'last node' where the search stops at
            node = self.find_bottom(self.get_root(), k)
            # add the entry to the appropriate place
            node.add(v)
            # initiate a variable stores index (default at the end of the list)
            index = -1
            # get the key list
            keys = node.get_key()
            # loop through the key list to find the index of k (just inserted)
            for key in keys:
                if key.lower() == k or key.upper() == k:
                    index = keys.index(key)

            # get the child list
            children = node.get_child()
            # insert a 'None child' in the right place
            # (there should be no child at that place after find_buttom)
            children.insert(index, None)

            # get the length of the key list
            length = len(keys)
            # remove the extra None if there is one when no overflow occurs
            if length < MAX_KEY+1:
                node.remove_child(index)

            # while overflow occurs (more than the max key, three keys)
            while length > MAX_KEY:
                # get the parent of the node
                parent = node.get_parent()
                # get the value list
                values = node.get_value()
                # get the child list
                children = node.get_child()

                # split the current node (because of overflow)
                # (L is the 'left side' and R is the 'right side')
                # left side contains the first two keys, along with the first
                # three children
                L = MSTNode(keys[0], None)
                L.set_value(0, values[0])
                L.add(values[1])
                L.add_child(children[0])
                L.add_child(children[1])
                L.add_child(children[2])

                # right side contains only the last key, along with the last
                # two children
                R = MSTNode(keys[3], None)
                R.set_value(0, values[3])
                R.add_child(children[3])
                R.add_child(children[4])

                # check if it is at the root
                if parent is None:
                    # create a new root above the 'overflow node' with the
                    # value correspond to the third key
                    root = MSTNode(keys[2], None)
                    root.set_value(0, values[2])
                    # update the root
                    self.set_root(root)
                    # now the parent of the node is the root
                    parent = root

                else:
                    # if it is not at the root, add the value correspond to
                    # the third key
                    parent.add(values[2])

                    '''
                    # 'erase' the old child (no longer the child)
                    parent.erase_child(node)
                    '''

                # get the index of the third key (which is added to the parent)
                index = parent.get_key().index(keys[2])
                # re-establish the child-parent relationship with R and L
                parent.set_child(L, index)
                parent.get_child().insert(index+1, R)
                L.set_parent(parent)
                R.set_parent(parent)
                # get the child lists
                L_children = L.get_child()
                R_children = R.get_child()
                # reset the parent of the children of the old node to L and R
                # if not None (as they are now the children of L or R)
                for child in L_children:
                    if child is not None:
                        child.set_parent(L)
                for child in R_children:
                    if child is not None:
                        child.set_parent(R)

                # now get the key list of the parent node, assign the length
                # to be of the parent node, and set the node to be its parent
                keys = parent.get_key()
                length = len(keys)
                node = parent

                # if no overflow occurs, remove the extra None at the end
                # otherwise the children will get split in the next iteration
                if length < 4:
                    node.remove_child(4)

    def find_bottom(self, node, k):
        ''' (MST, MSTNode, str) -> MSTNode
        Given a key k, return the pointer to the node that 'should' have the
        key k (but is not present). Used when find method fails.
        (note: this method should always start from the root)
        '''
        # base case: return None when reaching None
        if node is None:
            return None

        # get the key list from the node
        keys = node.get_key()
        # get the length of the key list
        length = len(keys)
        # get the child list from the node
        nodes = node.get_child()
        # make k to be uppercased for comparison purpose
        k = k.upper()

        # go through the shortest path and find the bottom node by attempting
        # to find k in the child node

        # if k is smaller than the first key, then recursively find k in the
        # first child of the current node
        if k < keys[0].upper():
            bottom = self.find_bottom(nodes[0], k)

        # if there is only one key or k is greater than the first key but
        # smaller than the second key, then recursively find k in the second
        # child of the current node
        elif length < 2 or keys[0].upper() < k < keys[1].upper():
            bottom = self.find_bottom(nodes[1], k)

        # if there are only two keys or k is greater than the second key but
        # smaller than the third key, recursively find k in the third child
        # of the current node
        elif length < 3 or keys[1].upper() < k < keys[2].upper():
            bottom = self.find_bottom(nodes[2], k)

        # if none of the above, then recursively find k in the last child of
        # the current node
        else:
            bottom = self.find_bottom(nodes[3], k)

        # when reaching None (the end of the path), the parent is the node we
        # are looking for (as if k exist, it should be in this bottom node)
        if bottom is None:
            return node

        # pass the bottom node
        return bottom

    def __eq__(self, mst_tree):
        ''' (MST, MST) -> bool
        Returns True if and only if two trees are the same
        (note: this must be implemented recursively)
        '''
        # get the roots of the trees
        root = self.get_root()
        mst_root = mst_tree.get_root()

        # return False if only one of the roots is None
        if root is None and mst_root is not None:
            return False

        # check whether the roots are equal
        elif root is not None:
            # the other case where only one of the roots is None
            if mst_root is None:
                return False

            else:
                # False if they are not equal
                if not root == mst_root:
                    return False

        else:
            # filter out where two roots are both None
            if root is not None and mst_root is not None:
                # get the subtrees from the roots
                subtrees = self.get_subtrees(root)
                mst_subtrees = mst_tree.get_subtrees(mst_root)
                # return True only when every subtrees equals
                return subtrees == mst_subtrees

        # return True as conditions are all met
        return True

    def get_subtree(self, node):
        ''' (MST, MSTNode) -> MST
        Given a node, return a MST that is rooted at the node
        '''
        return MST(node)

    def get_subtrees(self, node):
        ''' (MST, MSTNode) -> list of MST
        Given a node, return a list of MSTs that is rooted at the children of
        the node (in the order of the children list)
        '''
        # create an empty list to store subtrees
        subtrees = []
        # get the child list
        children = node.get_child()
        # loop through the child list
        for child in children:
            # append the MST rooted at the child to the subtree list
            subtrees.append(self.get_subtree(child))

        return subtrees

    def BFS(self):
        ''' (MST) -> str
        Returns a string representing the BFS traversal result of the tree.
        '''
        # initiate an empty string to store the string representation
        BFS = ''
        # initiate a variable for level
        level = 0

        # create a queue to store parent nodes
        q = Queue()
        # put the root into the queue
        q.put(self._root)
        # go over the nodes (of the tree) while the queue is not empty
        while not q.is_empty():
            # get the current node from the queue
            # create a list to store all the parent nodes
            node_list = []
            # put all the nodes from the queue to a list
            while not q.is_empty():
                # get the node from the queue
                node = q.get()
                if node is not None:
                    # add non-None node to the list
                    node_list.append(node)

            # create another queue to store child nodes
            Q = Queue()
            # create lists to store all the keys and values
            all_keys = []
            all_values = []
            # loop through the node list
            for node in node_list:
                # filter out any None (nodes)
                if node is not None:
                    # get the child list
                    children = node.get_child()
                    # add every non-None child of the parent node to the queue
                    for child in children:
                        if child is not None:
                            Q.put(child)

                    # get the keys and values from the parent node
                    keys = node.get_key()
                    values = node.get_value()
                    # append them all to their corresponding lists
                    for key in keys:
                        all_keys.append(key)
                    for value in values:
                        all_values.append(value)

            # create a list to store list of names
            name_lists = []
            # loop through the value lists (where value is a list of contacts)
            for value in all_values:
                # create a list to store names associated with one key
                name_list = []
                # loop through the contacts and append the names to the list
                for contact in value:
                    name_list.append(contact.get_name())
                # add the list of names to the name_lists
                name_lists.append(name_list)

            # (utilize 'double slicing' to 'interwine' key list and name_lists)
            # add two list together so that the length of the list is fixed
            k_and_n = all_keys + name_lists
            # assign keys to be at the even indices
            k_and_n[::2] = all_keys
            # assign name lists to be at the odd indices
            k_and_n[1::2] = name_lists
            # now every key is followed by a name list (corresponds to it)

            # construct the result string
            string = "Level_{}=[".format(str(level))
            # loop through the ordered list to get each pair (key and names)
            # (remove the single quote when getting string from the list)
            for index in range(0, len(k_and_n), 2):
                content = "{}:{}-".format(str(k_and_n[index].replace("'", "")),
                                          str(k_and_n[index+1]).replace("'",
                                                                        ""))

                # add them to the result string in order (left to right)
                string = string + content

            # add the string of this level to the BFS string
            BFS += (string[:-1] + "]" + "\n")

            # now replace the parent queue as the children are the next parents
            q = Q
            # increase the level by one
            level += 1

        return BFS

    def group_insert(self, contacts):
        ''' (MST, list of Contact) -> NoneType
        Given a list of contacts, insert them by the order of the list
        '''
        # loop through the contact list
        for contact in contacts:
            # the key is the first letter of the contact's name
            k = contact.get_name()[0]
            # insert it to the tree
            self.insert(k, contact)

            # can use self.BFS() to check the result after the insertion

    def check_child(self):
        ''' (self) -> (bool, int)
        Check the length of the child list of every node in the tree.
        '''
        # initiate a variable for level
        level = 0

        # create a queue to store parent nodes
        q = Queue()
        # put the root into the queue
        q.put(self._root)
        # go over the nodes (of the tree) while the queue is not empty
        while not q.is_empty():
            # create a list to store all the parent nodes
            node_list = []
            # put all the nodes from the queue to a list
            while not q.is_empty():
                # get the node from the queue
                node = q.get()
                if node is not None:
                    # add non-None node to the list
                    node_list.append(node)

            # create another queue to store child nodes
            Q = Queue()
            # loop through the node list
            for node in node_list:
                # get the child list
                children = node.get_child()
                if len(children) != 4:
                    return (False, level)
                # filter out any None (nodes)
                if node is not None:
                    # add every non-None child of the parent node to the queue
                    for child in children:
                        if child is not None:
                            Q.put(child)

            # now replace the parent queue as the children are the next parents
            q = Q
            # increase the level by one
            level += 1

        # if it goes through, then every child list has the right length
        return (True, level-1)
