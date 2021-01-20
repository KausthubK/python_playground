import os
from os.path import dirname, isfile, isdir
import shutil

os.system('mkdir -p test/a test/b test/c test/d && touch test/a/file.txt && touch test/b/file.txt')

shutil.rmtree("test")

os.system('mkdir -p test/a test/b test/c test/d && touch test/a/file.txt && touch test/b/file.txt')

os.remove('test/a/file.txt')
os.remove('test/b/file.txt')

if isfile('test/c/file.txt'):
    os.remove('test/c/file.txt')
else:
    print("Not a file otherwise this would fail!")

if isdir("test"):
    shutil.rmtree("test")
else:
    print("Not a dir otherwise this would fail!")

if isdir("test"):
    shutil.rmtree("test")
else:
    print("Not a dir otherwise this would fail!")

if isdir("test-blah"):
    shutil.rmtree("test-blah")
else:
    print("Not a dir otherwise this would fail!")

print("If you got here then it works...")
