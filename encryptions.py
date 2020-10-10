encryptionDictionary = {"a":"d", "b":"e", "c":"f","d":"g", "e":"h", "f":"i", "g":"j","h":"k","i":"l", "j":"m", "k":"n", "l":"o", "m":"p", "n":"q", "o":"r","p":"s", "q":"t", "r":"u", "s":"v", "t":"w", "u":"x", "v":"y", "w":"z", "x":"a", "y":"b", "z":"c"}

# numOfKeys = len(encryptionDictionary) 
# print(numOfKeys)

def encryptions(plaintext):
  cipherText = ""
  for char in plaintext: 
    if char in encryptionDictionary:
      cipherText += str(encryptionDictionary[char])
    else:
      print(char + "is not part of Encryption Dictionary")
      break
  return cipherText

plaintext = input("Enter a text: ")

print(plaintext)

print("You entered: "+ plaintext)
encryptedText = encryptions(plaintext)
print("Your encrypted text is: "+ encryptedText)

# def decryption(): 

# def encryptFunction(plaintext):
  
  
#   return cipherText