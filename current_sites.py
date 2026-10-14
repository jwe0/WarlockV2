import json
from datetime import datetime

sites_ = []
types = []
codes = []
links = []

file = [
    "# Warlock V2",
    "> Upgraded version of Warlock by me",
    "Simple social media recon tool similar to sherlock"
    
    "# All supported sites and there info", 
    
    
    "> Auto generated via [current_sites.py]", 
    
    
    
    ""]

def main():
    sites = json.load(open("core/dependencies/sites.json"))

    for site in sites:
        info = sites[site]

        link = info["link"]
        type = info["type"]
        code = info["code"]

        sites_.append(site)
        links.append(link)
        types.append(type)
        codes.append(code)


    sites_pad = max(len(site) for site in sites_)
    links_pad = max(len(link) for link in links) 
    types_pad = max(len(type) for type in types)
    codes_pad = max(len(str(code)) for code in codes)

    def generate_stats():
        
        types_ = {
            "status"        : 0,
            "site-content"  : 0,
            "title-content" : 0
        }

        sites = len(links)

        for i in range(len(links)):
            if types[i] == "status":
                types_["status"] += 1
            elif types[i] == "title-content":
                types_["title-content"] += 1
            elif types[i] == "site-content":
                types_["site-content"] += 1
        time_created = datetime.now().strftime(
            "%H:%M:%s"
        )
        date_created = datetime.now().strftime(
            "%d/%m/%Y"
        )

        return [
            "## Info",
            f"- Total links: `{str(sites)}`",
            "### Link types",
            f"- Status code: `{types_["status"]}`",
            f"- Site content: `{types_["site-content"]}`",
            f"- Title content: `{types_["title-content"]}`",
            "### Created",
            f"- Time: `{time_created}`",
            f"- Date: `{date_created}`",
            "## Sites table",
            "```"
        ]        


    stats = generate_stats()
    for stat in stats:
        file.append(stat)

    def line():
        info = f"+{"-" * (sites_pad + 4)}+{"-" * (types_pad + 4)}+{"-" * (codes_pad + 4)}+{"-" * (links_pad + 4)}+"
        file.append(info)
        print(info)

    line()
    info = f"| Sites {" " * (sites_pad - len("Sites") + 1)} | Type {" " * (types_pad - len("Type") + 1)} | Code {" " * (codes_pad - len("Code") + 2)}| Link {" " * (links_pad - len("Link") + 2)}|"
    file.append(info)
    print(info)
    line()

    for i in range(len(sites_)):
        info = f"| {sites_[i]} {" " * (sites_pad - len(sites_[i]) + 2)}| {types[i]} {" " * (types_pad - len(types[i]) + 2)}| {codes[i]} {" " * (codes_pad - len(str(codes[i])) + 2)}| {links[i]} {" " * (links_pad - len(links[i]) + 2)}|"
        file.append(info)
        print(info)
    line()
    file.append("```")
    dump_choice = input("Dump? y/n : ")
    if dump_choice.lower() == "y":
        with open("readme.md", "w") as dump:
            dump.write("\n".join(file))
main()