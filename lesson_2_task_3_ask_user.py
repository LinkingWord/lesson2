

def ask_user():
    try:
        while True:
            user_say = input('Как дела? ')
            if user_say == 'Хорошо':
                return('Отлично!')
                break
    except KeyboardInterrupt:
        return 'Спасибо, пока!'
      
                   
print(ask_user())