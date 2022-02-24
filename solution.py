####################################################################################################################################
#                                                       HashCode 2022: One Pizza                                                   #
####################################################################################################################################


import random

path = "input_data/e_elaborate"

file = open(path + ".in.txt", 'r').readlines()
n_customers = int(file[0])

final_customer = 0
final_menu = set()

book = []

for n in range(n_customers):
    likes = file[2*n+1].split()[1:]
    dislikes = file[2*n+2].split()[1:]
    #readable_client = {'likes': set(likes), 'dislikes': set(dislikes)}
    readable_client = [set(likes), set(dislikes)]
    book.append(readable_client)

for times in range(20):
    menu = set()
    new_menu = set()
    customer = 0

    for i in range(n_customers):
        new_menu = menu.union(book[i][0])
        new_menu = new_menu - set(book[i][1])
        count = 0

        for j in range(n_customers):
            if book[j][0] <= new_menu and book[j][1] & new_menu == set():
                count += 1

        if count > customer:
            customer = count
            menu = new_menu

    if customer > final_customer:
        final_customer = customer
        final_menu = menu

    random.shuffle(book)

output = str(len(final_menu)) + " " + ' '.join(final_menu)

with open(path + ".out.txt", "x") as file_o:
    file_o.write(output)
