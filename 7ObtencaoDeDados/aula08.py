from bs4 import BeautifulSoup
import requests
from collections import Counter
from matplotlib import pyplot as plt


url = "http://quotes.toscrape.com/"

soup = BeautifulSoup(requests.get(url).text, 'html5lib')



small = soup('small')

# for x in small:
#     print(x.text)

author_counts: dict = Counter(a.text
                 for a in small
                )




author = [author
        for author in author_counts.keys()
        ]               

counts = [amount
        for amount in author_counts.values()
        ]  


plt.bar(author, counts, 0.8)


plt.ylabel('Amount')
plt.xlabel('Author')

plt.xticks(rotation=20, fontsize=8)


plt.show()