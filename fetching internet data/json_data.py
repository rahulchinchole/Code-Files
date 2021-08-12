import urllib.request 
import json 


def main():
    webUrl = urllib.request.urlopen("https://earthquake.usgs.gov/earthquakes/feed/v1.0/geojson.php")
    #data = str(webUrl.getcode())  
    #dataRead = webUrl.read()
    #print(dataRead)

    data = json.loads(webUrl)

    if "title" in data["metadata"]["title"]:
        print(data["metadata"]["title"])


if __name__ == "__main__":
    main()

