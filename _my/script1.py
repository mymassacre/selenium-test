import glob
import pandas as pd

files_asuse = glob.glob(r'C:\Users\korne\Documents\Алтайэнергосбыт\2022-06\_население\_asuse\*.xlsx')
dfs_asuse = [pd.read_excel(f, sheet_name='Сверка ПО', skiprows=[0, 1]) for f in files_asuse]

asuse = pd.concat(dfs_asuse, ignore_index=True)

files_forsage_71_08 = glob.glob(r'C:\Users\korne\Documents\Алтайэнергосбыт\2022-06\_население\_forsage_71_08\*.csv')
dfs_forsage_71_08 = [pd.read_csv(f, sep=';', skiprows=range(0, 11), encoding='ANSI', low_memory=False)
                     for f in files_forsage_71_08]

forsage_71_08 = pd.concat(dfs_forsage_71_08, ignore_index=True)
