import json


def main():
    for i in apple:
        name = i[0]
        for j in spotify:
            if name == j[0]:
                same.append([name, j[1], j[2]])
                print("same: " + name)
                break
        if name != same[-1][0] and i[3] != "ensemble stars":
            not_same.append([name, i[1], i[2]])
    json.dump(same, open('src/same.json', 'w'), indent=4, ensure_ascii=False)
    json.dump(not_same, open('src/not_same.json', 'w'), ensure_ascii=False)
        

apple = json.load(open("src/shorted.json", "r"))
spotify = json.load(open("src/saved_list.json", "r"))
same = []
not_same = []
main()
