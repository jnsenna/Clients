from flask import Flask
from flask_restful import Api, Resource, reqparse
import sqlite3
from sqlite3 import Error

# database stored as a dictionary
clients = [
    {
        "first_name": "John",
        "last_name": "Smith",
        "address": "1234 Memory Lane"
    },
    {
        "first_name": "Joe",
        "last_name": "Bob",
        "address": "1234 Alphabet Ave"
    },
    {
        "first_name": "Nick",
        "last_name": "Doe",
        "address": "1010 Binary Street"
    }
]

#client resource for accessing "database"
class Client(Resource):
    # get method
    def get(self, name):
        for client in clients:
            if(name == client["first_name"]):
                return client, 200
        return "Client not found", 404

    def post(self, name):
        parser = reqparse.RequestParser()
        parser.add_argument("last_name")
        parser.add_argument("address")
        args = parser.parse_args()

        for client in clients:
            if(name == client["first_name"]):
                return "client with name {} already exists".format(name), 400

        client = {
            "first_name": name,
            "last_name": args["last_name"],
            "address": args["address"]
        }
        clients.append(client)
        return client, 201

    def put(self, name):
        parser = reqparse.RequestParser()
        parser.add_argument("last_name")
        parser.add_argument("address")
        args = parser.parse_args()

        for client in clients:
            if(name == client["first_name"]):
                client["last_name"] = args["last_name"]
                client["address"] = args["address"]
                return client, 200
        
        client = {
            "first_name": name,
            "last_name": args["last_name"],
            "address": args["address"]
        }
        clients.append(client)
        return client, 201

    def delete(self, name):
        global clients
        clients = [client for client in clients if client["last_name"] != name]
        return "{} is deleted.".format(name), 200

def create_database(filepath):
    try:
        conn = sqlite3.connect(filepath)
        print("Accessed database file at {}.".format(filepath))
        create_table(conn)
        create_clients(conn)
    except Error as e:
        print("Error: ", e)
    return None

def create_table(conn):
    sql = """ CREATE TABLE IF NOT EXISTS clients (
                                        first_name text PRIMARY KEY,
                                        last_name text NOT NULL,
                                        address text NOT NULL
                                    ); """
    try:
        c = conn.cursor()
        c.execute(sql)
    except Error as e:
        print("Error creating: ", e)

def create_clients(conn):
    sql = ''' INSERT INTO clients(first_name,last_name,address)
              VALUES(Joe,Smith,1234 Memory Lane) '''
    try:
        cur = conn.cursor()
        cur.execute(sql)
    except Error as e:
        print("Error inserting: ", e)
 
if __name__ == '__main__':
    app = Flask(__name__)
    api = Api(app)
    
    #create_database(r"C:\\Users\Jessica Senna\Desktop\GitHub\Clients\clients.db")

    api.add_resource(Client, "/client/<string:name>")

    app.run(debug=True)