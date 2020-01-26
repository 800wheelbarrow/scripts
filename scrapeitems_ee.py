import bs4, requests, re, sys

res = requests.get(sys.argv[1])
soup = bs4.BeautifulSoup(res.text, "html.parser")
elemname = soup.find_all(class_='partDetailLink')

for val in elemname:
	print(val.text.strip())
for prices in soup.find_all('td', string=re.compile("\$.+")):
	print(prices.text.strip())
