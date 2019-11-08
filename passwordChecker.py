import requests     # request url from pwnedpasswords
import hashlib      # hash the password for secure communication
import sys          # input from terminal


# get the object of passwords starting with the same 5 characters (in the hash)
def request_api_data(query_char):
    url = 'https://api.pwnedpasswords.com/range/' + query_char
    res = requests.get(url)
    if res.status_code != 200:
        raise RuntimeError(f'Error fetching: {res.status_code}, check the API and try again...')
    
    return res


def get_password_leaks(hashes, hash_to_check):
    # getting each entry in the API response, including the number of password leaks 
    hashes = (line.split(':') for line in hashes.text.splitlines())

    for h, count in hashes:
        if h == hash_to_check:
            return count
    
    return 0


def password_api_check(password):
    # using sha1 hashing function. The API requests the has in upper cases.
    sha1_password = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
    first5_chars, tail = sha1_password[:5], sha1_password[5:]
    response = request_api_data(first5_chars)
    return get_password_leaks(response, tail)
    

def main(args):
    for password in args:
        count = password_api_check(password)
        if count:
            print(f'{password} was found {count}. You should probably change it...')
        else:
            print(f'{password} was NOT found. Carry on!')



# getting the passwords to be processed from the terminal
main(sys.argv[1:])