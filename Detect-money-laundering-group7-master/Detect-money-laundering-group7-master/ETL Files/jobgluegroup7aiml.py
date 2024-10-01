import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job
from recipe_transforms import *
from awsglue.dynamicframe import DynamicFrame

# Generated recipe steps for DataPreparationRecipe_node1723633522028
def applyRecipe_node1723633522028(inputFrame, glueContext, transformation_ctx):
    frame = inputFrame.toDF()
    gc = glueContext
    df1 = ColumnStructure.SplitColumnSingleDelimiter.apply(
        data_frame=frame,
        glue_context=gc,
        transformation_ctx="DataPreparationRecipe_node1723633522028-df1",
        limit=1,
        include_in_split=True,
        pattern="\\s",
        source_column="timestamp",
    )
    df2 = Column.RenameColumn.apply(
        data_frame=df1,
        glue_context=gc,
        transformation_ctx="DataPreparationRecipe_node1723633522028-df2",
        source_column="timestamp_1",
        target_column="date",
    )
    df3 = Column.ChangeColumnDataType.apply(
        data_frame=df2,
        glue_context=gc,
        transformation_ctx="DataPreparationRecipe_node1723633522028-df3",
        source_column="date",
        column_data_type="date",
        replace_type="REPLACE_WITH_NULL",
    )
    df4 = Column.RenameColumn.apply(
        data_frame=df3,
        glue_context=gc,
        transformation_ctx="DataPreparationRecipe_node1723633522028-df4",
        source_column="timestamp_2",
        target_column="time",
    )
    df5 = Column.ChangeColumnDataType.apply(
        data_frame=df4,
        glue_context=gc,
        transformation_ctx="DataPreparationRecipe_node1723633522028-df5",
        source_column="from bank",
        column_data_type="string",
    )
    df6 = Column.ChangeColumnDataType.apply(
        data_frame=df5,
        glue_context=gc,
        transformation_ctx="DataPreparationRecipe_node1723633522028-df6",
        source_column="to bank",
        column_data_type="string",
    )
    df7 = Column.DeleteColumn.apply(
        data_frame=df6,
        glue_context=gc,
        transformation_ctx="DataPreparationRecipe_node1723633522028-df7",
        source_columns=["amount received"],
    )
    df8 = Column.ChangeColumnDataType.apply(
        data_frame=df7,
        glue_context=gc,
        transformation_ctx="DataPreparationRecipe_node1723633522028-df8",
        source_column="receiving currency",
        column_data_type="double",
    )
    df9 = Column.ChangeColumnDataType.apply(
        data_frame=df8,
        glue_context=gc,
        transformation_ctx="DataPreparationRecipe_node1723633522028-df9",
        source_column="payment currency",
        column_data_type="double",
    )
    df10 = Column.ChangeColumnDataType.apply(
        data_frame=df9,
        glue_context=gc,
        transformation_ctx="DataPreparationRecipe_node1723633522028-df10",
        source_column="col10",
        column_data_type="short",
    )
    df11 = Column.RenameColumn.apply(
        data_frame=df10,
        glue_context=gc,
        transformation_ctx="DataPreparationRecipe_node1723633522028-df11",
        source_column="receiving currency",
        target_column="amount received",
    )
    df12 = Column.RenameColumn.apply(
        data_frame=df11,
        glue_context=gc,
        transformation_ctx="DataPreparationRecipe_node1723633522028-df12",
        source_column="amount paid",
        target_column="recieving currency",
    )
    df13 = Column.RenameColumn.apply(
        data_frame=df12,
        glue_context=gc,
        transformation_ctx="DataPreparationRecipe_node1723633522028-df13",
        source_column="payment currency",
        target_column="amount paid",
    )
    df14 = Column.RenameColumn.apply(
        data_frame=df13,
        glue_context=gc,
        transformation_ctx="DataPreparationRecipe_node1723633522028-df14",
        source_column="payment format",
        target_column="payment currency",
    )
    df15 = Column.RenameColumn.apply(
        data_frame=df14,
        glue_context=gc,
        transformation_ctx="DataPreparationRecipe_node1723633522028-df15",
        source_column="is laundering",
        target_column="payment format",
    )
    df16 = Column.RenameColumn.apply(
        data_frame=df15,
        glue_context=gc,
        transformation_ctx="DataPreparationRecipe_node1723633522028-df16",
        source_column="col10",
        target_column="is laundering",
    )
    return DynamicFrame.fromDF(df16, gc, transformation_ctx)

args = getResolvedOptions(sys.argv, ['JOB_NAME'])
sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

# Script generated for node AWS Glue Data Catalog
AWSGlueDataCatalog_node1723633514106 = glueContext.create_dynamic_frame.from_catalog(database="aimlfinalgroup7database", table_name="rawdata", transformation_ctx="AWSGlueDataCatalog_node1723633514106")

# Script generated for node Data Preparation Recipe
# Adding configuration for certain Data Preparation recipe steps to run properly
spark.conf.set("spark.sql.legacy.timeParserPolicy", "LEGACY")
# Recipe name: DataPreparationRecipe_node1723633522028
DataPreparationRecipe_node1723633522028 = applyRecipe_node1723633522028(
    inputFrame=AWSGlueDataCatalog_node1723633514106,
    glueContext=glueContext,
    transformation_ctx="DataPreparationRecipe_node1723633522028")

# Script generated for node Amazon S3
AmazonS3_node1723635627884 = glueContext.write_dynamic_frame.from_options(frame=DataPreparationRecipe_node1723633522028, connection_type="s3", format="glueparquet", connection_options={"path": "s3://aimlprojectbigdatabucketgroup7all/input/", "partitionKeys": []}, format_options={"compression": "snappy"}, transformation_ctx="AmazonS3_node1723635627884")

# Script generated for node Amazon S3
AmazonS3_node1723635554196 = glueContext.write_dynamic_frame.from_options(frame=DataPreparationRecipe_node1723633522028, connection_type="s3", format="csv", connection_options={"path": "s3://aimlprojectbigdatabucketgroup7/cleandatacsv/", "compression": "snappy", "partitionKeys": []}, transformation_ctx="AmazonS3_node1723635554196")

# Script generated for node Amazon S3
AmazonS3_node1723635561495 = glueContext.write_dynamic_frame.from_options(frame=DataPreparationRecipe_node1723633522028, connection_type="s3", format="glueparquet", connection_options={"path": "s3://aimlprojectbigdatabucketgroup7/cleandataparquet/", "partitionKeys": []}, format_options={"compression": "snappy"}, transformation_ctx="AmazonS3_node1723635561495")

job.commit()