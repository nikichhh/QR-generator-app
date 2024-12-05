import qrcode
import PySimpleGUI as sg
from PIL import Image, ImageWin
import os
import platform


def print_image(file_path):
    try:
        if platform.system() == "Windows":
            os.startfile(file_path, "print")

    except Exception as e:
        sg.popup(f"Failed to print the file: {e}", title="Error")


layout = [
    [
        sg.Input(key='INPUT'),
        sg.Button('Create', key='CREATE_BTN', bind_return_key=True),
        sg.Button('Print', key='PRINT_BTN', disabled=True)
    ],
    [sg.Image(key='IMAGE', size=(200, 200))]
]
window = sg.Window('QR Generator', layout=layout)

filename = None

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break

    if event == 'CREATE_BTN':
        data = values['INPUT']
        if not data.strip():
            sg.popup("Please enter valid data to generate a QR code!", title="Error")
            continue

        save_name = sg.popup_get_file(
            "Save As",
            save_as=True,
            title="Save QR Code"
        )
        filename = f'{save_name}.png'

        if filename:
            try:
                qr = qrcode.make(data)
                qr.save(filename)
                window['IMAGE'].update(filename=filename)
                window['PRINT_BTN'].update(disabled=False)
            except Exception as e:
                sg.popup(f"An error occurred: {e}", title="Error")

    if event == 'PRINT_BTN':
        if filename:
            print_image(filename)
        else:
            sg.popup("No QR code to print. Please create one first.", title="Error")

window.close()