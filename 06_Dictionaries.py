# Dictionaries-> A changable orderd collection of unique key:value pairs
# fast because they use hashing , allow us to access a value  quickly
# Key -> Value
# Mutable
# Ordered ?????????? Find
person = {
    'name': "Sudeepta",
    "age": 21,
    "power": ["gomu gomu no", "Bankai", "Sharingan"],
    "music": {
        "anime": "Unreveal",
        "Hindi": "Besabriyan"
    }
}
##### MEETHODS ########
# .get(key) -> value
# .keys() -> all keys
# .values() -> all values
# .items() -> all items- entire dictionary
# .upadate({"name":"Naruto"})
# .clear(), .pop(),

# print(person["power"])
# person["goal"] = "Pirate King"
# print(person)
# person["name"] = 'DedSec'
# print(person)

for i in person:
    print(i)
