# Joshua Kitaigorod Lab 6
def encode(password):
    res = ''
    for char in password:
        if int(char) == 7 or int(char) == 8 or int(char) == 9:
            res += str(int(char) - 7)
        else:
            res += str(int(char) + 3)
    return res

def decode(password):
    res = ''
    for char in password:
        if int(char) == 0 or int(char) == 1 or int(char) == 2:
            res += str(int(char) + 7)
        else:
            res += str(int(char) - 3)
    return res

if __name__ == '__main__':
    i = 0
    while i == 0:
        print(f'\nMenu\n-------------\n1. Encode\n2. Decode\n3. Quit\n')
        option_num = int(input('Please enter an option: '))
        if option_num == 1:
            encode_pass = input('Please enter your password to encode: ')
            stored_encode = encode(encode_pass)
            print(f'Your password has been encoded and stored!')
        elif option_num == 2:
            stored_decode = decode(stored_encode)
            print(f'The encoded password is {stored_encode}, and the original password is {stored_decode}')
        elif option_num == 3:
            i += 1