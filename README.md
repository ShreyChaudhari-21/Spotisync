# Spotisync

This project demonstrates the creation of an ETL (Extract, Transform, Load) pipeline using AWS services to process and analyze Spotify data. The pipeline extracts data from CSV files, transforms the data by performing joins and merging operations, and loads the final dataset into AWS Athena for querying and visualization.

![AWS_Glue_ETL_architecture](https://github.com/user-attachments/assets/cc58fb15-bfae-451d-9de5-694529ba5939)


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
     

2. Upload Files to S3
- Uploaded all three files into an S3 bucket named “staging-layer” for further processing.

     ![Screenshot (229)](https://github.com/user-attachments/assets/cb6b891f-821f-4642-a66a-1e2b980acc36)
  
3. Data Crawling (AWS Glue)
- Created a Glue Crawler to discover and catalog the schema of the datasets.

  ![image](https://github.com/user-attachments/assets/a460af0a-0b69-4abe-89e2-2b4a7eba9e35)

 

4. Data Transformation
- Merged the three datasets using Glue:
  - Performed a join operation between `album.csv` and `artist.csv` using the `artist_id` column as the key.
  - Joined the combined data with `tracks.csv` using the `album_id` column as the key.
- Dropped some repeated fields like ‘id’, and ‘track_id’.
- Generated the final dataset by combining relevant columns and relationships.

  ![image](https://github.com/user-attachments/assets/25b4a19b-2a2b-4f4e-811b-a275bde4ed93)
  
  ![image](https://github.com/user-attachments/assets/602c2a43-3321-4f6f-9f9f-9d391f318e1c)




5. Load the Final Dataset
- Dumped the final transformed dataset back into the S3 bucket.

6. Query with Athena
- Used AWS Athena to query the final dataset directly from S3 for analysis and visualization.

  ![image](https://github.com/user-attachments/assets/9a4d5d4a-7cd5-4875-8c28-25efe5865ef5)

 



