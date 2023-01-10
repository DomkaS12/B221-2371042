data = {

"students":["Adam Levine", "Monica Muller", "John Deere", "John Deere", "Adam Peichl", "Martin Novak", "Michal Kuchař", "John Deere"],
"active":[True, False, True, True, True, False, True, True]

}

def usernames(info):
    students = (info["students"])
    active = (info["active"])
    if not len(students) == len(active):
        return None
    # creating usernames
    usernames = []
    for i in range(len(students)):
        if active[i]:
            temp = students[i].split(" ")
            first = str(temp[0][0:3]).lower()
            second = str(temp[1][0:5]).lower()
            username = second + first
            n=2
            while username in usernames:
                username = username[0:-1] + str(n)
                n+=1
            usernames.append(username)

    return usernames


data_new = usernames(data)
print(data_new)
