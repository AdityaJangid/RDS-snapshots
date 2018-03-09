import boto3
import pandas as pd
def lambda_handler(event, context):
    x = "column1","column2","column3","column4", "column5", "column6"  ## name your columns to read
    csv_to_write = ",".join(x)

    client = boto3.client('s3') #low-level functional API
    resource = boto3.resource('s3') #high-level object-oriented API

    my_bucket = resource.Bucket('BucketName') #subsitute this for your s3 bucket name.

    obj = client.get_object(Bucket='BucketName', Key='file_name.csv')

    grid_sizes = pd.read_csv(obj['Body'])


    for index, row in grid_sizes.iterrows():
        x= str(row["column1"]), str(row["column2"]),str(row["column3"]),str(row["column4"]), str(row["column5"]), str(row["column6"]), "\n" ##change the columns to read
        csv_rows = (",".join(x))
        csv_to_write= csv_to_write+csv_rows

    client.put_object(Body=csv_to_write, Bucket='BucketName', Key='out.csv')

