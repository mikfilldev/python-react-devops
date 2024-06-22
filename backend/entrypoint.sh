#!/bin/sh

DB_PATH="/app/products.db"

if [ -e  "$DB_PATH" ]; then
	echo "$DB_PATH exists."
else
	echo "$DB_PATH does not exist. Running db.py -a to Adds default product data to the database."
	python db.py -a
fi

python app.py --host 0.0.0.0 --port 8000