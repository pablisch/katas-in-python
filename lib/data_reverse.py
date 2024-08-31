# KEYWORDS: chunk, reverse, split, comprehension

# import numpy as np

sample = [1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,0,1,0,1,0,1,0]

# # This works but the import of numpy causes potential problems.
# # The tests don't like it and Codewars is sure not to.
# def data_reverse_numpy(data):
#     num_of_chunks = len(data) / 8
#     chunk_list = np.array_split(data, num_of_chunks)
#     reversed_chunks = chunk_list[::-1]
#     print (chunk_list)
#     print (reversed_chunks)
#     reversed_data = np.concatenate(reversed_chunks)
#     print (reversed_data)

# A basic solution of an inexperienced Python developer
def data_reverse_basic(data):
    # Step 1: split the data into chunks of 8 by pushing them into an empty list
    chunks = []
    num_of_chunks = int(len(data) / 8)
    for i in range(num_of_chunks):
        chunks.append(data[i*8:(i+1)*8])

    # Step 2: reverse the order of the chunks
    # NOTE: this could also have been done by modifying the chunks list: chunks.reverse()
    reversed_chunks = list(reversed(chunks))

    # Step 3: flatten the nested sublists. This syntax is a little tricky still.
    # The outer loop is 'for sublist in reversed_chunks' and iterates over each sublist
    # The inner loop is 'for item in sublist' which iterates over each item in each sublist as the outer loop iterates over that sublist in turn.
    # The beginning 'item' is each item from each sublist as it is put into the new list.
    # Alternatives are using a itertools, sum or more expressive loops.
    reversed_data = [item for sublist in reversed_chunks for item in sublist]
    return reversed_data

def data_reverse(data):
    # Step 1: Split data into chunks of 8 elements
    # [data[i * 8:(i + 1) * 8] => range from data, i.e. when i==0, data[0:8], when i==1, data[8:16] where the range end is exclusive.
    # for i in range(len(data) // 8)] => for loop in range data's length / 8 with no remainder, e.g. if len(data)==4, range(4), i.e. 0 to 3.
    chunks = [data[i * 8:(i + 1) * 8] for i in range(len(data) // 8)]

    # Step 2: Reverse the order of chunks
    reversed_chunks = list(reversed(chunks))

    # Step 3: Flatten the reversed chunks into a single list
    reversed_data = [item for sublist in reversed_chunks for item in sublist]

    return reversed_data


def data_reverse_codewars(data):
    res = []

    for i in range(len(data) - 8, -1, -8):
        print ("res before:", res)
        print ("i:", i)
        print ("chunk:", data[i:i + 8])
        res.extend(data[i:i + 8])
        print ("res after:", res, "\n")

    return res


data_reverse_codewars(sample)
