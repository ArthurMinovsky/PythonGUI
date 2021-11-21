from tkinter import *
from tkinter import ttk, messagebox  # ttk is theme of tk
import csv
import random


# CSV File
def WritetoCSV(data):
    with open('data.csv', 'a', newline='', encoding='utf-8') as file:
        fw = csv.writer(file)  # fw = file writer
        fw.writerow(data)
    print('save complete')

# Read CSV


def ReadCSV():
    with open('data.csv', newline='', encoding='utf-8') as file:
        fr = csv.reader(file)  # fr = file reader
        data = list(fr)
    # print(data)
    return data  # return คือ การส่งข้อมูลไปใข้งานต่อ


# main program
GUI = Tk()
GUI.title('โปรแกรมคำศัพท์ Flash Card')
GUI.geometry('700x700')

# font
FONT1 = ('Angsana New', 20, 'bold')
FONT2 = ('Angsana New', 20)
FONT3 = ('Angsana New',36,'bold')

# Tab
Tab = ttk.Notebook(GUI)

T1 = Frame(Tab)
T2 = Frame(Tab)

Tab.add(T1, text='Add')
Tab.add(T2, text='Flash Card')

Tab.pack(fill=BOTH, expand=1)


# title
L1 = ttk.Label(T1, text='Word', font=FONT1, foreground='green')
L1.pack()  # นำ L1 ไปติดโปรแกรมหลัก

# text box 1
v_title = StringVar()  # StringVar() Special Variable for save data from GUI
E1 = ttk.Entry(T1, textvariable=v_title, font=FONT2, width=30)
E1.pack()


# detail
L2 = ttk.Label(T1, text='Define', font=FONT1, foreground='green')
L2.pack()

# text box 2
v_detail = StringVar()
E2 = ttk.Entry(T1, textvariable=v_detail, font=FONT2, width=40)
E2.pack()

# Create functoin Update table
'''def UpdateTable():
        table.delete(*table.get_children()
                     )#clear recent data table.get_children// ดึงข้อมูลทั้งหมดในตารางเข้ามา
        alldata = ReadCSV() #Call function csv from above
        for row in alldata:
                table.insert('','end',value=row)
        global allquestion
        allquestion = ReadCSV()'''


allquestion = ReadCSV()


# Button Save
def NeWline(event=None):
    E2.focus()

# ฟังก์ชันบันทึกสิ่งที่อยู่ในตารางลงในไฟล์


def SaveQuestion(event=None):
    with open('data.csv', 'w', newline='', encoding='utf-8') as file:
        fw = csv.writer(file)  # fw = file writer
        fw.writerows(allquestion)
    print('save complete')


# ฟังก์ชันการเพิ่มค่า ในปุ่ม add
def SaveButton(event=None):
    SaveQuestion()
    title = v_title.get()  # .get() pick up value from variable v_title
    detail = v_detail.get()
    print(title)
    print(detail)
    dt = [title, detail]  # data
    WritetoCSV(dt)
    print('saving....')
    # clear data
    v_title.set('')  # command clear data
    v_detail.set('')
    E1.focus()  # make cursor at E1
    Rollback()  # Update Every pulse in button


E1.bind('<Return>', NeWline)
# Check E2 have Enter pulse if pulse call funtion SaveButton
E2.bind('<Return>', SaveButton)

B1 = Button(T1, text='Add', command=SaveButton)
B1.pack(ipadx=20, ipady=10, pady=20)

# ipadx = range of internal button axis x
# pady = range of external button axis y


# setting font for table

style = ttk.Style()
style.configure('Treeview.Heading', font=('Angsana New', 20))
style.configure('Treeview', font=('Angsana New', 18), rowheight=30)


# table
header = ('Title', 'Detail')  # ประกาศตัวแปร header

table = ttk.Treeview(T1, height=10, column=header,
                     show='headings')  # '''#ฟังก์ชันสร้างตารางแบบ Treeview (ใส่ GUI,ความสูงเเท่ากับ 10,จำนวนคอลัมน์,แสดงชื่อคอลัมน'''

table.place(x=20, y=300)  # วางตำแหน่งตารางที่ (แกน x=20, แกน y=300)

# หัวข้อของตาราง (Title, ชื่อคอลัมน์ 'header')
table.heading('Title', text='header')
table.column('Title', width=200)  # show detail column (Title , ความกว่าง=200)
table.heading('Detail', text='detail')
table.column('Detail', width=460)

# ทดลองใส่ข้อมูล
# '''row = ['GUI is?','GUI : Graphical User Interface'] #ประกาศตัวแปร row
# table.insert('','end',value=row) #แทรกตาราง ('section id ตารางถ้ามีsection','ให้เแทรกเพิ่มที่ตัวท้ายสุด',ค่าตาราง=ตัวแปรrow


# """ print(help(table)) คือการเรียกฟังชันต์ช่วยเหลือ โดยต้องระบุว่าจะให้มันช่วยเหลือในตัวคำสั่ง/ตัวแปรไหน"""'''

# ลบค่า
def DeleteQuestion(event=None):
    select = table.selection()  # check which is question?
    data = table.item(select)
    print('Which word to delete ',data['values'])
    if data['values'] in allquestion:
        check = messagebox.askquestion('Delete Confirmation', 'Do you want to delete or not?')
        if check == 'yes':
                allquestion.remove(data['values'])
                print('Count:', len(allquestion))
                SaveQuestion()
                # clear recent data table.get_children// ดึงข้อมูลทั้งหมดในตารางเข้ามา
                table.delete(*table.get_children())
                alldata = allquestion
                for row in alldata:
                        table.insert('', 'end', value=row)
                messagebox.showinfo('Completed', 'Deleted')
    else:
        messagebox.showinfo('Delete Error', 'Please choose word to delete.')


table.bind('<Delete>', DeleteQuestion)


# ฟังก์ชันในการรีเฟรชค่าและแก้บัค
def Rollback(event=None):
    table.delete(*table.get_children())
    alldata = ReadCSV()
    for row in alldata:
        table.insert('', 'end', value=row)
    global allquestion
    allquestion = ReadCSV()


table.bind('<F5>', Rollback)


# UpdateTable()

Rollback()

##################################################################################

# ส่วนของ Tab 2 flash card

v_question = StringVar()  # use collect question
v_question.set('-------question(press Next for start)--------')
R1 = ttk.Label(T2,textvariable=v_question, font=FONT3)
R1.pack(pady=20)

v_answer = StringVar()
v_answer.set('---------press Show for show answer----------')
R2 = ttk.Label(T2,wraplength=666,textvariable=v_answer,font=FONT3)
R2.pack(pady=20)

# Button
BF1 = Frame(T2)  # Create button frame
BF1.pack(pady=100)


v_current_ans = StringVar()  # hidden answer


def Next():
    q = random.choice(allquestion)
    v_question.set(q[0])
    v_answer.set('---------press Show for show answer----------')
    v_current_ans.set(q[1])
    BC3['state'] = 'normal'


def Show():
    # Bring Current hidden answer show in v_answer
    v_answer.set(v_current_ans.get())


# show score
score = 0
v_score = StringVar()
v_score.set('Score: {} point'.format(score))
Score = ttk.Label(T2, textvariable=v_score, font=('Impact', 30))
Score.place(x=400, y=600)


def ScoreUp():
    global score  # declare global variable into funtion
    score += 1  # score = score + 1
    v_score.set('Score: {} point'.format(score))
    BC3['state'] = 'disabled'


BC1 = ttk.Button(BF1, text='Next', command=Next)
BC2 = ttk.Button(BF1, text='Show', command=Show)
BC3 = ttk.Button(BF1, text='Score +1', command=ScoreUp)
BC1.grid(row=0, column=0, ipadx=20, ipady=30)
BC2.grid(row=0, column=1, ipadx=20, ipady=30)
BC3.grid(row=0, column=2, ipadx=20, ipady=30)


GUI.mainloop()
