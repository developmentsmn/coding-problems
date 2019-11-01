from collections import Counter

def countLetters(s):

    dic = { } 
    s = s.lower()

    dic = Counter(s)

    # for c in s:

    #     if c in dic:
    #         dic.update({ c: dic[c] +1  })
    #     else:
    #         dic.setdefault(c, 1)


    # for character in s:

    #     if character not in dic:
    #         dic.update({character : 1 })

    #     else:

    #         dic.update({character : dic[character]+1 })


    return dic

dic = countLetters("tebbem")



print(dic.items())

        