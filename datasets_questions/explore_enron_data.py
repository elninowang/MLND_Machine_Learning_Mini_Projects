#!/usr/bin/python

""" 
    Starter code for exploring the Enron dataset (emails + finances);
    loads up the dataset (pickled dict of dicts).

    The dataset has the form:
    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }

    {features_dict} is a dictionary of features associated with that person.
    You should explore features_dict as part of the mini-project,
    but here's an example to get you started:

    enron_data["SKILLING JEFFREY K"]["bonus"] = 5600000
    
"""

import pickle
import sys
import os
sys.path.append("../final_project/")
from poi_email_addresses import *

enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "r"))

count = 0;
poi_equal_1_count = 0
for k,v in enron_data.items():
    count += 1
    print "{} -- {} -- {}".format(k, len(v.values()), v)
    if v["poi"] == 1:
        poi_equal_1_count += 1

print "count: %d"%count
print "poi_equal_1_count: %d"%poi_equal_1_count

print
poi_with_email_count = 0
email_list = poiEmails()
poi_names_file = open('../final_project/poi_names.txt','r')
for line in poi_names_file:
    if line.startswith('(y)') or line.startswith('(n)'):
        name = line[4:]
        first_name = name[0: name.find(",")].strip().lower()
        last_name =  name[name.find(",")+1:].strip().lower()
        for email in email_list:
            if email.find(first_name) != -1 and email.find(last_name) != -1:
                poi_with_email_count += 1
                break

print "poi_with_email_count: %d"%poi_with_email_count
print
print enron_data["Prentice James".upper()]
print "James Prentice stocks: %d"%enron_data["Prentice James".upper()]["total_stock_value"]
print
print enron_data["Colwell Wesley".upper()]
print "Wesley Colwell from_this_person_to_poi: %d"%enron_data["Colwell Wesley".upper()]["from_this_person_to_poi"]

print
print enron_data["Skilling Jeffrey k".upper()]
print "Jeffrey Skilling from_this_person_to_poi: %d"%enron_data["Skilling Jeffrey k".upper()]["exercised_stock_options"]

print
quantified_salary_count = 0
known_email_address_count = 0
for k,v in enron_data.items():
    if v["salary"] != 'NaN': quantified_salary_count += 1
    if v["email_address"] != 'NaN': known_email_address_count += 1
print "quantified_salary_count: %d"%quantified_salary_count
print "known_email_address_count: %d"%known_email_address_count

print
nan_total_payments_count = 0
for k,v in enron_data.items():
    if v["total_payments"] == 'NaN':
        nan_total_payments_count += 1
print "nan_total_payments_count: %d and %d %%"%(nan_total_payments_count, (nan_total_payments_count*100/count))