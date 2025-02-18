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
    
    def pop(self, index: int = -1, data: bool = True) -> tuple[ChainedList, dict|ChainedList]:
        """
        Enlève l'élément à l'index spécifié de la liste chaînée et retourne un tuple de cette forme : (head, <data>)
        où <data> est élément.data si data = True ou l'objet ChainedList popé si data = False.
        """

        # Convertir l'index négatif en index positif
        if index < 0:
            index = self.get_size() + index
        
        # Cas du premier élément
        if index == 0:
            if data:
                return (self.get_next(), self.get_data())
            return (self.get_next(), self)
        
        # Cas des autres éléments
        head = self
        current = self
        i = 0
        while i < index:
            try:
                current = current.get_next()
            except Exception:
                raise IndexError("Index out of range")
            i += 1
        
        prev = current.get_prev()
        next = current.get_next()
        prev.set_next(next)
        if next:
            next.set_prev(prev)

        if data:
            return (head, current.get_data())
        return (head, current)

    def remove(self, index: int = -1) -> None:
        """
        Sert à supprimer la queue
        """
        current = self
        
        if self.get_next is None:
            self = None

        if index == -1:
            
            while current.get_next != None:
                previous = current
                current = current.get_next

            previous.set_next = None
        
        else:
            i = 0
            while i < index:
                current = current.get_next
            next = current.get_next
            prev = current.get_prev
            prev.set_next(next)

    
    def __str__(self):
        # Retourne la représentation en chaîne de caractères de la donnée du noeud actuel
        return str(self.get_data())