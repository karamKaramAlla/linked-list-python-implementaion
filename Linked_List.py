class Linked_List:
    __length = 1

    def __init__(self, head_data, tail_data="tail"):
        self.tail = self.Node(data=tail_data,nxt=None)
        self.head = self.Node(data=head_data,nxt=self.tail)

    def length(self):
        #returns the length of the linked list
        return self.__length
    def search_for(self,data):
        ''' a function that gets the data as a parameter and returns the node if it's found '''

        for i in range(0,self.__length()):
            if self.get_node(i).data == data :
                return self.get_node(i)

        return f"{data} is not found"

    def get_node(self, index):
        if index > self.__length:
            raise IndexError(" Linked List index out of range ")

        node = self.head

        i = 0
        while i < index:
            i += 1
            node = node.nxt

        return node

    def add(self,*nodes):
        for node in nodes:
            self.__add_node(node)

    def __add_node(self, data: object, index = -10) -> object:

        """
            a function that  adds a new element to the linked list
            taking the index that the element will be stored at
            the data of the element (it could be any type of data)
            if the index passed is greater than the lenght of the list
            it will raise an error.
            if there is no index passed it will add the element just before the tail node.
            when the function is called the count var increases by one to determain the lenght of the Linked List

        """

        if index == -10:
            index = self.__length

        self.__length += 1
        node = self.Node(data, self.get_node(index))
        self.get_node(index-1).nxt = node

    def pop(self):#deletes the last node before the tail

        self.delete(self.__length-1)
    def delete(self, index):
        #deletes a node with a given index

        self.get_node(index - 1).nxt = self.get_node(index + 1)
        self.__length -= 1

    def print_node(self, index):

        print(self.get_node(index).data)

    class Node:
        ''' a function that creates a node to be added to the linked list. '''
        def __init__(self, data, nxt):
            self.nxt = nxt
            self.data = data
