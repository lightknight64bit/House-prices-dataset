import pandas as pd 
import numpy as np
from sklearn.metrics import mean_squared_log_error
solution = pd.read_csv("solution.csv")
def score(solution, model_pred):
    solution = solution["SalePrice"].values
    model_pred = model_pred["SalePrice"].values
    try:
        return np.sqrt(mean_squared_log_error(solution,model_pred))
    except ValueError:
        return 'inf'

f = input("Would u like to score your own submission?(y/n):")
while f != "n":
    
    file = pd.read_csv(input("Enter file name:"))
    print("Your submission score is: %s" % score(solution, file))
    f = input("Would u like to score your own submission?(y/n):")

input("press enter to exit")
