import json, threading, tls_client, time
from bs4 import BeautifulSoup
from core.modules.logging import log

class Lookup:
    def __init__(self):
        self.prog = 0
        self.sites = json.load(open("core/dependencies/sites.json"))
        self.start_time = 0
        self.time_taken = 0
        self.result = {}
        self.stats  = {}

    def search(self, url, type, code, site):
        session = tls_client.Session()
        try:
            response = session.get(
                    url
                )

            if type == "status":
                if response.status_code == code:
                    self.result[site] = {
                        "url"   : url,
                        "type"  : type,
                        "code"  : str(code),
                        "extra" : {}
                    }
            elif type == "site-content":
                if code not in str(response.content):
                    self.result[site] = {
                        "url"   : url,
                        "type"  : type,
                        "code"  : str(code),
                        "extra" : {}
                    }
            elif type == "title-content":
                soup = BeautifulSoup(response.content, "html.parser")

                title = soup.find("title")

                if not title:
                    pass
                if code not in str(title):
                    self.result[site] = {
                        "url"   : url,
                        "type"  : type,
                        "code"  : str(code),
                        "extra" : {}
                    }
            else:
                log("error", "Invalid type provided")

        except Exception as e:
            log("error", e)
            pass
        self.prog += 1

    def lookup(self, username):
        self.start_time = time.time()
        for site in self.sites:
            site_info = self.sites[site]
            
            link  = site_info.get("link")
            type_ = site_info.get("type")
            code  = site_info.get("code")

            threading.Thread(
                target=self.search, args=[
                    link.format(username),
                    type_,
                    code,
                    site
                ]
            ).start()

        while self.prog < len(self.sites):
            pass
        
        self.time_taken = time.time() - self.start_time

        self.stats = {
            "sites_checked" : len(self.sites),
            "sites_found"   : len(self.result),
            "time_taken"    : self.time_taken
        }

        info = {
            "stats" : self.stats,
            "result" : self.result
        }

        return info

