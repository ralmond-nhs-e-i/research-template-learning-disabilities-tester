import pandas as pd

STPs = pd.read_csv(
    filepath_or_buffer = './analysis/STP.csv'
)
dict_stp = { stp : 1/len(STPs.index) for stp in STPs['stp_id'].tolist() }