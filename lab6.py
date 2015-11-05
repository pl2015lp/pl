"""1.�������, �� ����� ������ ���������� ���������� ����������� ������. [a-zA-Z]+. ���������� ��������� �������������� nltk.re_show()"""
from __future__ import division
import nltk, re, pprint
nltk.re_show(r'[a-zA-Z]+', 'ghy09ui$56h');
"""2.�������, �� ����� ������ ���������� ���������� ����������� ������. [A-Z][a-z]*. ���������� ��������� �������������� nltk.re_show()"""
nltk.re_show(r'[A-Z][a-z]*', 'ABghy09uDiC$56hfGfrd')
"""3.�������, �� ����� ������ ���������� ���������� ����������� ������. \d+(\.\d+)?. ���������� ��������� �������������� nltk.re_show()"""
nltk.re_show(r'\d+(\.\d+)?', '1.11111')
"""4.�������, �� ����� ������ ���������� ���������� ����������� ������. ([^aeiou][aeiou][^aeiou])*. ���������� ��������� �������������� nltk.re_show()"""
nltk.re_show(r'([^aeiou][aeiou][^aeiou])*','fadmedsid')
"""5.�������, �� ����� ������ ���������� ���������� ����������� ������. \w+|[^\w\s]+.. ���������� ��������� �������������� nltk.re_show()"""
nltk.re_show(r'\w+|[^\w\s]+.','b67_#$6')
"""6.�������, �� ����� ������ ���������� ���������� ����������� ������. p[aeiou]{,2}t  ���������� ��������� �������������� nltk.re_show()"""
nltk.re_show(r'p[aeiou]{,2}t','pt pat piot')
"""7.�������� ���������� �����, ���� ���������� ���������� ���������� ����� ������: �� ������ (a, an, the). """
nltk.re_show(r'\ban?\b|\bthe\b','a, an, the, there')
"""12.�������� ���������� ����� ��� ���������� ������ ������, �� don't ��  do �� n't? ��������  ���� ��� ���������� ����� �� ������: �n't|\w+�."""
print re.findall(r"do|n't", "don't")
"""14.	��������� ���� �������� ��� ������� re.sub() �������������� help(re.sub) . �������������� re.sub �������� �������� ��������� HTML ������� �������� �� �� ������. """
print re.sub(r'<.*?>', ' ', """<em class="property">exception </em><tt class="descclassname">re.</tt><tt class="descname">error</tt><a class="headerlink">test</a></dt><dd><p>Exception raised when a string passed""")
"""15.��������� ������� �. �������� ����� ������ � ������� � �������������� ������� ������ �� ����� findall()��� ������ � ������������� �����. """
from nltk.corpus import state_union
print re.findall(r'\bI\b|\b[Yy]ou\b|\b[Ss]?[Hh]e\b|\b[Ii]t\b|\b[Ww]e\b|\b[Tt]hey\b', state_union.raw('1945-Truman.txt'))
