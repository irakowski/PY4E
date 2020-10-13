"""Exercise 1:
Write a function called chop that takes a list and modifies it, 
removing the first and last elements, and returns None.
Then write a function called middle that takes a list and 
returns a new list that contains all but the first and last elements.
"""
def chop(lst):
    if len(lst) > 2:
        del lst[0]
        del lst[-1]
    lst = []


def middle(lst):
    new_list = lst[1:-1]
    return new_list
