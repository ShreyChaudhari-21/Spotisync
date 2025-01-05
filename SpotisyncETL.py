import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job
from awsgluedq.transforms import EvaluateDataQuality

args = getResolvedOptions(sys.argv, ['JOB_NAME'])
sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

# Default ruleset used by all target nodes with data quality enabled
DEFAULT_DATA_QUALITY_RULESET = """
    Rules = [
        ColumnCount > 0
    ]
"""

# Script generated for node spotify artists
spotifyartists_node1736033528125 = glueContext.create_dynamic_frame.from_options(format_options={"quoteChar": "\"", "withHeader": True, "separator": ",", "optimizePerformance": False}, connection_type="s3", format="csv", connection_options={"paths": ["s3://spotify-etl-metadata-store/staging-layer/artists_Spotify.csv"], "recurse": True}, transformation_ctx="spotifyartists_node1736033528125")

# Script generated for node spotify albums
spotifyalbums_node1736033557898 = glueContext.create_dynamic_frame.from_options(format_options={"quoteChar": "\"", "withHeader": True, "separator": ",", "optimizePerformance": False}, connection_type="s3", format="csv", connection_options={"paths": ["s3://spotify-etl-metadata-store/staging-layer/albums_Spotify.csv"], "recurse": True}, transformation_ctx="spotifyalbums_node1736033557898")

# Script generated for node spotify Tracks
spotifyTracks_node1736033559678 = glueContext.create_dynamic_frame.from_options(format_options={"quoteChar": "\"", "withHeader": True, "separator": ",", "optimizePerformance": False}, connection_type="s3", format="csv", connection_options={"paths": ["s3://spotify-etl-metadata-store/staging-layer/track_Spotify.csv"], "recurse": True}, transformation_ctx="spotifyTracks_node1736033559678")

# Script generated for node Join Album & Artist
JoinAlbumArtist_node1736034207278 = Join.apply(frame1=spotifyalbums_node1736033557898, frame2=spotifyartists_node1736033528125, keys1=["artist_id"], keys2=["id"], transformation_ctx="JoinAlbumArtist_node1736034207278")

# Script generated for node Join Tracks with Album & Artist
JoinTrackswithAlbumArtist_node1736034353361 = Join.apply(frame1=JoinAlbumArtist_node1736034207278, frame2=spotifyTracks_node1736033559678, keys1=["track_id"], keys2=["track_id"], transformation_ctx="JoinTrackswithAlbumArtist_node1736034353361")

# Script generated for node Drop Fields
DropFields_node1736034512719 = DropFields.apply(frame=JoinTrackswithAlbumArtist_node1736034353361, paths=["`.track_id`", "id"], transformation_ctx="DropFields_node1736034512719")

# Script generated for node Destination target DataWarehouse
EvaluateDataQuality().process_rows(frame=DropFields_node1736034512719, ruleset=DEFAULT_DATA_QUALITY_RULESET, publishing_options={"dataQualityEvaluationContext": "EvaluateDataQuality_node1736033518215", "enableDataQualityResultsPublishing": True}, additional_options={"dataQualityResultsPublishing.strategy": "BEST_EFFORT", "observations.scope": "ALL"})
DestinationtargetDataWarehouse_node1736034575680 = glueContext.write_dynamic_frame.from_options(frame=DropFields_node1736034512719, connection_type="s3", format="glueparquet", connection_options={"path": "s3://spotify-etl-metadata-store/datawarehouse/", "partitionKeys": []}, format_options={"compression": "snappy"}, transformation_ctx="DestinationtargetDataWarehouse_node1736034575680")

job.commit()