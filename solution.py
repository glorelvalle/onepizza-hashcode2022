####################################################################################################################################
#                                                       HashCode 2022: One Pizza                                                   #
####################################################################################################################################


import random

# select data folder
path = "input_data/a_an_example"

# open file
file = open(path + ".in.txt", 'r').readlines()

# read number of customers, which is in first line
n_customers = int(file[0])

# init some variables
final_customer = 0
final_menu = set()
book = []

# for each customer...
for n in range(n_customers):

    # read every 2 lines (likes and dislikes)
    likes, dislikes = file[2*n+1].split()[1:], file[2*n+2].split()[1:]

    # readable_client = {'likes': set(likes), 'dislikes': set(dislikes)}
    readable_client = [set(likes), set(dislikes)]

    # save customer preferences (book: [[Client 1: {likes} {dislikes}] ... [Client N: {likes} {dislikes}]])
    book.append(readable_client)

# repeat 20 times main algorithm
for times in range(20):

    # init actual menu, new menu and number of customers
    menu, new_menu, customer = set(), set(), 0

    # for each customer
    for i in range(n_customers):

        # add new preferences (likes) to menu
        new_menu = menu.union(book[i][0])

        # drop new preferences (dislikes) to menu
        new_menu = new_menu - set(book[i][1])

        # init count
        count = 0

        # count
        for j in range(n_customers):
            # check condition if actual menu is will (- customers)
            if book[j][0] <= new_menu and book[j][1] & new_menu == set():
                count += 1

        # save actual new menu if actual menu is will
        if count > customer:
            customer = count
            menu = new_menu

    # save final new menu if we pay off
    if customer > final_customer:
        final_customer = customer
        final_menu = menu

    # shuffle
    random.shuffle(book)

# dump final menu with defined structure
output = str(len(final_menu)) + " " + ' '.join(final_menu)

# save to txt
with open(path + ".out.txt", "x") as file_o:
    file_o.write(output)