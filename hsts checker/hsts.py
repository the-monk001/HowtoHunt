import requests
import sys

def banner():
    print("       ___   ___   ___         ___         ___   ___   v=beta")
    print("|   | |       |   |           |     |   | |     |     |  /  ")
    print("|-+-|  -+-    +    -+-        |     |-+-| |-+-  |     |-+   ")
    print("|   |     |   |       |       |     |   | |     |     |  \  ")
    print("       ---         ---         ---         ---   ---        ")
    print("                                                            ")
    print()
    print("                                                            ")
    print("Note : Program is not fully optimized.")
    print("Enter inuts as directed otherwise program will halted automatically.")
    print()


def check_HSTS(web):
    try:
        req=requests.get("https://"+web)
    except requests.exceptions.SSLError as error:
        print("Website Does Not have a Working SSL Certificate")
        exit(0)
        return "SSL ERRORS !"
    if "strict-transport-security" in req.headers:
        return "Yes| Header Found!"
    else:
        return "No | Header Found "


banner()

entered_site=str(input("Enter Url : "))
if "//" in entered_site:
    entered_site=str(input("Enter Url : ")).split("//")
elif "/" in entered_site:
    entered_site=entered_site[1].replace("/","")
print()    
k=check_HSTS(entered_site)
l=req=requests.get("https://"+entered_site)
l_0=req.status_code
print("======================HSTS CHECK====================")
print("Target            : ",entered_site)
print("HSTS Result       : ",k)
print("Response Code     : ",l_0)
print("====================================================")
print()
print()
if k == 'No | Header Found ':
    print("No HSTS Header @",entered_site)
    print()
    print()
