'''
SENG 207 PROGRAMMING PROJECT 2(a)
DESKTOP APPLICATION
INDEX NUMBER: 10968300
NAME: NYARKOA PRISCILLA YEBOAH
DEPARTMENT: FOOD PROCESS ENGINEERING
'''

import PySimpleGUI as psg
import pyttsx3

engine = pyttsx3.init()
psg.theme('Topanga')
psg.theme_button_color('black')
psg.theme_input_background_color('white')
psg.theme_input_text_color('black')
psg.theme_element_text_color('yellow')
psg.theme_text_color('white')

layout = [
    [psg.Text('Enter text here:',font=('Time New Romans', 15))],
    [psg.InputText(key='input',font=('Time New Romans', 15)),psg.Button('Speak',font=('Time New Romans', 15), key='speak')],
    [psg.Text('Choose a Voice:',font=('Time New Romans', 15)), psg.Radio('Female', "RADIO1", default=True, key='-FEMALE-',font=('Time New Romans', 15)), psg.Radio('Male', "RADIO1", key='-MALE-',font=('Time New Romans', 15))],
    [psg.Text('Adjust Volume:', font=('Time New Romans', 15)), psg.Slider(range=(0, 200), default_value=100, orientation='h', size=(20, 15), font=('Time New Romans', 15), key='-VOLUME-')],
    [psg.Text('Adjust Speed:', font=('Time New Romans', 15)), psg.Slider(range=(100, 500), default_value=200, orientation='h', size=(20, 15), font=('Time New Romans', 15), key='-SPEED-')],
    [psg.Button('Quit',font=('Time New Romans', 15))],
    [psg.Text('Designed by Priscilla Nyarkoa Yeboah')]
]

def speak(text,volume,speed):
    if values["-FEMALE-"]:
        Voice_ID = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0"
    else:
        Voice_ID = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_DAVID_11.0"
    engine.setProperty('voice', Voice_ID)
    engine.setProperty('volume', volume / 200)
    engine.setProperty('rate', speed)
    
    engine.say(text)
    engine.runAndWait()

window = psg.Window('Text-to-Speech PriscyApp', layout)

while True:
    event, values = window.read()

    if event == 'speak':
        text = values['input']
        volume = values['-VOLUME-']
        speed = values['-SPEED-']
        speak(text, volume, speed)

    if event == psg.WINDOW_CLOSED:
        break
    if event in (psg.WINDOW_CLOSED, 'Quit'):
        break
    
window.close()