def lang_genoeg(lengte):
    if lengte >= 120:
        line = 'Je bent lang genoeg voor de attractie!'
        return line
    else:
        line1 = 'Sorry, je bent te klein!'
        return line1

lengte = eval(input('Wat is je lengte? '))
res = lang_genoeg(lengte)
print(res)