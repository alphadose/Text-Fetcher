#Please use python2 for running this
#as mechanize is not availabe for python3
 

import mechanize

url = "http://localhost/Anish_Mukherjee_PHP/register.php"
br = mechanize.Browser()
print("Please enclose all of your inputs within \" \" \n")
name=input("Please enter your name \n")
age=input("Please enter your age \n")
password=input("Please enter your password \n")
link=input("Please enter link to save \n")
br.set_handle_robots(False) # ignore robots
br.open(url)
br.select_form(name="start")
br["name"] = name
br["age"] = age
br["pass"] = password
br["link"] = link
res = br.submit()
content = res.read()
with open("mechanize_results.html", "w") as f:
    f.write(content)