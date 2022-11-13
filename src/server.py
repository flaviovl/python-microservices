import datetime
import os

import jwt
from flask import Flask, request
from flask_mysqldb import MySQL

server = Flask(__name__)
mysql = MySQL(server)

# Config DB MySQL
server.config["MYSQL_HOST"] = os.environ.get("MYSQL_HOST")               # in terminal-> $ export MYSQL_HOST=localhost
server.config["MYSQL_USER"] = os.environ.get("MYSQL_USER")               # in terminal-> $ export MYSQL_USER=
server.config["MYSQL_PASSWORD"] = os.environ.get("MYSQL_PASSWORD")       # in terminal-> $ export MYSQL_PASSWORD=
server.config["MYSQL_DB"] = os.environ.get("MYSQL_DB")                   # in terminal-> $ export MYSQL_DB=
server.config["MYSQL_PORT"] = os.environ.get("MYSQL_PORT")               # in terminal-> $ export MYSQL_PORT=


# Criar rota login
@server.route("/login", methods=["POST"])
def login():
    auth = request.authorization
    
    if not auth:
        return ("missing credentials", 401)


    cur = mysql.connection.cursor()
    res = cur.execute(
        "SELECT email, password FROM user WHERE email=%s", (auth.username,)
    )

    
    if res > 0:
        user_row = cur.fetchone()
        email = user_row[0]
        password = user_row[1]
        
        if auth.username != email or auth.password != password:
            return ("invalid credentials", 401)
        
        else:
            return createJWT(auth.username, os.environ.get("JWT_SECRET"), True)
    else:
        return ("invalid credentials", 401)




if __name__ == "__main__":
    print("Rodando")
    # server.run(host="0.0.0.0", port=5000)
