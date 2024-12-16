#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 24 11:18:51 2024

@author: Bodhi Global Analysis (Jungyeon Lee)
"""

"""
Please define the parameters for data preprocessing pipeline
"""
import carob_data_preprocessing as dp

project_name = "UNFPA KAP Survey on GBV"

file_type = 'xlsx' 
# Original data format: xlsx, xls, csv

file_path = "Data/24-UNFPA-SS-1 - Raw_data"
# Original data location and name (excluding file extension): "Data/(name)"

file_path_others = "Data/24-UNFPA-SS-1 - Open-End.xlsx"
# Specify the path and name of the Excel sheet where the values from the open-ended columns will be saved (New file)
# For example: "Data/(project name) others.xlsx"

respondent_name = None
# Original column name for respondents' names (for anonymisation and duplicate removal)

identifiers = 'id'
# Identifiers for detecting duplicates (list, do not remove respondent_name)
# Recommendation: At least three identifiers

dates = [] 
# Remove the dates on which the pilot test was conducted from the data
# for example ['2024-07-18', '2024-07-22', '2024-07-23']

cols_new = ['id','s1', 's2', 's3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15','16', '17', '18', '19', 
 '20', '21', '22', '23.1', '23.2', '23.3', '23.4', '23.5', '23.6', '23.7', '24', '25','26', '27','28', '29',
 '30', '31', '32', '33.1', '33.2', '33.3', '33.4','33.5', '33.6', '33.7', '33.8', '33.9', '34.1', '34.2', '34.3', '34.4', '34.5', '34.6', '34.7', '34.8',
 '35.1', '35.2', '35.3', '35.4', '35.5', '35.6', '35.7', '36', '37.1', '37.10', '37.11', '37.2', '37.3', '37.4', '37.5', '37.6', '37.7', '37.8', '37.9', '38', '39', '40', '41',
 '42', '43', '44', '45', '46', '47', '48', '49', '50', '51', '52', '53', '54.1', '54.2', '54.3', '54.4', '54.5',
 '55', '56', '57', '58', '59', '60', '61.1', '61.2', '61.3', '61.4', '61.5', '61.6','61.7',
 '62', '63.1', '63.2', '63.3', '63.4', '63.5', '63.6', '63.7', '64',
 '65.1', '65.2', '65.3', '65.4', '65.5', '66', '67.1', '67.2', '67.3', '67.4', '67.5', '67.6', '67.7',
 '67.8', '68', '69', '70', '71', '72', '73', '74', '75', '76' ,'77',
 '78', '79', '80', '81', '82', '83', '84', '85', '86', '87', '88', '89', '90','91', '92', '93', '94',
 '95', '96', '97', '98', '99', '100', '101', '102', '103', '104',
 '105',  '106', '107', '108', '109', '110', '111.1', '111.2', '111.3', '111.4', '111.5', '112', '113', '114',
 '115', '116', '117.1', '117.10', '117.2', '117.3', '117.4', '117.5','117.6', '117.7', '117.8', '117.9',
 '118', '119', '120', '121', '122', '123', '124', '125', '126', '127', '128', '129', '130', '131', '132', '133', '134', '135', '136',
 '137', '138', '139', '140', '141', '142', '143', '144', '145', '146', '147',
 '148', '149.1', '149.2','149.3', '149.4', '149.5', '149.6', '149.7',
 '150', '151', '152', '153', '154']
# Specify new column names for data analysis (ensure they match the exact order of the existing columns)

list_del_cols = []
# Specify the columns to be excluded from the data analysis

miss_col = ['s1', 's2', 's3']
# Specify all columns that apply to all respondents for missing value detection

open_cols = ['6', '8', '10', '16', '52', '55', '69', '85', '153', '154']
# Specify the open-ended columns (which will be saved in a separate Excel sheet and removed from the data frame)

age_col = None
# If we don't have age group in this dataset, please specify the age columns (as str)

diss_cols = ['24', '25', '26', '27', '28', '29']
# If we have WG-SS questions in the dataset, please specify the columns (as list [])


"""
Run the pipeline for data preprocessing
del_type = 0 or 1
-> 0: Remove all missing values from the columns where missing values are detected
-> 1: First, remove columns where missing values make up 10% or more of the total data points
      Then, remove all remaining missing values from the columns where they are detected
"""

carob = dp.Preprocessing(project_name, file_path, file_path_others, list_del_cols, dates, miss_col, respondent_name, identifiers, open_cols, cols_new, age_col, diss_cols, del_type = 0, file_type=file_type)
carob.processing()