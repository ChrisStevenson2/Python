from tkinter import *
import ctypes
import random
import tkinter
 
# For a better looking screen
ctypes.windll.shcore.SetProcessDpiAwareness(1)

# Setup
root = Tk()
root.title('Type Speed Test')

# Setting the window dimensions
root.geometry('900x900')

# Font for Labels and Buttons
root.option_add("*Label.Font", "consolas 30")
root.option_add("*Button.Font", "consolas 30")


# functions
def keyPress(event=None):
    try:
        if event.char.lower() == labelRight.cget('text')[0].lower():
            # Deleting one from the right side.
            labelRight.configure(text=labelRight.cget('text')[1:])
            # Deleting one from the right side.
            labelLeft.configure(text=labelLeft.cget('text') + event.char.lower())
            #set the next Letter Lavbel
            currentLetterLabel.configure(text=labelRight.cget('text')[0])
    except tkinter.TclError:
        pass


def resetWritingLabels():
    # Text List
    possibleTexts = [
        'After two AI winters and ongoing battles for academic funding, we have entered a golden age in industry employment. Complex databases, fast and affordable processing units, and advanced algorithms have rejuvenated established fields of human expertise in mathematics, statistics, computer programming, graphics and visualization as well as good old problem-solving skills. In a global job market steadily automated and simplified by Web 2.0 technology, the field of machine learning provides a professional nirvana for human ingenuity and meaningful work. It’s a cognitively demanding occupation; one that goes far beyond tuning ad campaigns or tracking web traffic on side-by-side monitors. With jobs in this industry demanding expertise in three distinct fields, achieving machine intelligence is far from easy and demands a high level of expertise. The ideal skillset for a machine learning developer spans coding, data management, and knowledge of statistics and mathematics. Optional areas of expertise include data visualization, big data management, and practical experience in distributed computing architecture.'
        'For writers, a random sentence can help them get their creative juices flowing. Since the topic of the sentence is completely unknown, it forces the writer to be creative when the sentence appears. There are a number of different ways a writer can use the random sentence for creativity. The most common way to use the sentence is to begin a story. Another option is to include it somewhere in the story. A much more difficult challenge is to use it to end a story. In any of these cases, it forces the writer to think creatively since they have no idea what sentence will appear from the tool.',
        'The goal of Python Code is to provide Python tutorials, recipes, problem fixes and articles to beginner and intermediate Python programmers, as well as sharing knowledge to the world. Python Code aims for making everyone in the world be able to learn how to code for free. Python is a high-level, interpreted, general-purpose programming language. Its design philosophy emphasizes code readability with the use of significant indentation. Python is dynamically-typed and garbage-collected. It supports multiple programming paradigms, including structured (particularly procedural), object-oriented and functional programming. It is often described as a "batteries included" language due to its comprehensive standard library.',
        'As always, we start with the imports. Because we make the UI with tkinter, we need to import it. We also import the font module from tkinter to change the fonts on our elements later. We continue by getting the partial function from functools, it is a genius function that excepts another function as a first argument and some args and kwargs and it will return a reference to this function with those arguments. This is especially useful when we want to insert one of our functions to a command argument of a button or a key binding.'
    ]
    # Chosing one of the texts randomly
    text = random.choice(possibleTexts).lower()
    # defining where the text is split
    splitPoint = 0
    # Text that is already written
    global labelLeft
    labelLeft = Label(root, text=text[0:splitPoint], fg='grey')
    labelLeft.place(relx=0.5, rely=0.5, anchor=E)

    # Text which will be written
    global labelRight
    labelRight = Label(root, text=text[splitPoint:])
    labelRight.place(relx=0.5, rely=0.5, anchor=W)

    # This label shows the user which letter they have to press
    global currentLetterLabel
    currentLetterLabel = Label(root, text=text[splitPoint], fg='grey')
    currentLetterLabel.place(relx=0.5, rely=0.6, anchor=N)

    # Elapsed time
    global timeleftLabel
    timeleftLabel = Label(root, text=f'0 Seconds', fg='grey')
    timeleftLabel.place(relx=0.5, rely=0.4, anchor=S)

    global writeAble
    writeAble = True
    root.bind('<Key>', keyPress)

    global passedSeconds
    passedSeconds = 0

    # Binding callbacks to functions after a certain amount of time.
    root.after(60000, stopTest)
    root.after(1000, addSecond)

def stopTest():
    global writeAble
    writeAble = False
    
    # Calculating the amount of words
    amountWords = len(labelLeft.cget('text').split(' '))
    
    # Destroy all unwanted widgets.
    timeleftLabel.destroy()
    currentLetterLabel.destroy()
    labelRight.destroy()
    labelLeft.destroy()

    # Display the test results with a formatted string
    global ResultLabel
    ResultLabel = Label(root, text=f'Words per Minute: {amountWords}', fg='black')
    ResultLabel.place(relx=0.5, rely=0.4, anchor=CENTER)

    # Display a button to restart the game
    global ResultButton
    ResultButton = Button(root, text=f'Retry', command=restart)
    ResultButton.place(relx=0.5, rely=0.6, anchor=CENTER)

def restart():
    # Destry result widgets
    ResultLabel.destroy()
    ResultButton.destroy()

    # re-setup writing labels.
    resetWritingLabels()

def addSecond():
    # Add a second to the counter.

    global passedSeconds
    passedSeconds += 1
    timeleftLabel.configure(text=f'{passedSeconds} Seconds')

    # call this function again after one second if the time is not over.
    if writeAble:
        root.after(1000, addSecond)

# This will start the Test
resetWritingLabels()

# Start the mainloop
root.mainloop()