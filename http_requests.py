# import requests as req

# #res = req.get("http://nadocoding.tistory.com")
# res = req.get("http://google.com")
# # print("response code :", res.status_code)

# # if res.status_code == req.codes.ok
# #     print("success!!")

# res.raise_for_status()


# print(len(res.text))

# #print(res.text)

# with open("mygoogle.html", "w" , encoding="utf8") as f:
#     f.write(res.text)
#     print("save to file {}", f.name)



# def two_times(numberList):
#     result = []
#     for number in numberList :
#         result.append(number*2)
#     return result

# result = two_times([1,2,3,4,5,6])

# print(result)

import sys, pickle, os

# def two_times(x):
#     return x*2

# #numList = list (map(two_times, [1,2,3,4,5]))

# numList =  list(map(lambda a:a*2,[1,2,3,4,5]))

# print(numList)

# print(sys.path)


# with open('test.txt', 'wb') as f:
#     data = {1:'python', 2:'you need'}
#     pickle.dump(data,f)


# with open('test.txt', 'rb')  as f:
#     data = pickle.load(f)
#     print(data)   

print(os.getcwd())

print(os.environ['PATH'])