vegetable_list = ["carrot","beet","celery","spinach","mix spring"]

# create a testing list
my_vegetable_record = {
    "carrot":  1,
    "beet":    2,
    "celery":  3,
    "spinach": 1,
    "mix spring": 2
}

def suggest_list(my_list): 
    sort_list = sorted(my_list.items(), key = lambda item: item[1])
    return sort_list



print(suggest_list(my_vegetable_record))