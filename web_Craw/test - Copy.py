from urllib.request import urlopen
import re

url = "https://vnexpress.net/giao-duc"
page = urlopen(url)

html_bytes = page.read()
html = html_bytes.decode("utf-8")
title_index = html.find("<title>")
print(title_index)
start_index = title_index + len("<title>")
end_index = html.find("</title>")
title = html[start_index:end_index]

print(title)



pattern = "<title.*?>.*?</title.*?>"
match_results = re.search(pattern, html, re.IGNORECASE)
title = match_results.group()
title = re.sub("<.*?>", "", title) # Remove HTML tags

print(title)