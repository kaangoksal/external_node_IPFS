from flask import Flask
from flask_cors import CORS, cross_origin
from flask_sqlalchemy import SQLAlchemy

app = Flask('flask_server')
CORS(app)

# Database Settings
# ================================================================
#
# postgresql_username = "db_user"
# postgresql_password = "password"
# postgresql_host = "localhost"
# databse_name = "flask_server_db"
#
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
#
# app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://' + postgresql_username + ':' + postgresql_password + '@' + postgresql_host + '/' + databse_name
#
# db = SQLAlchemy(app)

# ================================================================

# CORS plus address settings
# ================================================================

app.config['server_addr'] = "http://www.example.com"
app.config['server_port'] = 5001
app.config['server_path'] = app.config["server_addr"] + ":" + app.config["server_port"]

# ================================================================

@app.after_request
def apply_caching(response):
   response.headers["Access-Control-Allow-Credentials"] = "true"
   response.headers["Access-Control-Allow-Origin"] = app.config['server_path']
   response.headers["Access-Control-Allow-Headers"] = "authorization, content-type"
   return response
