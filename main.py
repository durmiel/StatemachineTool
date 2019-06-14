
import os
from filemanager import FileManager


def main():
    filename = "TestStatemachine.txt"
    path = os.getcwd() + "\\Testdata\\" + filename

    parser = FileManager()
    states, transitions = parser.loadFromFile(path, isOwnFormat=True)
    print("States:")
    for state in states:
        print(state.getName())
        pass
    
    print("Transitions")
    for item in transitions:
        print(item.getCondition())
        print(item.getStartState())
        print(item.getEndState())
        pass
    
    pass


if __name__ == '__main__':
    main()
