def draw_stars(x):
    for num in x:
        if type(num) is int:
            print "*"*int(num)
        if type(num) is str:

            print num[0].lower()*len(num)

draw_stars([4, "Tom", 1, "Michael", 5, 7, "Jimmy Smith"])
