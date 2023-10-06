# This is a sample Python script.
from typing import Any

import pandas as pd
from pandas import DataFrame


# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows,
# actions, and settings.

def read_file(file_path="~/Documents/202308-202406/Pausania/data/basic.csv"):

    df: DataFrame | Any = pd.read_csv(file_path, sep=",", header=0,
                                      encoding="utf-8")
    if not df.empty: # avoid complaining NoneType
        df.fillna('', inplace=True)
    return df

'''the function has one parameter file_path, and one optional parameter'''
def read_xlsx(file_path, the_sheet="Sheet1"):
    '''
    :type file_path: str
    '''
    # one sheet at a time , "Relations"
    dic = pd.read_excel(file_path, sheet_name=[
    the_sheet])
    keys = dic.keys()
    df_annotation = pd.DataFrame(dic.get(the_sheet))
    if not df_annotation.empty:
        df_annotation.fillna('', inplace=True)

    return df_annotation
def print_file(df: object) -> object:
    columns = df.columns
    print(df.dtypes)
    for col in columns:
        print("---" + col + "---")
        for index in range(3):
            print(df[col].loc[index])

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    #df = read_file()
    file = "~/Documents/202308-202406/Pausania/data/OUTPUT 9Sept.xlsx"
    sheet = "RecogitoAnnotOutput2023-09-09"
    # df = read_xlsx(file, sheet)
    df = read_xlsx(file)
    print_file(df)
    print(df.shape)
    '''
    df["LAT"] = df["LAT"].apply(lambda x: 0.0 if not x else float(x))
    df["LNG"] = df["LNG"].apply(lambda x: 0.0 if not x else float(x))
    df["Lat2"] = df["LatLong2"].apply(lambda x: 0.0 if not x else
        float(x.split(",")[0]))
    df["Lng2"] = df["LatLong2"].apply(lambda x: 0.0 if not x else float(x.split(
        ",")[1]))
    df["DerLat"] = df["DerivedLatLng"].apply(lambda x: 0.0 if not x else
    float(x.split(",")[0]))
    df["DerLng"] = df["DerivedLatLng"].apply(lambda x: 0.0 if not x else
    float(x.split(",")[1]))
    print(df.shape)
    for type in df["TYPE"].unique():
        print("****"+type+"*****")
        print(df[df["TYPE"] == type].shape)
        print(df[df["TYPE"] == type].head())
    '''
    # check the value in DerivedLatLng
    # print(df["DerivedLatLng"].unique())
    # print(df["TTlate"].unique())