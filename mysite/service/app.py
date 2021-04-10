import os
from pyspark.sql import SparkSession

import pydoop.hdfs as hdfs
hdfs.user="hdoop"
hdfs.
from_path = '/home/tawfik/Documents/dev/DjangoExemple/README.md'
to_path ='hdfs://localhost:9000/python/outfile.txt'
try:
    hdfs.cp(from_path, to_path, mode='w+')
except IOError:
    hdfs.rm(to_path)
    hdfs.cp(from_path, to_path, mode='w+')
    