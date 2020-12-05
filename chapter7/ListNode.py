class List:
    def __init__(self, head = None, tail = None):
        self.head = head
        self.tail = tail
    
    def search_list(self, key):
        temp = self.head
        while temp and temp.data != key:
            temp = temp.next
        return temp


    # This takes O(n) space because a new linked list is created with the values from the first two linked lists
    # however it preserves the original lists
    def merge_sorted_lists_preserved(list1, list2):
        list1_temp = list1.head
        list2_temp = list2.head
        new_list = List()
        if list1_temp.data < list2_temp.data:
            new_list.head = Node(list1_temp.data)
            list1_temp = list1_temp.next
        else:
            new_list.head = Node(list2_temp.data)
            list2_temp = list2_temp.next
        temp = new_list.head
        while list1_temp and list2_temp:
            if list1_temp.data < list2_temp.data:
                temp.next = Node(list1_temp.data)
                list1_temp = list1_temp.next
            else:
                temp.next = Node(list2_temp.data)
                list2_temp = list2_temp.next
            temp = temp.next

        # think the above is ok
        if list1_temp is None:
            while list2_temp.next is not None:
                temp.next = Node(list2_temp.data)
                temp = temp.next
                list2_temp = list2_temp.next
            new_list.tail = temp
            new_list.tail.next = None
        else:
            while list1_temp is not None:
                temp.next = Node(list1_temp.data)
                temp = temp.next
                list1_temp = list1_temp.next
            new_list.tail = temp
            new_list.tail.next = None
        return new_list
        

    # Implement in place merge which only takes O(1) space
    def merge_sorted_lists_together(L1, L2):
         
        temp_change = None
        if list1_temp.data < list2_temp:
            temp = L1.head
        else:
            temp = L2.head

        temp_list1 = L1.head
        temp_list2 = L2.head
        while temp:


        

class Node:
    def __init__(self, data = 0, next = None):
        self.data = data
        self.next = next

    def insert_node(node, new_node):
        new_node.next = node.next
        node.next = new_node

    def delete_node(node):
        if node.next is None:
            node = None
        else:
            node.data = node.next.data
            node.next = node.next.next

a = Node(2)
b = Node (1, a)
c = Node(0, b)

d = Node(7)
e = Node(6, d)
f = Node(5, e)



temp = c

L = List(c, a)

L2 = List(f, e)

N = List.merge_sorted_lists(L, L2)

temp = N.head

while temp:
    print(temp.data)
    temp = temp.next




