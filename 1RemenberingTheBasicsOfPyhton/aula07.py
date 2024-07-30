import re

str_ = 'milk'
expression = 'FXE1A18'
cpf = '424.777.308-24'

match_ = re.match('m', str_)
search_ = re.search('k', str_)
split_ = len(re.split('l', str_)) == 2
sub_ = re.sub('[0-9]', '*', expression) == 'FXE*A**'
re_sub = re.sub('[.-]', '', cpf)


print(all
      ([
          match_,
          search_,
          split_,
          sub_,

    ]))

