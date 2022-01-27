# normal function

def square(input_nums):
    result = []
    for num in input_num:
        res = num * num
        result.append(res)
    return result


input_num = [1, 2, 3, 4, 5]
squared_output = square(input_num)
print("result :", squared_output)


# output: result : [1, 4, 9, 16, 25]

# generator function

def square_generator(input_nums):
    for num in input_nums:
        res = num * num
        yield res


input_num = [1, 2, 3, 4, 5]
sq_gen = square_generator(input_num)
print(sq_gen)
for i in range(len(input_num)):
    sq_num = next(sq_gen)
    print(sq_num)

'''
output :
<generator object square_generator at 0x0000026056C87360>
1
4
9
16
25
'''