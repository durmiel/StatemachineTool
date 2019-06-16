
import os
from statemachine import State, Transition


class FileManager(object):
    """Parser parse the own format and later the XML format"""

    def __init__(self):
        super(FileManager, self).__init__()
        pass

    def loadFromFile(self, path, isOwnFormat=False):
        states = transitions = None

        if path is None:
            raise AttributeError("No valid path")

        if not os.path.isfile(path):
            raise FileNotFoundError("File with path: " + path + " not found")

        if isOwnFormat:
            states, transitions = self.__loadOwnFormat(path)
            pass
        else:
            states, transitions = self.__loadXmlFile(path)
            pass

        return states, transitions
        pass

    def __loadXmlFile(self, path):
        print("XML Loaded!")
        return 0, 0
        pass

    def __loadOwnFormat(self, path):
        print("Start loading own format...")
        file = open(path, mode='r')
        fileContent = file.readlines()
        file.close()

        stateList = []
        transitionList = []
        marker = 0

        for item in fileContent:
            # skip comments
            if "#" in item:
                marker = marker + 1
                continue
                pass
            # add states to the list
            if marker == 1:
                state = State()
                state.setName(item[:-1])
                stateList.append(state)
                pass
            # add transitions to list
            if marker == 2:
                transition = self.__decodeTransitionFromLine(item, stateList)
                transitionList.append(transition)
                pass
            pass

        return stateList, transitionList
        pass

    def __decodeTransitionFromLine(self, line, stateList):
        parts = line[:-1].split(",")
        states = parts[0].split("-")

        if len(parts) > 1:
            condition = parts[1]
            pass
        else:
            condition = ""

        transition = Transition()
        transition.setCondition(condition)

        # look for the start states in the state list
        for state in stateList:
            if state.getName() == states[0]:
                transition.setStartState(state)
                break

        # look for the end states in the state list
        for state in stateList:
            if state.getName() == states[1]:
                transition.setEndState(state)
                break
        pass
