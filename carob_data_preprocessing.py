#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 24 11:07:52 2024

@author: Bodhi Global Analysis (Jungyeon Lee)
"""

"""
Please download following Python Libraries:
1. Pandas
2. Numpy
3. uuid
4. openpyxl
"""

import pandas as pd
import numpy as np
import uuid
from openpyxl import load_workbook

class Preprocessing:
    
    def __init__(self, name, file_path, file_path_others, list_del_cols, dates, miss_col, anon_col, identifiers, opened_cols, cols_new, 
                 age_col = None, diss_cols = None, del_type = 0, file_type='xlsx'):
        """
        - Initialise the Performance Management Framework class

        name: str, Name of the project
        file_path: str, Directory of the raw dataset
        file_path_others: str, Directory of the opened-end questions' answers
        list_del_cols: list, Columns list for deleting
        dates: list, Dates on which the pilot test was conducted from the data
        miss_col: list, 
        anon_col: str, Column for anonymisation (Respondent Name)
        identifiers: list, Columns for checking duplicates 
        opened_cols: list, Opened-end question columns
        cols_new: list, New names for the columns (for data analysis purpose)
        age_col: str, Column of age infromation (for age-grouping purpose)
        diss_cols: list, Column of WG-SS questions in the dataset (for disability-grouping purpose)
        del_type: int, [0 or 1]
        -> 0: Remove all missing values from the columns where missing values are detected
        -> 1: First, remove columns where missing values make up 10% or more of the total data points
              Then, remove all remaining missing values from the columns where they are detected
        file_type: str, filetype of the raw dataset
        """
        self.name = name
        self.file_path = file_path
        self.file_path_others = file_path_others
        self.file_type = file_type
        self.list_del_cols = list_del_cols
        self.dates = dates
        self.miss_col = miss_col
        self.anon_col = anon_col
        self.identifiers = identifiers
        self.opened_cols = opened_cols
        self.cols_new = cols_new
        self.age_col = age_col
        self.diss_cols = diss_cols
        self.del_type = del_type
        self.df = None
    
    def data_load(self):
        """
        - To load a dataset
        """
        file_path = self.file_path
        file_type = self.file_type
        if file_type == 'xlsx' or file_type == 'xls':
            df = pd.read_excel(f"{file_path}.{file_type}")
            df.columns = df.columns.astype(str)
            self.df = df
            return True
        elif file_type == 'csv':
            df = pd.read_csv(f"{file_path}.{file_type}")
            df.columns = df.columns.astype(str)
            self.df = df
            return True
        else:
            print("Please use 'xlsx', 'xls' or 'csv' file")
            return False
        
    def delete_columns(self):
        """
        - To drop unnecessary columns
        """
        df = self.df
        list_cols = self.list_del_cols
        df = df.drop(columns = list_cols)
        print(f'Number of columns: {len(df.columns)} | After removing the columns that are not needed for the analysis')
        self.df = df
        return True

    def date_filter(self):
        """
        - To remove dates on which the pilot test was conducted from the dataset
        """
        df = self.df 
        dates = self.dates
        for date in dates:
            df = df[df['today'] != date]
        self.df = df
        return True
        
    def missing_value_clean(self):
        """
        - To detect and remove missing values
        """
        miss_col = self.miss_col
        df = self.df
        del_type = self.del_type
        initial_data_points = len(df)
        num_missing_cols = {}
        print("")
        for col in miss_col:
            missing_count = df[col].isnull().sum()
            num_missing_cols[col] = missing_count
            print(f'Column {col} has {missing_count} missing values')
    
        if del_type == 0: # Remove all missing values from the columns where missing values are detected
            df_cleaned = df.dropna(subset=miss_col)

        # First, remove columns where missing values make up 10% or more of the total data points
        # Then, remove all remaining missing values from the columns where they are detected
        elif del_type == 1:
            threshold = 0.1 * initial_data_points
            cols_to_drop = [col for col, missing_count in num_missing_cols.items() if missing_count > threshold]
            df_cleaned = df.drop(columns=cols_to_drop)
            print("")
            print(f'Number of columns: {len(df.columns)} | After removing the columns that contained missing values more than 10% of data points')
            print(f'Dropped columns = {cols_to_drop}')
            df_cleaned = df_cleaned.dropna(subset=miss_col)
        
        remaind_data_points = len(df_cleaned)
        print("")
        print(f'Number of deleted missing values: {initial_data_points - remaind_data_points}')
        print(f"Number of data points after missing value handling: {remaind_data_points}")
        print("")
        self.df = df_cleaned
        return True
    
    def save_data(self):
        """
        - To save the new dataframe
        """
        df = self.df
        file_path = self.file_path
        file_type = self.file_type
        if file_type == 'xlsx' or file_type == 'xls':
            df.reset_index(drop=True, inplace = True)
            df.to_excel(f"{file_path}.{file_type}", index=True)
            self.df = df
            print("The revised dataset has been saved")
            return True
        elif file_type == 'csv':
            df.reset_index(drop=True, inplace = True)
            df.to_csv(f"{file_path}.{file_type}", index=False)
            self.df = df
            print("The revised dataset has been saved")
            return True
        else: 
            print("Please use 'xlsx', 'xls' or 'csv' file")
            return False
        if file_type == 'xlsx':
            df.reset_index(drop=True, inplace = True)
            df.to_excel(f"{file_path}.{file_type}", index=True)
            self.df = df
            print("The revised dataset has been saved")
            return True
        elif file_type == 'csv':
            df.reset_index(drop=True, inplace = True)
            df.to_csv(f"{file_path}.{file_type}", index=False)
            self.df = df
            print("The revised dataset has been saved")
            return True
        else: 
            print("Please use 'xlsx' or 'csv' file")
            return False
        
    def data_anonymisation(self):
        """
        - To implement a dataframe anonymisation
        """
        df = self.df
        col = self.anon_col
        file_path = self.file_path
    
        def generate_unique_strings(prefix, series):
            unique_values = series.unique()
            key_mapping = {value: f"{prefix}{uuid.uuid4()}" for value in unique_values}
            return series.map(key_mapping), key_mapping
        
        df[col], respondent_mapping = generate_unique_strings('respondent_', df[col])
        original = self.file_path
        self.file_path = f'{file_path}_anonymised'
        self.save_data()
        self.file_path = original
        self.df = df
        print("The respondent name has been anonymised")
        return True
    
    def duplicates(self):
        """
        - To detect and remove duplicates
        """
        df = self.df
        col = self.identifiers
        duplicates = df[df.duplicated(subset=col, keep=False)]
        print("")
        print(f"Number of duplicate based on '{col}': {len(duplicates)}")

        if not duplicates.empty:
            print("Duplicate rows:")
            print(duplicates)
    
        df_cleaned = df.drop_duplicates(subset=col, keep='first')
    
        print(f"Number of data points: {len(df_cleaned)} | After removing duplicates")
        print("")
        self.df = df_cleaned
        return True

    def open_ended_cols(self):
        """
        - To save opened-ended columns and remove these from the dataset
        """
        df = self.df
        cols = self.opened_cols
        file_path = self.file_path_others
        empty_df = pd.DataFrame()
        with pd.ExcelWriter(file_path, engine='openpyxl') as writer:
            empty_df.to_excel(writer, sheet_name='basic', index=False)
        
            max_length = 0
            unique_data = {}

            for col in cols:
                unique_values = df[col].dropna().unique()
                unique_data[col] = unique_values
                max_length = max(max_length, len(unique_values))
        
            combined_df = pd.DataFrame({col: pd.Series(unique_data[col]) for col in cols})
            combined_df.to_excel(writer, sheet_name='open_ended', index=False)
        
        print(f"Open-ended columns have been saved to '{file_path}': {cols} ")
        df = df.drop(columns=cols)
        print(f'Number of columns: {len(df.columns)} | After removing the open-ended columns')
        self.df = df
        return True

    def columns_redefine(self):
        """
        - To change column names for smoother data analysis
        """
        df = self.df
        new_cols = self.cols_new
        df.columns = new_cols
        self.df = df
        return True

    def age_group(self):
        """
        - To create new age group variable
        """
        df = self.df
        col = self.age_col
        bins = [17, 24, 34, 44, 54, 64, float('inf')]
        labels = ['18 - 24','25 - 34', '35 - 44', '45 - 54', '55 - 64', 'Above 65 years']
        df[col] = df[col].astype(int)
        df['Age Group'] = pd.cut(df[col], bins=bins, labels=labels, right=True)
        print('New age group variable (Age Group) has been created in this dataset')
        self.df = df
        return True
    
    def disability_wgss(self):
        """
        - To create disability group (based on the WG-SS)
        """
        df = self.df
        cols = self.diss_cols
        try:
            df['WG-Disability'] = ''
            
            def wg_ss(row, cols):
                values = row[cols]
                some_difficulty_count = (values == 'Some difficulty').sum()
                a_lot_of_difficulty = (values == 'A lot of difficulty').any() or (values == 'Cannot do at all').any()
                cannot_do_at_all = (values == 'Cannot do at all').any()
                if cannot_do_at_all:
                    return 'DISABILITY4'
                elif a_lot_of_difficulty:
                    return 'DISABILITY3'
                elif some_difficulty_count >= 2:
                    return 'DISABILITY2'
                elif some_difficulty_count >= 1:
                    return 'DISABILITY1'
                else:
                    return 'No_disability'
            df['WG-Disability'] = df.apply(lambda row: wg_ss(row, cols), axis=1)
            df['Disability'] = df['WG-Disability'].apply(lambda x: 'Disability' if x in ['DISABILITY4', 'DISABILITY3'] else 'No Disability')
            print('New disability variable (Disability) has been created in this dataset (Based on WG-SS)')
            self.df = df
            return True
        except Exception as e:
               print('New disability variable has not been created in this dataset')
               
    def gbv_attitude(self):
        """
        - To create GBV Attitude Scale
        """
        df = self.df
        score_map = {'Strongly disagree':0,'Disagree':1,'Neither agree or disagree':2,'Agree':3,'Strongly agree':4}
        try:
            df['gbv_attitude_girl'] = ''
            df['gbv_attitude_boy'] = ''
            def scoring_girl(row):
                score = 0
                columns = ['87','88','89','90','91','92','93','94','95']
                for col in columns:
                    score += score_map.get(row[col], 0)
                return score
            
            def scoring_boy(row):
                score = 0
                columns = ['96','97','98','99','100','101','102','103','104']
                for col in columns:
                    score += score_map.get(row[col], 0)
                return score
            
            df['score_gbv_g'] = df.apply(scoring_girl, axis=1)
            df['gbv_attitude_girl'] = df['score_gbv_g'].apply(lambda x: 'Not Negative Attitude' if x > 20 else 'Negative Attitude')
            df['score_gbv_b'] = df.apply(scoring_boy, axis=1)
            df['gbv_attitude_boy'] = df['score_gbv_b'].apply(lambda x: 'Not Negative Attitude' if x > 20 else 'Negative Attitude')
            print('New GBV Attitude variable has been created in this dataset')
            self.df = df
            return True
        except Exception as e:
               print('New GBV Attitude variable has not been created in this dataset')
               
    def gbv_personal_beliefs(self):
        """
        - To create Social Norm and Beliefs about GBV Scale
        """
        df = self.df
        score_map = {'Agree':1,"Unsure":2,'Disagree but not ready to tell others':3,'Disagree and ready to tell others':4}
        try:
            df['b_response_sex_violence'] = 0
            df['b_husband_right_violence'] = 0
            df['b_protect_family_honour'] = 0
            
            def categorise_response(value):
                if 1 <= value < 2:
                    return 'Negative response'
                elif 2 <= value < 3:
                    return 'Moderate response'
                elif 3 <= value <= 4:
                    return 'Positive response'
                else:
                    return 'Invalid'
            
            def scoring_sv(row):
                score = 0
                count = 0
                columns = ['118','119','120','121','122','123']
                
                for col in columns:
                    if pd.notna(row[col]):
                        score += score_map.get(row[col], 0)
                        count += 1
                
                if count > 0:
                    return score / count
            
            def scoring_hr(row):
                score = 0
                count = 0
                columns = ['124','125','126','127']
                
                for col in columns:
                    if pd.notna(row[col]):
                        score += score_map.get(row[col], 0)
                        count += 1
                
                if count > 0:
                    return score / count
            
            def scoring_pf(row):
                score = 0
                count = 0
                columns = ['128','129','130','131','132']
                
                for col in columns:
                    # Check if the value exists in score_map and is not missing
                    if pd.notna(row[col]):  # Skip NaN values
                        score += score_map.get(row[col], 0)  # Add score based on score_map
                        count += 1  # Increment count of valid values
                
                # If there are any valid values, calculate the average, otherwise return 0
                if count > 0:
                    return score / count
            
            df['b_response_sex_violence'] = df.apply(scoring_sv, axis=1)
            df['b_husband_right_violence'] = df.apply(scoring_hr, axis=1)
            df['b_protect_family_honour'] = df.apply(scoring_pf, axis=1)
            df['group_b_sex_violence'] = df['b_response_sex_violence'].apply(categorise_response)
            df['group_b_husband_violence'] = df['b_husband_right_violence'].apply(categorise_response)
            df['group_b_protect_honour'] = df['b_protect_family_honour'].apply(categorise_response)
            print('New GBV Personal Beliefs variable has been created in this dataset')
            self.df = df
            return True
        except Exception as e:
               print('New GBV Attitude variable has not been created in this dataset')
               
    def gbv_social_norm(self):
        """
        - To create Social Norm and Beliefs about GBV Scale
        """
        df = self.df
        score_map = {'None of them':1,"A few of them":2,'About half of them':3,'Most of them':4, 'All of them':5}
        try:
            df['s_response_sex_violence'] = 0
            df['s_husband_right_violence'] = 0
            df['s_protect_family_honour'] = 0
            
            def categorise_response(value):
                if 1 <= value < 2.5:
                    return 'Positive response'
                elif 2.5 <= value < 3.5:
                    return 'Moderate response'
                elif 3.5 <= value <= 5:
                    return 'Negative response'
                else:
                    return 'Invalid'
            
            def scoring_sv(row):
                score = 0
                count = 0
                columns = ['133','134','135','136','137']
                
                for col in columns:
                    if pd.notna(row[col]):
                        score += score_map.get(row[col], 0)
                        count += 1
                
                if count > 0:
                    return score / count
            
            def scoring_hr(row):
                score = 0
                count = 0
                columns = ['138','139','140','141','142','143']
                
                for col in columns:
                    if pd.notna(row[col]):
                        score += score_map.get(row[col], 0)
                        count += 1
                
                if count > 0:
                    return score / count
            
            def scoring_pf(row):
                score = 0
                count = 0
                columns = ['144','145','146','147']
                
                for col in columns:
                    # Check if the value exists in score_map and is not missing
                    if pd.notna(row[col]):  # Skip NaN values
                        score += score_map.get(row[col], 0)  # Add score based on score_map
                        count += 1  # Increment count of valid values
                
                # If there are any valid values, calculate the average, otherwise return 0
                if count > 0:
                    return score / count
            
            df['s_response_sex_violence'] = df.apply(scoring_sv, axis=1)
            df['s_husband_right_violence'] = df.apply(scoring_hr, axis=1)
            df['s_protect_family_honour'] = df.apply(scoring_pf, axis=1)
            df['group_s_sex_violence'] = df['s_response_sex_violence'].apply(categorise_response)
            df['group_s_husband_violence'] = df['s_husband_right_violence'].apply(categorise_response)
            df['group_s_protect_honour'] = df['s_protect_family_honour'].apply(categorise_response)
            print('New GBV Personal Beliefs variable has been created in this dataset')
            self.df = df
            return True
        except Exception as e:
               print('New GBV Attitude variable has not been created in this dataset')

    def processing(self):
        """
        - To conduct data pre-processing
        1. Load the raw dataset
        2. Re-define variable names
        3. Handle duplicates
        4. Anonymise data (Respondents' names)
        5. Remove pilot test data points
        6. Drop unnecessary columns
        7. Handle missing values
        8. Extract answers from open-ended questions
        9. Create age and disability groups
        10. Save the cleaned dataset
        """
        self.data_load()
        self.columns_redefine()
        print(f'Initial data points: {len(self.df)}')
        self.duplicates()
        print(f'Initial number of columns: {len(self.df.columns)}')
        self.delete_columns()
        self.missing_value_clean()
        self.open_ended_cols()
        if self.age_col != None:
            self.age_group()
        if self.diss_cols != None:
            self.disability_wgss()
        self.gbv_attitude()
        self.gbv_social_norm()
        self.gbv_personal_beliefs()
        original = self.file_path
        self.file_path = f'{self.file_path}_cleaned'
        self.save_data()
        self.file_path = original
        print("")
        print(f'Final number of data points: {len(self.df)}')
        print(f"Cleaned dataframe has been saved: {self.file_path}_cleaned.{self.file_type}")
        return True