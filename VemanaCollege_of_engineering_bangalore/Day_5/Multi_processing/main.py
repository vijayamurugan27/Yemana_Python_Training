import multiprocessing as mp
import time
import math


results_a = []
results_b = []
results_c = []



def make_calculation1(numbers):
    for number in numbers:
        results_a.append(math.sqrt( number **4))


def make_calculation2(numbers):
    for number in numbers:
        results_b.append(math.sqrt( number **16))


def make_calculation3(numbers):
    for number in numbers:
        results_c.append(math.sqrt( number **20))



if __name__ == "__main__":
    number_list = list(range(5000000))

    # for multiprocessing
    p1 = mp.Process(target=make_calculation1, args=(number_list,))
    p2 = mp.Process(target=make_calculation2, args=(number_list,))
    p3 = mp.Process(target=make_calculation3, args=(number_list,))

    temp_a = results_a
    temp_b = results_b
    temp_c = results_c

    start = time.time()
    p1.start()
    p2.start()
    p3.start()
    end = time.time()
    print("For multi processing time :",end-start)

    # for normal processing.
    start1 = time.time()
    make_calculation1(number_list)
    make_calculation2(number_list)
    make_calculation3(number_list)
    end1 = time.time()

    print( "For normal processing time :" ,end1 - start1)

    print(temp_a==results_a)
    print(temp_b==results_b)
    print(temp_c == results_c)

