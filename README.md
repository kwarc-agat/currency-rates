# Enterprise profits

Sample visualisation of sales records in given time range for bussiness analysis purpose.

## Features

- interactive data chart
- API to consume
- available data:
    - sample sales data in USD and PLN
    - USD/PLN rate based on NBP API

## Technologies

- Python
    - Django
    - sqlite3
    - request
- JavaScript, Vue
- HTML
- Bootstrap

## Web App Demo

![alt text](https://github.com/kwarc-agat/currency-rates/blob/master/demo_images/img_1.jpg)

![alt text](https://github.com/kwarc-agat/currency-rates/blob/master/demo_images/img_2.jpg)

![alt text](https://github.com/kwarc-agat/currency-rates/blob/master/demo_images/img_3.jpg)

## Getting started

```sh
git clone https://github.com/kwarc-agat/skryptowe20.git
```
Navigate to project directory and create virtual environment:

```sh
python -m venv env
env\Scripts\activate
```

Install dependancies:

```sh
pip install django
pip install djangorestframework
```

Migrate the database and run server

```sh
python manage.py migrate
python manage.py runserver
```

## API Demo

(after running the server as described above type following URLs in your browser)

Browsing all currency and sales records in the database:

```sh
http://localhost:8000/
http://localhost:8000/currency/
http://localhost:8000/sales/
```
Get USD exchange rate from the date range

```sh
http://localhost:8000/rate/31-10-2013/01-10-2013
http://localhost:8000/rate/15-08-2014
```

Get sales value in PLN and USD from the date range:

```sh
http://localhost:8000/sale/17-03-2013/05-03-2013
http://localhost:8000/sale/08-08-2012
```


Get "unrecognized url" response when date range is not in the database

```sh
http://localhost:8000/rate/31-10-2020
http://localhost:8000/sale/11-12-2002
```

Number of requests is limited to 10 per minute per user - exceeding the limit results in "404 Page Not Found"
