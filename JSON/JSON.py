import json

" load: json data from file" \
"loads: from string" \
"dump: write json objects to file" \

json_file = open("data.txt", "r", encoding="utf-8")  # utf-8 for non-ascii, not my case
data = json.load(json_file)
json_file.close()
print(data)

print(type(data))  # dict

# loads if it arrives as a string, common in client-server apps

value = """
    {
    "title" : "Example",
    "actors" : null ,
    "bugdet" : 500000
    }
    """

"false would transform to False, null to None"

data_string = json.loads(value)
print(data_string)

# store data in a db
# dict to string: dumps

print(json.dumps(data))  # from python to js...None -> null, True -> true
# json assumes all chars are ascii, if they are not, should call:
print(json.dumps(data, ensure_ascii=False))

data2 = {}
data2["Title"] = "Title_ex"
data2["Director"] = "Director_ex"

file2 = open("data2.txt", "w", encoding="utf-8")
json.dump(data2, file2, ensure_ascii=False)
file2.close()