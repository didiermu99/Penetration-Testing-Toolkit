import hashlib

def read_wordlist(file):
    try:
        with open(file, "r") as f:
            return f.read().splitlines()
    except Exception as e:
        print(f"Error reading wordlist: {e}")
        return []

def crack_password(hash, algorithm, wordlist):
    print(f"Attempting to crack {algorithm} hash: {hash}")
    for word in wordlist:
        if algorithm == "md5":
            test_hash = hashlib.md5(word.encode()).hexdigest()
        elif algorithm == "sha1":
            test_hash = hashlib.sha1(word.encode()).hexdigest()
        elif algorithm == "sha256":
            test_hash = hashlib.sha256(word.encode()).hexdigest()
        else:
            print("Unsupported algorithm!")
            return None

        if test_hash == hash:
            return word
    return None

if __name__ == "__main__":
    hash = input("Enter the hash to crack: ")
    algorithm = input("Enter the hash algorithm (md5/sha1/sha256): ")
    wordlist_path = input("Enter the path to the wordlist: ")

    wordlist = read_wordlist(wordlist_path)
    if not wordlist:
        print("Wordlist is empty or not found!")
        exit()

    result = crack_password(hash, algorithm, wordlist)
    if result:
        print(f"Password found: {result}")
    else:
        print("Password not found in wordlist.")