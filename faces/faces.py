def playback():
    n = input()
    emoji = {
        ":)": "🙂",
        ":(": "🙁 ",
        ":D": "😃",
        ";)": "😉",
        # Add more mappings as needed
    }
    p = n
    for i, y in emoji.items():

        p = p.replace(i,y)


    print(p)
playback()