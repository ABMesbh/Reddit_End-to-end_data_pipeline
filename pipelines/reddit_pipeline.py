import pandas as pd
from etls.reddit_etl import connect_reddit, extract_posts, load_data_to_csv, transform_data
from utils.constants import Client_id, Output_path, Secret

def reddit_pipeline(file_name: str, subreddit: str, time_filter='day', limit= None):

    # connecting to reddit
    instance = connect_reddit(Client_id, Secret, True)

    # extraction
    posts = extract_posts(instance, subreddit, time_filter, limit)
    
    post_df = pd.DataFrame(posts)
    
    # transformation
    posts_transformed = transform_data(post_df)

    # loading to csv
    file_path =  f'{Output_path}/{file_name}.csv'

    load_data_to_csv(posts_transformed , file_path)

    return file_path