
def readFile(path):
    with open(path,'r') as f:
        guest_number = f.readline()
        guest_prefs = []
        dislike_count = {}
        for i in range(int(guest_number)):
            likes = f.readline()
            likes = likes.split()
            like_list = []
            for i in range(int(likes[0])):
                like_list.append(likes[i+1])

            dislikes = f.readline()
            dislikes = dislikes.split()
            dislike_list = []
            for i in range(int(dislikes[0])):
                dislike_list.append(dislikes[i+1])
                if dislikes[i+1] in dislike_count:
                    dislike_count[dislikes[i+1]] += 1
                else:
                    dislike_count[dislikes[i+1]] = 1
            
            guest_pref = {}
            guest_pref['likes'] = like_list
            guest_pref['dislikes'] = dislike_list
            guest_prefs.append(guest_pref)

        return dislike_count, guest_prefs




if __name__ == "__main__":
    path = 'hashcode/input_data/'
    files = ['a_an_example.in.txt','b_basic.in.txt', 'c_coarse.in.txt', 'd_difficult.in.txt', 'e_elaborate.in.txt']
    # for file in files:
    #     print(readFile(path+file))
    d,d2 = readFile(path+files[2])
    print(d)
    print(d2)
    print(sorted(d, key=d.get, reverse=True))
    