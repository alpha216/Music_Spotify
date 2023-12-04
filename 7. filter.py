import json
import pickle

def main():
    count = 0 
    ids = []
    # while(count < len(found)-2):
        
    #     is_pass = 0
    #     if found[count][0] == found[count][3]:
    #         is_pass += 1
    #     if found[count][1] == found[count][4]:
    #         is_pass += 1   
    #     if found[count][2] == found[count][5]:
    #         is_pass += 1
        
    #     if is_pass >= 2:
    #         print(found[count][0] + " / " + found[count][1] + " / " + found[count][2] + " | " + found[count][3] + " / " + found[count][4] + " / " + found[count][5])
    #         ids.append(found[count][6])
    #     count += 3
    #     pickle.dump(ids, open('src/ids.p', 'wb'))
        
        
    for i in found:
        is_pass = 0
        if i[0] == i[3]:
            is_pass += 1
        if i[1] == i[4]:
            is_pass += 1   
        if i[2] == i[5]:
            is_pass += 1
        
        if is_pass >= 2:
            print(i[0] + " / " + i[1] + " / " + i[2] + " | " + i[3] + " / " + i[4] + " / " + i[5])
            ids.append(i[6])
        count += 3
        pickle.dump(ids, open('src/ids.p', 'wb'))

# def main():
#     temp = []
#     for i in found:
#         if len(temp) != 0:
#             if temp[-1][0] != i[0]:
#                 temp.append(i)
#         else:
#             temp.append(i)

#     print(temp)
#     json.dump(temp, open('src/only_first.json', 'w'), ensure_ascii=False, indent=4)  

if __name__ == '__main__':
    # found = json.load(open('src/found.json', 'r'))
    found = json.load(open('src/only_first.json', 'r'))

    main()
    