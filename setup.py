"""
Scripts to run to set up our database
"""

from model import db, Order

# Create the database tables for our model
db.connect()
db.create_tables([Order])



