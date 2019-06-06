import requests

URL = 'https://api.rss2json.com/v1/api.json'

PARAMS =  {
	'rss_url': 'http://blog.fossasia.org/author/uday96/feed/',
	'api_key': 'qsmzjtyycc49whsfvf5ikzottxrbditq3burojhd',
	'count': 50
}

r = requests.get(url = URL, params = PARAMS)

data = r.json()

blogs = data['items']

for blog in blogs:
	tags = blog['categories']
	tag_str = ""
	for tag in tags:
		tag_str += "  - "+tag+"\n"
	
	img = blog['thumbnail']
	title = blog['title']
	date = blog['pubDate'].split(" ")[0]
	link = blog['link']
	
	file_str = "---\nlayout: blog\ntype: blog\nimage: %s\ntitle: %s\ndate: %s\npermalink: %s\nlabels:\n%s---" % (img, title, date, link, tag_str)
	file = open(title+".md","w")
	file.write(file_str)
	file.close()