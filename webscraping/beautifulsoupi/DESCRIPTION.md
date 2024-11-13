# Beautifulsoup4

Using the requests library we are capable of getting website information that we can then manipulate in our programs. However, as you witnessed in the third requests challenge, the data we get from websites is filled with HTML tags that taints the data we really want to look at. Thankfully someone created a library called `beautifulsoup4` that allows us to scan through this data, find particular tags, and grab the data we really want.

We are only going to touch the bare surface of `beautifulsoup` in these beginner challenges. To dive deeper visit the [Beautiful Soup Documentation](https://www.crummy.com/software/BeautifulSoup/bs4/doc/) page.

## The Basics
```python
from bs4 import BeautifulSoup

# Create a 'Soup' object that we use to parse HTML
soup = BeautifulSoup(WEBSITE_DATA, 'html.parser')

# We can use this soup object to identify all
# occurances of a particular tag.

links = soup.find_all('a') # This returns a list that contains ALL anchor tags.

# Here is how you could go about scraping all
# of the actual links from those anchor tags.
for link in links:
	print(link.get('href'))

```
