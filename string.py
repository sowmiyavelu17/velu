def mid_string_of_stars(text1,text2,text3):

    maksimum=max(len(text1),len(text2),len(text3))

    minimum=min(len(text1), len(text2),len(text3))

    m=(maksimum+minimum)/2 

    middle_string='*'*m
    return middle_string
