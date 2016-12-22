# Databricks notebook source
"hi"

# COMMAND ----------

from pyspark.sql import Row

array = [Row(key="a", group="vowels", value=1),
         Row(key="b", group="consonants", value=2),
         Row(key="c", group="consonants", value=3),
         Row(key="d", group="consonants", value=4),
         Row(key="e", group="vowels", value=5)]
dataframe = sqlContext.createDataFrame(sc.parallelize(array))

display(dataframe)

# COMMAND ----------

