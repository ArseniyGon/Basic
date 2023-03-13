from abc import ABC, abstractmethod


class Move(ABC):
    @abstractmethod
    def piece_moves(self):
        pass

class Item(Move):
    def piece_moves(self):
        print("Object moves")
obj1 = Item()
obj1.piece_moves()
