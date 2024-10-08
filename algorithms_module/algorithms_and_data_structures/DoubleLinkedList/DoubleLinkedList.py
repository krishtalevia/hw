from __future__ import annotations

class Node:
    def __init__(self, data: any):
        self.data = data
        self.prev = None
        self.next = None

class DoubleLinkedList:
    def __init__(self):
        self.__head = None
        self.__tail = None
        self.__count = 0

    def is_empty(self) -> bool:
        if self.__head is None:
            return True

        return False

    def add_back(self, data) -> None:
        new_node = Node(data)
        if self.is_empty():
            self.__head = new_node
            self.__tail = new_node
        else:
            self.__tail.next = new_node
            new_node.prev = self.__tail
            self.__tail = new_node

        self.__count += 1

    def add_front(self, data) -> None:
        new_node = Node(data)
        if self.is_empty():
            self.__head = new_node
            self.__tail = new_node
        else:
            new_node.next = self.__head
            self.__head.prev = new_node
            self.__head = new_node

        self.__count += 1

    def remove(self, data: any) -> bool:
        iterator = self.__head

        while iterator is not None:
            if iterator.data == data:
                if iterator == self.__head:
                    self.__head = iterator.next
                    self.__head.prev = None

                elif iterator == self.__tail:
                    self.__tail = iterator.prev
                    self.__tail.next = None

                else:
                    iterator.prev.next = iterator.next
                    iterator.next.prev = iterator.prev

                self.__count -= 1
                return True

            iterator = iterator.next

    def find(self, data: any) -> bool:
        iterator = self.__head

        while iterator is not None:
            if iterator.data == data:
                return True
            iterator = iterator.next

        return False

    def get_head(self):
        return self.__head

    def __str__(self) -> str:
        elements = []
        iterator = self.__head
        while iterator is not None:
            elements.append(str(iterator.data))
            iterator = iterator.next
        return ' <-> '.join(elements)