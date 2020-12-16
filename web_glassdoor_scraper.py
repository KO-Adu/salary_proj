


# -*- coding: utf-8 -*-
"""
Created on Fri Dec 11 17:49:19 2020

@author: koadu
"""

import glassdoor_scraper as gs
import pandas as pd
path = 'C:/Users/koadu/Documents/salary_proj/chromedriver.exe'

# df = gs.get_jobs('data scientist', 10, False, path, 0)
df = gs.get_jobs(1000, False, path, 10)

df.to_csv('glassdoor_jobs.csv', index = False)