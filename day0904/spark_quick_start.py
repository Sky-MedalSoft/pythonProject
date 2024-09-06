from pyspark import SparkConf, SparkContext

conf = SparkConf().setMaster("local[*]").setAppName("Spark Quick Start")
sc = SparkContext(conf=conf)
print(sc.version)
sc.stop()