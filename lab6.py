"""1.Описати, які класи стрічок відповідають наступному регулярному виразу. [a-zA-Z]+. Результати перевірити використовуючи nltk.re_show()"""
from __future__ import division
import nltk, re, pprint
nltk.re_show(r'[a-zA-Z]+', 'ghy09ui$56h');
"""2.Описати, які класи стрічок відповідають наступному регулярному виразу. [A-Z][a-z]*. Результати перевірити використовуючи nltk.re_show()"""
nltk.re_show(r'[A-Z][a-z]*', 'ABghy09uDiC$56hfGfrd')
"""3.Описати, які класи стрічок відповідають наступному регулярному виразу. \d+(\.\d+)?. Результати перевірити використовуючи nltk.re_show()"""
nltk.re_show(r'\d+(\.\d+)?', '1.11111')
"""4.Описати, які класи стрічок відповідають наступному регулярному виразу. ([^aeiou][aeiou][^aeiou])*. Результати перевірити використовуючи nltk.re_show()"""
nltk.re_show(r'([^aeiou][aeiou][^aeiou])*','fadmedsid')
"""5.Описати, які класи стрічок відповідають наступному регулярному виразу. \w+|[^\w\s]+.. Результати перевірити використовуючи nltk.re_show()"""
nltk.re_show(r'\w+|[^\w\s]+.','b67_#$6')
"""6.Описати, які класи стрічок відповідають наступному регулярному виразу. p[aeiou]{,2}t  Результати перевірити використовуючи nltk.re_show()"""
nltk.re_show(r'p[aeiou]{,2}t','pt pat piot')
"""7.Написати регулярний вираз, який встановлює відповідність наступному класу стрічок: всі артиклі (a, an, the). """
nltk.re_show(r'\ban?\b|\bthe\b','a, an, the, there')
"""12.Написати регулярний вираз для токенізації такого тексту, як don't до  do та n't? Пояснити  чому цей регулярний вираз не працює: «n't|\w+»."""
print re.findall(r"do|n't", "don't")
"""14.	Прочитати файл допомоги про функцію re.sub() використовуючи help(re.sub) . Використовуючи re.sub напишіть програму видалення HTML розмітки замінивши її на пробіли. """
print re.sub(r'<.*?>', ' ', """<em class="property">exception </em><tt class="descclassname">re.</tt><tt class="descname">error</tt><a class="headerlink">test</a></dt><dd><p>Exception raised when a string passed""")
"""15.Прочитати Додаток А. Дослідити явища описані у Додатку А використовуючи корпуси текстів та метод findall()для пошуку в токенізованому тексті. """
from nltk.corpus import state_union
print re.findall(r'\bI\b|\b[Yy]ou\b|\b[Ss]?[Hh]e\b|\b[Ii]t\b|\b[Ww]e\b|\b[Tt]hey\b', state_union.raw('1945-Truman.txt'))
