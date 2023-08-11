import ray
ray.init(address='auto')

from pytictoc import TicToc
t = TicToc()

@ray.remote
def fn(x):
    return x*x

blah = [1, 2, 3, 4, 5, 6, 7, 8, 9]

t.tic()
blah_sq_futures = [fn.remote(x=b) for b in blah]
print(ray.get(blah_sq_futures))
t.toc()
