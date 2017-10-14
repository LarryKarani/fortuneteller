import requests
from bs4 import BeautifulSoup

def horoscope():

	url = ''

	signs = ['aries', 'taurus', 'gemini', 'cancer', 'virgo', 
	'libra', 'scorpio' 'sagitarius', 'capricorn', 'aquarius', 'pisces']

	while True:
		rinput = input(" please input your sign > ")
		sign = str.lower(rinput)
		sign = str.strip(sign)

		if sign not in signs:
			print("please provide a valid sign")
			break

		elif sign in signs:
			for i in range(len(signs)):

				if sign == signs[i]:
					url = "https://www.horoscope.com/us/horoscopes/general/horoscope-general-daily-today.aspx?sign={0}".format(i + 1)

					page = requests.get(url).text
					soup = BeautifulSoup(page, "html.parser")
					horoscope_ = soup.find("div", attrs={"class": "horoscope-content"}).text

					return horoscope_
		

	

print(horoscope())



	