# TODO-1: Ask the user for input
# TODO-2: Save data into dictionary {name: price}
# TODO-3: Whether if new bids need to be added
# TODO-4: Compare bids in dictionary

import art
import datetime

# variables

# sample of data -> auctions = { "auction_1" : ['item 1',{bidder_1 : 10.00}] }

auctions = {}
bidders = []
str_bidders = ""

# functions

def clear_terminal_ansi():
    """
    
    """
    # \033[H moves cursor to top home, \033[2J clears the screen
    print("\033[H\033[2J", end="")

def add_auction(auction_name, item_name, bids={}):
    auctions[auction_name] = [item_name, bids]

def add_bidder(auction_name, name):
    auctions[auction_name][1][name] = 0

def add_bid(auction_name, name, bid):
    auctions[auction_name][1][name] += bid

# menu

while True:
    print(
f"""
    {art.logo}
    Welcome to the secret auction program.
        1 - New Auction
        2 - New Bidder
        3 - Start Auction
        4 - Results
        0 - Exit
"""
    )

    option = int(input('Insert option: '))

    match option:
        case 1:
            auction_name = str(input("Insert the auction name please: "))
            item_name = str(input("Insert the item name please: "))

            add_auction(auction_name, item_name)

            print(auctions[auction_name])

        case 2:
            while True:
                name = str(input("What is their name?:  "))

                # adding to dictionary

                add_bidder(auction_name, name)

                # auctions[auction_name][1][name] = 0

                # new bidder? 

                new_bidder = str(input("Are there any other bidders? Type 'y' or 'n'.    "))

                print(auctions[auction_name][1])

                if new_bidder == 'y':
                    continue
                else:
                    clear_terminal_ansi()
                    break
        case 3:
            while True:

                for bidder in auctions[auction_name][1]:
                    print(f"{bidder}'s turn. ")
                    bid = float(input("What's your bid?: "))
                    add_bid(auction_name, bidder, bid)
                    print(bidder, auctions[auction_name][1][bidder])
                # checking out?

                more_bids = str(input("Continue bidding? y/n    "))
                if more_bids == 'y':
                    continue
                elif more_bids == 'n':
                    clear_terminal_ansi()
                    break
                else:
                    print("Insert valid option.")
        case 4:
            i = 0
            for bidder in auctions[auction_name][1]:
                i += 1
                bidders.append(f"       {bidder} - R$ {auctions[auction_name][1][bidder]:.2f}")

            # sorting on asc

            bidders.sort(reverse=True)

            #building the string for the results print
            
            str_bidders = "\n".join(bidders)

            # clearing terminal

            clear_terminal_ansi()
    
            # printing the results

            result = f"""
Results from auction of {auctions[auction_name][0]}
{str_bidders}
"""

            print(result)
            while True:
                save_file = str(input("Would you like to save the results on a file? y/n"))
                if save_file in "Yy":
                    file_name = f"{datetime.date.today()}_{auction_name}.txt"
                    with open(file_name, "w", encoding="utf-8") as file:
                        file.write(result)
                    break
                else:
                    if save_file in "nN":
                        break
                    else:
                        print("Select a valid option")
                        continue
        case 0:
            print("Bye bye!")
            break
        case __:
            print("Insert valid option")
            continue