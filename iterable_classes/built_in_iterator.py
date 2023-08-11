class ItemLoader:
    """
    A class that contains information that needs to be delivered bit by bit.
    
    iterate via generator.

    Usage:
    """
    def __init__(self):
        self.items = [1, 2, 3, 4, 5]
        self.__next_idx = 0

    def __iter__(self):
        return iter(self.items)
    
    def __next__(self):
        return self.next()

    def next(self):
        if self.__next_idx < len(self.items):
            ret_item, self.__next_idx = self.items[self.__next_idx], self.__next_idx + 1
            return ret_item
        raise StopIteration()
        
    
