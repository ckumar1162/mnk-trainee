# Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

# def first(needle,haystack):
#     if needle in haystack:
#         return haystack.index(needle)
#     else:
#         return -1

# print(first("sad","sadbutsad"))
# print(first("leeto","leetcode"))
def first(needle,haystack):
    for i in range(len(haystack)):
        for j in range(len(needle)):
            if haystack[i] == needle[j]:
                return j
            else:
                return -1
print(first("sad","butsad"))
print(first("leeto","leetcode"))
