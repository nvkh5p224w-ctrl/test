# Problem 2 - Batting Average
# Enter 0 for last name to stop.

def batting_average(hits, at_bats):
    if at_bats == 0:
        return 0.0
    return hits / at_bats

def main():
    player_count = 0

    while True:
        last_name = input("Enter player's last name (0 to stop): ")
        if last_name == "0":
            break

        hits = int(input("Enter number of hits: "))
        at_bats = int(input("Enter number of at bats: "))

        average = batting_average(hits, at_bats)
        print(f"{last_name} batting average: {average:.3f}\n")
        player_count += 1

    print(f"Number of players entered: {player_count}")

if __name__ == "__main__":
    main()
