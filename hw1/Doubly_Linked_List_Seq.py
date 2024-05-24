class Doubly_Linked_List_Node:
    def __init__(self, x):
        self.item = x
        self.prev = None
        self.next = None

    def later_node(self, i):
        if i == 0: return self
        assert self.next
        return self.next.later_node(i - 1)

class Doubly_Linked_List_Seq:
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        node = self.head
        while node:
            yield node.item
            node = node.next

    def __str__(self):
        return '-'.join([('(%s)' % x) for x in self])

    def build(self, X):
        for a in X:
            self.insert_last(a)

    def get_at(self, i):
        node = self.head.later_node(i)
        return node.item

    def set_at(self, i, x):
        node = self.head.later_node(i)
        node.item = x

    def insert_first(self, x):
        new_node = Doubly_Linked_List_Node(x)
        if self.head is None:
            self.head = new_node 
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    def insert_last(self, x):
        new_node = Doubly_Linked_List_Node(x)
        if self.head is None:
            self.head =new_node
            self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node


    def delete_first(self):
        if self.head is None:
            return
        elif self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = None
        return self


    def delete_last(self):
        if self.head is None:
            return
        elif self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None
        return self

    def remove(self, x1, x2):
        L2 = Doubly_Linked_List_Seq()
        L2.head = x1
        L2.tail = x2
        #check on L1 head:
        if self.head == x1:
            self.head = x2.next 
            if self.head:
                self.head.prev = None
        else:
            x1.prev.next = x2.next
        #check on L2 tail:
        if self.tail == x2:
            self.tail = x1.prev 
            if self.tail:
                self.tail.next = None 
        else: 
            x2.next.prev = x1.prev
        #detach L2 from L1:
        x1.prev = None 
        x2.next = None
        return self

    def splice(self, x, L2):
        if L2.head is None:
            return
        if self.head is None:
            if L2 is None:
                return None
            else:
                self.head = L2.head
                self.tail = L2.tail
                L2.head = None
                L2.tail = None
                return
       
        else:
            y1= L2.head
            y2 = L2.tail
            xn = x.next
            x.next = y1
            print(f"Splicing after node with item {x.item}")
            print(f"L2 head item: {y1.item}, L2 tail item: {y2.item}")
            y1.prev = x
            if x == self.tail:
                self.tail = y2
            else:
                xn.prev = y2
                y2.next = xn
            L2.head = None
            L2.tail = None 
            return
            
#added test case:
def test_insert_first():
    dll = Doubly_Linked_List_Seq()
    dll.insert_first(10)
    assert dll.head.item == 10
    assert dll.tail.item == 10
    assert dll.head.prev is None
    assert dll.head.next is None
    
    dll.insert_first(20)
    assert dll.head.item == 20
    assert dll.tail.item == 10
    assert dll.head.next.item == 10
    assert dll.head.prev is None
    assert dll.tail.prev.item == 20
    assert dll.tail.next is None
    
    print("test_insert_first passed!")

def test_insert_last():
    dll = Doubly_Linked_List_Seq()
    dll.insert_last(10)
    assert dll.head.item == 10
    assert dll.tail.item == 10
    assert dll.head.prev is None
    assert dll.head.next is None
    
    dll.insert_last(20)
    assert dll.head.item == 10
    assert dll.tail.item == 20
    assert dll.head.next.item == 20
    assert dll.head.prev is None
    assert dll.tail.prev.item == 10
    assert dll.tail.next is None
    
    print("test_insert_last passed!")

def test_delete_first():
    dll = Doubly_Linked_List_Seq()

    # Test deleting from an empty list
    dll.delete_first()
    assert dll.head is None
    assert dll.tail is None

    # Test deleting the only element in the list
    dll.insert_first(10)
    dll.delete_first()
    assert dll.head is None
    assert dll.tail is None

    # Test deleting the first element from a list with multiple elements
    dll.insert_last(10)
    dll.insert_last(20)
    dll.insert_last(30)
    dll.delete_first()
    assert dll.head.item == 20
    assert dll.head.prev is None
    assert dll.head.next.item == 30
    assert dll.tail.item == 30

    # Test deleting the first element again
    dll.delete_first()
    assert dll.head.item == 30
    assert dll.head.prev is None
    assert dll.head.next is None
    assert dll.tail.item == 30

    # Test deleting the first element to empty the list
    dll.delete_first()
    assert dll.head is None
    assert dll.tail is None


    print("test_delete_first passed!")

def test_delete_last():
    dll = Doubly_Linked_List_Seq()
    dll.insert_last(10)
    dll.insert_last(20)
    dll.insert_last(30) #10-20-30
    dll.delete_last()
    assert dll.tail.item == 20
    print("passed delete last test!")

def test_splice():
    dll1 = Doubly_Linked_List_Seq()
    dll2 = Doubly_Linked_List_Seq()

    # Build the first list
    dll1.build([1, 2, 3])
    # Build the second list
    dll2.build([4, 5, 6])

    # Get reference to the node in dll1 where we want to splice dll2
    x = dll1.head.later_node(1)  # This should be the node with item 2

    # Splice dll2 into dll1 after the node with item 2
    dll1.splice(x, dll2)

    # Check the contents of dll1 after splicing
    assert list(dll1) == [1, 2, 4, 5, 6, 3], f"Expected [1, 2, 4, 5, 6, 3] but got {list(dll1)}"
    assert dll2.head is None and dll2.tail is None, "dll2 should be empty after splicing"

    # Check the links in dll1 to ensure the integrity of the doubly linked list
    node = dll1.head
    while node.next:
        assert node.next.prev == node, "The next node's prev should point to the current node"
        node = node.next

    print("test_splice passed!")

def run_all_tests():
    test_insert_first()
    test_insert_last()
    test_delete_first()
    test_delete_last()
    test_splice()

run_all_tests()                                                                                             