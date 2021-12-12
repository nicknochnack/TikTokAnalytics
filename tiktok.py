# Importing the tiktok Python SDK
from TikTokApi import TikTokApi as tiktok
# Import JSON for export of data
import json
# Import data processing helper
from helpers import process_results 
# Import pandas to create dataframes
import pandas as pd
# Import sys dependency to extract command line arguments
import sys

def get_data(hashtag):
    # Get cookie data
    verifyFp = "verify_kx2ee558_BH6fvQVi_cXHF_4lfK_Bimg_hH0lYMCV6Vm6"
    # Setup instance
    api = tiktok.get_instance(custom_verifyFp=verifyFp, use_test_endpoints=True)
    # Get data by hashtag
    trending = api.by_hashtag(hashtag)
    # Process data
    flattened_data = process_results(trending)
    # Convert the preprocessed data to a dataframe
    df = pd.DataFrame.from_dict(flattened_data, orient='index')
    df.to_csv('tiktokdata.csv', index=False)

if __name__ == '__main__':
    get_data(sys.argv[1])

