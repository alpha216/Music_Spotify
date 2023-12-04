import json
import pickle

def main():
    count = 0 
    ids = []
    names = []

    for i in found:
        is_pass = 0
        if i[0] in i[3] or i[3] in i[0]:
            is_pass += 1
        if i[1] in i[4] or i[4] in i[1]:
            is_pass += 1   
        if i[2] in i[5] or i[5] in i[2]:
            is_pass += 1
        
        if is_pass >= 2:
            if len(names) == 0:
                names.append(i[0])
                ids.append(i[6])
                print(i[0] + " / " + i[1] + " / " + i[2] + " | " + i[3] + " / " + i[4] + " / " + i[5])
            if i[0] != names[-1]:
                names.append(i[0])
                ids.append(i[6])
                print(i[0] + " / " + i[1] + " / " + i[2] + " | " + i[3] + " / " + i[4] + " / " + i[5])
        count += 3
        pickle.dump(ids, open('src/ids.p', 'wb'))

if __name__ == '__main__':
    found = json.load(open('src/found.json', 'r'))
    # found = json.load(open('src/only_first.json', 'r'))

    main()
    