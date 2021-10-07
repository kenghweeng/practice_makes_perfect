# Wrong code:
def at_least_n(lst, n):
    for i in lst: ## wrong, should replace lst with lst.copy()
        if i<n:
            lst.remove(i)
    return lst
    
at_least_n([7,5,1,6,2,3], 6)

# Correct code:
# def at_least_n(lst, n):
#     for i in lst.copy(): ## wrong, should replace lst with lst.copy()
#         if i<n:
#             lst.remove(i)
#     return lst