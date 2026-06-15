
#Closures

def multiplication_table_generator(n):
    def multiplication_table(limit):
        for i in range(limit):
            print(f"{n} x {i} = {n*i}")
    return multiplication_table

two_multiplication_table = multiplication_table_generator(2)
seven_multiplication_table = multiplication_table_generator(7)
hundred_multiplication_table = multiplication_table_generator(100)

two_multiplication_table(20)
seven_multiplication_table(20)
hundred_multiplication_table(20)