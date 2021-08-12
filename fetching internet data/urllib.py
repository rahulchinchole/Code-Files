# ufile = urllib.urlopen(url) -- returns a file like object for that url

# text = ufile.read() -- can read from it, like a file (readlines() etc. also work)

# info = ufile.info() -- the meta info for that request. info.gettype() is the mime type, e.g. 'text/html'

# baseurl = ufile.geturl() -- gets the "base" url for the request, which may be different from the original because of redirects

# urllib.urlretrieve(url, filename) -- downloads the url data to the given file path

# urlparse.urljoin(baseurl, url) -- given a url that may or may not be full, and the baseurl of the page it comes from, return a full url. Use geturl() above to provide the base url.


from typing import Text
import urllib.request

# def main():
#     webUrl = urllib.request.urlopen("https://www.google.com")
#     print("Url code: " + str(webUrl.getcode()))
#     data = webUrl.read()
#     print(data)

# if __name__ == "__main__":
#     main()

## Given a url, try to retrieve it. If it's text/html,
## print its base url and its text.

def main():
    filename = "retrieved.txt"
    ufile = urllib.request.urlopen("https://developers.google.com/edu/python/utilities")
    info = ufile.info()
    print(info)
    if info.get_content_type() == "text/html":
        print("Base URL: " + ufile.geturl())
        text = ufile.read()
        print(text)
       

if __name__ == "__main__":
    main()



