# def biggie_size(list):

#     for i in range(len(list)):
#         if list[i] > 0:
#             list[i] = "big"
#     return list

# print(biggie_size([-1, 3, 5, -5]))

# ===================================== #

# def count_positives(list):
#     num = 0
#     for i in list:
#         if i > 0:
#             num += 1
#     list[len(list)-1] = list
#     return list

# print(count_positives([1,6,-4,-2,-7,-2]))
# print(count_positives([-1,1,1,1]))

# ===================================== #

# def sum_total(list):
#     sum = 0
#     for i in list:
#         sum += i
#     return sum
# print(sum_total([1,2,3,4]))
# print(sum_total([6,3,-2]))

# ===================================== #

# def average(list):
#     avg = 0
#     for i in list:
#         avg += i
#     return (avg/len(list))
# print(average([1,2,3,4]))

# ===================================== #

# def length(list):
#     return len(list)
# print(length([37,2,1,-9]))

# ===================================== #

# def minimum(list):
#     if len(list) == 0:
#         return False
#     else:
#         minnum = list[0]
#         for i in list:
#             if i < minnum:
#                 minnum = i
#         return minimum


# print(minimum([37, 2, 1, -9]))
# print(minimum([]))

# ===================================== #

# def ultimate_analysis(list):
#     dict = {'sumTotal': 0,
#             'average': 0,
#             'minimum': list[0], 
#             'maximun': list[0], 
#             'length': len(list)}
#     return dict

# print(ultimate_analysis([37,2,1,-9]))

# ===================================== #

# def reverse_list(list):
#     list = list[::-1]
#     return list
# print(reverse_list([37,2,1,-9]))