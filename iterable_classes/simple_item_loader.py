class SimpleItemLoader:
    """
    A simple iterable class:

    Usage via for loop:
    >>>sil = SimpleItemLoader()
    >>>for item in sil:
           print(item)

    Usage via next():
    >>>sil = SimpleItemLoader()
    >>>sil_iter = iter(sil)
    >>>next(sil_iter)
    """
    def __init__(self):
        self.items = [1, 2, 3, 4, 5]

    def __iter__(self):
        return iter(self.items)
    
