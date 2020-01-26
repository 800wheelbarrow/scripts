import bs4, requests, sys

res = requests.get(sys.argv[1])
soup = bs4.BeautifulSoup(res.text, "html.parser")
elems = soup.select('html body div.main div.init-view div.checkout div.complete div.grid-container div.grid-x.grid-margin-x.grid-margin-y div.cell.small-12.large-9 div.grid-x.grid-margin-x.grid-margin-y div.cell.small-12 div.cartPresentation div.cartPresentation__items div.cartPresentation__item div.grid-x.grid-margin-x.grid-margin-y div.cell.small-8.medium-9.large-10 div.grid-x.grid-margin-x div.cell.small-12.large-6.cartPresentation__header a.cartPresentation__productName')
elems2 = soup.select('html body div.main div.init-view div.checkout div.complete div.grid-container div.grid-x.grid-margin-x.grid-margin-y div.cell.small-12.large-9 div.grid-x.grid-margin-x.grid-margin-y div.cell.small-12 div.cartPresentation div.cartPresentation__items div.cartPresentation__item div.grid-x.grid-margin-x.grid-margin-y div.cell.small-8.medium-9.large-10 div.grid-x.grid-margin-x div.cell.small-12.medium-4.large-2 div.cartPresentation--mobileHeader div.cartPresentation__total')

for val in elems:
	print(val.text.strip())
for val in elems2:
	print(val.text.strip())
