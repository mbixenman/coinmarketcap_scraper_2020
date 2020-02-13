from bs4 import BeautifulSoup # gets you cool stuff that we cannot find on our own
import os
import pandas as pd
import glob

if not os.path.exists("parsed_files"):
	os.mkdir("parsed_files")

df = pd.DataFrame()

for one_file_name in glob.glob("html_files/*.html"):
	print("parsing " + one_file_name)
	

	scraping_time = os.path.basename(one_file_name).replace("coinmarketcap","").replace(".html","")
	f = open(one_file_name, "r") # file name is different based on opening
	soup = BeautifulSoup(f.read(), 'html.parser') # beautifulsoup will parse the html file into the soup var
	f.close()
	# soup will extract the text from the html and show it to you
	# this way we can use a lot of functions on the soup variable that we can't do with the html file

	currencies_table = soup.find("tbody") # find tbody tag within soup, save it as currencies_table
	currency_rows = currencies_table.find_all("tr") # finding the tr tag for row, saving as currencies_row

	for r in currency_rows:
		currency_price = r.find("td", {"class":"cmc-table__cell--sort-by__price"}).find("a", {"class":"cmc-link"}).text.replace("$","").replace(",","")
		currency_name = r.find("td", {"class":"cmc-table__cell--sort-by__name"}).find("a",{"class":"cmc-link"}).text
		currency_marketcap = r.find("td",{"class":"cmc-table__cell--sort-by__market-cap"}).find("div",{"class":""}).text.replace("$","").replace(",","")
		currency_supply = r.find("td",{"class":"cmc-table__cell--sort-by__circulating-supply"}).find("div",{"class":""}).text
		currency_link = r.find("td",{"class":"cmc-table__cell--sort-by__name"}).find("a",{"class":"cmc-link"})["href"]
		df = df.append({
				'time': scraping_time,
				'name': currency_name,
				'price': currency_price,
				'marketcap': currency_marketcap,
				'supply': currency_supply,
				'link': currency_link
			}, ignore_index=True)

	

	df.to_csv("parsed_files/coinmarketcap_dataset.csv")

print("parsing complete")
print(df)
# print(f) # if you open f you see some small data on the gateway, not the full html file
# html_content = f.read()
# print(html_content) # this will read the actual html file

# print <td class="cmc-table__cell cmc-table__cell--sortable cmc-table__cell--right cmc-table__cell--sort-by__price"><a href="/currencies/bitcoin/markets/" class="cmc-link">$9,542.93</a></td>