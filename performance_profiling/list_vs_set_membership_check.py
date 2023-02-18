import pytictoc
import string
import random

string_len = 10
num_names = 100
names = []
for i in range(num_names):
    names.append(str(''.join(random.choices(string.ascii_uppercase + string.digits, k = string_len))))

name_set = set(names)

### Method A - List in a loop
def in_names_loop(l1: list):
    ret = []
    for i in range(len(l1)):
        ret.append(str(i) in l1)
    return ret

### Method C - Set in a loop
def in_names_set_loop(s1: set):
    ret = []
    for i in range(len(s1)):
        ret.append(str(i) in s1)
    return ret

### Method C - List with list comp
def in_names_list_comp(l1: list):
    ret = [str(i) for i in range(len(l1)) if str(i) in l1]
    return ret

### Method D - Set with list comp
def in_names_set_list_comp(s1: set):
    ret = [str(i) for i in range(len(s1)) if str(i) in s1]
    return ret


tickerA = pytictoc.TicToc()
tickerA.tic()
in_names_loop(l1=names)
print("Method A: in_names_loop")
tickerA.toc()


tickerB = pytictoc.TicToc()
tickerB.tic()
in_names_set_loop(s1=name_set)
print("Method B: in_names_set_loop")
tickerB.toc()

tickerC = pytictoc.TicToc()
tickerC.tic()
in_names_list_comp(l1=names)
print("Method C: in_names_list_comp")
tickerC.toc()


tickerD = pytictoc.TicToc()
tickerD.tic()
in_names_set_list_comp(s1=name_set)
print("Method D: in_names_set_list_comp")
tickerD.toc()
