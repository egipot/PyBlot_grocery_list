#App 1: To-do list app
#Use this cli.py to test the program in the terminal
#Then use pyinstaller to create a standalone executable app (.exe file) or use streamlit to create a web app

import actions
import time

print(time.strftime('%b %d %Y, %H:%M:%S'))


goods = []


while True:
    user_prompt = input('Type add, show, edit, bought or exit: ')
    user_prompt = user_prompt.strip() 
    
    if user_prompt.startswith('add'):    
        good = user_prompt[4:] + '\n'

        #custom function call
        goods = actions.get_goods()
            
        goods.append(good)

        actions.write_goods(goods)
                
    elif user_prompt.startswith('show'): 
        #print(user_prompt[:4])
        goods = actions.get_goods()
        
        for index, item in enumerate(goods):
            item = item.title()
            item = item.strip('\n')
            print(f'{index+1}: {item}')
        
    elif user_prompt.startswith('edit'): 
        try:
            number = int(user_prompt[5:])
            number = number-1
            #print(number)

            goods = actions.get_goods()
            #print(goods)
            #print(len(goods))

            #check the validity of input number
            if number not in range (len(goods)):        
                #print (number)
                #print(number not in range (len(goods))) #just checking the logic
                print('There is no item in that number. Exiting the edit option...')
            else:
                new_good = input('Enter new to do: ')
                goods[number] = new_good + '\n'
                #print(goods)

                actions.write_goods(goods)    
                
        except ValueError:
            print('Command is invalid.')
            continue 


    elif user_prompt.startswith('bought'): 
        try:
            number = int(user_prompt[9:])
                
            goods = actions.get_goods()
            index_completed = number - 1
            good_completed = goods[index_completed].strip('\n')
            #print(goods)
            #print(len(goods))            
            goods.pop(index_completed)

            message = f'The item "{good_completed}" has been bought and has been removed from the list.'
            print(message)

            actions.write_goods(goods)
             
        except IndexError:
            print('There is no item in that number. Try again.')
            
    elif user_prompt.startswith('exit'): 
        break
        
    else:
        print('Unknown command. Expected add or show or or edit or bought or exit.')