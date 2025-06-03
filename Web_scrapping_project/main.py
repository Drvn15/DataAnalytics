from bs4 import BeautifulSoup

with open("Bike_retail.html", "r", encoding="utf-8") as file:
    html_content = file.read()

soup = BeautifulSoup(html_content, 'lxml')

bikes = soup.find_all('div', class_='Bike')


for bike in bikes:
    Company = bike.find('h2', class_='Company').text
    Model = bike.find('p', class_='Model').text
    Price = bike.find('p', class_='Price').text
    print(f"Company: {Company}\nModel: {Model}\nPrice: {Price}\n{'-'*30}")
