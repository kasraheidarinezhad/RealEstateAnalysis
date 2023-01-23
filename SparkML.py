from pyspark.sql.functions import monotonically_increasing_id
from pyspark.sql.functions import avg
from pyspark.sql.functions import mean
from pyspark.sql.types import FloatType
from pyspark.sql.functions import udf
from pyspark.sql import SparkSession

# Create a SparkSession
spark = SparkSession.builder\
        .master("local")\
        .appName("DataPipeline")\
        .getOrCreate()

#        .config('spark.ui.port','4050')\

df = spark.read.csv("D:\RealEstateAnalysis\housing.csv", header=True, inferSchema=True)
df.printSchema()
df.select(avg("total_rooms")).show()
df.count()
df.select(*[mean(c) for c in df.columns]).show()
df = df.withColumn('id', monotonically_increasing_id())
df = df[['id'] + df.columns[:-1]]
df.show(3)
#print(df.count())
df.groupby('ocean_proximity').agg({col: 'avg' for col in df.columns[3:-1]}).show()

def squared(value):
    return value * value

squared_udf = udf(squared , FloatType())
df.withColumn('total_rooms_squared', squared_udf('total_rooms')).show(5)

spark.stop()
