import re

txt = "The rain in Spain"
x = re.search("^The.*Spain$", txt)

if x:
  print("YES! We have a match!")
else:
  print("No match")

txt = "<td> 2 days 13:11:14.1231</td>"
x = re.search("^<td?>.*days.*?</td>$", txt)

out_txt = re.sub(r"^<td?>.*days", '<td style="background-color:mediumseagreen;>.*?days', txt)
print(x)
print(out_txt)
