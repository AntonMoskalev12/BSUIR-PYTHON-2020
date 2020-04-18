# Открытие файла
import sys
import argparse


def createparser():
    pars = argparse.ArgumentParser()
    pars.add_argument('-filename', '--path', type=open)
    pars.add_argument('-task', '--tasknumber', type=int)
    return pars


parser = createparser()
namespace = parser.parse_args(sys.argv[1:])
if namespace.path:
    line = [line.strip() for line in namespace.path]
else:
    with open('D:\\Games\\text1.txt', 'r') as somefile:
        line = [line.strip() for line in somefile]


def dictionary_placement(strings):
    dictionary = {}
    for e in strings:
        if e in dictionary:
            dictionary[e] += 1
        else:
            dictionary[e] = 1
    return dictionary


# 1/2 задания
if namespace.tasknumber == 1 or namespace.tasknumber is None:
    vocabulary = dictionary_placement(line[0].split(" "))
    print(vocabulary)
    mylist = sorted(vocabulary.items(), reverse=True, key=lambda i: i[1])
    print(' '.join([word for word, count in mylist[:10]]))
# Быстрая сортировка
if namespace.tasknumber == 2 or namespace.tasknumber is None:
    def quicksort(nums):
        if len(nums) <= 1:
            return nums
        else:
            rand = random.choice(nums)
            nums1 = []
            nums2 = []
            nums3 = []
            for number in nums:
                if number < rand:
                    nums1.append(number)
                elif number > rand:
                    nums2.append(number)
                else:
                    nums3.append(number)
            return quicksort(nums1) + nums3 + quicksort(nums2)

# Сортировка слияниями
    def mergesort(strings):
        if len(strings) > 1:
            mid = len(strings) // 2
            lefthalf = strings[:mid]
            righthalf = strings[mid:]

            mergesort(lefthalf)
            mergesort(righthalf)

            l = 0
            j = 0
            k = 0
            while l < len(lefthalf) and j < len(righthalf):
                if lefthalf[l] < righthalf[j]:
                    strings[k] = lefthalf[l]
                    l = l + 1
                else:
                    strings[k] = righthalf[j]
                    j = j + 1
                k = k + 1

            while l < len(lefthalf):
                strings[k] = lefthalf[l]
                l = l + 1
                k = k + 1

            while j < len(righthalf):
                strings[k] = righthalf[j]
                j = j + 1
                k = k + 1
        return strings
# 3/4 задания
    import random
    quick = line[1].split(" ")
    for element in range(0, len(quick)):
        quick[element] = int(quick[element])
    merge = line[2].split(" ")
    for element in range(0, len(merge)):
        merge[element] = int(merge[element])
    print("Быстрая сортировка - ", quicksort(quick))
    print("Сортировка слияниями - ", mergesort(merge))

# Первый доп
if namespace.tasknumber == 3 or namespace.tasknumber is None:
    def fib(number):
        if number == 1:
            yield 1
        else:
            fib1 = 1
            fib2 = 1
            yield 1
            yield 1
            for elem in range(0, number - 2):
                fib_sum = fib1 + fib2
                yield fib_sum
                fib1 = fib2
                fib2 = fib_sum
    n = int(line[3])
    my_generator = fib(n)
    print(my_generator)
    for i in my_generator:
        print(i)

