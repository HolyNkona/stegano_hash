"""
2022 
SimpleHash
Feel free to use it =)

"""

class hash():
    """
    class for hashing any string data
    """

    def __init__(self):
        self.special_symbols_dehash = {
            '0000' : ' ',
            '0001' : '.',
            '0002' : ',',
            '0003' : ':',
            '0004' : ';',
            '0005' : '(',
            '0006' : ')',
            '0007' : '-',
            '0008' : "'",
            '0009' : '\n',
        }
        self.special_symbols_hash = {
            ' ' : '0000',
            '.' : '0001',
            ',' : '0002',
            ':' : '0003',
            ';' : '0004',
            '(' : '0005',
            ')' : '0006',
            '-' : '0007',
            "'" : "0008",
            '\n' : '0009',
        }
        
    def gethash(self, data: str) -> dict:
        """

        Hashing and creating key to dehash for inserted data

        Args:
            data (str): data to be hashed

        Returns:
            dict (str) : (int): {'hash' : hash, 'key' : key}

        """
        self.hash = []
        self.key = []
        for letter in data:
            if letter in self.special_symbols_hash:
                self.hash.append(self.special_symbols_hash[letter])
                self.key.append('00')
                continue
            key = 80
            self.key.append(str(key))
            self.hash.append(str(ord(letter)*key))
        return {'hash' : int(''.join(self.hash)), 'key' : int(''.join(self.key))}

    def dehash(self, hash: dict) -> str:
        """
        
        Dehashing data by key from func gethash

        Args:
            hash (dict): hashed data with key from func gethash 
        
        Raise:
            ValueError: if hash or key are not int

        Returns:
            str: dehashed data

        """
        key = hash['key']
        hash = hash['hash']
        if not isinstance(hash, int) or not isinstance(key, int):
            return 'Hash or key are not int'
        self.keys = []
        self.words = []
        self.res = []
        if type(hash) == int:
            hash = str(hash)
        if type(key) == int:
            key = str(key)
        for k in [key[i:i+2] for i in range(0, len(key), 2)]:
            self.keys.append(k)
        for w in [hash[j:j+4] for j in range(0, len(hash), 4)]:
            self.words.append(w)
        for word in range(len(self.words)):
            if self.words[word] in self.special_symbols_dehash:
                self.res.append(self.special_symbols_dehash[self.words[word]])
                continue
            self.res.append(chr(int(self.words[word]) // int(self.keys[word])))
        return ''.join(self.res)

    def hide(self, data: dict, path:str = None):
        """
        
        Hiding getted from gethash func dict in file(image,sound,etc)
        
        Args:
            data (dict): hashed data with key from func gethash
            path (str): path to file example: ['test.mp3'] if file in the same folder as script

        """
        with open(path, 'ab') as file:
            file.write(str(data).encode())

    def unhide(self, path:str) -> str:
        try:
            res = dict()
            with open(path, 'rb') as file:
                hash = str(file.read()).split("{")[-1:]
                hash = hash[0].replace("\\'", "'")
            deh = hash[:-2].replace(',', '').split(' ')
            res['hash'] = int(deh[1])
            res['key'] = int(deh[3])
            return self.dehash(res) 
        except FileNotFoundError:
            return 'No such file or directory'
        except IndexError:
            return 'No hidden text in this file :)'
    
