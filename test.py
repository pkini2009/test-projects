def recurse(param):
    print (param)
    if param < 1024:
        recurse(param*param)

recurse(2)

