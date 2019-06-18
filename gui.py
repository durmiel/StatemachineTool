import tkinter as tk
import tkinter.filedialog as fdialog

class Gui(object):
    """Gui is the root element of the Statemachine Tool. It
        represents the root gui element """

    def __init__(self, title):
        super(Gui, self).__init__()
        self.__uiRoot = tk.Tk()
        self.__uiRoot.title(title)
        self.__uiRoot.geometry('612x341')

        self.__initFrameButtons(self.__uiRoot)

        FrameStatemachine = tk.Frame(self.__uiRoot, width=600, height=300,
                                     highlightbackground="black", highlightcolor="black",
                                     highlightthickness=1)
        FrameStatemachine.pack()

        self.__uiRoot.mainloop()
        pass

    def __initFrameButtons(self, rootUi):
        FrameButtons = tk.Frame(self.__uiRoot, width=600, height=100)
        FrameButtons.pack()

        BtLoadFile = tk.Button(FrameButtons, text="Load",
                               width=10, command=self.__loadStatemachineFromFile)
        BtLoadFile.grid(row=1, column=1, padx=7.5, pady=6)

        BtSaveFile = tk.Button(FrameButtons, text="Save",
                               width=10, command=self.__saveStatemachineFromFile)
        BtSaveFile.grid(row=1, column=2, padx=7.5, pady=6)

        BtNewState = tk.Button(FrameButtons, text="State",
                               width=10, command=self.__addState)
        BtNewState.grid(row=1, column=3, padx=7.5, pady=6)

        BtNewTransition = tk.Button(
            FrameButtons, text="Transistion", width=10, command=self.__addTransition)
        BtNewTransition.grid(row=1, column=4, padx=7.5, pady=6)

        BtExit = tk.Button(FrameButtons, text="Exit", width=10,
                           command=self.__exitGui)
        BtExit.grid(row=1, column=5, padx=7.5, pady=6)
        pass

    def __exitGui(self):
        self.__uiRoot.destroy()
        pass

    def __loadStatemachineFromFile(self):
        fileName = fdialog.askopenfilename(
            parent=self.__uiRoot, initialdir='C:/',
            title='Choose file',
            filetypes=[('Text Files', '.txt'),
                       ('XML Files', '.xml')]
            )
        if fileName is "":
            return
        print(fileName)
        pass

    def __saveStatemachineFromFile(self):
        fileName = fdialog.asksaveasfilename(
            parent=self.__uiRoot, initialdir='C:/',
            title='Choose file',
            filetypes=[('Text Files', '.txt'),
                       ('XML Files', '.xml')]
            )
        pass

    def __addState(self):
        pass

    def __addTransition(self):
        pass
