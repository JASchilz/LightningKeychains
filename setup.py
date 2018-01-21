"""
Scripts to run to set up our database
"""

from model import db, Order

# Create the database tables for our model
db.connect()
db.drop_tables([Order], True)
db.create_tables([Order])



