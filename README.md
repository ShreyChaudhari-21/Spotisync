# Spotisync

This project demonstrates the creation of an ETL (Extract, Transform, Load) pipeline using AWS services to process and analyze Spotify data. The pipeline extracts data from CSV files, transforms the data by performing joins and merging operations, and loads the final dataset into AWS Athena for querying and visualization.

---
Overview

Objective
- To process and analyze Spotify's dataset by building an ETL pipeline using AWS services.
- Integrate three separate datasets (`artist.csv`, `album.csv`, and `tracks.csv`) into one final output for further analysis.

Technologies Used
- AWS S3: For storing datasets and final output files.
- AWS Glue: For crawling, transforming, and joining data.
- AWS Athena: This is used to query and analyze the final dataset.

---

Workflow Steps

1. Dataset
- Downloaded three CSV files:
  1. `artist.csv` - Contains data about Spotify artists.
  2. `album.csv` - Contains data about Spotify albums.
  3. `tracks.csv` - Contains data about Spotify tracks.
     ![Screenshot (229)](https://github.com/user-attachments/assets/cb6b891f-821f-4642-a66a-1e2b980acc36)


2. Upload Files to S3
- Uploaded all three files into an S3 bucket named “staging-layer” for further processing.
 
3. Data Crawling (AWS Glue)
- Created a Glue Crawler to discover and catalog the schema of the datasets.
 

4. Data Transformation
- Merged the three datasets using Glue:
  - Performed a join operation between `album.csv` and `artist.csv` using the `artist_id` column as the key.
  - Joined the combined data with `tracks.csv` using the `album_id` column as the key.
- Dropped some repeated fields like ‘id’, and ‘track_id’.
- Generated the final dataset by combining relevant columns and relationships.
  


5. Load the Final Dataset
- Dumped the final transformed dataset back into the S3 bucket.

6. Query with Athena
- Used AWS Athena to query the final dataset directly from S3 for analysis and visualization.
 



