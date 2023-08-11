from pytictoc import TicToc
t = TicToc()

def fn(x):
    return x*x

blah = [1, 2, 3, 4, 5, 6, 7, 8, 9]

t.tic()
blah_sq = [fn(x=b) for b in blah]
print(blah_sq)
t.toc()
