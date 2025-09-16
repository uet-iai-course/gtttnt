def add_to_list(item:str, target: list[str]=[]):
    target.append(item)
    return target

l1= add_to_list("James")
add_to_list("Sandra")
print(l1)