def nr_increases(arr):
    x = sum([arr[x + 1] > arr[x] for x in range(len(arr) - 1)])
    print('nr increases:', x)

with open('1_input.txt') as f: 
    arr = [int(x) for x in f.readlines()]

nr_increases(arr)

sum3_values = [arr[x] + arr[x+1] + arr[x+2] for x in range(len(arr) - 2)]
nr_increases(sum3_values)
