from tkinter import *
from tkinter.ttk import Progressbar
import pyttsx3
import time
from pygame import mixer
# imported all necessary librarys

mixer.init()
mixer.music.load('kbc.mp3')#added and loaded kbc theme music.
mixer.music.play(1)

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)#used system voice for output
# created a list of questions for game 
questions = ["what is the highest score in ODI cricket?",
             "which Team WON WTC first Edition ?",
             "What is Highest score for india in T20 cricket?",
             "What is the national currency of the United States of America (USA)?",
             "Guido van Rossum in 1991 designed which language?",
             "garampani sanctury is located at ?",
             "Which one is the first fully supported 64-bit operating system?",
             "Red cresent day is celebrated on which day?",
             "what time corresponds to 23:23 hours ?",
             "Wgravity chembers are use to remove what?",
             "Which is the largest planet in our Solar system?",
             "How many continents are there in the world?",
             "How many years are there in one Millenium?",
             "Hockey Was introduced in the asian games in?",
             "Durand cup is associated with which game ?",
             "The international literacy day is observer on which Day?"]
# created list for option 1

first_option = ["209", "India",
                "109", "Euro",
                "Javascript", "assam",
                "Windows 7", "may 8", "11:23PM", "SO",
                "Earth", "8",
                "100 years", "1958-Tokyo", "Cricket","sep 8"]
# created list for option 2
second_option = ["183", "AUS",
                 "126", "Peso ",
                 "Python", "Diphu",
                 "Linux", "june 9", "11.11PM", "NO",
                 "Uranus", "5",
                 "50 years",
                 "1962-jakrta", "Football","Nov 28"]
# created list for option 3
third_option = ["264*", "Eng",
                "117", "Dollar",
                "Java", "kohima",
                "Mac", "may 16", "7:23PM", "sus. matter",
                "Mars", "7",
                "500 years",
                "1966-BK", "Hockey","May 2"]
# created list for option 4
fourth_option = ["205", "NZ",
                 "108", "Yen",
                 "JS", "gangtok",
                 "Windows XP", "april 7", "9.11PM", "CO",
                 "Jupiter",
                 "6",
                 "1000 years", "1970-BK",
                 "Volleyball","Sep 22"]
# created list for correct answers 
correct_answers = ["264*", "NZ", "126", "Dollar", "Python", "assam",
                   "Linux", "may 8", "7:23PM", "sus. matter", "Jupiter", "7", "1000 years", "1958-Tokyo",
                   "Football","sep 8"]
# for i in range(16):
#     time.sleep(5)
#  This is a function that takes an event as input and returns nothing.
def select(event):
    mixer.music.set_volume(1)
    b = event.widget
    value = b['text']
# created four progress bars, each of which has a label.
    callButton.config(image='')
    progressbarA.place_forget()
    progressbarLabelA.place_forget()

    progressbarB.place_forget()
    progressbarLabelB.place_forget()

    progressbarC.place_forget()
    progressbarLabelC.place_forget()

    progressbarD.place_forget()
    progressbarLabelD.place_forget()
# created a loop that checks if answer correspondes to question is correct or not
    for i in range(16):
        if value == correct_answers[i]:
            if value == first_option[15]:
# if the answer of the last question is correct the playagain() function gets called 
                def playagain():
                    phoneLifelineButton.config(state=NORMAL, image=phoneImage)
                    lifeline50Button.config(state=NORMAL, image=image50)
                    audiencePoleButton.config(state=NORMAL, image=audiencePole)
                    amountlabel.config(image=amountimage)
                    questionArea.delete(1.0, END)
                    questionArea.insert(END, questions[0])
                    optionButton1.config(text=first_option[0])
                    optionButton2.config(text=second_option[0])
                    optionButton3.config(text=third_option[0])
                    optionButton4.config(text=fourth_option[0])
                    root2.destroy()
                    mixer.music.load('kbc.mp3')
                    mixer.music.play(1)
# this function resets the window to normal state and display the questions from starting 

                def on_closing():#destroys the window
                    root2.destroy()
                    root.destroy()

                amountlabel.config(image=image15)
                mixer.music.stop()
                mixer.music.load('Kbcwon.mp3')
                mixer.music.play()
# window created for winner image
                root2 = Toplevel()
                root2.overrideredirect(True)
                root2.grab_set()
                root2.config(bg='black')
                root2.geometry('500x400+140+30')
                root2.title('You won 7 cr')
                mixer.music.load('7cr.mp3')
                mixer.music.play(1)
                centerimg = PhotoImage(file='center.png')
                imgLabel = Label(root2, image=centerimg, bd=0, )
                imgLabel.pack(pady=30)
# displays result of game 
                winlabel = Label(root2, text='You Won', font=('arial', 40, 'bold'), bg='black', fg='white')
                winlabel.pack()
# used to place a image of happy emoji
                happyimage = PhotoImage(file='happy.png')
                happYLabel = Label(root2, image=happyimage, bg='black')
                happYLabel.place(x=400, y=280)

                happYLabel1 = Label(root2, image=happyimage, bg='black')
                happYLabel1.place(x=30, y=280)
# created a button play again to restart the game 
                playagainButton = Button(root2, text='Play Again', font=('arial', 20, 'bold'), bg='black', fg='white',
                                         bd=0
                                         , activebackground='black', cursor='hand2', activeforeground='white',
                                         command=playagain)
                playagainButton.pack()
# created a button to close the game 
                closeButton = Button(root2, text='Close', font=('arial', 20, 'bold'), bg='black', fg='white', bd=0
                                     , activebackground='black', cursor='hand2', activeforeground='white',
                                     command=on_closing)
                closeButton.pack()

                root2.protocol('WM_DELETE_WINDOW', on_closing)
                root2.mainloop()
                break
# deletes previous question and adds next question 
            questionArea.delete(1.0, END)
            questionArea.insert(END, questions[i+1])
# updates answers according to questions
            optionButton1.config(text=first_option[i + 1])
            optionButton2.config(text=second_option[i + 1])
            optionButton3.config(text=third_option[i + 1])
            optionButton4.config(text=fourth_option[i + 1])
            amountlabel.config(image=images[i])
# if the answern of question is not correct tryagain function gets called 
        if value not in correct_answers:
            def tryagain():
                mixer.music.load('kbc.mp3')
                mixer.music.play(-1)
                phoneLifelineButton.config(state=NORMAL, image=phoneImage)
                lifeline50Button.config(state=NORMAL, image=image50)
                audiencePoleButton.config(state=NORMAL, image=audiencePole)

                questionArea.delete(1.0, END)
                questionArea.insert(END, questions[0])
                optionButton1.config(text=first_option[0])
                optionButton2.config(text=second_option[0])
                optionButton3.config(text=third_option[0])
                optionButton4.config(text=fourth_option[0])
                amountlabel.config(image=amountimage)
                root1.destroy()
# closes the window
            def on_closing():
                root1.destroy()
                root.destroy()
# sets the window to display message that you loss the game 
            mixer.music.stop()
            root1 = Toplevel()
            root1.overrideredirect(True)
            root1.grab_set()
            root1.config(bg='black')
            root1.geometry('500x400+140+30')
            root1.title('You won 0 rupees')
            img = PhotoImage(file='center.png')
            imgLabel = Label(root1, image=img, bd=0)
            imgLabel.pack(pady=30)
            loselabel = Label(root1, text='You Lose', font=('arial', 40, 'bold'), bg='black', fg='white')
            loselabel.pack()
            sadimage = PhotoImage(file='sad.png')
            sadlabel = Label(root1, image=sadimage, bg='black')
            sadlabel.place(x=400, y=280)
            sadlabel1 = Label(root1, image=sadimage, bg='black')
            sadlabel1.place(x=30, y=280)
# created a tryagain button
            tryagainButton = Button(root1, text='Try Again', font=('arial', 20, 'bold'), bg='black', fg='white', bd=0
                                    , activebackground='black', cursor='hand2', activeforeground='white',
                                    command=tryagain)
            tryagainButton.pack()

            closeButton = Button(root1, text='Close', font=('arial', 20, 'bold'), bg='black', fg='white', bd=0
                                 , activebackground='black', cursor='hand2', activeforeground='white',
                                 command=on_closing)
            closeButton.pack()

            root1.protocol('WM_DELETE_WINDOW', on_closing)

            root1.mainloop()
# mainloop ended for roo1
            break

# created a 50-50 lifeline which can be used by only one time throughout the game 
def lifeline50():
    lifeline50Button.config(image=image50x)
    lifeline50Button.config(state=DISABLED)

    if questionArea.get(1.0, 'end-1c') == questions[0]:
        optionButton1.config(text ='')
        optionButton4.config(state = DISABLED)

    if questionArea.get(1.0, 'end-1c') == questions[1]:
        optionButton3.config(text='')
        optionButton1.config(text='')

    if questionArea.get(1.0, 'end-1c') == questions[2]:
        optionButton3.config(text='')
        optionButton4.config(text='')

    if questionArea.get(1.0, 'end-1c') == questions[3]:
        optionButton2.config(text='')
        optionButton4.config(text='')

    if questionArea.get(1.0, 'end-1c') == questions[4]:
        optionButton3.config(text='')
        optionButton4.config(text='')

    if questionArea.get(1.0, 'end-1c') == questions[5]:
        optionButton2.config(text='')
        optionButton3.config(text='')

    if questionArea.get(1.0, 'end-1c') == questions[6]:
        optionButton1.config(text='')
        optionButton3.config(text='')

    if questionArea.get(1.0, 'end-1c') == questions[7]:
        optionButton3.config(text='')
        optionButton4.config(text='')

    if questionArea.get(1.0, 'end-1c') == questions[8]:
        optionButton2.config(text='')
        optionButton4.config(text='')

    if questionArea.get(1.0, 'end-1c') == questions[9]:
        optionButton1.config(text='')
        optionButton4.config(text='')

    if questionArea.get(1.0, 'end-1c') == questions[10]:
        optionButton1.config(text='')
        optionButton3.config(text='')

    if questionArea.get(1.0, 'end-1c') == questions[11]:
        optionButton1.config(text='')
        optionButton2.config(text='')

    if questionArea.get(1.0, 'end-1c') == questions[12]:
        optionButton1.config(text='')
        optionButton2.config(text='')

    if questionArea.get(1.0, 'end-1c') == questions[13]:
        optionButton2.config(text='')
        optionButton3.config(text='')

    if questionArea.get(1.0, 'end-1c') == questions[14]:
        optionButton1.config(text='')
        optionButton4.config(text='')
    if questionArea.get(1.0, 'end-1c') == questions[15]:
        optionButton2.config(text='')
        optionButton3.config(text='')

# created a second lifeline named audience poll which can be used by only once 
def audiencePoleLifeline():
    audiencePoleButton.config(image=audiencePolex)
    audiencePoleButton.config(state=DISABLED)
# placed 4  progressbar on windows with a position 
    progressbarA.place(x=580, y=190)
    progressbarLabelA.place(x=580, y=320)

    progressbarB.place(x=620, y=190)
    progressbarLabelB.place(x=620, y=320)

    progressbarC.place(x=660, y=190)
    progressbarLabelC.place(x=660, y=320)

    progressbarD.place(x=700, y=190)
    progressbarLabelD.place(x=700, y=320)
# added value for progressbar to provide correct answers 
    if questionArea.get(1.0, 'end-1c') == questions[0]:
        progressbarA.config(value=0)

        progressbarB.config(value=2)

        progressbarC.config(value=95)

        progressbarD.config(value=3)

    if questionArea.get(1.0, 'end-1c') == questions[1]:
        progressbarA.config(value=2)

        progressbarB.config(value=8)

        progressbarC.config(value=0)

        progressbarD.config(value=90)

    if questionArea.get(1.0, 'end-1c') == questions[2]:
        progressbarA.config(value=10)

        progressbarB.config(value=80)

        progressbarC.config(value=5)

        progressbarD.config(value=5)

    if questionArea.get(1.0, 'end-1c') == questions[3]:
        progressbarA.config(value=8)

        progressbarB.config(value=12)

        progressbarC.config(value=70)

        progressbarD.config(value=10)

    if questionArea.get(1.0, 'end-1c') == questions[4]:
        progressbarA.config(value=3)
        progressbarB.config(value=80)

        progressbarC.config(value=15)

        progressbarD.config(value=2)

    if questionArea.get(1.0, 'end-1c') == questions[5]:
        progressbarA.config(value=80)

        progressbarB.config(value=10)

        progressbarC.config(value=4)

        progressbarD.config(value=6)

    if questionArea.get(1.0, 'end-1c') == questions[6]:
        progressbarA.config(value=20)

        progressbarB.config(value=50)

        progressbarC.config(value=20)

        progressbarD.config(value=10)

    if questionArea.get(1.0, 'end-1c') == questions[7]:
        progressbarA.config(value=90)

        progressbarB.config(value=7)

        progressbarC.config(value=0)

        progressbarD.config(value=3)

    if questionArea.get(1.0, 'end-1c') == questions[8]:
        progressbarA.config(value=8)

        progressbarB.config(value=2)

        progressbarC.config(value=90)

        progressbarD.config(value=0)

    if questionArea.get(1.0, 'end-1c') == questions[9]:
        progressbarA.config(value=10)

        progressbarB.config(value=15)

        progressbarC.config(value=70)

        progressbarD.config(value=5)

    if questionArea.get(1.0, 'end-1c') == questions[10]:
        progressbarA.config(value=10)

        progressbarB.config(value=10)

        progressbarC.config(value=20)

        progressbarD.config(value=60)

    if questionArea.get(1.0, 'end-1c') == questions[11]:
        progressbarA.config(value=18)

        progressbarB.config(value=5)

        progressbarC.config(value=75)

        progressbarD.config(value=2)

    if questionArea.get(1.0, 'end-1c') == questions[12]:
        progressbarA.config(value=2)

        progressbarB.config(value=0)

        progressbarC.config(value=8)

        progressbarD.config(value=90)

    if questionArea.get(1.0, 'end-1c') == questions[13]:
        progressbarA.config(value=60)

        progressbarB.config(value=30)

        progressbarC.config(value=5)

        progressbarD.config(value=5)

    if questionArea.get(1.0, 'end-1c') == questions[14]:
        progressbarA.config(value=13)

        progressbarB.config(value=80)

        progressbarC.config(value=6)

        progressbarD.config(value=1)
    if questionArea.get(1.0, 'end-1c') == questions[15]:
        progressbarA.config(value=60)

        progressbarB.config(value=12)

        progressbarC.config(value=12)

        progressbarD.config(value=16)

# created a 3rd lifelien (call a friend ) and loaded a calling music 
def phoneLifeline():
    mixer.music.stop()
    mixer.music.load('calling.mp3')
    mixer.music.play()

    phoneLifelineButton.config(image=phoneImageX, state=DISABLED)
    callButton.config(image=callimage)

# this function helps to get output of correect answers from lifeline 
def phoneclick():
    mixer.music.load('kbc.mp3')
    mixer.music.play(-1)
    mixer.music.set_volume(0)
# runs forloop for  getting correct answers output 
    for i in range(16):
        if questionArea.get(1.0, 'end-1c') == questions[i]:
            engine.say(f'The Answer is {correct_answers[i]}')
            engine.runAndWait()

# created main window for game 
root = Tk()
root.geometry('1270x652+0+0')
root.resizable(0, 0)
root.title('kaun banega crorepati🤑')
root.config(bg='black')
# left frame 
leftFrame = Frame(root, bg='black', padx=90)
leftFrame.grid(row=0, column=0)
# right frame 
rightFrame = Frame(root, bg='black', padx=50, pady=25)
rightFrame.grid(row=0, column=1)
# top frame 
topFrame = Frame(leftFrame, bg='black', pady=15)
topFrame.grid(row=0, column=0)
# middleframe 
middleFrame = Frame(leftFrame, bg='black', pady=15)
middleFrame.grid(row=1, column=0)
# botton frame
bottomFrame = Frame(leftFrame, bg='black')
bottomFrame.grid(row=2, column=0)
# added center image 
centreImage = PhotoImage(file='center.png')
logoLabel = Label(middleFrame, image=centreImage, bd=0, width=300, height=200, bg='black')
logoLabel.grid(row=0, column=0)
# added image for 50-50 lifeline
image50 = PhotoImage(file='50-50.png')
image50x = PhotoImage(file='50-50-X.png')

lifeline50Button = Button(topFrame, image=image50, bd=0, bg='black', cursor='hand2', activebackground='black', width=180,
                      height=80, command=lifeline50)
lifeline50Button.grid(row=0, column=0)
# added image for AudiencePoll lifeline
audiencePole = PhotoImage(file='audiencePole.png')
audiencePolex = PhotoImage(file='audiencePoleX.png')
audiencePoleButton = Button(topFrame, image=audiencePole, bd=0, bg='black', cursor='hand2', activebackground='black',
                            width=180, height=80, command=audiencePoleLifeline)
audiencePoleButton.grid(row=0, column=1)
# added image for caal a friend lifeline
phoneImage = PhotoImage(file='phoneAFriend.png')
phoneImageX = PhotoImage(file='phoneAFriendX.png')
phoneLifelineButton = Button(topFrame, image=phoneImage, bd=0, bg='black', cursor='hand2', activebackground='black', width=180,
                     height=80, command=phoneLifeline)
phoneLifelineButton.grid(row=0, column=2)

callimage = PhotoImage(file='phone.png')
callButton = Button(root, bg='black', bd=0, activebackground='black', cursor='hand2', command=phoneclick)
callButton.place(x=70, y=260)
# used 16 images with marks on increasing amount of prize
amountimage = PhotoImage(file='Picture0.png')
image1 = PhotoImage(file='Picture1.png')
image2 = PhotoImage(file='Picture2.png')
image3 = PhotoImage(file='Picture3.png')
image4 = PhotoImage(file='Picture4.png')
image5 = PhotoImage(file='Picture5.png')
image6 = PhotoImage(file='Picture6.png')
image7 = PhotoImage(file='Picture7.png')
image8 = PhotoImage(file='Picture8.png')
image9 = PhotoImage(file='Picture9.png')
image10 = PhotoImage(file='Picture10.png')
image11 = PhotoImage(file='Picture11.png')
image12 = PhotoImage(file='Picture12.png')
image13 = PhotoImage(file='Picture13.png')
image14 = PhotoImage(file='Picture14.png')
image15 = PhotoImage(file='Picture15.png')
# created image list for easy accessibility
images = [image1, image2, image3, image4, image5, image6, image7, image8, image9, image10, image11, image12, image13
    , image14, image15]

amountlabel = Label(rightFrame, image=amountimage, bg='black', bd=0)
amountlabel.grid(row=0, column=0)
# added layout for showing options 
layoutimage = PhotoImage(file='lay.png')
layoutlabel = Label(bottomFrame, image=layoutimage, bg='black', bd=0)
layoutlabel.grid(row=0, column=0)


questionArea = Text(bottomFrame, font=('arial', 18, 'bold'), bg='black', fg='white', width=34, height=2,
                        wrap='word',bd=0)
questionArea.place(x=70,y=10)

questionArea.insert(END, questions[0])



# created label for  option list
# opt1
labelA = Label(bottomFrame, font=('arial', 16, 'bold'), text='A:', bg='black', fg='white')
labelA.place(x=60,y=110)
optionButton1 = Button(bottomFrame, text=first_option[0], font=('arial', 18, 'bold'), bg='black', fg='white',
                              cursor='hand2',bd=0,activebackground='black',activeforeground='white')
optionButton1.place(x=100,y=100)
# opt2
labelB = Label(bottomFrame, font=('arial', 16, 'bold'), text='B:', bg='black', fg='white')
labelB.place(x=330,y=110)
optionButton2 = Button(bottomFrame, text=second_option[0], font=('arial', 18, 'bold'), bg='black', fg='white',
                              cursor='hand2',bd=0,activebackground='black',activeforeground='white')
optionButton2.place(x=370,y=100)
# opt3
labelC = Label(bottomFrame, font=('arial', 16, 'bold'), text='C:', bg='black', fg='white')
labelC.place(x=60,y=190)

optionButton3 = Button(bottomFrame, text=third_option[0], font=('arial', 18, 'bold'), bg='black', fg='white',
                             cursor='hand2',bd=0,activebackground='black',activeforeground='white')
optionButton3.place(x=100,y=180)
# opt4
labelD = Label(bottomFrame, font=('arial', 16, 'bold'), text='D:', bg='black', fg='white')
labelD.place(x=330,y=190)

optionButton4 = Button(bottomFrame, text=fourth_option[0], font=('arial', 18, 'bold'), bg='black', fg='white',
                             cursor='hand2',bd=0,activebackground='black',activeforeground='white')
optionButton4.place(x=370,y=180)
# progressbar design

progressbarA = Progressbar(root, orient=VERTICAL, mode='determinate', length=120)

progressbarLabelA = Label(root, text='A', font=('arial', 20, 'bold'), bg='black', fg='white')

progressbarB = Progressbar(root, orient=VERTICAL, mode='determinate', length=120)

progressbarLabelB = Label(root, text='B', font=('arial', 20, 'bold'), bg='black', fg='white')

progressbarC = Progressbar(root, orient=VERTICAL, mode='determinate', length=120)

progressbarLabelC = Label(root, text='C', font=('arial', 20, 'bold'), bg='black', fg='white')

progressbarD = Progressbar(root, orient=VERTICAL, mode='determinate', length=120)

progressbarLabelD = Label(root, text='D', font=('arial', 20, 'bold'), bg='black', fg='white')
# binds the event 
optionButton1.bind('<Button-1>', select)
optionButton2.bind('<Button-1>', select)
optionButton3.bind('<Button-1>', select)
optionButton4.bind('<Button-1>', select)
# end of code .
root.mainloop()
root.quit()
# Thank You❤️