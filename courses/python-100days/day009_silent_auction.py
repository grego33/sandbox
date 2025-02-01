

def clear_screen():
    print("\n"*100)

def add_bid(bids: dict[str, int]):
    name = input("Your name: ")
    bid = int(input("What is your bid? $"))
    bids[name] = bid

def any_more_bidders() -> bool:
    more = input("Are there any more bidders (y/n)?")
    return (more == "y")

def highest_bidder(bids):
    highest = 0
    winner = ""
    for name in bids:
        if bids[name] > highest:
            highest = bids[name]
            winner = name
    return winner

print("This is a silent auction")
bids = {}
finished = False;

only_bidder = input("Are you the only bidder (y/n?")
if only_bidder == "y":
    add_bid(bids)
elif only_bidder == "n":
    while not finished:
        clear_screen()
        add_bid(bids)
        finished = not any_more_bidders()

winner = highest_bidder(bids)
print(f"And the winner is {winner} with a bid of ${bids[winner]}")
