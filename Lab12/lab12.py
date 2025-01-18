from dataclasses import dataclass, field

ranks = {"A": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7,
         "8": 8, "9": 9, "10": 10, "J": 11, "Q": 12, "K": 13}
suits = {"O": 1, "E": 2, "C": 3, "P": 4}


@dataclass
class Card:
    """ The card's class

    Attributes:
    suit  -- the card's symbol (O, E, C or P)
    value -- the card's value (A, 2, 3, ..., 10, J, Q or K)
    """

    rank: str
    suit: str

    def __lt__(self, other):
        """ Compare two cards based on their ranks

        Attributes:
        self  -- the card itself
        other -- the other card to compare against

        Returns:
        bool  -- True if the card is smaller than the other card, False
                 otherwise
        """
        if ranks[self.rank] != ranks[other.rank]:
            return ranks[self.rank] < ranks[other.rank]
        else:
            return suits[self.suit] < suits[other.suit]

    def __repr__(self):
        return f"{self.rank}{self.suit}"


@dataclass
class Player:
    """ The player class

    Attributes:
    Hand -- the hand of the player
    """

    hand: list
    stack: list = field(default_factory=list)

    def bubble_sort(self, what: str, ordained=False):
        """ A bubble sort inspired algorithm"""

        if what == "hand":
            what = self.hand
        else:
            what = self.stack

        while not ordained:
            ordained = True
            for i in range(len(what) - 1):
                if what[i + 1] > what[i]:
                    what[i + 1], what[i] = what[i], what[i + 1]
                    ordained = False

    def binary_search(self, rank: str, left: int, right: int) -> int:
        """ A binary search algorithm

        Attributes:
        rank  -- the rank that will be searched
        left  -- the position on the far left of the list
        right -- the position on the far right of the list

        Returns:
        int   -- the position of the card in the card list
        """
        if right < left:
            return False

        mid = (left + right) // 2
        if ranks[rank] == ranks[self.hand[mid].rank]:
            return mid
        elif ranks[rank] < ranks[self.hand[mid].rank]:
            return self.binary_search(rank, mid + 1, right)
        else:
            return self.binary_search(rank, left, mid - 1)

    def search_lower(self, lower_rank: str) -> int:
        """ Find the lowest rank card bigger or equal to
        the lower_rank

        Attributes:
        lower_rank  -- the rank that will be compared

        Returns:
        int   -- the position of the card in the card list
        """
        card_pos = False
        for c in self.hand[::-1]:
            if ranks[c.rank] >= ranks[lower_rank]:
                card_pos = self.binary_search(
                    c.rank, 0, len(self.hand) - 1)
                break

        return card_pos


def sort_and_print(number_players: int, players: list):
    """ Sort the hands and print them

    Attributes:
    players -- the list of players
    """

    for i in range(len(players)):
        players[i].bubble_sort("hand")
        print(f"Jogador {i + 1} \nMão:", *players[i].hand)
    print("Pilha: ")


def main():
    """ The main function of the code"""

    # Receiving the inputs and organizing it
    number_players = int(input())
    players, stack = [], []
    new_round, has_winner = True, False
    play_number = 0

    for i in range(number_players):
        cards = []
        cards_str_list = input().split(", ")
        for card_str in cards_str_list:
            if card_str.startswith("10"):
                rank = "10"
                suit = card_str[-1]
            else:
                rank = card_str[0]
                suit = card_str[-1]
            cards.append(Card(rank, suit))
        players.append(Player(cards))

    doubt = int(input())

    # In fact initiate the game
    sort_and_print(number_players, players)

    while not has_winner:
        for i in range(number_players):
            play_number += 1
            if new_round:
                lower_rank = players[i].hand[-1].rank
                new_round = False

            players[i].stack = []
            card_pos = players[i].search_lower(lower_rank)

            # Make sure every card of the same value is played
            while players[i].hand != []:
                if card_pos is not False:
                    lie = False
                    player_card = players[i].hand.pop(card_pos)
                    players[i].stack.append(player_card)
                    lower_rank = player_card.rank
                    card_pos = players[i].binary_search(
                        lower_rank, 0, len(players[i].hand) - 1)
                elif players[i].stack == []:
                    lie = True
                    lie_rank = players[i].hand[-1].rank
                    players[i].stack.append(players[i].hand.pop(-1))
                elif lie is True:
                    lie_pos = players[i].binary_search(
                        lie_rank, 0, len(players[i].hand) - 1)
                    if lie_pos is not False:
                        players[i].stack.append(players[i].hand.pop(lie_pos))
                    else:
                        break
                else:
                    break

            # Add the player.stack to the stack in the correct order
            players[i].bubble_sort("stack")
            stack += players[i].stack[::-1]
            print(f"[Jogador {i + 1}] {len(players[i].stack)} "
                  + f"carta(s) {lower_rank} \nPilha:", *stack)

            # literally the name of the game
            if play_number == doubt:
                print(f"Jogador {i + 2 if i + 1 < len(players) else 1}"
                      + " duvidou.")
                new_round = True
                play_number = 0
                if lie is False:
                    players[i + 1 if i + 1 < len(players) else 0].hand += stack
                else:
                    players[i].hand += stack
                sort_and_print(number_players, players)
                stack = []

            # Check for winners
            if len(players[i].hand) == 0:
                print("Jogador", i + 1, "é o vencedor!")
                has_winner = True
                break


if __name__ == "__main__":
    main()
