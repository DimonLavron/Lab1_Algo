import time

class Jackscrew:
    def __init__(self, max_lifting_weight, producer, color, own_weight):
        self.max_lifting_weight = max_lifting_weight
        self.producer = producer
        self.color = color
        self.own_weight = own_weight

def bubble_sort(array):
    global comparisons_cnt, swaps_cnt
    sorted = False
    n = len(array)
    while not sorted:
        sorted = True
        for i in range(1, n):
            comparisons_cnt += 1
            if array[i-1].max_lifting_weight < array[i].max_lifting_weight:
                swaps_cnt += 1
                array[i-1], array[i] = array[i], array[i-1]
                sorted = False
    return array


def merge(first_array, second_array):
    global comparisons_cnt, swaps_cnt
    first_pointer = 0
    second_pointer = 0
    first_length = len(first_array)
    second_length = len(second_array)
    result = []

    while first_pointer < first_length and second_pointer < second_length:
        comparisons_cnt += 1
        if first_array[first_pointer].own_weight <= second_array[second_pointer].own_weight:
            result.append(first_array[first_pointer])
            first_pointer += 1
            swaps_cnt += 1
        else:
            result.append(second_array[second_pointer])
            second_pointer += 1
            swaps_cnt += 1

    swaps_cnt += first_length - first_pointer + second_length - second_pointer

    result += first_array[first_pointer:] + second_array[second_pointer:]

    return result

def merge_sort(array):
    if len(array) < 2:
        return array

    middle = len(array) // 2
    return merge(merge_sort(array[:middle]), merge_sort(array[middle:]))


input_file = open("input.txt", "r")
output_file = open("output.txt", "w")
input_array = []
for line in input_file:
    int_data = [int(i) for i in line.split(',')]
    max_lifting_weight, producer, color, own_weight = int_data
    input_array.append(Jackscrew(max_lifting_weight, producer, color, own_weight))

output_file.write("--------Bubble Sort--------\n")
start_time = time.time()
comparisons_cnt = 0
swaps_cnt = 0
bubble_sorted_array = bubble_sort(input_array)
end_time = time.time()
output_file.write("Algorithm time: " + str(end_time - start_time) + "\n")
output_file.write("Comparisons number: " + str(comparisons_cnt) + "\n")
output_file.write("Swaps number: " + str(swaps_cnt) + "\n")
output_file.write("Result: " + str([i.max_lifting_weight for i in bubble_sorted_array])+"\n")


output_file.write("--------Merge Sort--------\n")
start_time = time.time()
comparisons_cnt = 0
swaps_cnt = 0
merge_sorted_array = merge_sort(input_array)
end_time = time.time()
output_file.write("Algorithm time: " + str(end_time - start_time) + "\n")
output_file.write("Comparisons number: " + str(comparisons_cnt) + "\n")
output_file.write("Swaps number: " + str(swaps_cnt) + "\n")
output_file.write("Result: " + str([i.own_weight for i in merge_sorted_array]))
