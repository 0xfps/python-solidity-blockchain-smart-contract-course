namelist = {"Acts": 23, "Romans": 40}
print(namelist['Acts'])
print("Romans" in namelist)
print(namelist.get("Romans"))
print(namelist.get("Ephesians", "Not in list"))