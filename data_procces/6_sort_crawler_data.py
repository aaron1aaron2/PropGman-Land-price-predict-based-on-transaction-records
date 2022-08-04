"""
Author: 何彥南 (yen-nan ho)
Github: https://github.com/aaron1aaron2
Email: aaron1aaron2@gmail.com
Create Date: 2022.08.04
Last Update: 2022.08.04
Describe: 爬蟲資料整理 
"""
import pandas as pd

transaction_df = pd.read_csv('data/procces/1_sort_data/transaction_land.csv')


coordinate_result_df = pd.read_csv('data/procces/2_get_coordinate/c.csv')
coordinate_miss_df = pd.read_csv('data/procces/2_get_coordinate/crawler_miss.csv')


land_code_tran_df = pd.read_csv('data/procces/3_land_code_transform/crawler_result.csv')
