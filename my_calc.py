import math

while True:
    print('')
    print('Select an option... \n')

    options = [
        '0. addition',
        '1. subtractions',
        '2. multiplication',
        '3. division',
        '4. modulo',
        '5. raising to a power',
        '6. square root',
        '7. logarithim'
        '8. sine',
        '9. cosine',
        '10. tangent \n',
        '11. exit the application',
        ]

    for option in options:
        print(option)

    calc_option = int(input('\n your selection: '))

    if calc_option not in list(range(12)):
        print(f"{calc_option} is not an option, please select again")
        
    if calc_option == 11:
        exit()
        
    def return_to_main_menu():
        reply = input("\n Return to main menu? (y/n) ")
        if reply.lower() == "y":
            return None
        if reply.lower() == "n":
            exit()
        else:
            print('\n please select a valid option')
            return_to_main_menu()
    
    result_line = '\n the result is: '
        
    def accuire_2_numbers(opr):
        print('\n enter first number \n')
        x = int(input('first number: '))
        print('\n enter second number \n')
        y = int(input('second number: '))
        if opr == 'sub':
            print(result_line , x - y)
        if opr == 'add':
            print(result_line, x + y)
        if opr == 'multi':
            print(result_line , x * y)
        if opr == 'divi':
            if y == 0:
                print('\n sorry, division by zero isn\'t possible')
            else:
                print(result_line, x / y)
        if opr == 'modulo':
            if y == 0:
                print('\n sorry, modulo by zero isn\'t possible')
            else:
                print(result_line , x%y)
        return_to_main_menu()
        
    if calc_option == 0:
        accuire_2_numbers('add')
        
    if calc_option == 1:
        accuire_2_numbers('sub')
        
    if calc_option == 2:
        accuire_2_numbers('multi')
        
    if calc_option == 3:
        accuire_2_numbers('divi')
        
    if calc_option == 4:
        accuire_2_numbers('modulo')
