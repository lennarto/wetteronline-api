import requests
import json
import bs4

class WetterOnline:
    def __init__(self, run_tests = False):
        pass
    
    def location_get_url(self, location):
        """
        Returns the specific weather URL of a given `location`, if the `location` is not found returns `False`.
        """

        r = requests.get(f"https://www.wetteronline.de/search?ireq=true&pid=p_search&searchstring={location}", allow_redirects = False)
        #print("-----")
        #print(r.status_code)
        #print(r.headers)
        #print("-----")
        soup = bs4.BeautifulSoup(r.text, "lxml")
        try:
            if soup.find("a").get("href").startswith("/wetter/"):
                return soup.find("a").get("href")#.lstrip("/wetter/")
            else:
                return False
        except:
            return False
    
    def location_autocomplete(self, location):
        """
        Returns a list of autocompletions of a given `location`, if the `location` is not found returns `False`.
        """

        r = requests.get(f"https://www.wetteronline.de/autosuggest?ireq=true&pid=a_autosuggest&s={location}", allow_redirects = False)
        #print("-----")
        #print(r.status_code)
        #print(r.headers)
        #print("-----")
        returnlist = []
        for i in r.json():
            if "id" in list(i):
                returnlist.append(i["n"])
        if returnlist == []:
            return False
        else:
            return returnlist

    
    