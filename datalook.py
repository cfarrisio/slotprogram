from google.cloud import bigquery

# Instantiates a client
client = bigquery.Client()

# SQL query to retrieve top 10 records from blackhole_database table
query = """
SELECT *
FROM `bigquery-public-data.blackhole_database.blackhole`
LIMIT 10
"""

# Execute the query
query_job = client.query(query)

# Print the results
for row in query_job:
    print(f"{row}")
