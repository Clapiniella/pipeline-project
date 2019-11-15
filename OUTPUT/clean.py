import numpy as np
import pandas as pd
import os
import re

to_replace=['en-US','en-GB','en-CA']
col_to_drop= ['ratings_count', 'text_reviews_count','isbn']
col_to_rename= {"# num_pages":"num_pages"}

def clean(data,to_replace,col_to_drop, col_to_rename):
    data = data[data.average_rating > 4]  
    data = data.drop(columns=col_to_drop)
    data = data.rename(columns=col_to_rename)
    data["authors"] = data["authors"].str.replace("J.K. Rowling-Mary GrandPré", "J.K. Rowling")
    for i in to_replace:
        data["language_code"] = data['language_code'].str.replace(i, "eng")
    
    return data  
    
df= clean(df, to_replace, col_to_drop, col_to_rename)