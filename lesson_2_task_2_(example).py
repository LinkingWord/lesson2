

def get_calories(fruit):
  if fruit == 'apple':
    return 52
  if fruit == 'pear':
    return 57
  if fruit == 'banana':
    return 89
  if fruit == 'tomato':
    return 17
  return None


my_fruit = 'tomato'
print(get_calories(my_fruit))