import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn import preprocessing
import pickle
from sklearn.svm import SVC

def testSVCPickle(text):
    filename = r'C:\Users\jake_\OneDrive\Desktop\Macquarie University\Personal Projects\Cybersecurity\Django\three\mysite\corpus\Scikit_Model\finalized_model_91_percent.sav'
    loaded_model = pickle.load(open(filename, 'rb'))
    listText = []
    listText.append(text)

    print("listText: ")
    #print(listText)

    predictionText = loaded_model.predict(listText)
    print(predictionText)

    listText = []
    return predictionText

def PPShares3rdParty(text):
    #print("type: ")
    #print(type(testSVCPickle(text)))
    #print(type(testSVCPickle(text)[0]))
    if testSVCPickle(text)[0] == 1:
        print("Privacy Policy is Positive for sharing information with third party")
        return True

    print("Privacy Policy is Negative for sharing information with third party")
    return False
