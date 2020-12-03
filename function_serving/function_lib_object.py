class FnLib():
    def __init__(self, which_processes: list):
        self.selected_processes = which_processes
        self.processes = {
            "process1": self.__proc1,
            "process2": self.__proc2
        }
    
    def forward(self, value: int):
        for sp in self.selected_processes:
            value = self.processes[sp](value)
        return value
    
    def __proc1(self, i: int):
        print("Process (1): " + str(i))
        return i+1
    
    def __proc2(self, i: int):
        print("Process (2): " + str(i))
        return i+1

fl = FnLib(which_processes=["process1", "process2"])
retval = fl.forward(value=10)
print(retval)