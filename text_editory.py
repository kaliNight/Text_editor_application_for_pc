import tkinter as tk
from tkinter import ttk, font, filedialog, colorchooser
from tkinter import messagebox as m_box
import os

win=tk.Tk()
win.title('Editor')
win.geometry('1200x800')
win.wm_iconbitmap('icon2.ico')

#icons
align_center=tk.PhotoImage(file=r'icons2\align_center.png')
align_left=tk.PhotoImage(file=r'icons2\align_left.png')
align_right=tk.PhotoImage(file=r'icons2\align_right.png')
bold=tk.PhotoImage(file=r'icons2\bold.png')
clear_all=tk.PhotoImage(file=r'icons2\clear_all.png')
copy=tk.PhotoImage(file=r'icons2\copy.png')
cut=tk.PhotoImage(file=r'icons2\cut.png')
dark=tk.PhotoImage(file=r'icons2\dark.png')
exit=tk.PhotoImage(file=r'icons2\exit.png')
find=tk.PhotoImage(file=r'icons2\find.png')
font_color=tk.PhotoImage(file=r'icons2\font_color.png')
italic=tk.PhotoImage(file=r'icons2\italic.png')
light_default=tk.PhotoImage(file=r'icons2\light_default.png')
light_plus=tk.PhotoImage(file=r'icons2\light_plus.png')
monokai=tk.PhotoImage(file=r'icons2\monokai.png')
new=tk.PhotoImage(file=r'icons2\new.png')
night_blue=tk.PhotoImage(file=r'icons2\night_blue.png')
i_open=tk.PhotoImage(file=r'icons2\open.png')
paste=tk.PhotoImage(file=r'icons2\paste.png')
red=tk.PhotoImage(file=r'icons2\red.png')
save=tk.PhotoImage(file=r'icons2\save.png')
save_as=tk.PhotoImage(file=r'icons2\save_as.png')
status_bar=tk.PhotoImage(file=r'icons2\status_bar.png')
tool_bar=tk.PhotoImage(file=r'icons2\tool_bar.png')
underline=tk.PhotoImage(file=r'icons2\underline.png')



#menu
menu=tk.Menu(win,tearoff=False)
file=tk.Menu(menu,tearoff=False)
edit=tk.Menu(menu,tearoff=False)
view=tk.Menu(menu,tearoff=False)
theme=tk.Menu(menu,tearoff=False)

menu.add_cascade(label='File',menu=file)
menu.add_cascade(label='Edit',menu=edit)
menu.add_cascade(label='View',menu=view)
menu.add_cascade(label='Theme',menu=theme)
win.config(menu=menu)









la_frame=tk.Frame(win) 
la_frame.pack(fill=tk.X)



text=tk.Text(win,wrap='word',relief=tk.FLAT)
text.pack(fill='both',expand=True)

extra_char=2
extra_char_sub=1



text.focus_set()


scrollbar=tk.Scrollbar(text,command=text.yview)
scrollbar.pack(side=tk.RIGHT,fill=tk.Y)

text.config(yscrollcommand=scrollbar.set,font=('Arial',12))








tv_font=tk.StringVar()
tv_size=tk.StringVar()

font=ttk.Combobox(la_frame,width=15,state='readonly',textvariable=tv_font)
font['values']=tk.font.families()
font.current(tk.font.families().index('Arial'))
font.grid(row=0,column=0,padx=5,pady=3)


size=ttk.Combobox(la_frame,width=15,state='readonly',textvariable=tv_size)
size['values']=tuple(range(8,81,2))
size.grid(row=0,column=1)
size.current(0)

v_font='Arial'
v_size=12



def f_font(event:None):
    global v_font
    v_font=tv_font.get()
    text.config(font=(v_font,v_size))
    
font.bind('<<ComboboxSelected>>',f_font)

def f_size(event:None):
    global v_size
    v_size=tv_size.get()
    text.config(font=(v_font,v_size))
    
size.bind('<<ComboboxSelected>>',f_size)






v_italic='roman'
v_bold='normal'
v_underline='normal'



def f_bold():
    global v_bold
    if tk.font.Font(font=text['font']).actual()['weight']=="normal":
        text.config(font=(v_font,v_size,'bold'))
        v_bold='bold'
    else:
        text.config(font=(v_font,v_size,'normal'))
        v_bold='normal'

def f_italic():
    global v_italic
    if tk.font.Font(font=text['font']).actual()['slant']=="roman":
        text.config(font=(v_font,v_size,v_bold,'italic'))
        v_italic='italic'
    else:
        text.config(font=(v_font,v_size,v_bold,'roman'))
        v_italic='roman'

def f_underline():
    global v_underline
    if tk.font.Font(font=text['font']).actual()['underline']==0:
        text.config(font=(v_font,v_size,v_bold,'underline'))
        v_underline=1
    else:
        text.config(font=(v_font,v_size,v_bold,'normal'))
        v_underline=0

        

b_bold=ttk.Button(la_frame,image=bold,command=f_bold)
b_bold.grid(row=0,column=2,padx=5,pady=3)



b_italic=ttk.Button(la_frame,image=italic,command=f_italic)
b_italic.grid(row=0,column=3,padx=5,pady=3)

b_underline=ttk.Button(la_frame,image=underline,command=f_underline)
b_underline.grid(row=0,column=4,padx=5,pady=3)


def f_font_color():
    color=colorchooser.askcolor()
    text.config(foreground=color[1])


b_font_color=ttk.Button(la_frame,image=font_color, command=f_font_color)
b_font_color.grid(row=0,column=5,padx=5,pady=3)

def f_align_left():
    global extra_char
    extra_char=1
    data=text.get(1.0,'end')
    text.tag_config('left',justify=tk.LEFT)
    text.delete(1.0,tk.END)
    text.insert(tk.INSERT,data,'left')

def f_align_right():
    global extra_char
    extra_char=1
    data=text.get(1.0,'end')
    text.tag_config('right',justify=tk.RIGHT)
    text.delete(1.0,tk.END)
    text.insert(tk.INSERT,data,'right')

def f_align_center():
    global extra_char
    extra_char=1
    data=text.get(1.0,tk.END)
    text.tag_config('center',justify=tk.CENTER)
    text.delete(1.0,tk.END)
    text.insert(tk.INSERT,data,'center')




b_align_left=ttk.Button(la_frame,image=align_left, command=f_align_left)
b_align_left.grid(row=0,column=6,padx=5,pady=3)

b_align_center=ttk.Button(la_frame,image=align_center,command=f_align_center)
b_align_center.grid(row=0,column=7,padx=5,pady=3)

b_align_right=ttk.Button(la_frame,image=align_right,command=f_align_right)
b_align_right.grid(row=0,column=8,padx=5,pady=3)


status_menu=tk.Label(text='Status Bar')
status_menu.pack(side=tk.BOTTOM)

def f_status_menu(event:None):
    global char
    global extra_char_sub
    if text.edit_modified():
        word=len(text.get(1.0,tk.END).split())
        if extra_char==2:
            char=len(text.get(1.0,tk.END))
            status_menu.config(text=f'Character: {char} Word: {word}')
        if extra_char==1:
            char=len(text.get(1.0,tk.END))-extra_char_sub
            extra_char_sub+=1
            status_menu.config(text=f'Character: {char} Word: {word}')
    text.edit_modified(False)


text.bind('<<Modified>>',f_status_menu)

path=''


def f_new(event=None):
    global path
    modified=text.get(1.0,tk.END)
    if modified!='':
        m_box_return=m_box.askyesnocancel('Warning','Do you wan\'t to save changes' )
        if m_box_return==True:
            f_save()
            path=''
            text.delete(1.0,tk.END)
        if m_box_return==False:
            path=''
            text.delete(1.0,tk.END)
        if m_box_return==None:
            None
    else:
        path=''
        text.delete(1.0,tk.END)
    text.edit_modified(False)
        
file.bind(f_new)
    

file.add_command(label='New',image=new,compound=tk.LEFT,accelerator='Ctrl+N',command=f_new)

def f_open(event=None):
    global path
    modified=text.get(1.0,tk.END)
    if modified!='':
        m_box_return=m_box.askyesnocancel('Warning','Do you wan\'t to save changes' )
        if m_box_return==True:
            f_save()
            path=filedialog.askopenfilename(title='open',initialdir=os.getcwd(),filetypes=(('Text File','*.txt'),('All files','*.*')))
            f=open(path,'r',newline='')
            text.delete(1.0,tk.END)
            text.insert(1.0,f.read())
            f.close()
        if m_box_return==False:
            path=filedialog.askopenfilename(title='open',initialdir=os.getcwd(),filetypes=(('Text File','*.txt'),('All files','*.*')))
            f=open(path,'r',newline='')
            text.delete(1.0,tk.END)
            text.insert(1.0,f.read())
            f.close()
        if m_box_return==None:
            None
    else:
        path=filedialog.askopenfilename(title='open',initialdir=os.getcwd(),filetypes=(('Text File','*.txt'),('All files','*.*')))
        f=open(path,'r',newline='')
        text.delete(1.0,tk.END)
        text.insert(1.0,f.read())
        f.close()
    text.edit_modified(False)
        

file.add_command(label='Open',image=i_open,compound=tk.LEFT,accelerator='Ctrl+O',command=f_open)




def f_save(event=None):
    global path
    if path=='':
        f=filedialog.asksaveasfile(title='save',mode='w',defaultextension='.txt',initialdir=os.getcwd(),filetypes=(('Text file','*.txt'),('All files','*.*')))
        data=text.get(1.0,tk.END)
        f.write(data)
        f.close()   
    else:
        data=text.get(1.0,tk.END)
        f=open(path,'w',newline='')
        f.write(data)
        f.close()
        

file.add_command(label='Save',image=save,compound=tk.LEFT,accelerator='Ctrl+S',command=f_save)

def f_save_as(event=None):
    f=filedialog.asksaveasfile(title='save',mode='w',defaultextension='.txt',initialdir=os.getcwd(),filetypes=(('Text file','*.txt'),('All files','*.*')))
    data=text.get(1.0,tk.END)
    f.write(data)
    f.close()    

file.add_command(label='Save_as',image=save_as,compound=tk.LEFT,accelerator='Alt+S',command=f_save_as)

def f_exit():
    m_box_return=m_box.askyesnocancel('Warning','Do you wan\'t to save this file' )
    if m_box_return==True:
        f_save()
        win.destroy()
    if m_box_return==False:
        win.destroy()
    if m_box_return==None:
        None

file.add_command(label='Exit',image=exit,compound=tk.LEFT,accelerator='Ctrl+Q',command=f_exit)



edit.add_command(label='Copy',image=copy,compound=tk.LEFT,accelerator='Ctrl+C',command=lambda:text.event_generate('<Control c>'))
edit.add_command(label='Paste',image=paste,compound=tk.LEFT,accelerator='Ctrl+V',command=lambda:text.event_generate('<Control v>'))
edit.add_command(label='Cut',image=cut,compound=tk.LEFT,accelerator='Ctrl+X',command=lambda:text.event_generate('<Control x>'))    
edit.add_command(label='Clear All',image=clear_all,compound=tk.LEFT,accelerator='Alt+X',command=lambda:text.delete(1.0,tk.END))


word=tk.StringVar()
replace_word=tk.StringVar()


        



def f_find(event=None):
    find_win=tk.Toplevel()
    find_win.geometry('350x200+500+200')
    find_win.resizable(0,0)

    find_frame=tk.LabelFrame(find_win)
    find_frame.config(text='Find/Replace')
    find_frame.pack(pady=40)

    l_find=tk.Label(find_frame,text="Find")
    l_find.grid(row=0,column=0,padx=4,pady=4)
    l_replace=tk.Label(find_frame,text="Replace")
    l_replace.grid(row=1,column=0,padx=4,pady=4)

    i_find=tk.Entry(find_frame,width=20,textvariable=word)
    i_find.grid(row=0,column=1,padx=4,pady=4)
    i_replace=tk.Entry(find_frame,width=20,textvariable=replace_word)
    i_replace.grid(row=1,column=1,padx=4,pady=4)

    def f_b_find():
        text.tag_remove('word',1.0,tk.END)
        word=i_find.get()
        if word:
            start_index='1.0'
            while(start_index!=tk.END):
                start_index=text.search(word,start_index,tk.END)
                end_index=f'{start_index}+{len(word)}c'
                text.tag_add('word',start_index,end_index)
                text.tag_config('word',foreground='red',background='yellow')
                start_index=end_index
            
   
    b_find=ttk.Button(find_frame,text='Find',command=f_b_find)
    b_find.grid(row=2,column=0,padx=4,pady=4)
    
    def f_b_replace():
        word=i_find.get()
        replace_word=i_replace.get()
        if word and replace_word:
            data=text.get(1.0,tk.END)
            data=data.replace(word,replace_word)
            text.delete(1.0,tk.END)
            text.insert(tk.INSERT,data,1.0)
            text.tag_remove('replace_word',1.0,tk.END)
            start_index=1.0
            while(start_index!=tk.END):
                start_index=text.search(replace_word,start_index,tk.END)
                end_index=f'{start_index}+{len(replace_word)}c'
                text.tag_add('replace_word',start_index,end_index)
                text.tag_config('replace_word',foreground='red',background='yellow')
                start_index=end_index


    b_replace=ttk.Button(find_frame,text='Replace',command=f_b_replace)
    b_replace.grid(row=2,column=1,padx=4,pady=4)


edit.add_command(label='Find',image=find,compound=tk.LEFT,accelerator='Ctrl+F',command=f_find)

hide_tool_bar=tk.BooleanVar()
hide_status_bar=tk.BooleanVar()
hide_tool_bar.set(True)
hide_status_bar.set(True)



def f_tool_bar(event=None):
    global hide_tool_bar
    if hide_tool_bar:
        la_frame.pack_forget()
        hide_tool_bar=False
    else:
        text.pack_forget()
        status_menu.pack_forget()
        scrollbar.pack_forget()
        la_frame.pack(fill=tk.X)
        text.pack(fill='both',expand=True)
        scrollbar.pack(side=tk.RIGHT,fill=tk.Y)
        status_menu.pack(side=tk.BOTTOM)
        hide_tool_bar=True

def f_status_bar(event=None):
    global hide_status_bar
    if hide_status_bar:
        status_menu.pack_forget()
        hide_status_bar=False
    else:
        status_menu.pack(side=tk.BOTTOM)
        hide_status_bar=True
        


view.add_checkbutton(label='Toll Bar',onvalue=True,image=tool_bar,compound=tk.LEFT,accelerator='Ctrl+T',variable=hide_tool_bar,command=f_tool_bar)
view.add_checkbutton(label='Status Bar',onvalue=True,image=status_bar,compound=tk.LEFT,accelerator='Alt+t',variable=hide_status_bar,command=f_status_bar)

color_dict={
    'Light Default':('#000000','#ffffff'),
    'Light Plus':('#474747','#e0e0e0'),
    'Dark':('#c4c4c4','#2d2d2d'),
    'Red':('#2d2d2d','#ffe8e8'),
    'Monokai':('#d3b774','#474747'),
    'Night Blue':('#ededed','#6b9dc2')
}



color_var=tk.StringVar()

def f_theme():
    color=color_var.get()
    print(color)
    text.config(foreground=color[0:7],background=color[8:])
    
theme.add_radiobutton(label='Light Default',image=light_default,compound=tk.LEFT,variable=color_var,command=f_theme,value=color_dict['Light Default'])
theme.add_radiobutton(label='Light Plus',image=light_plus,compound=tk.LEFT,variable=color_var,command=f_theme,value=color_dict['Light Plus'])
theme.add_radiobutton(label='Dark',image=dark,compound=tk.LEFT,variable=color_var,command=f_theme,value=color_dict['Dark'])
theme.add_radiobutton(label='Red',image=red,compound=tk.LEFT,variable=color_var,command=f_theme,value=color_dict['Red'])
theme.add_radiobutton(label='Monokai',image=monokai,compound=tk.LEFT,variable=color_var,command=f_theme,value=color_dict['Monokai'])
theme.add_radiobutton(label='Night Blue',image=night_blue,compound=tk.LEFT,variable=color_var,command=f_theme,value=color_dict['Night Blue'])

win.bind('<Control-n>',f_new)
win.bind('<Control-o>',f_open)
win.bind('<Control-s>',f_save)
win.bind('<Alt-s>',f_save_as)
win.bind('<Control-q>',f_exit)
win.bind('<Control-f>',f_find)
win.bind('<Control-t>',f_tool_bar)
win.bind('<Alt-t>',f_status_bar)



win.mainloop()
