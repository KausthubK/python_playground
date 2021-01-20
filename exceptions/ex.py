try:
    a = 1/0
except Exception as e:
    print("EXCEPTION!")
    print(e)
    with open('./file_error_1.log', 'w') as f:
        f.write("EXCEPTION!\n")
        f.write(str(e))

try:
    l = [1, 2, 3]
    l[4]
except Exception as e:
    with open('./file_error_2.log', 'w') as f:
        f.write("EXCEPTION!\n")
        f.write(str(e))