import pandas as pd
import numpy as np
fvc_range=pd.read_csv('fvc_ranges.txt')
def fetch_normal(age, sex):
    fvc_sub = fvc_range[(fvc_range["Gender"] == sex) &
                        (fvc_range["Age_min"] <= age) &
                        (fvc_range["Age_max"] >= age) &
                        (fvc_range["Risk_type"] == "Normal") ]
    fvc_min = fvc_sub["FVC_min"].iloc[0]
    print(fvc_min)
    return fvc_min


def predict_stage(age, gender, avg_fvc):
    stage=''
    fvc_min=fetch_normal(age,gender)
    if 0.71*fvc_min<=avg_fvc<=0.80*fvc_min:
        stage='STAGE 1'
    elif 0.61*fvc_min<=avg_fvc<=0.70*fvc_min:
        stage='STAGE 2'
    elif 0.41*fvc_min<=avg_fvc<=0.60*fvc_min:
        stage='STAGE 3'
    elif 0<=avg_fvc<=0.40*fvc_min:
        stage='Stage 4'
    else:
        stage='NA'
    return stage


stage_new=predict_stage(56,'Male',600)
print(stage_new)