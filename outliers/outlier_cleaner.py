#!/usr/bin/python
import numpy as np

def outlierCleaner(predictions, ages, net_worths):
    """
        Clean away the 10% of points that have the largest
        residual errors (difference between the prediction
        and the actual net worth).

        Return a list of tuples named cleaned_data where 
        each tuple is of the form (age, net_worth, error).
    """
    errors = net_worths-predictions
    errors_abs = np.abs(errors).reshape(-1)
    result = np.sort(errors_abs)
    limit = result[len(result)*9//10]

    ### your code goes here
    cleaned_data = []
    for i in range(len(errors_abs)):
        if errors_abs[i] < limit:
            cleaned_data.append((ages[i][0], net_worths[i][0], errors[i][0]))

    return cleaned_data

