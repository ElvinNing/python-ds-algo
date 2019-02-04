morse_code = [".-","-...","-.-.","-..",".","..-.","--.","....",
              "..",".---","-.-",".-..","--","-.","---",".--.",
              "--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
character = list('abcdefghijklmnopqrstuvwxyz')
dic = dict(zip(character, morse_code))

set = {''.join(dic.get(c) for c in word) for word in words}