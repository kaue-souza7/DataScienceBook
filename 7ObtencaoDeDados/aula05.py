
from collections import Counter
from pathlib import Path

FILE_NAME = Path().parent.resolve() / '7ObtencaoDeDados' / 'email.txt'
# print(FILE_NAME)

def get_domain(email_address):
    """separa no '@' e retonra a ultiima parte"""  
    domain = email_address.lower().split('@')[-1]
    return domain

with open(FILE_NAME, 'r') as file:
    domain_counts = Counter(
                            get_domain(line.split("\n")[0])
                            for line in file
                            if '@' in line
    )


# print(domain_counts)

domain_counts = sorted(domain_counts.items(), key=lambda domain: domain[1])

print(domain_counts)

domain_list = []
amount_domain = []

for domain, qtd in domain_counts:
    domain_list.append(domain)
    amount_domain.append(qtd)



from matplotlib import pyplot as plt



plt.bar(domain_list, amount_domain, 0.5)
plt.ylabel('Amount domains')
plt.xlabel('Domains Existents')
plt.xticks(rotation=18, fontsize= 8.5)


plt.show()






