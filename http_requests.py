import requests as req

#res = req.get("http://nadocoding.tistory.com")
res = req.get("http://google.com")
# print("response code :", res.status_code)

# if res.status_code == req.codes.ok
#     print("success!!")

res.raise_for_status()


print(len(res.text))

#print(res.text)

with open("mygoogle.html", "w" , encoding="utf8") as f:
    f.write(res.text)
    print("save to file {}", f.name)
