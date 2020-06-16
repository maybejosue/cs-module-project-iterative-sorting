hello = [85, 46, 27, 81, 94, 9, 27, 38, 43, 99, 37, 63, 31, 42, 14]

print(hello)

current_value = 1
save_current_value = hello[1]
neighboring_value = 2
hello[current_value] = hello[neighboring_value]
hello[neighboring_value] = save_current_value
print(hello)
