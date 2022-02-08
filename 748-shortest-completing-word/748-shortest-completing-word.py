# class Solution:
#     def shortestCompletingWord(self, licensePlate: str, words: List[str]) -> str:
#         dictt = dict()
#         for letter in licensePlate:
#             if letter.isalpha():
#                 if letter.lower() not in dictt:
#                     dictt[letter.lower()] = 1
#                 else:
#                     dictt[letter.lower()] += 1
#         # print(dictt)
#         for word in words:
            
class Solution:
    def shortestCompletingWord(self, licensePlate: str, words: List[str]) -> str:
        valid_words = []
        plates_letters = self.count_letters(licensePlate)
        i = 0
        for word in words: 
            counter = 0
            word_letters = self.count_letters(word)
            for key in word_letters:
                if key in plates_letters:
                    if word_letters[key] >= plates_letters[key]: 
                        counter += 1
                    if counter == len(plates_letters):
                        valid_words.append((word,len(word),i))
            i +=1
        valid_words=sorted(valid_words, key=lambda x:(x[1], x[2]))
        return valid_words[0][0] 
     
    def count_letters(self,word):
        word_count = {}
        for char in word.lower():
            if char.isalpha():
                if char not in word_count:
                    word_count[char] =  1
                else:
                    word_count[char] +=  1  
        return word_count
  