
import psycopg2
from flask import Flask
from flask_restful import Resource, Api

# [TODO] Please add your postgres db url here
url = "postgresql://anushabharat:pass@localhost:5432"
# connect to postgres db
connection = psycopg2.connect(url)
# Initialise flask app
app = Flask(__name__)
api = Api(app)

class HttpRequests(Resource):
    # Method to get all companies associated with a given operator
    @app.route("/companies/<operator_name>",  methods=['GET'])
    def get_companies(operator_name):
        cursor = connection.cursor()
        # query the company db for all companies which have a given operator name
        query = "select nm_fantasia from company_db where nm_socio = %s;"
        cursor.execute(query, (operator_name,))
        companies = cursor.fetchall()
        return companies

    # Method to get all operators associated with a given company
    @app.route("/operators/<company_name>",  methods=['GET'])
    def get_operators(company_name):
        cursor = connection.cursor()
        # query the company db for all operators which have a given company name
        query = "select nm_socio from company_db where nm_fantasia = %s;"
        cursor.execute(query, (company_name,))
        operators = cursor.fetchall()
        return operators
    
    # Method to get all companies connected to a given company via shared operators
    @app.route("/all_companies/<company_name>",  methods=['GET'])
    def get_all_associated_companies(company_name):
        cursor = connection.cursor()
        # query the company db to get the operator of a given company
        query_1 = "select nm_socio from company_db where nm_fantasia = %s;"
        cursor.execute(query_1, (company_name,))
        operator = cursor.fetchone()
        # query the company db to get all companies which have the same operator
        query_2 = "select nm_fantasia from company_db where nm_socio = %s;"
        cursor.execute(query_2, (operator,))
        companies = cursor.fetchall()
        return companies

# Run the flask app
if __name__ == '__main__':
    app.run()  
