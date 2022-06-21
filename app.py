from flask import Flask, render_template, make_response, request
from flask_restful import Api, Resource, reqparse
import mysql.connector
import jwt
import base64

app = Flask(__name__)
api = Api(app)

reg_req_parse = reqparse.RequestParser()
reg_req_parse.add_argument("username", type=str, help="Username")
reg_req_parse.add_argument("password", type=str, help="Password")
reg_req_parse.add_argument("email", type=str, help="Email")

lookup_req_parse = reqparse.RequestParser()
lookup_req_parse.add_argument("UID", type=int, help="User ID")

class Register(Resource):
    def post(self):
        args = reg_req_parse.parse_args()
        cookies = request.cookies
        request_username = args.get("username")
        request_password = args.get("password")
        request_email = args.get("email")
        
        try:
            
            mydb = mysql.connector.connect(
                host="localhost",
                user=jwt.decode(base64.b64decode(cookies.get("Token")), "", algorithms=['HS256']).get("db_user"),
                password=jwt.decode(base64.b64decode(cookies.get("Token")), "", algorithms=['HS256']).get("password"),
                database=jwt.decode(base64.b64decode(cookies.get("Token")), "", algorithms=['HS256']).get("db")
            )
            cursor = mydb.cursor()
            cursor.execute("select count(*) from users;")
            uid = cursor.fetchall()[0][0] + 1
            cursor.execute("select username from users where username='{}';".format(request_username))
            count = len(cursor.fetchall())
            if count > 0:
                mydb.close()
                return {"status": "User already exists!"}, 500

            cursor.execute("insert into users (username, password, email, id) values ( '{}', '{}', '{}', {});".format(request_username, request_password, request_email, uid))
            mydb.commit()
            mydb.close()

            return {"username": request_username, "password": request_password, "email": request_email, "id": uid, "cookies": cookies, "status": "Successfully registered" }
        except:
            return{"status": "Some error occured!"}, 500
            
class Lookup(Resource):
    def post(self):
        args = lookup_req_parse.parse_args()
        uid = args.get("UID")
        cookies = request.cookies
        try:
            mydb = mysql.connector.connect(
                host="localhost",
                user=jwt.decode(base64.b64decode(cookies.get("Token")), "", algorithms=['HS256']).get("db_user"),
                password=jwt.decode(base64.b64decode(cookies.get("Token")), "", algorithms=['HS256']).get("password"),
                database=jwt.decode(base64.b64decode(cookies.get("Token")), "", algorithms=['HS256']).get("db")
            )
            cursor = mydb.cursor()
            cursor.execute("select username from users where id={}".format(uid))
            usernameArr = cursor.fetchall()
            mydb.close()
            if len(usernameArr) == 1:
                return {"username": usernameArr[0][0], "status": "exists"}
            elif len(usernameArr) == 0:
                return {"status":"We do not have a Wrlder number {} :(((".format(uid)}, 500
        except:
            return {"status": "Some error occured!"}, 500
            
api.add_resource(Register, "/api/register")
api.add_resource(Lookup, "/api/lookup")

@app.route('/')
def index():
    resp = make_response(render_template('index.html'))
    resp.set_cookie('Token', "ZXlKaGJHY2lPaUpJVXpJMU5pSXNJblI1Y0NJNklrcFhWQ0o5LmV5SmtZaUk2SW0xaGFXNGlMQ0prWWw5MWMyVnlJam9pY205dmRDSXNJbkJoYzNOM2IzSmtJam9pVTJWamRYSmxVR0Z6YzNkdmNtUXhNak1pZlEuYmViZG12eDYwbDV5eE5TSHE4dF9OUUR0ZllvNFhEdFFaNkdFQjZ5UDNfVQ==")
    return resp

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True, port=5000)
