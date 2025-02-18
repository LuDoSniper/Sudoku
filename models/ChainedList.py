from __future__ import annotations

class ChainedList:
    def __init__(self, data: dict, prev: ChainedList|None = None, next: ChainedList|None = None) -> None:
        self.__data = data
        self.__prev = prev
        self.__next = next
    
    # Getter / Setter
    def get_data(self) -> dict:
        return self.__data
    def set_data(self, data: dict) -> None:
        self.__data = data
    
    def get_prev(self) -> ChainedList|None:
        return self.__prev
    def set_prev(self, prev: ChainedList|None) -> None:
        self.__prev = prev
    
    def get_next(self) -> ChainedList|None:
        return self.__next
    def set_next(self, next: ChainedList|None) -> None:
        self.__next = next
    
    # Methods
    def get_size(self) -> int:
        """
        Retourne la taille de la liste chaînée.
        """
        current = self
        size = 0
        while current is not None:
            size += 1
            current = current.get_next()
        return size

    def append(self, data: dict) -> None:
        """
        Ajoute un élément à la fin de la liste chaînée.
        """
        new = ChainedList(data, self)
        current = self
        while current.get_next() is not None:
            current = current.get_next()
        new.set_prev(current)
        current.set_next(new)
    
    def pop(self, index: int = -1, data: bool = True) -> dict|ChainedList:
        """
        Enlève le dernier élément de la liste chaînée et le retourne.
        Retourne la data si data = True ou retourne l'objet ChainedList si data = False.
        """
        if index < 0:
            index = self.get_size() + index

        current = self
        i = 0
        while i < index:
            if current.get_next() is None:
                raise IndexError("Index out of range")
            current = current.get_next()
            i += 1
        if i > 0:
            current.get_prev().set_next(current.get_next())
            if i < self.get_size() - 1:
                current.get_next().set_prev(current.get_prev())
        else:
            current.get_next().set_prev(None)
        current.set_prev(None)
        current.set_next(None)
        if data:
            return current.get_data()
        return current
