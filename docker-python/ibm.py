
def subsetA(arr):

    n = len(arr)
    arr.sort()
    total_sum = sum(arr)

    subset_sum = 0
    subset_A = []

    for num in arr:
             
             if subset_sum <= total_sum - subset_sum:
                 subset_sum += num
                 subset_A.append(num)  
             else:

                break
        
    return subset_A


if __name__ == '__main__':

    arr = [3,7,5,6,2]
    print(subsetA(arr))






#     def subsetA(arr):

#         n = len(arr)
#         arr.sort()  # Ordena o array em ordem crescente
#         total_sum = sum(arr)
        
#         subset_sum = 0
#         subset_A = []
        
#         # Percorre o array para formar o subconjunto A
#         for num in arr:
#             if subset_sum <= total_sum - subset_sum:
#                 subset_sum += num
#                 subset_A.append(num)
#             else:
#                 break
        
#         return subset_A

# if __name__ == '__main__':
#     arr = [3, 7, 5, 6, 2]
#     result = subsetA(arr)
#     print(result)
