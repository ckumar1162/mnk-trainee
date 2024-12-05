def format_name(f_name, l_name):
    print(f_name.title())
    print(l_name.title())
    print(f_name.title(), l_name.title())
    #return f_name.title()+ " "+ l_name.title()
    f = f_name.title()
    l = l_name.title()
    return f"{f} {l}"





#print(format_name("rohit","ekbote"))

formated_name = format_name("rohit","ekbote")
print(formated_name)

def function_1(text):
    return text + text


def function_2(text):
    return text.title()


output = function_2(function_1("hello"))
print(output)