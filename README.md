# stegano_hash
Simple hash algorithm + some steganography. Script help you to hash some text and hide it to any file (image,media etc)

Usage:

  1. Create an object of class hash
  <code>
  from stegano_hash import hash
  
  data = hash()
  </code>
  
  2. Try to hash something
  <code>
  from stegano_hash import hash
  
  data = hash().gethash('any text over here')
  </code>
  gethash returns dict {'hash' : hash, 'key' : key}
  
  3. Hide hashed text
  <code>
  from stegano_hash import hash
  
  data = hash().gethash('any text over here')
  hash().hide('path_to_file.mp3', data)
  </code>
  Now choosen file contains your hashed data
  
  4. Unhide your data
  <code>
  from stegano_hash import hash
  
  data = hash().gethash('any text over here')
  hash().hide('path_to_file.mp3', data)
  res = hash().unhide('path_to_file.mp3')
  print(res)
  </code>
  
  5. To dehash data use dehash
  <code>
  from stegano_hash import hash
  
  data = hash().gethash('any text over here')
  res = hash().dehash(data)
  print(res)
  </code>
