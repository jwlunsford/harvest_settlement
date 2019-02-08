import sys

from sqlalchemy import Column, ForeignKey, Integer, String, Float, Boolean, Date

from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy.orm import relationship

from sqlalchemy import create_engine

Base = declarative_base()

# end of SQLAlchemy Configuration

class Buyer(Base):
    # represents table Buyer
    __tablename__ = 'buyer'

    id = Column(Integer, primary_key = True)
    company = Column(String(50), nullable = False)


class Crew(Base):
    # represents table Crew Lookup
    __tablename__ = 'crew'

    id = Column(Integer, primary_key = True)
    name = Column(String(50), nullable = False)


class Destination(Base):
    # represents table Destination Lookup
    __tablename__ = 'destination'

    id = Column(Integer, primary_key = True)
    name = Column(String(50), nullable = False)
    location = Column(String(50), nullable = False)


class Product(Base):
    # represents table Product Lookup
    __tablename__ = 'product'

    id = Column(Integer, primary_key = True)
    name = Column(String(10), nullable = False)
    description = Column(String(50), nullable = False)


class ProductRate(Base):
    # represents linking table betwen product and contract
    __tablename__ = 'product_rate'

    id = Column(Integer, primary_key = True)
    product_price = Column(Float, nullable = False)
    product_id = Column(Integer, ForeignKey('product.id'))
    contract_id = Column(Integer, ForeignKey('contract.id'))
    product = relationship('Product')
    contract = relationship('Contract')


class Contract(Base):
    # represents table Contract
    __tablename__ = 'contract'

    id = Column(Integer, primary_key = True)
    ref_num = Column(String(6), nullable = False)
    active = Column(Boolean, nullable = False)
    buyer_id = Column(Integer, ForeignKey('buyer.id'))
    buyer = relationship('Buyer')


class SaleType(Base):
    # reprsenets table SaleType Lookup
    __tablename__ = 'sale_type'

    id = Column(Integer, primary_key = True)
    type_desc = Column(String(20), nullable = False)



class Sale(Base):
    # represents table Sale
    __tablename__ = 'sale'

    id = Column(Integer, primary_key = True)
    name = Column(String(50), nullable = False)
    acres = Column(Integer, nullable = False)
    type_id = Column(Integer, ForeignKey('sale_type.id'))
    contract_id = Column(Integer, ForeignKey('contract.id'))
    sale_type = relationship(SaleType)
    contract = relationship(Contract)



class Settlement(Base):
    # represents table Settlement
    __tablename__ = 'settlement'

    id = Column(Integer, primary_key = True)
    date = Column(Date, nullable = False)
    net_tons = Column(Float, nullable = False)
    price = Column(Float, nullable = False) # needs to be a dynamic lookup
    loads = Column(Integer, nullable = False)
    total = Column(Float, nullable = False)
    sale_id = Column(Integer, ForeignKey('sale.id'))
    dest_id = Column(Integer, ForeignKey('destination.id'))
    prod_rate_id = Column(Integer, ForeignKey('product_rate.id'))
    crew_id = Column(Integer, ForeignKey('crew.id'))
    sale = relationship(Sale)
    dest = relationship(Destination)
    prod_rate = relationship(Product)
    crew = relationship(Crew)



# create the database
engine = create_engine('sqlite:///HarvestContracts.db')

Base.metadata.create_all(engine)












