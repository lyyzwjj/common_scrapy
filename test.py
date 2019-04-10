dict = {"a": 1, "b": "2"}
print(list(dict.keys()))
print(list(dict.values()))
for key in dict.keys():
    print(key)
    print(dict[key])
print(dict.get("b"))
import json
print(json.dumps(dict))
