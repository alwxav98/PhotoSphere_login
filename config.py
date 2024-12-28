import os

SECRET_KEY = os.getenv("SECRET_KEY", "mysecretkey")
SQLALCHEMY_DATABASE_URI = "mssql+pyodbc://Lexie\\SQLEXPRESS/PhotoSphere?driver=ODBC+Driver+18+for+SQL+Server&TrustServerCertificate=yes"

SQLALCHEMY_TRACK_MODIFICATIONS = False
