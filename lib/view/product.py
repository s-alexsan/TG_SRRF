import PySimpleGUI as sg
from controller.database.crud import *

def screen():

    # ! toolbar
    toolbar_menu = [
        ['File', ['New', 'Edit', 'Delete', 'Exit']],
    ]
    data = readAllProduct()
    header = ['Code','Name', 'Description']
    
    # ! layout
    if not data:
        dataRegister = [
            [sg.Text(text='No register')]
        ]
    else:
        dataRegister = [
            [sg.Table(values=data, headings=header, num_rows=18, row_height=20, max_col_width=30, justification='left', key='tbProduct', enable_events=True)]
        ]

    layout = [
        [sg.Menu(toolbar_menu)],
        [sg.Column(dataRegister)],
        [sg.Frame(title='Filter', layout=[
            [sg.InputCombo(['Code', 'Product'], key='cbmFilter', default_value = 'Product'), sg.Input('', key='lblInput')],
            [sg.Button(button_text='Search'), sg.Button(button_text='Clear')]
        ])]
    ]
    window = sg.Window('Product', layout,size=(800,500))

    while True:
        event, value = window.read(timeout=20)
        
        if event == 'New':
            productNewOld()
            data = readAllProduct()
            window.Element('tbProduct').update(values=data)
        if event == 'Edit':
            productNewOld(window.Element('tbProduct').Values[window.Element('tbProduct').SelectedRows[0]][0])
            data = readAllProduct()
            window.Element('tbProduct').update(values=data)
        if event == 'Exit' or event == sg.WIN_CLOSED:
            break
        if event == 'Delete':
            if deleteProduct(window.Element('tbProduct').Values[window.Element('tbProduct').SelectedRows[0]][0]) == 1:
                data = readAllProduct()
                window.Element('tbProduct').update(values=data)
        if event == 'Search':
                data = readProductFilter(value['cbmFilter'], value['lblInput'])
                window.Element('tbProduct').update(values=data)
        if event == 'Clear':
            data = readAllProduct()
            window.Element('tbProduct').update(values=data)
    window.close()


#
# * Function that going to see the screen of product
#
#
def productNewOld(pk_product = None):
    if pk_product != None:
        data            = readProductByPk(pk_product)
        product         = data[0][1]
        description     = data[0][2]
        inactive        = data[0][3]
        rdInactive      = [sg.Checkbox('Inactive', default=inactive, key='IInactive')]
        btnInsertUpdate = 'Update'
        title           = 'Edit Product {}'.format(product)
    else:
        product            = ''
        description        = ''
        rdInactive         = []
        btnInsertUpdate = 'Register'
        title           = 'New Product'

    # ! LAYOUT
    layout = [
        [sg.Text("Product", size=(10,1), key='lblProduct'), sg.Input(product, key = 'IProduct')],
        [sg.Text("Description", size=(10,1), key='lblDescription'), sg.Multiline(default_text = description, key='IDescription')],
        rdInactive,
        [sg.HorizontalSeparator()],
        [sg.Button(button_text=btnInsertUpdate), sg.Exit(button_text="Cancel")],
    
    ]
    window = sg.Window(title, layout)


    while True:
        event, values = window.Read(timeout=20, timeout_key='timeout')
        if event is None or event == 'Cancel':  
            break
        
        if event == 'Register':
            created = createProduct(values)
            if created == 1:
                window.close()
            elif created == 0:
                sg.Popup('Fail in register')
            elif created == -1:
                sg.Popup('Product invalid')
            elif created == -2:
                sg.Popup('Description invalid')
        if event == 'Update':
            updated = updateProduct(values, pk_product)
            if updated == 1:
                window.close()
            elif updated == 0:
                sg.Popup('Fail in register')
            elif updated == -1:
                sg.Popup('Product invalid')
            elif updated == -2:
                sg.Popup('Description invalid')
    window.close()