import json

def main():
    count = 0 
    while(count < len(tosearch)-3):
        for i in range(3):
            found[count*3+i].insert(2, tosearch[count][2].replace(' - EP', '').replace(' - Single', ''))
            print(found[count*3+i])
        count += 1

    json.dump(found, open('src/found_2.json', 'w'), indent= 0, ensure_ascii=False)

if __name__ == '__main__':
    found = json.load(open('src/found.json', 'r'))
    tosearch = json.load(open('src/not_same.json', 'r'))
    main()