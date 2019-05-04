from node import Node
class SingleLinkedList():
    ''' represents a single linked list'''
    def __init__(self):
        '''(SingleLinkedList) ->NoneType
        initializes the references of an empty SLL'''
        self._size = 0
        self._head = None
        self._tail = None
    def get_head(self):
        ''' (SingleLinkedList)->Node
        returns the pointer to the head of the list'''
        return self._head
    def get_tail(self):
        ''' (SingleLinkedList)->Node
        returns the pointer to the tail of the list'''
        return self._tail
    def set_head(self, new_head):
        ''' (SingleLinkedList, Node)->NoneType
        set the head to point to the new_head'''
        self._head = new_head
    def set_tail(self, new_tail):
        ''' (SingleLinkedList, Node)->NoneType
        set the tail to point to the new_tail'''
        self._tail = new_tail
    
    
    def is_empty(self):
        '''(SingleLinkedList) -> bool
        returns true if no item is in this SLL'''
        return self._size == 0
    
    def size(self):
        '''(SingleLinkedList) -> int
        returns the number of items in this SLL'''
        return self._size
    
    def add_first(self, element):
        '''(SingleLinkedList, obj) -> NoneType
        adds a node to the first of the SLL'''
        # create a node that point to the head
        node = Node(element, self._head)
        # let head point to the node
        self._head = node
        # if this node is the first node in this SLL, tail should point to this node too
        if (self._size == 0):
            self._tail = node
        # increment the size
        self._size += 1
   
    def add_last(self, element):
        '''(SingleLinkedList, obj) -> NoneType
        adds a node to the end of this SLL'''
        # create a node with the given element that points to None
        node = Node(element, None)
        if (self._tail != None):
            # let the _next part of the tail to point to newly created node
            self._tail.set_next(node)
            #let tail to point to the added node
        self._tail = node
            # if this node is the first node in this SLL, let head to point to this node too
        if (self._size == 0):
            self._head = node
        # increment the size
        self._size += 1
        
    def remove_first(self):
        '''(SingleLinkedList, obj) -> obj
        remvoe the node from the head of this SLL and returns the element stored in this node'''
        # sset element to None in case SLL was empty
        element = None
        # if SLL is not empty
        if (self._head is not None):
            # get the first node
            node = self._head
            # let head point to the second node
            self._head = self._head.get_next()
            # decrement the size
            self._size -= 1
            #set the _next of previous head to point to None (for garbage collection purpose)
            node.set_next(None)
            # get the element stored in the node
            element = node.get_element()
        #return the element of the removed node
        return element
            
    def __str__(self):
        '''(SingleLinkedList) -> str
        returns the items in the SLL in a string form
        '''
        # define a node, which points to the head
        cur = self._head
        # define an empty string to be used as a container for the items in the SLL
        result = ""
        # loop over the SSL until you get to the end of the SSL
        while (cur is not None):
            # get the element of the current node and attach it to the final result
            result = result + str(cur.get_element())  + ", "
            # proceed to next node
            cur = cur.get_next()
        return "(" + result[:-2] + ")"

if(__name__ == "__main__"):
    first_node = Node("A")
    print(first_node)
    second_node = Node("B", first_node)
    print(second_node)
    # the address of first_node is what we hold in second_node._next
    print(hex(id(first_node)))
    
    my_ll = SingleLinkedList()
    print(my_ll.remove_first())
    print(my_ll)
    my_ll.add_first("A")
    my_ll.add_last("B")
    my_ll.add_first("C")
    my_ll.add_last("D")
    print(my_ll)
    print(my_ll.remove_first())
    print(my_ll)

            
        
        
        
        








