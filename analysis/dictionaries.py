import pandas as pd

STPs = pd.read_csv(
    filepath_or_buffer = './codelists/STP.csv'
)
dict_stp = { stp : 1/len(STPs.index) for stp in STPs['stp_id'].tolist() }