import cv2, PySimpleGUI as sg
from view import user

def screenHome():
    sg.theme('DarkTeal12')
    # ! TOOLBAR MENU
    toolbar_menu = [
        ['Arquivo', ['Usuário', 'Operador', 'Imagens', 'Sair']],
        ['Reconhecimento', ['Eigenfaces', 'Fisherface', 'LBPH']]
    ]
    # ! LAYOUT
    layout = [
        [sg.Menu(toolbar_menu)],
        [sg.Image(r'background/bg.png')]
    ]
    window = sg.Window('Menu', layout, location=(0,0))

    while True:
        event, value = window.read(timeout=20)
        
        # * Screen main
        if event == 'Usuário':
            user.screenUser()
        if event == 'Sair' or event == sg.WIN_CLOSED:
            break
    window.close()