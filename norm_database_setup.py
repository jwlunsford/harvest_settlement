import sys

from datetime import datetime

from sqlalchemy import Column, ForeignKey, Integer, String, Float, Boolean, Date, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref
from sqlalchemy import create_engine

Base = declarative_base()

# end of SQLAlchemy Configuration

class Buyer(Base):
    # represents table Buyer Lookup
    __tablename__ = 'buyer'

    buyer_id = Column(Integer, primary_key=True)
    company_name = Column(String(50), nullable=False, unique=True)
    # the reverse side of this relationship is not needed,
    # so no backref parameter is used
    crews = relationship('Crew')


class Crew(Base):
    # represents table Crew Lookup
    __tablename__ = 'crew'

    crew_id = Column(Integer, primary_key=True)
    crew_name = Column(String(50), nullable=False, unique=True)
    buyer_id = Column(Integer, ForeignKey('buyer.buyer_id'))


class Product(Base):
    # represents table Product Lookup
    __tablename__ = 'product'

    product_id = Column(Integer, primary_key=True)
    product_name = Column(String(10), nullable=False)
    product_descr = Column(String(50), nullable=False)
    contracts = relationship('ContractProduct', back_populates='product')


class ContractProduct(Base):
    # represents a product on a single contract
    __tablename__ = 'contract_product'
    contract_id = Column(Integer, ForeignKey('Contract.contract_id'),
                         primary_key=True)
    product_id = Column(Integer, ForeignKey('Product.product_id'),
                        primary_key=True)
    price = Column(Float, nullable=False)
    product = relationship('Product', back_populates='contracts')
    contract = relationship('Contract', back_populates='products')


class Contract(Base):
    # represents table Contract
    __tablename__ = 'contract'

    contract_id = Column(Integer, primary_key = True)
    ref_num = Column(String(6), nullable = False)
    active = Column(Boolean, nullable = False)
    created_on = Column(DateTime, default=datetime.now)
    updated_on = Column(DateTime, default=datetime.now, onupdate=datetime.now)
    buyer_id = Column(Integer, ForeignKey('buyer.id'))
    buyer = relationship('Buyer')
    products = relationship('Contract_Product', back_populates='contract')
    harvests = relationship('Harvest', backref='contract')


class HarvestType(Base):
    # reprsenets table SaleType Lookup
    __tablename__ = 'harvest_type'

    htype_id = Column(Integer, primary_key = True)
    htype_desc = Column(String(20), nullable = False)
    harvests = relationship("Harvest", backref='htype')


class Harvest(Base):
    # represents table Harvest
    __tablename__ = 'harvest'

    harvest_id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    acres = Column(Integer, nullable=False)
    created_on = Column(DateTime, default=datetime.now)
    updated_on = Column(DateTime, default=datetime.now, onupdate=datetime.now)
    htype_id = Column(Integer, ForeignKey('harvest_type.id'))
    contract_id = Column(Integer, ForeignKey('contract.id'))

    payments = relationship('Payments', backref='harvest')


class Payment(Base):
    # represents table Payment
    __tablename__ = 'payment'

    payment_id = Column(Integer, primary_key=True)
    payment_date = Column(Date, nullable=False)
    payment_tons = Column(Float, nullable=False)
    payment_loads = Column(Integer, nullable=False)
    payment_amt = Column(Float, nullable=False)
    created_on = Column(DateTime, default=datetime.now)
    updated_on = Column(DateTime, default=datetime.now, onupdate=datetime.now)

    harvest_id = Column(Integer, ForeignKey('harvest.harvest_id'))
    dest_id = Column(Integer, ForeignKey('destination.dest_id'))


class Destination(Base):
    # represents table Destination Lookup
    __tablename__ = 'destination'

    dest_id = Column(Integer, primary_key=True)
    dest_name = Column(String(50), nullable=False)
    dest_descr = Column(String(250), nullable=False)

    payments = relationship('Payment', backref='destination')


# create the database
engine = create_engine('sqlite:///Harvest_Settlement.db')

Base.metadata.create_all(engine)












