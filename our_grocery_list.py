import streamlit as st
import actions
import os

if not os.path.exists("goods.txt"):
    with open('goods.txt', 'w') as file:
        pass
    

def add_good():
    good = st.session_state['new_good'] + '\n'  #refers to the good in the input box
    #print(good)
    goods.append(good)
    actions.write_goods(goods)
    st.session_state.new_good = text_input
    if 'new_good' == '' or 'new_good' == ' ':
        return


def complete_good(key):
    num = int(key)
    st.info(f'This item "{goods.pop(num)}" has been bought; hence, removed from the list.')
    actions.write_goods(goods)

#retrieve the good list in goods.txt - to be displayed
goods = actions.get_goods()

st.title('Our Grocery List')
st.subheader('Stick to the shopping list and avoid impulse purchases!')
#st.write('This app aims that you stick to the shopping list and avoid impulse purchases.')

for index, good in enumerate(goods[1:], start=1):
    checkbox = st.checkbox(good.capitalize(), key=index,
                        on_change=complete_good, args=(str(index)))
   

text_input = st.text_input(label='', placeholder="Add a new item to buy...",
                        disabled=False,
                        on_change=add_good, key='new_good', 
                        help="Type a new item to buy and press Enter to add it to the list.")

#print('Hello')
#st.session_state