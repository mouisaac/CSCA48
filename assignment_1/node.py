class Node():
    '''represents a node as a building block of a single linked list'''

    def __init__(self, element, next_node=None):
        '''(Node, obj, Node) -> NoneType
        construct a node as building block of a single linked list'''

        self._element = element
        self._next = next_node

    def set_next(self, next_node):
        '''(Node, Node) -> NoneType
        set node to point to next_node'''
        self._next = next_node

    def set_element(self, element):
        '''(Node, obj) ->NoneType
        set the _element to a new value'''
        self._element = element

    def get_next(self):
        '''(Node) -> Node
        returns the reference to next node'''
        return self._next

    def get_element(self):
        '''(Node) -> obj
        returns the element of this node'''
        return self._element

    def __str__(self):
        '''(Node) -> str
        returns the element of this node and the reference to next node'''
        return "(" + str(self._element) + ", " + str(hex(id(self._next))) + ")"


if (__name__ == "__main__"):
    a = Node("A")
    print(a)
    b = Node("B")
    print(hex(id(b)))
    a.set_next(b)
    print(a)
