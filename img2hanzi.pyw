# -*- coding: UTF-8 -*-
from PIL import Image
import tkinter
s="丶十大天凹安阿画冒害巢焦盟箍黎霖赢瞿靡鼍霸鬻罐矗戆蠼爨齉"

def get_char(r,g,b,alpha=256):
	if alpha==0:
		return "　"
	gray=int(0.2126*r+0.7152*g+0.0722*b)
	return s[int(gray*len(s)/257)]

def gen():
	input_file=input_entry.get()
	output_file=output_entry.get()
	width=80
	height=80
	img=Image.open(input_file)
	img=img.resize((width,height),Image.NEAREST)
	txt=""
	for i in range(height):
		for j in range(width):
			txt+=get_char(*img.getpixel((j,i)))
		txt+="\n"
	with open(output_file,"w") as f:
		f.write(txt)

win=tkinter.Tk()
win.title("标题")
win_width=200
win_height=80
win.geometry("%dx%d+%d+%d"%(win_width,win_height,(win.winfo_screenwidth()-win_width)//2,(win.winfo_screenheight()-win_height)//2))
input_entry=tkinter.Entry()
input_entry.pack()
output_entry=tkinter.Entry()
output_entry.insert(tkinter.END,"output.txt")
output_entry.pack()
btn=tkinter.Button(text="确认",command=gen)
btn.pack()
win.mainloop()