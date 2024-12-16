#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 17 15:52:03 2024

@author: ijeong-yeon
"""

import bodhi_indicator as bd
import bodhi_PMF as pmf
import pandas as pd

# Please assign the file path of the cleaned dataset
df = pd.read_excel('data/24-UNFPA-SS-1 - Data_cleaned.xlsx')

# Creating indicators and social demographics for data analysis
age = bd.Indicator(df, "Age Group", None, ['s1'], i_cal=None, i_type='count', description='Which age group do you belong to?', period='KAP', target = None)
age.add_breakdown({'s2':'Region', 's3':'Gender', 'Disability':'Disability'})
age.add_var_order(['18-24', "25-34", '35-44','45-54', '55-64',"65 and over"])
age.add_kap_label(['18-24', "25-34", '35-44','45-54', '55-64',"65 and over"])

region = bd.Indicator(df, "Region", None, ['s2'], i_cal=None, i_type='count', description='Where is your region of residence?', period='KAP', target = None)
region.add_breakdown({'s1':'Age Group', 's3':'Gender', 'Disability':'Disability'})
region.add_var_order(['Upper Nile', "Jonglei", 'Unity States',"GPAA", 'RAA'])
region.add_kap_label(['Upper Nile', "Jonglei", 'Unity States',"GPAA", 'RAA'])

gender = bd.Indicator(df, "Gender", None, ['s3'], i_cal=None, i_type='count', description='What is your sex/gender?', period='KAP', target = None)
gender.add_breakdown({'s2':'Region', 's1':'Age Group', 'Disability':'Disability'})
gender.add_var_order(['Male', "Female", 'Non-binary',"Other","Prefer not to say"])
gender.add_kap_label(['Male', "Female", 'Non-binary',"Other","Prefer not to say"])

occupation = bd.Indicator(df, "Occupation", None, ['17'], i_cal=None, i_type='count', description='What is your current occupation?', period='KAP', target = None)
occupation.add_breakdown({'s2':'Region', 's1':'Age Group', 's3':'Gender', 'Disability':'Disability'})
occupation.add_var_order(['Student', "Employed", 'Self-employed',"Pastoralist","Housewife/househusband", "Unemployed", "Prefer not to say", "Other"])
occupation.add_kap_label(['Student', "Employed", 'Self-employed',"Pastoralist","Housewife/househusband", "Unemployed", "Prefer not to say", "Other"])

si = bd.Indicator(df, "Source of Information", None, ['19'], i_cal=None, i_type='count', description='How do you get your information and news?', period='KAP', target = None)
si.add_breakdown({'s2':'Region', 's1':'Age Group', 's3':'Gender', 'Disability':'Disability'})
si.add_var_order(['Social Media', "Radio", 'Word of mouth',"The church or mosque","CSOs and NGOs", "Elders or other community based organisations", "Smoke symbols", "Other"])
si.add_kap_label(['Social Media', "Radio", 'Word of mouth',"The church or mosque","CSOs and NGOs", "Elders or other community based organisations", "Smoke symbols", "Other"])

maternity = bd.Indicator(df, "Maternity", None, ['21'], i_cal=None, i_type='count', description='What is your relationship status?', period='KAP', target = None)
maternity.add_breakdown({'s2':'Region', 's1':'Age Group', 's3':'Gender', 'Disability':'Disability'})
maternity.add_var_order(['Currently married', "Polygamous marriage", 'Living with partner',"Single","Divorced", "Widowed", "Prefer not to say", "Other"])
maternity.add_kap_label(['Currently married', "Polygamous marriage", 'Living with partner',"Single","Divorced", "Widowed", "Prefer not to say", "Other"])

disability = bd.Indicator(df, "Disability", None, ['Disability'], i_cal=None, i_type='count', description='Disability Status (WG-SS)', period='KAP', target = None)
disability.add_breakdown({'s2':'Region', 's1':'Age Group', 's3':'Gender'})
disability.add_var_order(['No Disability', "Disability"])
disability.add_kap_label(['No Disability', "Disability"])

gbv_attitude_g = bd.Indicator(df, "gbv_attitude_girl", None, ['gbv_attitude_girl'], i_cal=None, i_type='count', description='Attitude Toward GBV Scale', period='KAP', target = None)
gbv_attitude_g.add_breakdown({'s2':'Region', 's1':'Age Group', 's3':'Gender', 'Disability':'Disability', 'group_b_sex_violence':"Beliefs_SV", "group_b_husband_violence":"Beliefs_HV", "group_b_protect_honour":"Beliefs_PH", 
                              'group_s_sex_violence':"Norms_SV", "group_s_husband_violence":"Norms_HV", "group_s_protect_honour":"Norms_PH", "32":"Perceived Knowledge"})
gbv_attitude_g.add_var_order(['Negative Attitude', "Not Negative Attitude"])
gbv_attitude_g.add_kap_label(['Negative Attitude', "Not Negative Attitude"])

gbv_attitude_gs = bd.Indicator(df, "gbv_attitude_girl_score", None, 'score_gbv_g', i_cal=None, i_type='count', description='GBV Attitude Toward Girls (Score)', period='KAP', target = None, chi = True)
gbv_attitude_gs.add_breakdown({'s2':'Region', 's1':'Age Group', 's3':'Gender', 'Disability':'Disability', 'group_b_sex_violence':"Beliefs_SV", "group_b_husband_violence":"Beliefs_HV", "group_b_protect_honour":"Beliefs_PH", 
                              'group_s_sex_violence':"Norms_SV", "group_s_husband_violence":"Norms_HV", "group_s_protect_honour":"Norms_PH", "32":"Perceived Knowledge"})

gbv_attitude_b = bd.Indicator(df, "gbv_attitude_boy", None, ['gbv_attitude_boy'], i_cal=None, i_type='count', description='GBV Attitude Toward Boys', period='KAP', target = None)
gbv_attitude_b.add_breakdown({'s2':'Region', 's1':'Age Group', 's3':'Gender', 'Disability':'Disability', 'group_b_sex_violence':"Beliefs_SV", "group_b_husband_violence":"Beliefs_HV", "group_b_protect_honour":"Beliefs_PH", 
                              'group_s_sex_violence':"Norms_SV", "group_s_husband_violence":"Norms_HV", "group_s_protect_honour":"Norms_PH", "32":"Perceived Knowledge"})
gbv_attitude_b.add_var_order(['Negative Attitude', "Not Negative Attitude"])
gbv_attitude_b.add_kap_label(['Negative Attitude', "Not Negative Attitude"])

gbv_b_1 = bd.Indicator(df, "Beliefs_SV", None, ['group_b_sex_violence'], i_cal=None, i_type='count', description='GBV Beliefs: Sexual Violence', period='KAP', target = None)
gbv_b_1.add_breakdown({'s2':'Region', 's1':'Age Group', 's3':'Gender', 'Disability':'Disability', 'gbv_attitude_girl':'GBV Attitude (Girls)', 'gbv_attitude_boy':'GBV Attitude (Boys)'})
gbv_b_1.add_var_order(['Negative response', "Moderate response","Positive response"])
gbv_b_1.add_kap_label(['Negative response', "Moderate response","Positive response"])

gbv_b_2 = bd.Indicator(df, "Beliefs_HV", None, ['group_b_husband_violence'], i_cal=None, i_type='count', description="GBV Beliefs: Husband's Right to Use Violence", period='KAP', target = None)
gbv_b_2.add_breakdown({'s2':'Region', 's1':'Age Group', 's3':'Gender', 'Disability':'Disability', 'gbv_attitude_girl':'GBV Attitude (Girls)', 'gbv_attitude_boy':'GBV Attitude (Boys)'})
gbv_b_2.add_var_order(['Negative response', "Moderate response","Positive response"])
gbv_b_2.add_kap_label(['Negative response', "Moderate response","Positive response"])

gbv_b_3 = bd.Indicator(df, "Beliefs_PH", None, ['group_b_protect_honour'], i_cal=None, i_type='count', description='GBV Beliefs: Protect Family Honour', period='KAP', target = None)
gbv_b_3.add_breakdown({'s2':'Region', 's1':'Age Group', 's3':'Gender', 'Disability':'Disability', 'gbv_attitude_girl':'GBV Attitude (Girls)', 'gbv_attitude_boy':'GBV Attitude (Boys)'})
gbv_b_3.add_var_order(['Negative response', "Moderate response","Positive response"])
gbv_b_3.add_kap_label(['Negative response', "Moderate response","Positive response"])

gbv_s_1 = bd.Indicator(df, "Norms_SV", None, ['group_s_sex_violence'], i_cal=None, i_type='count', description='GBV Social Norms: Sexual Violence', period='KAP', target = None)
gbv_s_1.add_breakdown({'s2':'Region', 's1':'Age Group', 's3':'Gender', 'Disability':'Disability', 'gbv_attitude_girl':'GBV Attitude (Girls)', 'gbv_attitude_boy':'GBV Attitude (Boys)'})
gbv_s_1.add_var_order(['Negative response', "Moderate response","Positive response"])
gbv_s_1.add_kap_label(['Negative response', "Moderate response","Positive response"])

gbv_s_2 = bd.Indicator(df, "Norms_HV", None, ['group_s_husband_violence'], i_cal=None, i_type='count', description="GBV Social Norms: Husband's Right to Use Violence", period='KAP', target = None)
gbv_s_2.add_breakdown({'s2':'Region', 's1':'Age Group', 's3':'Gender', 'Disability':'Disability', 'gbv_attitude_girl':'GBV Attitude (Girls)', 'gbv_attitude_boy':'GBV Attitude (Boys)'})
gbv_s_2.add_var_order(['Negative response', "Moderate response","Positive response"])
gbv_s_2.add_kap_label(['Negative response', "Moderate response","Positive response"])

gbv_s_3 = bd.Indicator(df, "Norms_PH", None, ['group_s_protect_honour'], i_cal=None, i_type='count', description='GBV Social Norms: Protect Family Honour', period='KAP', target = None)
gbv_s_3.add_breakdown({'s2':'Region', 's1':'Age Group', 's3':'Gender', 'Disability':'Disability', 'gbv_attitude_girl':'GBV Attitude (Girls)', 'gbv_attitude_boy':'GBV Attitude (Boys)'})
gbv_s_3.add_var_order(['Negative response', "Moderate response","Positive response"])
gbv_s_3.add_kap_label(['Negative response', "Moderate response","Positive response"])

know_gbv = bd.Indicator(df, "Know GBV", None, ['30'], i_cal=None, i_type='count', description='Do you know what Gender-Based Violence (GBV) is?', period='KAP', target = None)
know_gbv.add_breakdown({'s2':'Region', 's1':'Age Group', 's3':'Gender', 'Disability':'Disability'})
know_gbv.add_var_order(['Yes', "No"])
know_gbv.add_kap_label(['Yes', "No"])

knowledge_gbv = bd.Indicator(df, "Knowledge GBV", None, ['32'], i_cal=None, i_type='count', description='How much knowledge do you think you have about GBV?', period='KAP', target = None)
knowledge_gbv.add_breakdown({'s2':'Region', 's1':'Age Group', 's3':'Gender', 'Disability':'Disability','gbv_attitude_girl':'GBV Attitude (Girls)', 'gbv_attitude_boy':'GBV Attitude (Boys)'})
knowledge_gbv.add_var_order(['Very limited', "Limited", "Moderate", "Good", "Very good"])
knowledge_gbv.add_kap_label(['Very limited', "Limited", "Moderate", "Good", "Very good"])

type_gbv = bd.Indicator(df, "Type GBV", None, ['33.1','33.2', '33.3', '33.4', '33.5', '33.6', '33.7', '33.8', '33.9'], i_cal=None, i_type='count', description='What type of GBV do you know about?', period='KAP', target = None)
type_gbv.add_breakdown({'s2':'Region', 's1':'Age Group', 's3':'Gender', 'Disability':'Disability'})
type_gbv.add_var_change({1: "Yes", 0: "No"})
type_gbv.add_var_order([1, 0])
type_gbv.add_kap_label(['Rape', "Sexual assault", "Physical assault",'Child, Early, Forced Marriage and Unions',"Denial of resources, opportunities, or services",
                        "Psychological/emotional abuse", "Female Genital Mutilation", "Technology-related GBV", "None"])

type_knowledge_gbv_1 = bd.Indicator(df, "Knowledge Rape", None, ['34.1'], i_cal=None, i_type='count', description='How much knowledge do you think you have about this GBV?: Rape', period='KAP', target = None)
type_knowledge_gbv_1.add_breakdown({'s2':'Region', 's1':'Age Group', 's3':'Gender', 'Disability':'Disability'})
type_knowledge_gbv_1.add_var_order(['Very limited', "Limited", "Moderate", "Good", "Very good"])
type_knowledge_gbv_1.add_kap_label(['Very limited', "Limited", "Moderate", "Good", "Very good"])

type_knowledge_gbv_2 = bd.Indicator(df, "Knowledge Sexual assault", None, ['34.2'], i_cal=None, i_type='count', description='How much knowledge do you think you have about this GBV?: Sexual assault', period='KAP', target = None)
type_knowledge_gbv_2.add_breakdown({'s2':'Region', 's1':'Age Group', 's3':'Gender', 'Disability':'Disability'})
type_knowledge_gbv_2.add_var_order(['Very limited', "Limited", "Moderate", "Good", "Very good"])
type_knowledge_gbv_2.add_kap_label(['Very limited', "Limited", "Moderate", "Good", "Very good"])

type_knowledge_gbv_3 = bd.Indicator(df, "Knowledge Physical assault", None, ['34.3'], i_cal=None, i_type='count', description='How much knowledge do you think you have about this GBV?: Physical assault', period='KAP', target = None)
type_knowledge_gbv_3.add_breakdown({'s2':'Region', 's1':'Age Group', 's3':'Gender', 'Disability':'Disability'})
type_knowledge_gbv_3.add_var_order(['Very limited', "Limited", "Moderate", "Good", "Very good"])
type_knowledge_gbv_3.add_kap_label(['Very limited', "Limited", "Moderate", "Good", "Very good"])

type_knowledge_gbv_4 = bd.Indicator(df, "Knowledge Early marriage", None, ['34.4'], i_cal=None, i_type='count', description='How much knowledge do you think you have about this GBV?: Child, Early, Forced Marriage and Unions', period='KAP', target = None)
type_knowledge_gbv_4.add_breakdown({'s2':'Region', 's1':'Age Group', 's3':'Gender', 'Disability':'Disability'})
type_knowledge_gbv_4.add_var_order(['Very limited', "Limited", "Moderate", "Good", "Very good"])
type_knowledge_gbv_4.add_kap_label(['Very limited', "Limited", "Moderate", "Good", "Very good"])

type_knowledge_gbv_5 = bd.Indicator(df, "Knowledge Denial resources", None, ['34.5'], i_cal=None, i_type='count', description='How much knowledge do you think you have about this GBV?: Denial of resources, opportunities, or services', period='KAP', target = None)
type_knowledge_gbv_5.add_breakdown({'s2':'Region', 's1':'Age Group', 's3':'Gender', 'Disability':'Disability'})
type_knowledge_gbv_5.add_var_order(['Very limited', "Limited", "Moderate", "Good", "Very good"])
type_knowledge_gbv_5.add_kap_label(['Very limited', "Limited", "Moderate", "Good", "Very good"])

type_knowledge_gbv_6 = bd.Indicator(df, "Knowledge Emotional abuse", None, ['34.6'], i_cal=None, i_type='count', description='How much knowledge do you think you have about this GBV?: Psychological/emotional abuse', period='KAP', target = None)
type_knowledge_gbv_6.add_breakdown({'s2':'Region', 's1':'Age Group', 's3':'Gender', 'Disability':'Disability'})
type_knowledge_gbv_6.add_var_order(['Very limited', "Limited", "Moderate", "Good", "Very good"])
type_knowledge_gbv_6.add_kap_label(['Very limited', "Limited", "Moderate", "Good", "Very good"])

type_knowledge_gbv_7 = bd.Indicator(df, "Knowledge Female GM", None, ['34.7'], i_cal=None, i_type='count', description='How much knowledge do you think you have about this GBV?: Female Genital Mutilation', period='KAP', target = None)
type_knowledge_gbv_7.add_breakdown({'s2':'Region', 's1':'Age Group', 's3':'Gender', 'Disability':'Disability'})
type_knowledge_gbv_7.add_var_order(['Very limited', "Limited", "Moderate", "Good", "Very good"])
type_knowledge_gbv_7.add_kap_label(['Very limited', "Limited", "Moderate", "Good", "Very good"])

type_knowledge_gbv_8 = bd.Indicator(df, "Knowledge Technology GBV", None, ['34.8'], i_cal=None, i_type='count', description='How much knowledge do you think you have about this GBV?: Technology-related GBV', period='KAP', target = None)
type_knowledge_gbv_8.add_breakdown({'s2':'Region', 's1':'Age Group', 's3':'Gender', 'Disability':'Disability'})
type_knowledge_gbv_8.add_var_order(['Very limited', "Limited", "Moderate", "Good", "Very good"])
type_knowledge_gbv_8.add_kap_label(['Very limited', "Limited", "Moderate", "Good", "Very good"])

main_source = bd.Indicator(df, "GBV main source", None, ['35.1','35.2','35.3','35.4','35.5','35.6','35.7'], i_cal=None, i_type='count', description='What are your main sources of information about GBV?', period='KAP', target = None)
main_source.add_breakdown({'s2':'Region', 's1':'Age Group', 's3':'Gender', 'Disability':'Disability'})
main_source.add_var_change({1: "Yes", 0: "No"})
main_source.add_var_order([1, 0])
main_source.add_kap_label(['News and Articles', "Social Media", "Book", "Academic papers", "Television and films", "Educational videos", "Other"])

av_gbv_service = bd.Indicator(df, "Aware of GBV Service", None, ['36'], i_cal=None, i_type='count', description='Do you know any available GBV Services in your community?', period='KAP', target = None)
av_gbv_service.add_breakdown({'s2':'Region', 's1':'Age Group', 's3':'Gender', 'Disability':'Disability'})
av_gbv_service.add_var_order(['Yes', "No"])
av_gbv_service.add_kap_label(['Yes', "No"])

list_gbv_service = bd.Indicator(df, "List of GBV Service", None, ['37.1','37.2', '37.3', '37.4', '37.5', '37.6',
                                                                            '37.7','37.8','37.9','37.10','37.11'], i_cal=None, i_type='count', description='Please describe the GBV services you know about', period='KAP', target = None)
list_gbv_service.add_breakdown({'s2':'Region', 's1':'Age Group', 's3':'Gender', 'Disability':'Disability'})
list_gbv_service.add_var_change({1: "Yes", 0: "No"})
list_gbv_service.add_var_order([1, 0])
list_gbv_service.add_kap_label(['GBV case management', "Medical care services", 'Mental health services',"Psychosocial support","Legal assistance services", "Safe shelter", "Safe spaces", "Security/police",
                        "Livelihood/economic empowerment support", "Emergency basic need support", "Other"])

know_report_gbv = bd.Indicator(df, "Know reporting GBV Cases", None, ['38'], i_cal=None, i_type='count', description='Do you know who to report cases of GBV to?', period='KAP', target = None)
know_report_gbv.add_breakdown({'s2':'Region', 's1':'Age Group', 's3':'Gender', 'Disability':'Disability'})
know_report_gbv.add_var_order(["Yes", "No"])
know_report_gbv.add_kap_label(["Yes", "No"])

subject_report_gbv = bd.Indicator(df, "Subject reporting GBV Cases", None, ['39'], i_cal=None, i_type='count', description='Who would you report cases of GBV to?', period='KAP', target = None)
subject_report_gbv.add_breakdown({'s2':'Region', 's1':'Age Group', 's3':'Gender', 'Disability':'Disability'})
subject_report_gbv.add_var_order(["Health facility", "Police", "Psychosocial support", "NGOs/International NGOs", "Religious leaders", "Community group", "Prefer not to say", "Other"])
subject_report_gbv.add_kap_label(["Health facility", "Police", "Psychosocial support", "NGOs/International NGOs", "Religious leaders", "Community group", "Prefer not to say", "Other"])

ex_report_gbv = bd.Indicator(df, "Experience reporting GBV Cases", None, ['40'], i_cal=None, i_type='count', description='Have you ever reported any GBV incident before?', period='KAP', target = None)
ex_report_gbv.add_breakdown({'s2':'Region', 's1':'Age Group', 's3':'Gender', 'Disability':'Disability'})
ex_report_gbv.add_var_order(["Yes", "No"])
ex_report_gbv.add_kap_label(["Yes", "No"])

report_time = bd.Indicator(df, "Timing reporting the GBV Case", None, ['41'], i_cal=None, i_type='count', description='When did you report the GBV incident?', period='KAP', target = None)
report_time.add_breakdown({'s2':'Region', 's1':'Age Group', 's3':'Gender', 'Disability':'Disability'})
report_time.add_var_order(["Immediately", "After some days", "After some weeks", "After some months"])
report_time.add_kap_label(["Immediately", "After some days", "After some weeks", "After some months"])

report_type = bd.Indicator(df, "Reporting - GBV type", None, ['42'], i_cal=None, i_type='count', description='What was the type of GBV you reported?', period='KAP', target = None)
report_type.add_breakdown({'s2':'Region', 's1':'Age Group', 's3':'Gender', 'Disability':'Disability'})
report_type.add_var_order(['Rape', "Sexual assault", "Physical assault",'CEFMU',"Denial of resources",
                        "Psychological emotional abuse", "Female Genital Mutilation", "Technology-related GBV", "Prefer not to say", "Other"])
report_type.add_kap_label(['Rape', "Sexual assault", "Physical assault",'CEFMU',"Denial of resources",
                        "Psychological emotional abuse", "Female Genital Mutilation", "Technology-related GBV", "Prefer not to say", "Other"])

report_location = bd.Indicator(df, "Reporting - GBV location", None, ['43'], i_cal=None, i_type='count', description='Where did the GBV incident occur?', period='KAP', target = None)
report_location.add_breakdown({'s2':'Region', 's1':'Age Group', 's3':'Gender', 'Disability':'Disability'})
report_location.add_var_order(["Home", "Home of friend/neighbour","At a market","Public space","School","Workplace","Prefer not to say", "Other"])
report_location.add_kap_label(["Home", "Home of friend/neighbour","At a market","Public space","School","Workplace","Prefer not to say", "Other"])

report_responsible = bd.Indicator(df, "Reporting - GBV perpetrator", None, ['44'], i_cal=None, i_type='count', description='Who was responsible for the incident?', period='KAP', target = None)
report_responsible.add_breakdown({'s2':'Region', 's1':'Age Group', 's3':'Gender', 'Disability':'Disability'})
report_responsible.add_var_order(["Husband","Partner","Boyfriends (including ex-boyfriends)","Teachers","Community member","Other family member","Prefer not to say", "Other"])
report_responsible.add_kap_label(["Husband","Partner","Boyfriends","Teachers","Community member","Other family member","Prefer not to say", "Other"])

report_level = bd.Indicator(df, "Difficulty level of reporting", None, ['45'], i_cal=None, i_type='count', description='Did you find the reporting difficult?', period='KAP', target = None)
report_level.add_breakdown({'s2':'Region', 's1':'Age Group', 's3':'Gender', 'Disability':'Disability'})
report_level.add_var_order(["Yes", "No"])
report_level.add_kap_label(["Yes", "No"])

report_level_reason = bd.Indicator(df, "Reason of Difficulty level", None, ['46'], i_cal=None, i_type='count', description='Can you share why you found it difficult to report the GBV incident?', period='KAP', target = None)
report_level_reason.add_breakdown({'s2':'Region', 's1':'Age Group', 's3':'Gender', 'Disability':'Disability'})
report_level_reason.add_var_order(["Stigma from partner", "Stigma from community", "Did not trust anyone", "Thought nothing could be done", "Afraid of further violence",
                                   "Nobody would believe me" , "Thought I would be blamed", "Did not know where to go", "Other"])
report_level_reason.add_kap_label(["Stigma from partner", "Stigma from community", "Did not trust anyone", "Thought nothing could be done", "Afraid of further violence",
                                   "Nobody would believe me" , "Thought I would be blamed", "Did not know where to go", "Other"])

knowledge_gp = bd.Indicator(df, "Knowledge - Government Policies", None, ['47'], i_cal=None, i_type='count', description='How well do you understand government policies about GBV?', period='KAP', target = None)
knowledge_gp.add_breakdown({'s2':'Region', 's1':'Age Group', 's3':'Gender', 'Disability':'Disability'})
knowledge_gp.add_var_order(['Very limited', "Limited", "Moderate", "Good", "Very good"])
knowledge_gp.add_kap_label(['Very limited', "Limited", "Moderate", "Good", "Very good"])

knowledge_gp_can = bd.Indicator(df, "Able to name the policies", None, ['48'], i_cal=None, i_type='count', description='Can you name the government policies about GBV?', period='KAP', target = None)
knowledge_gp_can.add_breakdown({'s2':'Region', 's1':'Age Group', 's3':'Gender', 'Disability':'Disability'})
knowledge_gp_can.add_var_order(["Yes", "No"])
knowledge_gp_can.add_kap_label(["Yes", "No"])

knowledge_laws = bd.Indicator(df, "Knowledge - Laws", None, ['50'], i_cal=None, i_type='count', description='How well do you understand laws related to GBV?', period='KAP', target = None)
knowledge_laws.add_breakdown({'s2':'Region', 's1':'Age Group', 's3':'Gender', 'Disability':'Disability'})
knowledge_laws.add_var_order(['Very limited', "Limited", "Moderate", "Good", "Very good"])
knowledge_laws.add_kap_label(['Very limited', "Limited", "Moderate", "Good", "Very good"])

knowledge_laws_can = bd.Indicator(df, "Able to name the laws", None, ['51'], i_cal=None, i_type='count', description='Can you name the laws about GBV?', period='KAP', target = None)
knowledge_laws_can.add_breakdown({'s2':'Region', 's1':'Age Group', 's3':'Gender', 'Disability':'Disability'})
knowledge_laws_can.add_var_order(["Yes", "No"])
knowledge_laws_can.add_kap_label(["Yes", "No"])

knowledge_s_methods = bd.Indicator(df, "Aware of social methods", None, ['53'], i_cal=None, i_type='count', description='Are you aware of any social, religious or traditional methods or guidelines used in addressing GBV?', period='KAP', target = None)
knowledge_s_methods.add_breakdown({'s2':'Region', 's1':'Age Group', 's3':'Gender', 'Disability':'Disability'})
knowledge_s_methods.add_var_order(["Yes", "No"])
knowledge_s_methods.add_kap_label(["Yes", "No"])

s_methods = bd.Indicator(df, "Social Methods", None, ['54.1','54.2', '54.3', '54.4', '54.5'], i_cal=None, i_type='count', description='Which are these methods?', period='KAP', target = None)
s_methods.add_breakdown({'s2':'Region', 's1':'Age Group', 's3':'Gender', 'Disability':'Disability'})
s_methods.add_var_change({1: "Yes", 0: "No"})
s_methods.add_var_order([1, 0])
s_methods.add_kap_label(['Sharia law', "Traditional courts", 'Mediation by village elders',"Discussions between aggrieved families", "Other"])

support_need_gbv = bd.Indicator(df, "Support needs", None, ['56'], i_cal=None, i_type='count', description='What support do you believe should be provided to GBV survivors?', period='KAP', target = None)
support_need_gbv.add_breakdown({'s2':'Region', 's1':'Age Group', 's3':'Gender', 'Disability':'Disability'})
support_need_gbv.add_var_order(["Counselling and therapy", "Safe shelters and housing assistance", "Legal assistance", "Medical", "Community support groups", "Other"])
support_need_gbv.add_kap_label(["Counselling and therapy", "Safe shelters and housing assistance", "Legal assistance", "Medical", "Community support groups", "Other"])

barriers_survivors = bd.Indicator(df, "Barriers", None, ['57'], i_cal=None, i_type='count', description='What barriers do you anticipate in aiding GBV survivors?', period='KAP', target = None)
barriers_survivors.add_breakdown({'s2':'Region', 's1':'Age Group', 's3':'Gender', 'Disability':'Disability'})
barriers_survivors.add_var_order(["Fear of retaliation from the perpetrator", "Stigma", "Lack of awareness about available support services", "Cultural or societal norms", "Financial dependence or economic barriers", "Other"])
barriers_survivors.add_kap_label(["Fear of retaliation from the perpetrator", "Stigma", "Lack of awareness about available support services", "Cultural or societal norms", "Financial dependence or economic barriers", "Other"])

actions_perpetrators = bd.Indicator(df, "Actions perpetrators", None, ['58'], i_cal=None, i_type='count', description='What actions do you think should be taken against perpetrators of GBV?', period='KAP', target = None)
actions_perpetrators.add_breakdown({'s2':'Region', 's1':'Age Group', 's3':'Gender', 'Disability':'Disability'})
actions_perpetrators.add_var_order(["Legal prosecution and enforcement", "Mandatory participation in rehabilitation and counselling programmes", "Pretection Orders/Restaining orders to protect survivors", "GBV prevention education", "None of them", "Other"])
actions_perpetrators.add_kap_label(["Legal prosecution and enforcement", "Mandatory participation in rehabilitation and counselling programmes", "Pretection Orders/Restaining orders to protect survivors", "GBV prevention education", "None of them", "Other"])

factors_preventing_gbv = bd.Indicator(df, "Contribution GBV Prevention", None, ['59'], i_cal=None, i_type='count', description='What do you consider the most crucial individual contribution to preventing GBV?', period='KAP', target = None)
factors_preventing_gbv.add_breakdown({'s2':'Region', 's1':'Age Group', 's3':'Gender', 'Disability':'Disability'})
factors_preventing_gbv.add_var_order(["Education and awareness-raising about GBV", "Gender equality", "Advocating for GBV policies and laws change", "Attending GBV prevention programmes", "Other"])
factors_preventing_gbv.add_kap_label(["Education and awareness-raising about GBV", "Gender equality", "Advocating for GBV policies and laws change", "Attending GBV prevention programmes", "Other"])

female_gbv = bd.Indicator(df, "GBV Target - W", None, ['60'], i_cal=None, i_type='count', description='Do you think women can suffer from GBV?', period='KAP', target = None)
female_gbv.add_breakdown({'s2':'Region', 's1':'Age Group', 's3':'Gender', 'Disability':'Disability'})
female_gbv.add_var_order(["Yes", "No"])
female_gbv.add_kap_label(["Yes", "No"])

female_gbv_impacts = bd.Indicator(df, "GBV Impcats - w", None, ['61.1','61.2', '61.3', '61.4', '61.5', '61.6', '61.7'], i_cal=None, i_type='count', description='What impact does GBV have on women?', period='KAP', target = None)
female_gbv_impacts.add_breakdown({'s2':'Region', 's1':'Age Group', 's3':'Gender', 'Disability':'Disability'})
female_gbv_impacts.add_var_change({1: "Yes", 0: "No"})
female_gbv_impacts.add_var_order([1, 0])
female_gbv_impacts.add_kap_label(['Physical injury', "Mental health difficulties", 'Social stigma and rejection',"Health (STIs and HIV)", "Poverty",
                                  "Discrimination", "Other"])

male_gbv = bd.Indicator(df, "GBV Target - M", None, ['62'], i_cal=None, i_type='count', description='Do you think men can suffer from GBV?', period='KAP', target = None)
male_gbv.add_breakdown({'s2':'Region', 's1':'Age Group', 's3':'Gender', 'Disability':'Disability'})
male_gbv.add_var_order(["Yes", "No"])
male_gbv.add_kap_label(["Yes", "No"])

male_gbv_impacts = bd.Indicator(df, "GBV Impacts - m", None, ['63.1','63.2', '63.3', '63.4', '63.5', '63.6', '63.7'], i_cal=None, i_type='count', description='What impact does GBV have on men?', period='KAP', target = None)
male_gbv_impacts.add_breakdown({'s2':'Region', 's1':'Age Group', 's3':'Gender', 'Disability':'Disability'})
male_gbv_impacts.add_var_change({1: "Yes", 0: "No"})
male_gbv_impacts.add_var_order([1, 0])
male_gbv_impacts.add_kap_label(['Physical injury', "Mental health difficulties", 'Social stigma and rejection',"Health (STIs and HIV)", "Poverty",
                                  "Discrimination", "Other"])

gender_gbv = bd.Indicator(df, "Suffering GBV more", None, ['64'], i_cal=None, i_type='count', description='Who suffers more from GBV?', period='KAP', target = None)
gender_gbv.add_breakdown({'s2':'Region', 's1':'Age Group', 's3':'Gender', 'Disability':'Disability'})
gender_gbv.add_var_order(["Men", "Women", "Equally", "Neither"])
gender_gbv.add_kap_label(["Men", "Women", "Equally", "Neither"])

age_gbv = bd.Indicator(df, "Victims of GBV", None, ['65.1','65.2', '65.3', '65.4', '65.5'], i_cal=None, i_type='count', description='Which age groups can be victims of GBV?', period='KAP', target = None)
age_gbv.add_breakdown({'s2':'Region', 's1':'Age Group', 's3':'Gender', 'Disability':'Disability'})
age_gbv.add_var_change({1: "Yes", 0: "No"})
age_gbv.add_var_order([1, 0])
age_gbv.add_kap_label(['0-11', "12-18", '19-64',"65 and over", "All of them"])

child_gbv = bd.Indicator(df, "Child GBV victims", None, ['66'], i_cal=None, i_type='count', description='Do you think a child can be a victim of GBV?', period='KAP', target = None)
child_gbv.add_breakdown({'s2':'Region', 's1':'Age Group', 's3':'Gender', 'Disability':'Disability'})
child_gbv.add_var_order(["Yes", "No"])
child_gbv.add_kap_label(["Yes", "No"])

reason_occur_gbv = bd.Indicator(df, "Why GBV occurring", None, ['67.1','67.2', '67.3', '67.4', '67.5', '67.6', '67.7', '67.8'], i_cal=None, i_type='count', description='Why do you think GBV occurs in your area?', period='KAP', target = None)
reason_occur_gbv.add_breakdown({'s2':'Region', 's1':'Age Group', 's3':'Gender', 'Disability':'Disability'})
reason_occur_gbv.add_var_change({1: "Yes", 0: "No"})
reason_occur_gbv.add_var_order([1, 0])
reason_occur_gbv.add_kap_label(['Gender inequality', "Cultural customs", 'Economic stress',"Lack of education", "Weak legal protections",
                                "Relationship dynamics", "Addiction", "Other"])

gbv_serious = bd.Indicator(df, "GBV matters", None, ['68'], i_cal=None, i_type='count', description='Do you think GBV is a serious matter?', period='KAP', target = None)
gbv_serious.add_breakdown({'s2':'Region', 's1':'Age Group', 's3':'Gender', 'Disability':'Disability'})
gbv_serious.add_var_order(["Yes", "No"])
gbv_serious.add_kap_label(["Yes", "No"])

common_gbv = bd.Indicator(df, "level of common", None, ['70','71', '72', '73', '74'], i_cal=None, i_type='count', description='Do you think this form of GBV is common in your community?', period='KAP', target = None)
common_gbv.add_breakdown({'s2':'Region', 's1':'Age Group', 's3':'Gender', 'Disability':'Disability'})
common_gbv.add_var_order(["Not common", 'Common', 'Very common'])
common_gbv.add_kap_label(['Rape', "Sexual assault", 'Child, early, forced marriage and unions',"Denial of resources, opportunities, or services",
                                "Psychological and emotional abuse"])

feel_safe_gbv = bd.Indicator(df, "level of feel safe", None, ['75','76', '77', '78'], i_cal=None, i_type='count', description='Do you feel safe in the following contexts?', period='KAP', target = None)
feel_safe_gbv.add_breakdown({'s2':'Region', 's1':'Age Group', 's3':'Gender', 'Disability':'Disability'})
feel_safe_gbv.add_var_order(["Very unsafe", 'Unsafe', 'Neither safe nor unsafe', 'Safe', 'Very safe'])
feel_safe_gbv.add_kap_label(['Inside the home', "In the community during the day", 'In the community at night',"Outside the community"])

risk_rate_gbv = bd.Indicator(df, "Risk level", None, ['79','80', '81', '82', '83'], i_cal=None, i_type='count', description='How would you rate the risk of the following forms of GBV in your neighbourhood?', period='KAP', target = None)
risk_rate_gbv.add_breakdown({'s2':'Region', 's1':'Age Group', 's3':'Gender', 'Disability':'Disability'})
risk_rate_gbv.add_var_order(["Very low risk", 'Low risk', 'Medium risk', 'High risk', 'Very high risk'])
risk_rate_gbv.add_kap_label(['Rape', "Sexual assault", 'Child, early, forced marriage and unions',"Denial of resources, opportunities, or services",
                                "Psychological and emotional abuse"])

opinion_gender_roles = bd.Indicator(df, "Gender roles", None, ['105','106','107','108'], i_cal=None, i_type='count', description='What is your opinion about gender roles in the following contexts?', period='KAP', target = None)
opinion_gender_roles.add_breakdown({'s2':'Region', 's1':'Age Group', 's3':'Gender', 'Disability':'Disability'})
opinion_gender_roles.add_var_order(["Strongly disagree", 'Disagree', 'Neither agree or disagree', 'Agree', 'Strongly agree'])
opinion_gender_roles.add_kap_label(['Household finances are a man’s responsibility', "Taking care of children is a woman’s responsibility", 
                                    'Avoiding pregnancy is a woman’s responsibility',"Household affairs (cooking, laundry etc) are a woman’s responsibility"])

feel_victims = bd.Indicator(df, "Feeling encountering", None, ['109'], i_cal=None, i_type='count', description='How do you feel when you encounter a victim of GBV?', period='KAP', target = None)
feel_victims.add_breakdown({'s2':'Region', 's1':'Age Group', 's3':'Gender', 'Disability':'Disability'})
feel_victims.add_var_order(["Neutral", "Distressed", "Concerned", "Sympathetic", "Supportive"])
feel_victims.add_kap_label(["Neutral", "Distressed", "Concerned", "Sympathetic", "Supportive"])

will_support_gbv = bd.Indicator(df, "Willing to support", None, ['110'], i_cal=None, i_type='count', description='Are you willing to assist a person in a GBV crisis?', period='KAP', target = None)
will_support_gbv.add_breakdown({'s2':'Region', 's1':'Age Group', 's3':'Gender', 'Disability':'Disability'})
will_support_gbv.add_var_order(["Yes", "No"])
will_support_gbv.add_kap_label(["Yes", "No"])

ways_support_gbv = bd.Indicator(df, "Ways to support", None, ['111.1','111.2','111.3','111.4','111.5'], i_cal=None, i_type='count', description='How would you assist someone in a GBV crisis?', period='KAP', target = None)
ways_support_gbv.add_breakdown({'s2':'Region', 's1':'Age Group', 's3':'Gender', 'Disability':'Disability'})
ways_support_gbv.add_var_change({1: "Yes", 0: "No"})
ways_support_gbv.add_var_order([1, 0])
ways_support_gbv.add_kap_label(['Provide emotional support', "Offer practical assistance", 'Provide relevant information',"Advocacy or campaign", "Other"])

tolerance_gbv = bd.Indicator(df, "Tolerance", None, ['112','113','114','115'], i_cal=None, i_type='count', description='How would you rate your tolerance of GBV in the following contexts?', period='KAP', target = None)
tolerance_gbv.add_breakdown({'s2':'Region', 's1':'Age Group', 's3':'Gender', 'Disability':'Disability'})
tolerance_gbv.add_var_order(["Not acceptable", 'Acceptable', 'Unsure'])
tolerance_gbv.add_kap_label(['Domestic settings', "Workplace", 'Public spaces',"Conflict setting"])

victim_fault = bd.Indicator(df, "Victim faults", None, ['116'], i_cal=None, i_type='count', description='Do you think victims are sometimes/partly responsible for GBV?', period='KAP', target = None)
victim_fault.add_breakdown({'s2':'Region', 's1':'Age Group', 's3':'Gender', 'Disability':'Disability'})
victim_fault.add_var_order(["Yes", "No"])
victim_fault.add_kap_label(["Yes", "No"])

reason_victim_fault = bd.Indicator(df, "Why victim faults", None, ['117.1','117.2','117.3','117.4','117.5','117.6','117.7','117.8','117.9','117.10'], i_cal=None, i_type='count', description='Why do you think that victims are sometimes/partly responsible?', period='KAP', target = None)
reason_victim_fault.add_breakdown({'s2':'Region', 's1':'Age Group', 's3':'Gender', 'Disability':'Disability'})
reason_victim_fault.add_var_change({1: "Yes", 0: "No"})
reason_victim_fault.add_var_order([1, 0])
reason_victim_fault.add_kap_label(["Provocative behaviour", 'Provocative clothing',"Wrong decision-making", "Staying in abusive relationship", "Ignoring warning signs",
                                   "Use of alcohol or drugs", "Inadequate self-defence", "Neglect of personal responsibility", "Delay in reporting abuse", "Other"])

ex_gbv_programmes = bd.Indicator(df, "Experiences of programs", None, ['148'], i_cal=None, i_type='count', description='Have you ever participated in any GBV prevention programmes?', period='KAP', target = None)
ex_gbv_programmes.add_breakdown({'s2':'Region', 's1':'Age Group', 's3':'Gender', 'Disability':'Disability'})
ex_gbv_programmes.add_var_order(["Yes", "No"])
ex_gbv_programmes.add_kap_label(["Yes", "No"])

list_gbv_programmes = bd.Indicator(df, "List Expererience program", None, ['149.1','149.2','149.3','149.4','149.5','149.6','149.7'], i_cal=None, i_type='count', description='What GBV prevention programmes have you attended before?', period='KAP', target = None)
list_gbv_programmes.add_breakdown({'s2':'Region', 's1':'Age Group', 's3':'Gender', 'Disability':'Disability'})
list_gbv_programmes.add_var_change({1: "Yes", 0: "No"})
list_gbv_programmes.add_var_order([1, 0])
list_gbv_programmes.add_kap_label(["Women’s rights", "Women empowerment", "Stigma reduction","Understanding of GBV",
                                    'Equality',"GBV prevention and response", "Other"])

will_programmes = bd.Indicator(df, "Willingness GBV program", None, ['150'], i_cal=None, i_type='count', description='Are you willing to attend GBV prevention programmes in the future?', period='KAP', target = None)
will_programmes.add_breakdown({'s2':'Region', 's1':'Age Group', 's3':'Gender', 'Disability':'Disability'})
will_programmes.add_var_order(["Yes", "No"])
will_programmes.add_kap_label(["Yes", "No"])

want_programmes = bd.Indicator(df, "Interest GBV program", None, ['151'], i_cal=None, i_type='count', description='Which type of GBV prevention programmes are you most interested in?', period='KAP', target = None)
want_programmes.add_breakdown({'s2':'Region', 's1':'Age Group', 's3':'Gender', 'Disability':'Disability'})
want_programmes.add_var_order(["Workshop", "Training courses", "Webinars or online courses", "Community events", "Volunteer programmes", "Other"])
want_programmes.add_kap_label(["Workshop", "Training courses", "Webinars or online courses", "Community events", "Volunteer programmes", "Other"])

important_programmes = bd.Indicator(df, "Important GBV program", None, ['152'], i_cal=None, i_type='count', description='What GBV prevention programme is the most important in your region?', period='KAP', target = None)
important_programmes.add_breakdown({'s2':'Region', 's1':'Age Group', 's3':'Gender', 'Disability':'Disability'})
important_programmes.add_var_order(["Women's rights", "Women empowerment", "Stigma reduction", "Understanding of GBV", "Equality", "Prevention and response of GBV", "Other"])
important_programmes.add_kap_label(["Women's rights", "Women empowerment", "Stigma reduction", "Understanding of GBV", "Equality", "Prevention and response of GBV", "Other"])


# Create PMF model for the project
carob = pmf.PerformanceManagementFramework('UNFPA KAP Survey on GBV', 'KAP')

# Add the indicators to the PMF model
carob.add_indicators([age, region, gender, occupation, si, maternity, disability, know_gbv, knowledge_gbv, gbv_attitude_g,gbv_attitude_gs, gbv_attitude_b, gbv_b_1, gbv_b_2, gbv_b_3, gbv_s_1, gbv_s_2, gbv_s_3, type_gbv, 
                     type_knowledge_gbv_1, type_knowledge_gbv_2, type_knowledge_gbv_3, type_knowledge_gbv_4, type_knowledge_gbv_5,type_knowledge_gbv_6,type_knowledge_gbv_7,type_knowledge_gbv_8,
                     main_source, av_gbv_service, list_gbv_service, know_report_gbv, subject_report_gbv, ex_report_gbv, report_time,report_type, report_location, report_responsible, 
                                           report_level, report_level_reason, knowledge_gp, knowledge_gp_can,knowledge_laws, knowledge_laws_can, knowledge_s_methods, s_methods,
                                           support_need_gbv,barriers_survivors,actions_perpetrators,factors_preventing_gbv,female_gbv, female_gbv_impacts,
                                           male_gbv, male_gbv_impacts,gender_gbv,age_gbv,child_gbv,reason_occur_gbv,gbv_serious,tolerance_gbv,common_gbv,feel_safe_gbv,risk_rate_gbv])
                      
file_path1 = 'data/24-UNFPA-SS-1 KAP Statistics.xlsx' # The file path of the KAP statistics
file_path2 = 'data/24-UNFPA-SS-1 KAP Chi2 Results.xlsx' # The file path of the chi2 test results
folder = 'visuals/'  # The file path for data visualisation

# Run the entire data analysis pipeline
carob.PMF_generation(file_path1, file_path2, folder) 
