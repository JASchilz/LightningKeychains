# Lighting Keychains

A demonstration [lightning network](https://lightning.network/) store, using the [LND](https://github.com/lightningnetwork/lnd) lightning client, written in Python using [Flask](https://github.com/pallets/flask) and [peewee](https://github.com/coleifer/peewee). Currently running on testnet3 and viewable at [https://lightningkeychains.com](https://lightningkeychains.com): try it out (it could be down)!

With this project I hope to demonstrate how easy it is to integrate a command line lightning network client with your own favorite code base. In particular, the file [lnd.py](lnd.py) provides the Python functions which interact with the LND client. Creating a slick user interface is not in the scope of this project.

## Requirements

In addition to the package requirements listed in [requirements.txt](requirements.txt), you must also have a functioning LND client. LND must be installed, connected to the network, and available at the command line the store can create invoices and receive payments. If you encounter difficulty registering payments in the web store, first check that you are able to receive payments at the command line using `lncli`.

This project requires Python3.

## Configuration

Looking at the [model.py](model.py) file, you can provide a `DATABASE_URL` environment variable to change the backing database store from SQLite to any database supported by the peewee ORM.

## Installation/Running

Supposing that LND is running and connected to the network, you can download and run the web store with:
```
$ git clone git@github.com:JASchilz/LightningKeychains.git
$ cd LightningKeychains
$ pip3 install -r requirements.txt   # Might want to do this inside a virtual environment.
$ python3 setup.py                   # Creates the database tables.
$ python3 main.py
```

On subsequent runs, you should only have to run `python3 main.py`.

On your machine, you might invoke Python3 and Pip3 using the commands `python` and `pip`, but in any case be sure that you are running Python v3.

Documenting how to deploy to a production environment is outside the scope of this project. For more information, you can read deployment instructions from Flask and peewee.

## Further Development

When the LND opens to mainnet, I may roll the [https://lightningkeychains.com](https://lightningkeychains.com) (it could be down) store to mainnet and begin selling actual 3D printed keychains. To support that, I would program in e-mail sending and an administrative interface that I could use to process orders.
