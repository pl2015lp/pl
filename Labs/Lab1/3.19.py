Python 2.7.3 (default, Apr 10 2012, 23:31:26) [MSC v.1500 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> #ѕеретвор≥ть стр≥чку msg на список стр≥чок, кожна з €ких в≥дпов≥даЇ одному слову використовуючи split() оператор без символа розд≥ленн€ та наступними символами розд≥ленн€: подв≥йн≥ лапки, табул€ц≥€, посл≥довн≥сть проб≥л≥в, посл≥довн≥сть табул€ц≥й та проб≥л≥в.
>>> 
>>> msg = "Olha Turchyniak"
>>> msg.split("")

Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    msg.split("")
ValueError: empty separator
>>> msg.split(" ")
['Olha', 'Turchyniak']
>>> msg.cplit("	")

Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    msg.cplit("	")
AttributeError: 'str' object has no attribute 'cplit'
>>> msg.split("	")
['Olha Turchyniak']
>>> msg.split("   ")
['Olha Turchyniak']
>>> msg.split("     			")
['Olha Turchyniak']
>>> 
