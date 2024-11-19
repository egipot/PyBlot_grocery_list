
#pip install FreeSimpleGUI everytime
import FreeSimpleGUI as sg
import actions
import time
import os

if not os.path.exists("goods.txt"):
    with open('goods.txt', 'w') as file:
        pass

sg.theme('LightGreen3')

clock = sg.Text('', key='clock')
label = sg.Text('Type in a goods to buy: ')
input_box = sg.InputText(tooltip = 'Enter an item to buy here...', key = 'good') 
add_button = sg.Button('Add')
edit_button = sg.Button('Edit')
show_button = sg.Button('Show')
bought_button = sg.Button('Bought')
exit_button = sg.Button('Exit')
list_box = sg.Listbox(values=actions.get_goods(), 
                      key='goods', 
                      enable_events=True, 
                      size=[45,10])

window = sg.Window('My Grocery List App', 
                   layout = [[clock],
                             [label], 
                             [input_box, add_button],
                             [list_box, edit_button, bought_button], 
                             [exit_button]], #1 row enclosed in a square bracket []
                   font=('Arial', 14))

          
while True:
    event, values = window.read(timeout=10)
    window["clock"].update(value=time.strftime('%b %d %Y, %H:%M:%S'))
    if event == 'Add':
        goods = actions.get_goods()
        new_good = values['good'] + '\n'
        goods.append(new_good) 
        #print(goods)
        actions.write_goods(goods)
        window['goods'].update(values=goods)
        window['good'].update(value='')
        
    
    elif event == 'Edit':
        try:
            good_to_edit = values['goods'][0]
            new_good = values['good']
            #print(f'4 good to edit: {new_good}')

            goods = actions.get_goods()
            index = goods.index(good_to_edit)
            goods[index] = new_good
            actions.write_goods(goods)
            window['goods'].update(values=goods)
            #window['good'].update(value='')
        except:
            #print('Please select an item first.')
            sg.popup('Please select an item first.', font=('Arial', 14))

    elif event == 'goods':
        window['good'].update(value=values['goods'][0])

    elif event =='Bought':
        try:
            good_already_bought = values['goods'][0]
            goods = actions.get_goods()
            goods.remove(good_already_bought)
            actions.write_goods(goods)
            window['goods'].update(values=goods)
            window['good'].update(value='')
            good_already_bought = good_already_bought.strip('\n')
            sg.popup(f'The item "{good_already_bought}" has been bought and removed in the list.', font=('Arial', 14))
        except:
            sg.popup('Please select an item first.', font=('Arial', 14))

    elif event == 'Exit':
        break
    elif event == sg.WIN_CLOSED:
        break


window.close()