import os

# mysql+pymysql://your-username:your-password@localhost/your-schema?ssl_ca=BaltimoreCyberTrustRoot.crt.pem'
DATABASE_URI = 'mysql+pymysql://{dbuser}:{dbpass}@{dbhost}/{dbname}?ssl_ca=DigiCertGlobalRootG2.crt.pem'.format(
    dbuser=os.environ.get('AZURE_MYSQL_USER'),
    dbpass=os.environ.get('AZURE_MYSQL_PASSWORD'),
    dbhost=os.environ.get('AZURE_MYSQL_HOST'),
    dbname=os.environ.get('AZURE_MYSQL_NAME')
)
