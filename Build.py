# Haxe project compiler (using lime)
# Made by sphis_Sinco

import subprocess

from tkinter import *
from tkinter import ttk
import tkinter

PROJECT_TITLE = "Haxe project compiler"
PROJECT_VERSION = "1.1.1"

dashD_not_required = ['debug' 'watch']
target_platforms = ['hl', 'windows', 'html5']

def runSubP():
        compile_args = ['lime', 'test', combo_box.get()]

        build_flags_array = custom_build_flags.get('1.0', 'end-1c').split('.')

        i = 0
        while i < build_flags_array.__len__():

                prefix = '-D'
                item = build_flags_array[i]

                if not item == '':
                        # this doesnt work for some reason.
                        if dashD_not_required.__contains__(item) == True:
                                prefix = '-'
                                print(item)

                        compile_args.append(f'{prefix}{item}')
                i = i + 1

        print(f'Building for {combo_box.get()} with the build flags: {build_flags_array}')
        
        print(compile_args.__str__())

        # Execute a simple bash command
        result = subprocess.run(compile_args, capture_output=True, text=True)

        value = ""

        # Check if the command was successful
        if result.returncode == 0:
                # Print the output of the command
                value=result.stdout
                print(result.stdout)
        else:
                # Print the error message
                value=result.stderr
                print(result.stderr)

        
        output.delete(1.0, END)
        output.insert(END, value)

tkinter_ui = tkinter.Tk()
tkinter_ui.title(f'{PROJECT_TITLE} v{PROJECT_VERSION}')
tkinter_ui.geometry('640x608')

project_text = Label(tkinter_ui, text=f'{PROJECT_TITLE} (v{PROJECT_VERSION})\nMade by sphis_Sinco')
project_text.pack(pady=10)

def select(event):
    selected_item = combo_box.get()
    target_platform_text.config(text='Selected target platform: ' + selected_item)

# Create a label
target_platform_text = tkinter.Label(tkinter_ui, text='Selected target platform: '+target_platforms[0])
target_platform_text.pack(pady=10)

# Create a Combobox widget
combo_box = ttk.Combobox(tkinter_ui, values=target_platforms)
combo_box.pack(pady=5)

# Set default value
combo_box.set(target_platforms[0])

# Bind event to selection
combo_box.bind('<<ComboboxSelected>>', select)

# cbf
custom_build_flags = Text(tkinter_ui, height=10, width=64)
custom_build_flags.pack()
custom_build_flags.insert(END, '')

# compile button
run = tkinter.Button(tkinter_ui, text='Compile', width=25, command=runSubP)
run.pack(pady=10)

# terminal outputs  
output = Text(tkinter_ui, height=10, width=64)
output.pack(pady=10)
output.insert(END, '')

# init stuff
combo_box.set(target_platforms[0])
       
custom_build_flags.delete(1.0, END)
custom_build_flags.insert(END, 'Seperate your build flags with a .')

output.delete(1.0, END)
output.insert(END, 'TRACE LOGS WILL GO HERE')
       
selected_item = combo_box.get()
target_platform_text.config(text='Selected target platform: ' + selected_item)

# menu stuff
menu = Menu(tkinter_ui)
tkinter_ui.config(menu=menu)

filemenu = Menu(menu)

def clear_ui():
       combo_box.set(target_platforms[0])
       
       custom_build_flags.delete(1.0, END)
       custom_build_flags.insert(END, 'Seperate your build flags with a .')

       output.delete(1.0, END)
       output.insert(END, 'TRACE LOGS WILL GO HERE')
       
       selected_item = combo_box.get()
       target_platform_text.config(text='Selected target platform: ' + selected_item)

filemenu.add_command(label='Reset', command=clear_ui)
filemenu.add_separator()

def save_build_flags():
       with open('build_flags.txt', 'w') as file:
                file.write(custom_build_flags.get('1.0', 'end-1c'))

def save_trace_logs():
       with open('trace_logs.txt', 'w') as file:
                file.write(output.get('1.0', 'end-1c'))

def load_build_flags():
       # make this not be a specific file
       with open('build_flags.txt', 'r') as file:
                custom_build_flags.delete(1.0, END)
                custom_build_flags.insert(END, file.read())

filemenu.add_command(label='Save trace logs as text file', command=save_trace_logs)
filemenu.add_command(label='Save build flags as text file', command=save_build_flags)
filemenu.add_command(label='Load build flags from a  text file', command=load_build_flags)

filemenu.add_separator()

def add_build_flag(flag):
        custom_build_flags.insert(END, f'.{flag}')

def add_debug_flag():
        add_build_flag('debug')

def add_watch_flag():
        add_build_flag('watch')

filemenu.add_command(label='Add debug build flag', command=add_debug_flag)
filemenu.add_command(label='Add watch build flag', command=add_watch_flag)

filemenu.add_separator()
filemenu.add_command(label='Exit', command=tkinter_ui.quit)
filemenu.add_separator()
menu.add_cascade(label='File', menu=filemenu)

tkinter_ui.mainloop()

clear_ui()