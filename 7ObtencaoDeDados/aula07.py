from bs4 import BeautifulSoup
import requests

html = requests.get("http://www.example.com").text
soup = BeautifulSoup(html, 'html5lib')

first_paragraph = soup.p.text # type: ignore
print(first_paragraph)

# first_paragraph_id = soup.p['id'] # surge KeyError se não tiver 'id'
first_paragraph_id2 = soup.p.get('id') # type: ignore
# print(first_paragraph_id2) # None


# Você pode obter múltiplas marcações ao mesmo tempo:
all_paragraphs = soup.find_all('p') # ou apenas soup('p')
paragraphs_with_ids = [p
                        for p in soup('p')
                        if soup.p.get('id') # type: ignore
                        ]

print(paragraphs_with_ids)



# Frequentemente, você encontrará marcações com uma class específica:
important_paragraphs = soup('p', {'class': 'important'})
important_paragraphs2 = soup('p', 'important')
important_paragraphs3 = [p
                            for p in soup('p')
                            if 'important' in p.get('class', [])
                        ]


# Você pode combiná-los para implementar uma lógica mais elaborada. Por
# exemplo, se você quiser encontrar todo elemento <span> que está contido dentro
# de um elemento <div>, você poderia fazer assim:

spans_inside_divs = [
                    span
                    for div in soup('div')
                    for span in div('span')
                ]

print(spans_inside_divs)

