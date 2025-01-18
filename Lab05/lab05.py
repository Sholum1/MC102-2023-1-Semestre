# Define the first user input
genome=input()

# Define the functions
def revert(i:int,j:int)->str:
    """Reverts the genome, initializing from the letter in the i position and ending in the letter in the j position

    Parameters:
    i   -- the position of the first letter
    j   -- the position of the last letter

    Returns:
    str -- the inverted genome
    """

    position_to_revert=genome[i:j+1]
    reverted_part_genome=position_to_revert[::-1]
    reverted_genome=genome[0:i]+reverted_part_genome+genome[j+1:]
    return reverted_genome

def transpose(i:int,j:int,k:int)->str:
    """Exchange the order of the set of letters beginning at position i and ending at position j with the set of letter beginning at position j+1 and ending at position k

    Parameters:
    i   -- the position of the first letter of the first set
    j   -- the position of the last letter of the first set
    k   -- the position of the last letter of the second set

    Returns:
    str -- the transposed genome
    """

    first_set=genome[i:j+1]
    second_set=genome[j+1:k+1]
    transposed_genome=genome[0:i]+second_set+first_set+genome[k+1:]
    return transposed_genome

def combine(g:str,i:int)->str:
    """Combines the current genome with the given genome

    Parameters:
    g   -- the genome that will be combined
    i   -- the position that the g str will be added

    Returns:
    str -- the combined genome
    """

    combined_genome=genome[0:i]+g+genome[i:]
    return combined_genome

def concatenate(g:str)->str:
    """Adds a new genome to the end of the current genome

    Parameters:
    g   -- the genome that will be added

    Returns:
    str -- the concatenated genome
    """

    concatenated_genome=genome+g
    return concatenated_genome


def remove(i:int,j:int)->str:
    """Remove a part of the genome

    Parameters:
    i   -- the position that the remove process will start
    j   -- the position that the remove process will finish

    Returns:
    str -- the genome without the removed part
    """

    removed_genome=genome[0:i]+genome[j+1:]
    return removed_genome

def transpose_and_revert(i:int,j:int,k:int)->str:
    """Does the same as transpor i j k followed by reverter i k

    Parameters:
    i   -- the position of the first letter of the first set and the position of the first letter to be reverted
    j   -- the position of the last letter of the first set
    k   -- the position of the last letter of the second set and the position of the last letter to be reverted

    Returns:
    str -- the genome transposed and reverted
    """

    first_set=genome[i:j+1]
    second_set=genome[j+1:k+1]
    transposed_genome=genome[0:i]+second_set+first_set+genome[k+1:]
    position_to_revert=transposed_genome[i:k+1]
    reverted_part_genome=position_to_revert[::-1]
    transposed_and_reverted_genome=transposed_genome[0:i]+reverted_part_genome+transposed_genome[k+1:]
    return transposed_and_reverted_genome

def search(g:str)->int:
    """Looks for the number of times on genome repeats inside other genome

    Parameters:
    g   -- the genome that will be searched

    Returns:
    int -- the number of times the genome repeats inside the other genome
    """

    number=0
    i=0
    while i<=len(genome):
        if genome[i:i+len(g)]==g:
            number=number+1
            i=i+len(g)
        else:
            i=i+1
    print(number)
    return number

def bidirectional_search(g:str)->int:
    """Does the same as search, but counts the repetitions in the reverse genome

    Parameters:
    g   -- the genome that will be searched

    Returns:
    int -- the number of times the genome repeats inside the other genome and its inverse
    """

    i=0
    number_current=0
    while i<=len(genome):
        if genome[i:i+len(g)]==g:
            number_current=number_current+1
            i=i+len(g)
        else:
            i=i+1
    reversed_genome=revert(0,len(genome))
    number_reversed=0
    j=0
    while j<len(reversed_genome):
        if reversed_genome[j:j+len(g)]==g:
            number_reversed=number_reversed+1
            j=j+len(g)
        else:
            j=j+1
    number=number_current+number_reversed
    print(number)
    return number

def show():
    """Print the current genome"""

    print(genome)

# Make the program usable
while True:
    what_to_do=input()
    what_to_do_split_list=what_to_do.split()

    if what_to_do_split_list[0]=="reverter":
        i=int(what_to_do_split_list[1])
        j=int(what_to_do_split_list[2])
        genome=revert(i,j)
    elif what_to_do_split_list[0]=="transpor":
        i=int(what_to_do_split_list[1])
        j=int(what_to_do_split_list[2])
        k=int(what_to_do_split_list[3])
        genome=transpose(i,j,k)
    elif what_to_do_split_list[0]=="combinar":
        g=str(what_to_do_split_list[1])
        i=int(what_to_do_split_list[2])
        genome=combine(g,i)
    elif what_to_do_split_list[0]=="concatenar":
        g=str(what_to_do_split_list[1])
        genome=concatenate(g)
    elif what_to_do_split_list[0]=="remover":
        i=int(what_to_do_split_list[1])
        j=int(what_to_do_split_list[2])
        genome=remove(i,j)
    elif what_to_do_split_list[0]=="transpor_e_reverter":
        i=int(what_to_do_split_list[1])
        j=int(what_to_do_split_list[2])
        k=int(what_to_do_split_list[3])
        genome=transpose_and_revert(i,j,k)
    elif what_to_do_split_list[0]=="buscar":
        g=str(what_to_do_split_list[1])
        search(g)
    elif what_to_do_split_list[0]=="buscar_bidirecional":
        g=str(what_to_do_split_list[1])
        bidirectional_search(g)
    elif what_to_do=="mostrar":
        show()
    elif what_to_do=="sair":
        break
