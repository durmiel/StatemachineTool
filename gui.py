import tkinter as tk


class Gui(object):
    """Gui is the root element of the Statemachine Tool. It
        represents the root gui element """

    def __init__(self, title):
        super(Gui, self).__init__()
        self.__uiRoot = tk.Tk()
        self.__uiRoot.title(title)
        self.__uiRoot.geometry('612x341')

        BtLoadFile = tk.Button(self.__uiRoot, text="Load", width=10)
        BtLoadFile.grid(row=1, column=1, padx=7.5, pady=6)

        BtSaveFile = tk.Button(self.__uiRoot, text="Save", width=10)
        BtSaveFile.grid(row=1, column=2, padx=7.5, pady=6)

        BtNewState = tk.Button(self.__uiRoot, text="State", width=10)
        BtNewState.grid(row=1, column=3, padx=7.5, pady=6)

        BtNewTransition = tk.Button(self.__uiRoot, text="Transistion",
                                    width=10)
        BtNewTransition.grid(row=1, column=4, padx=7.5, pady=6)

        BtExit = tk.Button(self.__uiRoot, text="Exit", width=10,
                           command=self.__exitGui)
        BtExit.grid(row=1, column=5, padx=7.5, pady=6)

        FrameStatemachine = tk.Frame(self.__uiRoot, bg='cyan', width=600,
                                     height=300)
        FrameStatemachine.grid(row=2, column=1, columnspan=5)

        self.__uiRoot.mainloop()
        pass

    def __exitGui(self):
        self.__uiRoot.destroy()
        pass


class GuiState(tk.Frame):
    """Gui element for the state class"""

    def __init__(self, parent, stateName):
        tk.Frame.__init__(self, parent)
