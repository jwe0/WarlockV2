import os
from pystyle import Center, Colorate, Colors
from core.modules.logging import log
from core.modules.lookup import Lookup


class Main:
    def __init__(self):
        ""

    def menu(self):
        os.system("clear")
        art = """              
                  .

                   .
         /^\     .
    /\   "V"
   /__\   I      O  o
  //..\  I     .            ╦ ╦╔═╗╦═╗╦  ╔═╗╔═╗╦╔═
  \].`[/  I                 ║║║╠═╣╠╦╝║  ║ ║║  ╠╩╗
  /l\/j\  (]    .  O        ╚╩╝╩ ╩╩╚═╩═╝╚═╝╚═╝╩ ╩ v2
 /. ~~ ,\/I          .     
 \ L__j^\/I       o
  \/--v}  I     o   .
  |    |  I   _________
  |    |  I c(`       ')o    Developed by /jwe0
  |    l  I   \.     ,/
_/j  L l\_!  _//^---^\_

"""
        print(Colorate.Vertical(Colors.blue_to_cyan, art))
        # log("info", "Developed by /jwe0")
    def show_data(self, data):
        stats = data["stats"]
        result = data["result"]

        checked = stats["sites_checked"]
        valid   = stats["sites_found"]
        time_taken = stats["time_taken"]

        log("info", "Info")
        log("info", f"↬ Valid   [{valid}/{checked}]")
        log("info", f"↬ Elapsed [{time_taken}]")
        log("info", "-" * 25)

        for i in result:
            url = result[i]["url"]
            type = result[i]["type"]
            code = result[i]["code"]
            
            
            log("success", i)
            log("info", f"↬ {url}")
            log("info", f"↬ {type}"),
            log("info", f"↬ {code}")
            log("info", "-" * 25)



    def main(self):
        self.menu()

        while True:
            target = log("input", f"Username")

            check = log("input", f"Target [{target}] | confirm? y/n")

            if check.lower() == "y":
                break
            log("error", "Cancelled by user [incorrect username]")
        log("info", f"Target selected [{target}]")

        execute = log("input", "Execute script? y/n")

        if execute.lower() == "n":
            log("error", "Attack cancelled")
            exit()
        log("info", "Excecuting script")

        lookup = Lookup()

        result = lookup.lookup(target)

        log("info", "-" * 25)

        self.show_data(result)



if __name__ == "__main__":
    main = Main()
    main.main()