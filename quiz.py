from enum import Enum

class State(str,Enum):
    QUESTION_1 = "This is question 1"
    QUESTION_2 = "This is question 2"
    QUESTION_3 = "This is question 3"
    RESULT_1 = "Result 1"
    RESULT_2 = "Result 2"

class Trigger(str,Enum):
    ANSWER_1 = "This is answer 1"
    ANSWER_2 = "This is answer 2"
    ANSWER_3 = "This is answer 3"
    ANSWER_4 = "This is answer 4"
    ANSWER_5 = "This is answer 5"
    ANSWER_6 = "This is answer 6"


