import numpy as np
import random as rn
import pandas as pd
import hashlib
class Reader:
    def __init__(self,path):
        self.df = pd.read_csv(path)
    def get_column_values(self,column_no=3):
        col=self.df[self.df.columns[column_no-1]].tolist()
        return col
    def concatenate_odd(self, l: list):
        odd_col_3 = []
        for i in range(len(l)):
            if (i % 2 == 0):  # since first element is considered 0 but it is an odd item
                odd_col_3.append(str(l[i]))
        single_string = ''.join(odd_col_3) # concatenate results
        return single_string
class Hasher:
    def __init__(self, string):
        self.string=string
    def MD5(self):
        print("The concatenated string should be:  result should be: {}".format(self.string))
        result = hashlib.md5(self.string.encode())
        print("The hashed MD5 result should be: {}".format(result.hexdigest()))

read=Reader(r'annual-enterprise-survey-2020-financial-year-provisional-csv.csv')
concatenated=read.get_column_values(3)
results=read.concatenate_odd(concatenated)
hash=Hasher(results)
hash.MD5()