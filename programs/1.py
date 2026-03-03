import pickle

cookie={"name":"Hari","value":1234}
pickle.dump(cookie,open("cookie.pkl","wb"))

#load cookie
load_cookie=pickle.load(open("cookie.pkl","rb"))
print(load_cookie)