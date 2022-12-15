# Advent of Code 2022 - Day 6



# ========== PART 1 ========== #

def start_of_pck(data):
    
    marker = []
    unique = []

    for i in range(len(data)):
        # Defining the first possible marker
        marker = [data[i], data[i+1], data[i+2], data[i+3]]
        # create a Set from the marker
        unique = set(marker)
        if len(marker) == len(unique):
            return i+4


# ========== PART 2 ========== #

def start_of_msg(data, limiter):

    marker = []
    unique = []

    for i in range(len(data)):
        tmp = ""
        for j in range(limiter + 1):
            tmp += data[i+j]

        marker = list(tmp)
        unique = set(marker)

        if len(marker) == len(unique):
            return i + limiter # i = starter, limiter = length of marker
    

if __name__ == "__main__":

    # Opening input file
    with open("input.txt", "r") as fd:
        
        datastream = fd.readline()
        
    # Finding the first start-of-packet marker
    packet_chars = start_of_pck(datastream)

    print(f"Characters processed: {packet_chars}")
    
    # Finding the first start-of-message marker    
    message_chars = start_of_msg(datastream, 14)

    print(f"Characters processed: {message_chars}")
