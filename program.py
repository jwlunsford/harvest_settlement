from flask import Flask
app = Flask(__name__)

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Buyer, Crew, Destination, Product, ProductRate, Contract, SaleType, Sale, Settlement

# connect the Database
engine = create_engine('sqlite:///HarvestContracts.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()

# create the Routes

@app.route('/')
@app.route('/index')
def index():
    return 'Main landing page for the App'



@app.route('/contracts')
def contracts():
    # view active contracts in the database



if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=9000)

