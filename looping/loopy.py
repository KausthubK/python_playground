arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

print(arr)

chunk_size = 4
chunks = (len(arr) - 1) // chunk_size + 1
for i in range(chunks):
     batch = arr[i*chunk_size:(i+1)*chunk_size]
     print(batch)
