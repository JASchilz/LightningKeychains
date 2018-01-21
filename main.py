import os
import json
import subprocess

from flask import Flask, render_template, request, redirect, url_for, session, send_from_directory
from wtfpeewee.orm import model_form
import wtforms

from model import Order
from lnd import make_invoice, get_info

app = Flask(__name__)

OrderForm = model_form(Order)
del OrderForm.cost_satoshis
del OrderForm.payment_request
del OrderForm.request_hash
del OrderForm.tracking_number
del OrderForm.paid
del OrderForm.expired

identity_pubkey = get_info()['identity_pubkey']

@app.context_processor
def inject_identity_pubkey():
    return {'identity_pubkey': identity_pubkey}

@app.route('/')
def home():
    return render_template('order.jinja2', form=OrderForm())

@app.route('/about/')
def about():
    return render_template('about.jinja2')

@app.route('/orders/', methods=['POST'])
def create_order():
    order = Order()
    
    form = OrderForm(request.form, obj=order)
    
    if form.validate():
        form.populate_obj(order)

        order.keychain_text = order.keychain_text.strip()
        order.cost_satoshis = 100 + 25*len(order.keychain_text)

        invoice = make_invoice(order.cost_satoshis)

        order.payment_request = invoice["pay_req"] 
        order.request_hash = invoice["r_hash"] 
        
        order.save()  
    
        return redirect(url_for('retrieve_order', order_id=order.id))
    else:
        return render_template('order.jinja2', form=form)
        

@app.route('/orders/<order_id>/')
def retrieve_order(order_id):
    order = Order.select().where(Order.id==order_id).get()
    order.update_paid()
    return render_template('detail.jinja2', order=order)

@app.route('/static/<path:path>')
def send_static(path):
    return send_from_directory('static', path)
    

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)

	
