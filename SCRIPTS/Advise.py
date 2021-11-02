"""
DESIGN ASSISTANT
"""


"""
PREPARE
"""
def discretize():
    """
    discretize options for Qt values

    :return:
    """
    pass

"""
ADVISE - interact with designer
"""
def predict():
    """
    "What would be the best type of... given my scenario.."

    IN : all Q values
    OUT : CO2e/ CO2e/m2


    IN : nearly all Q values
    ACTION : fill missing
    OUT : CO2e/ CO2e/m2

    :return:
    """

    pass

def recommend():

    """
    "What would be the best type of... given my scenario.."

    IN : all Q values but 1... or more + detail of interest (best/ordered/worse)

    ACTION : Predict for all intermediate values, order result

    OUT : value of caract that gives CO2e/ CO2e/m2 for this detail
    :return:
    """
    pass

"""
ANALYZE - provide general info
"""

def benchmark():

    """
    Done without model/model of 1 variable

    IN : 1 Q  + detail of interest (best/worst/most common)

    OUT : info about Q
    :return:
    """
    pass

def impact():

    """
    Done without model/model of 1 variable

    IN : 1 Q  + detail of interest (best/worst/most common)

    ACTION : run recommend for all subfeatures - delta = max - min

    OUT : delta it can have
    :return:
    """
    pass

def studyComponents():
    """
    Done without model/model of 1 variable

    IN : all Q
    ACTION : run impact for all variab / subfeatures - delta = max - min
    OUT : variab with biggest delta - target features
    :return:
    """
    pass

#todo : this can all go i linear regression file