import webbrowser,requests,bs4

print("ÕıÔÚËÑË÷.....")

res = requests.get('http://goole.com/search?q=¡¯+' '.join(sys.argv[1:]')
res.raise_for_status()

soup = bs4.BeautifulSoup(res.text)

list =soup.select('.r a')

num = min(4,len(list))
for i in range(num):
    webbrowser.open('')