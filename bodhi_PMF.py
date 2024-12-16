#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 17 15:47:28 2024

@author: Bodhi Global Analysis (Jungyeon Lee)
"""
import pandas as pd
import bodhi_data_analysis as bodhi

class PerformanceManagementFramework:
    
    def __init__(self, name, ptype):
        """
        - Initialise the Performance Management Framework class

        name: str, Name of the project
        ptype: str, Type of the project (KAP, Evaluation)
        """
        self.name = name
        self.ptype = ptype
        self.indicators = []

    def add_indicators(self, indicators):
        """
        - Add the project indicators to the PMF

        indicators: list, List of all the indicators
        """
        for indicator in indicators:
            self.indicators.append(indicator)
            print(f'{indicator.indicator_name} has been added to the data analysis pipeline')
            
        self.tool = bodhi.Data_analysis(self.name, self.indicators)
        self.tool.indicator_analysis()
        return True
 
    def PMF_generation(self, file_path1, file_path2, folder):
        """
        - Generate tables from all the indicators
        file_path1: str, a location where the tables will be saved
        file_path2: str, a location where the chi2 test results will be saved
        """
        empty_df1 = pd.DataFrame()
        with pd.ExcelWriter(file_path1, engine='openpyxl') as writer:
            empty_df1.to_excel(writer, sheet_name='Tables', index=False)
            
        empty_df2 = pd.DataFrame()
        with pd.ExcelWriter(file_path2, engine='openpyxl') as writer:
            empty_df2.to_excel(writer, sheet_name='Chi2 Tests', index=False)
            
        if self.ptype == 'Evaluation':
            self.tool.tables(file_path1, folder)
            self.tool.chi2_test(file_path2)
        elif self.ptype == 'KAP':
            self.tool.chi2_test(file_path2)
            self.tool.kap(file_path1, folder)
        
        print("\nData analysis has been finished")