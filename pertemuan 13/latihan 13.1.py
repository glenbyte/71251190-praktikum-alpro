data = {
    "Pendidikan": ["Duolingo", "Classdojo", "Google Classroom", "Canva"],
    "Game": ["Minecraft", "HOK", "Monster Hunter", "CODM"],
    "Produktivitas": ["Canva", "Notion", "Google Classroom"],
    "Sosial Media": ["Instagram", "Facebook", "Duolingo", "X"]
}
test = {}
for g, t in data.items():
    for app in t:
        test[app] = test.get(app, 0) + 1
print("aplikasi di 1 kategori:")
for app, j in test.items():
    if j == 1:
        for kat, apps in data.items():
            if app in apps:
                print(f"  {app} = {kat}")
print("\naplikasi di 2 kategori:")
for app, j in test.items():
    if j == 2:
        kat_list = [k for k, v in data.items() if app in v]
        print(f"  {app} = {' & '.join(kat_list)}")