

def compare_strings(str1, str2):
    if str1 == str2:
        return 1
    if len(str1) > len(str2):
        return 2
    if str2 == 'learn':
        return 3 
    return None


str1 = input('Ведите значение: ')
str2 = input('Ведите значение: ')


print(compare_strings(str1, str2))