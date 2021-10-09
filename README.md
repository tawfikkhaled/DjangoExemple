Runnning the project:
    - run cd mysite puis python manage.py runserver 8000
    - run cd frontend puis npm start




create : django-admin startproject mysite
run  : python manage.py runserver 8000
create : python manage.py startapp polls
create :  (in postgresql) create database django_admin;
create : python manage.py migrate
create : python manage.py createsuperuser
run : python manage.py test polls
create : python manage.py startapp todo




(Adding Spark)
Linux : 
create : download java and spark-3.1.1-bin-hadoop2.7
create : export SPARK_HOME=/opt/apache-spark/spark-3.1.1-bin-hadoop2.7 export PATH = $PATH:$SPARK_HOME/bin  (eventuellement même chose pour java)
run : pyspark
Windows : 
create : download java and spark-3.1.1-bin-hadoop2.7
create : download winutils and put it in c:\hadoop\bin (à créer)
cerate : ajouter les variable d'environnement SPAR_HOME et HADOOP_HOME ry ajouter les bins dans path
create : créer c:\tmp\hive et exécuter winutils chmod 777 c:\tmp\hive pour que hadoop  peut y accèder
run : pyspark
create  : ajouter if "x%PYSPARK_DRIVER_PYTHON%"=="x" (
  set PYSPARK_DRIVER_PYTHON=python
  if not [%PYSPARK_PYTHON%] == [] set PYSPARK_DRIVER_PYTHON=%PYSPARK_PYTHON%
  set PYSPARK_PYTHON=python
) à spark-submid2.cmd pour ne pas avoir l'erreur Python not found


run  : spark-submit %filename%
run  : même chose dépuis ubuntu wsl

installation hadoop 
create : https://clubhouse.io/developer-how-to/how-to-set-up-a-hadoop-cluster-in-docker/
run : remove all containers : docker container rm -f $(docker ps | grep -o "^[a-z,0-9]*")
run : docker-compose down to delete containers of the docker compose
run : passwd to change password for namenode and datanode (password : hadoop for root)


create :   single node hadoop on windows : https://towardsdatascience.com/installing-hadoop-3-2-1-single-node-cluster-on-windows-10-ac258dd48aef
create :   single node hadoop on ubuntu : https://phoenixnap.com/kb/install-hadoop-ubuntu



Frontend prject : 
run : cd mysite/client/static/client/frontendrequire puis gulp watch


