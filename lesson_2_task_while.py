

def find_person(name, user_name):            
    while True:
        if user_name == 'Валера':
            print('Валера найден')
            break


name = ['Вася', 'Маша', 'Петя', 'Валера', 'Саша', 'Даша']        
user_name = name.pop()

print(find_person(name, user_name))
        

  






# while user_name = 'Валера': 
    # print('Валера нашелся')
    # name.pop()
    # name = [3] в таком случае получается бесконечный цикл и я, блин, не понимаю, ПОЧЕМУ?!!!   
    # name == 'Валера'
    
    