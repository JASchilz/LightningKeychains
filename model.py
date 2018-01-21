import os

from peewee import Model, CharField, BooleanField, DateTimeField, IntegerField

from playhouse.db_url import connect

from lnd import get_invoice

db = connect(os.environ.get('DATABASE_URL', 'sqlite:///my_database.db'))

class Order(Model):
    keychain_text = CharField(max_length=10)

    contact_email = CharField(max_length=255)

    recipient_name = CharField(max_length=255)
    recipient_address1 = CharField(max_length=255)
    recipient_address2 = CharField(max_length=255, null=True)
    recipient_city = CharField(max_length=255)
    recipient_state = CharField(max_length=255)
    recipient_zip = CharField(max_length=255)

    cost_satoshis = IntegerField()
    
    payment_request = CharField(max_length=255)
    request_hash = CharField(max_length=255)
    paid = BooleanField(default=False)
    expired = BooleanField(default=False)

    tracking_number = CharField(max_length=255, null=True)

    def update_paid(self):
        if not self.paid:
            invoice = get_invoice(self.request_hash)

            self.paid = invoice['settled']

            if self.paid:
                self.save()

