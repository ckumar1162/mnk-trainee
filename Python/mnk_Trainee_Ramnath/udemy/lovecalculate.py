def calculate_love_score(name1, name2):
    name1 = name1.lower()
    name2 = name2.lower()
    com_names = name1 + name2

    t = com_names.count("t")
    r = com_names.count("r")
    u = com_names.count("u")
    e = com_names.count("e")

    first_digit = t + r + u + e

    l = com_names.count("l")
    o = com_names.count("o")
    v = com_names.count("v")
    e = com_names.count("e")
    sec_digit = l + o + v + e
    print(f"{first_digit}{sec_digit}")


calculate_love_score("kanye west", "kim kardashian")
