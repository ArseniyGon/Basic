import copy


class Node:

    # Function to initialise the node object
    def __init__(self, data):
        self.data = data  # Assign data
        self.next = None  # Initialize next as null


# Linked List class contains a Node object
class LinkedList:

    # Function to initialize head
    def __init__(self):
        self.head = None

    # This function prints contents of linked list
    # starting from head
    def printList(self):
        temp = self.head
        while (temp):
            print(temp.data)
            temp = temp.next


# Code execution starts here
if __name__ == '__main__':
    # Start with the empty list
    llist = LinkedList()

    llist.head = Node(1)
    second = Node(2)
    third = Node(3)

    llist.head.next = second;  # Link first node with second
    second.next = third;  # Link second node with the third node

    llist.printList()

def somef(a):
    a + 1
x = 10 #[__]
somef(x) # создается копия, передается только значение(копия)
print(x)

def somef2(y):          # изменяемые (словари, сеты, массивы)
    y.update({"color": "red"})
thisdict = {
        "brand": "Ford",
        "model": "Mustang",
        "year": 1964
    }
somef2(thisdict)  # работаем с оригиналом, передается ссылка
print(thisdict)

r1 = []  #[__]   [__]

r2 = [1,2,r1]

r3 = copy.deepcopy(r2)
# r3 = copy.copy(r2)


r1.append(1)

print(r3)