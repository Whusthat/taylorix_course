import ast


def build_dictonary(string):
    key_freq = {}
    key = {}
    for char in string:
        if char in key_freq:
            key_freq[char] += 1
        else:
            key_freq[char] = 1
            key[char] = ''
    return key_freq, key


def build_nodes(dict):
    all_nodes = []
    # go over ever item in our dictonary (key, probability) and create a node from it
    for item in dict.items():
        key = item[0]
        probability = item[1]
        node = Node(key, probability)
        all_nodes.append(node)
    return all_nodes


def build_tree(dict):
    sorted_node_list = dict
    while len(sorted_node_list) > 1:
        # make sure the list is sorted before you extract the 2 Nodes with the lowest probabilities
        sorted_node_list = sorted(sorted_node_list, key=lambda node: node.probability)
        # check if more than 1 item is left in list
        if len(sorted_node_list) > 1:
            # grab the 2 nodes with the lowest probabilities
            low_value_node = sorted_node_list[0]
            high_value_node = sorted_node_list[1]
            # combine the 2 nodes and combine their KeyAttribute and ProbabilitiesAttribute
            combined_node = Node(low_value_node.key + high_value_node.key,
                                 low_value_node.probability + high_value_node.probability)
            # set pointers to the 2 nodes we created the combined node from
            combined_node.left = low_value_node
            combined_node.right = high_value_node
            # remove the nodes we combined
            sorted_node_list.pop(0)
            sorted_node_list.pop(0)
            # add the combined node to list
            sorted_node_list.append(combined_node)
        # if only 1 item is left and is a combined_node we have our root of tree
    else:
        start = sorted_node_list[0]
        return start


def walk_tree(string):
    start = root
    char_list = string
    while len(char_list) > 0:
        # if object.left and object.right == none -> we know that the node we are in right now does not have any
        # pointers to other objects, so we can proceed with the next char
        if start.left is None and start.right is None:
            char_list = char_list.replace(char_list[0], '')
            start = root
        # every time we go left we add a 0 to the code_list and set a new starting point
        elif char_list[0] in start.left.key:
            start = start.left
            code_list[char_list[0]] += '0'
        # every time we go left we add a 1 to the code_list and set a new starting point
        elif char_list[0] in start.right.key:
            start = start.right
            code_list[char_list[0]] += '1'


def generate_bit_string(string, dict):
    text_to_compress = string
    huffman_code_list = dict
    compressed_text = ''
    for char in text_to_compress:
        compressed_text += huffman_code_list.get(char)
    return compressed_text


def compress(string, dict):
    bit_string = string
    fill_bits = 8 - len(string) % 8
    # fill missing bits
    for bit in range(fill_bits):
        bit_string += '1'

    decimal_string = ''
    uft_chars = ''
    for x in range(1, len(bit_string)+1):
        decimal_string += bit_string[x-1]
        if x % 8 == 0:
            uft_chars += chr(int(decimal_string, 2))
            decimal_string = ''
    dict['fill_bits'] = fill_bits

    return uft_chars, dict


def decompress():
    with open('huffman_files/encoded.txt', 'r', encoding='utf-8') as d:
        file_content = d.readlines()
        d_list = ast.literal_eval(file_content[-1])
        file_content.pop(-1)
        compressed_text = ''
        for line in file_content:
            compressed_text += line.replace('\n', '')

    bit_string = ''
    fill_bits_count = d_list['fill_bits']
    d_list.pop('fill_bits')

    # char to bin
    for char in compressed_text:
        binary = format(ord(char), 'b')
        if len(binary) < 9:
            add_0_bits = 8 - len(binary)
            bit_string += (add_0_bits * '0') + binary

    # remove fill bits from bit string
    bit_string = bit_string[:len(bit_string) - fill_bits_count]
    decompressed_text = ''
    hold_bits = ''

    while len(bit_string) > 0:
        hold_bits += bit_string[0]
        bit_string = bit_string.replace(bit_string[0], '', 1)
        if hold_bits in d_list.values():
            for char, s in d_list.items():
                if s == hold_bits:
                    decompressed_text += char
                    hold_bits = ''

    with open('huffman_files/decoded.txt', 'w', encoding='utf-8') as w:
        w.write(decompressed_text)

    return decompressed_text


class Node:
    def __init__(self, key, probability):
        self.key = key
        self.probability = probability
        self.left = None
        self.right = None


def read_file():
    with open('huffman_files/input.txt', 'r', encoding='utf-8') as r:
        lines = r.readlines()
        text_input = ''

        for line in lines:
            text_input += line

    return text_input


def save_file(chars, decode_list):
    with open('huffman_files/encoded.txt', 'w', encoding='utf-8') as w:
        w.write(chars)
        w.writelines('\n' + str(decode_list))


# get our input
text = read_file()

# build dictonary from letters in text, and prepare the code_list for later use
dictonary, code_list = build_dictonary(text)

# create nodes
node_list = build_nodes(dictonary)

# build tree and get root of tree + assign pointers to object.left and object.right value
root = build_tree(node_list)

# walk through tree
walk_tree(text)

# generate a string of bits
compressed_string_bits = generate_bit_string(text, code_list)

# change the string of bits to ascii chars and compress the input string
compressed_string_ascii, decode_list = compress(compressed_string_bits, code_list)
save_file(compressed_string_ascii, decode_list)

# function to decompress the file\string
decompressed_string = decompress()

# original size
o_size = len(text)

# compressed size
c_size = len(compressed_string_ascii) + len(str(decode_list))

# difference in size
d_size = 100 - c_size / o_size * 100

# print output
print(f'{dictonary}\n'
      f'The code table is {code_list}\n'
      f'***************************************************************************************************\n'
      f'The uncompressed string was: {o_size} bytes, \n'
      f'The compressed string + list to decode is: ~{c_size}  bytes \n'
      f'The compressed file is: '
      f'{round(d_size, 2)} % of the original string \n'
      f'{text == decompressed_string}')

