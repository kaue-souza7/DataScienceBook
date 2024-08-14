
from dateutil.parser import parse
import json, requests
from collections import Counter


endpoint = 'https://api.github.com/users/joelgrus/repos'
repos = json.loads(requests.get(endpoint).text)

# for x in repos:
#     print(x['created_at'])

dates = [parse(repo["created_at"]) for repo in repos]

month_counts = Counter(date.month for date in dates)
weekday_counts = Counter(date.weekday() for date in dates)

# print(weekday_counts)


last_5_repositories = sorted(repos,
                            key= lambda r: r['created_at'],
                            reverse=True
                        )[:5]

# print(last_5_repositories)

last_5_languages = [repo['language']
                    for repo in last_5_repositories
]

print(last_5_languages)