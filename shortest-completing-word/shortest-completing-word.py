#http://blog.gainlo.co/index.php/2015/12/15/a-step-by-step-guide-to-solve-coding-problems/
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
  
        
        
        
        
        
        
        #this worked
        
#         plates_letters = {}
#         valid_words = []
#         shortest = None
#         words_dict = {} 
#         for char in licensePlate.lower():
#             if char.isalpha():
#                 if char not in plates_letters:
#                     plates_letters[char] = 1
#                 else:
#                     plates_letters[char] += 1
        
    
#         for i,word in enumerate(words):
#             counter = 0
#             for key,value in plates_letters.items():
#                 if word.count(key) >= value:
#                     counter +=1
#                 if counter == len(plates_letters):
#                     valid_words.append((word,len(word),i))
#         valid_words=sorted(valid_words, key=lambda x:(x[1], x[2]))
#         return valid_words[0][0]
   
                    
                
                
        
        
        