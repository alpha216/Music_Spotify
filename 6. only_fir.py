import json

def main():
    temp = []
    for i in found:
        if len(temp) != 0:
            if temp[-1][0] != i[0]:
                temp.append(i)
        else:
            temp.append(i)

    print(temp)
    json.dump(temp, open('src/only_first.json', 'w'), ensure_ascii=False, indent=4)  

if __name__ == '__main__':
    # found = json.load(open('src/found.json', 'r'))
    found = json.load(open('src/found_2.json', 'r'))

    main()