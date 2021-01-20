# -*- coding: utf-8 -*-
"""
Created on Tue Dec 15 23:14:27 2020

@author: koadu
"""

import pandas as pd

df = pd.read_csv('glassdoor_jobs.csv')



#salary parsing

df = df[df['Salary Estimate'] != '-1']

salary = df['Salary Estimate'].apply(lambda x: x.split('(')[0])

minus_kd = salary.apply(lambda x: x.replace('k','').replace('CA$',''))
                        
df['min_salary'] = pd.to_numeric(minus_kd.apply(lambda x: x.split('-')[0]))
df['max_salary'] = pd.to_numeric(minus_kd.apply(lambda x: x.split('-')[1]))
df['avg_salary'] = (df.min_salary + df.max_salary)/2

#comapny name text only
df['company'] = df.apply(lambda x: x['Company Name'] if x['Rating'] <0 else x['Company Name'][:-3], axis =1)


#age of company
# df['age'] = df.apply(lambda x: 2020 - pd.to_numeric(x['Founded']) if pd.to_numeric(x['Founded']) != -1 else x['Founded'], axis =1)
df['age'] = df.Founded.apply(lambda x: x if x<1 else 2020 -x)

#parsing of job description (python, etc)
df['python_yn'] = df['Job Description'].apply(lambda x: 1 if 'python' in x.lower() else 0)
# print(df.python_yn.value_counts())

df['R_yn'] = df['Job Description'].apply(lambda x: 1 if 'r studio' in x.lower() or 'r-studio' in x.lower() else 0)
# print(df.R_yn.value_counts())

df['spark_yn'] = df['Job Description'].apply(lambda x: 1 if 'spark' in x.lower() else 0)
# print(df.spark_yn.value_counts())

df['aws_yn'] = df['Job Description'].apply(lambda x: 1 if 'aws' in x.lower() else 0)
# print(df.aws_yn.value_counts())

df['excel_yn'] = df['Job Description'].apply(lambda x: 1 if 'excel' in x.lower() else 0)
# print(df.excel_yn.value_counts())

df_out = df.copy()

df_out.to_csv('salary_data_cleaned.csv', index = False)

