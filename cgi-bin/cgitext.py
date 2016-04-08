#!/Library/Frameworks/Python.framework/Versions/3.5/bin/python3
# -*- coding: utf-8 -*-

import cgi
import locale
locale.setlocale(locale.LC_ALL, '')

html_top = """
<!DOCTYPE html>
<head>
	<meta charset="UTF-8">
	<title>計算結果</title>
	<style type="text/css">
		header {
		}
		div#kekka {
			margin-top:50px;
			margin-left:100px;
		}
		span#suuzi {
			font-size:6em;
			font-coler:red;
		}
		div#true {
			margin-top:50px;
			margin-left:150px;
		}
	</style>

</head>
<body>
<header>
	<h1>計算結果</h1>
</header>
"""
html_kekka = """
<div id="kekka">
残り<span id="suuzi">%s</span>円です。
</div>
"""
html_true = """
<div id="true">
まだ超えてません。<br>
残り<span id="suuzi">%s</span>働けますね。


</div>
"""
html_false = """
あらら、超えちゃいましたね。
"""
html_botom = """
</body>
</html>
"""

form = cgi.FieldStorage()			#フォームの値をformに取得
#各月をint型で格納
jan = int(form.getvalue('1',''))
feb = int(form.getvalue('2',''))
mar = int(form.getvalue('3',''))
apr = int(form.getvalue('4',''))
may = int(form.getvalue('5',''))
jun = int(form.getvalue('6',''))
jul = int(form.getvalue('7',''))
aug = int(form.getvalue('8',''))
sep = int(form.getvalue('9',''))
oct = int(form.getvalue('10',''))
nov = int(form.getvalue('11',''))
dec = int(form.getvalue('12',''))
kyuuryo= int(form.getvalue('kyuuryo',''))
which = form.getvalue('scheme','')


#残りの額を計算
sum=jan+feb+mar+apr+may+jun+jul+aug+sep+oct+nov+dec
koujo=1030000-sum
nokori=int(koujo/kyuuryo)
koujo=locale.currency(koujo,False,True)	#3ケタごとにカンマを付ける


#残りの時間を計算
if which == "hourly" :
	text = str(nokori)+"時間"
if which == "daily" :
	text = str(nokori)+"日"


print(html_top)
print(html_kekka % str(koujo))
if nokori > 0 :
	print(html_true % text)
else :
	print(html_false)

print(html_botom)
