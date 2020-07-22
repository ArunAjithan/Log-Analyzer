from flask import Flask
from flask_cors import CORS
from Database_Operations import DatabaseOperations
app = Flask(__name__)
co_rs = CORS(app)


@app.route('/legacyknowledgebuilder')
def legacyknowledgebuilder():

    t_model = DatabaseOperations()
    t_model.database_fun()

    return 'successefully stored insightfull information to legacy knowledge builder'


@app.route('/AbendAnalysis')
def AbendAnalysis():

    t_model = DatabaseOperations()
    t_model.database_fun()

    return 'successefully stored insightfull information to Abend Analysis'

if __name__ == '__main__':
    app.run(debug=True)
