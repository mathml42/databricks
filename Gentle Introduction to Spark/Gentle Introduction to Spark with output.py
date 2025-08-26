# Databricks notebook source
dbutils.fs.ls("/")

# COMMAND ----------

spark

# COMMAND ----------

dbutils.fs.ls('./databricks-datasets/amazon/data20K/')

# COMMAND ----------

df = spark.read.format("parquet").load("dbfs:/databricks-datasets/amazon/data20K")

# COMMAND ----------

df.show()

# COMMAND ----------

display(df)

# COMMAND ----------

from pyspark.sql import functions as F
brand_new_column = F.col("rating_percentage")
df = df.withColumn("rating_percentage", (F.col("rating") / F.lit(5)) * F.lit(100))
display(df.withColumn("half_rating_percentage", brand_new_column))

# COMMAND ----------

df.schema

# COMMAND ----------

df.printSchema()

# COMMAND ----------

from pyspark.sql.types import *

df_cast_test = df

df_cast_test = df_cast_test.withColumn("rating", F.col("rating").cast(IntegerType()))
df_cast_test = df_cast_test.withColumn("rating_percentage", (F.col("rating")/F.lit(5)) * F.lit(100))
df_cast_test = df_cast_test.withColumn("review_timestamp", F.col("review").try_cast(TimestampType()))
display(df_cast_test)

# COMMAND ----------

df_select_test = df

any_arbitrary_expression = (F.col("rating") + F.lit(1)).alias("arbitrary_expr")

df_select_test = df_select_test.select("*", any_arbitrary_expression)
display(df_select_test)

# COMMAND ----------

display(df_select_test.select("rating_percentage","review"))

# COMMAND ----------

import pandas as pd
from datetime import datetime
pandas_df = pd.DataFrame({"x": [1,2,3,4], "y":["a","b","c","d"]})
pandas_df["t"] = [datetime.now()] * len(pandas_df)
pandas_df

# COMMAND ----------

spark_df = spark.createDataFrame(pandas_df)
spark_df = spark_df.withColumn("z", F.col("t").cast(LongType()))
spark_df = spark_df.withColumn("t_recreated",F.col("z").cast(TimestampType()))


# COMMAND ----------

spark_df.collect()

# COMMAND ----------

display(spark_df)

# COMMAND ----------

