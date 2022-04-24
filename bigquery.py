import google
from google.cloud import bigquery



def bq(query):

    client = bigquery.Client()

    query_job = client.query(query)
    df = query_job.to_dataframe()
    json = df.to_json(orient='records')

    return json
