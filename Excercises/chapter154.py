import FreeSimpleGUI as sg

feet_label = sg.Text("Enter Feet: ")
feet_input_box = sg.InputText(key='feet_input', default_text="")

inches_label = sg.Text("Enter Inches: ")
inches_input_box = sg.InputText(key='inches_input', default_text="")

convert_button =sg.Button("Convert", key='convert_button')

window = sg.Window("Converter", layout=[[feet_label, feet_input_box],
                                        [inches_label, inches_input_box],
                                        [[convert_button]]])

window.read()
window.close()