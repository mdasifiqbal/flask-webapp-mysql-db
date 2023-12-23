import os

DATABASE_URI = 'mysql+pymysql://{dbuser}:{dbpass}@{dbhost}/{dbname}'.format(
    dbuser=os.environ.get('AZURE_MYSQL_USER'),
    dbpass=os.environ.get('AZURE_MYSQL_PASSWORD'),
    dbhost=os.environ.get('AZURE_MYSQL_HOST'),
    dbname=os.environ.get('AZURE_MYSQL_NAME')
)
