
# def say_my_name(name):
#     print(f"hail {name} hail{name}hail {name}")


# say_my_name("Sudeepta")

# Default parameters
# Positional parameters
# Nameansd parameters

# def sum(a, b=12):
#     return a + b


# ans = sum(12)
# print(ans)

# TypeHinting -> for documentation
# def sum(a: int, b: int) -> int:
#     return a + b


# ans = sum(12, 5)
# print(ans)
# ==================Bigger Guy=================================
def biggerGuy(a, b):
    if (a < b):
        return b
    else:
        return a


result = biggerGuy(13, 20)
print(result)
