FILEPATH = 'goods.txt'

#custom actions to avoid redundant code
def get_goods(filepath_r=FILEPATH):
    """
    Read a text file and return the list of to do items.
    """
    with open(filepath_r,'r') as getfile_local:
        getgoods_local = getfile_local.readlines()
    return getgoods_local 


def write_goods(goods_arg, filepath_w=FILEPATH):
    """
    Write the new/updated list of to do items
    into the existing text file.
    """
    with open(filepath_w,'w') as writefile_local:
        writefile_local.writelines(goods_arg)
 

#print(__name__) #prints "actions" when the main.py is run (due to import action command)

#conditional block
#But when you run actions.py directly, the value of that variable is __main__.
#And that allows us to have this condition here.
if __name__ == '__main__':
    #print('Hello')
    print(get_goods())