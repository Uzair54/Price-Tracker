import requests
from bs4 import BeautifulSoup
import smtplib
import csv
from datetime import date

def check_price():
    csv_file=open('cms_scraper.csv','w')
    csv_writer = csv.writer(csv_file)
    csv_writer.writerow(['date','price'])
    source = requests.get('https://www.extra.com/en-om/white-goods/-refrigerators/large/samsung-fridge-top-mount-freezer-inverter-600-0l-snow-white/p/100079270').text
    soup= BeautifulSoup(source,'lxml')
    title = soup.find('span',class_='promotion-title-text').text
    price = soup.find('div',class_='c_product-price-current').text
    price=price.split('.')[0]
    print(title)
    price=price.strip()
    converted_price=float(price[0:3])
    today = str(date.today())
    csv_writer.writerow([today,converted_price])
    if(converted_price<180):
        send_mail()
    csv_file.close()

def send_mail():
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login('muzair0510@gmail.com','Uzair@358')
    subject = 'Price fell down!'
    body = 'Check the extra link https://www.extra.com/en-om/white-goods/-refrigerators/large/samsung-fridge-top-mount-freezer-inverter-600-0l-snow-white/p/100079270'
    message = f"Subject : {subject}\n\n{body}"
    server.sendmail(
        'muzair0510@gmail.com',
        'muzair0510@gmail.com',
        message
    )
    print('HEY Email has been sent!')
    server.quit()

check_price()