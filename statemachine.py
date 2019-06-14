
import uuid


class State(object):
    """This class represents a state in a state diagram"""

    def __init__(self):
        super(State, self).__init__()
        self.__name = ""
        self.__transitions = []

    def setName(self, name):
        if name is not None:
            self.__name = name
            pass
        else:
            raise AttributeError("Condition is None")
        pass

    def getName(self):
        return self.__name


class Transition(object):
    """docstring for Transition"""

    def __init__(self):
        super(Transition, self).__init__()
        self.__condition = ""
        self.__startState = None
        self.__endState = None
        self.__id = uuid.uuid4()
        pass

    def setCondition(self, condition):
        if condition is not None:
            self.__condition = condition
            pass
        else:
            raise AttributeError("Condition is None")
        pass

    def getCondition(self):
        return self.__condition
        pass

    def setStartState(self, startState):
        if startState is not None:
            if isinstance(startState, State):
                self.__startState = startState
            pass
        else:
            raise AttributeError("Error. startState is None")
        pass

    def getStartState(self):
        return self.__startState
        pass

    def setEndState(self, endState):
        if endState is not None:
            if isinstance(endState, State):
                self.__endState = endState
            pass
        else:
            raise AttributeError("Error. endState is None")
        pass

    def getEndState(self):
        return self.__endState
        pass
