import json
from random import randint

str_js = """{
    "response": {
        "count": 5961878,
        "items": [{
            "first_name": "Елизавета",
            "id": 620471795,
            "last_name": "Сопова",
            "can_access": true
        }, {
            "first_name": "Роман",
            "id": 614752515,
            "last_name": "Малышев",
            "can_access": true
}]

}
}"""
#print(type(str_js))
data = json.loads(str_js)
#print(data['response']['count'])
#print(type(data))
for item in data['response']['items']:
    #print(item['first_name'])
    del item['id']
    item['likes'] = randint(0, 1000)
#print(data['response']['items'])
    s = json.loads(str_js)
    print(type(s))
with open("data_1.json", "w") as file:
    json.dump(data, file)