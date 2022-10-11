import math

while True:
    '''allows for the calculator functionality to run constantly unless directly closed by the user'''
    print('')
    print('Select an option... \n')

# all the calc options
    options = [
        '0. addition',
        '1. subtractions',
        '2. multiplication',
        '3. division',
        '4. modulo',
        '5. raising to a power',
        '6. square root',
        '7. log',
        '8. sine',
        '9. cosine',
        '10. tangent \n',
        '11. exit the application',
        ]


    for option in options:
        '''print the option menu screen'''
        print(option)

    calc_option = int(input('\n your selection: '))

    if calc_option not in list(range(12)):
        '''if a user inputs a number not within the option menu screen they are asked to select again'''
        print(f"{calc_option} is not an option, please select again")
        
    if calc_option == 11:
        '''closes the application for the user'''
        exit()
        
    def return_to_main_menu():
        '''after a user completes an operation they are asked if they want to return to the main
        menu or exit the application'''
        reply = input("\n Return to main menu? (y/n) ")
        if reply.lower() == "y":
            return None
        if reply.lower() == "n":
            exit()
        if reply.lower() not in ['y' , 'n']:
            print('\n please select a valid option')
            return_to_main_menu()
    
    
    #line used to display the answer for the user
    result_line = '\n the result is: '
    
    
    def rerun_logo_fun():
        '''if the user doesnt select a valid option for if they want to provide their own base
        number, the logo func will ask again'''
        print('\n please select a valid option')
        logo_func()
    
    
    def logo_func():
        '''the logo functionality'''
        base_wanted = input('\n do you want to provide the base number? default is base 10. (y/n): ')
        if base_wanted.lower() == 'y':
            base = int(input('\n enter base: '))
            num = int(input('\n enter number: '))
            print(result_line , math.log(num , base))
            return_to_main_menu()
        if base_wanted.lower() == 'n':
            num = int(input('\n enter number: '))
            print(result_line , math.log10(num))
            return_to_main_menu()
        if base_wanted.lower() not in ['y' , 'n']:
            rerun_logo_fun()
        
        
    def accuire_2_numbers(opr):
        '''majority of the calculator functionality exists here where it asks for 2 numbers 
        and returns the appropiate answer, more complex functionality will have their own methods'''
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
        
        if opr == 'expo':
            print(result_line, x ** y)
        
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
        
        
    if calc_option == 5:
        accuire_2_numbers('expo')
        
    if calc_option == 6:
        print('\n enter the number \n')
        x = int(input('number: '))
        print(result_line , math.sqrt(x))
        return_to_main_menu()
        
            
    if calc_option == 7:
        logo_func()
        
    if calc_option == 8:
        print('\n enter the number \n')
        x = int(input('number: '))
        print(result_line , math.sin(x))
        return_to_main_menu()
        
    if calc_option == 9:
        print('\n enter the number \n')
        x = int(input('number: '))
        print(result_line , math.cos(x))
        return_to_main_menu()
        
        
    if calc_option == 10:
        print('\n enter the number \n')
        x = int(input('number: '))
        print(result_line , math.tan(x))
        return_to_main_menu()