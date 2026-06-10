import art

print(art.logo)

# TODO-1: Ask the user for input

name = input("Hello! What is your name?: \n")
price = int(input("How much would you like to bid? \n"))

# TODO-2: Save data into dictionary {name: price}

saved_bids = {}

for name in saved_bids:
        print(name)
for price in saved_bids:
        print(price)

saved_bids[name] = price

# TODO-3: Whether if new bids need to be added and compare the bids.

another_bidder = input("Is there any one else, who would like to bid? Enter Y/N: \n")

while another_bidder == "Y":
    print("\n" * 30)
    name = input("Hello! What is your name?: \n")
    price = int(input("How much would you like to bid? \n"))
    saved_bids[name] = price
    another_bidder = input("Is there any one else, who would like to bid? Enter Y/N: \n")
    if another_bidder == "N":
        largest_number= max(saved_bids.values())
        for name in saved_bids:
            if saved_bids[name] == largest_number:
                print(f"The winner is {name} with a bid of ${price}")
