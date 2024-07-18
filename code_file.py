import pyshorteners
import pyshorteners.shorteners


url = input("Enter your url: ")


def shortenurl(url):

    s = pyshorteners.Shortener()
    short_url = s.tinyurl.short(url)
    print("The shortened url is : ",short_url)


shortenurl(url)    