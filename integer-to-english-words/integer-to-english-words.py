class Solution:
    def numberToWords(self, num):
        chunks = ['Thousand','Million','Billion']
        tens = ['','','Twenty','Thirty','Forty','Fifty','Sixty','Seventy','Eighty','Ninety']
        one_19 = ['','One','Two','Three','Four','Five','Six',
                 'Seven','Eight','Nine','Ten','Eleven','Twelve','Thirteen','Fourteen','Fifteen',
                 'Sixteen','Seventeen','Eighteen','Nineteen']
        def to_words(num):
            if num == 0:
                return []
            if num<20:
                return [one_19[num]]
            if num<100:
                return [tens[num//10]] + to_words(num%10)
            if num<1000:
                return [one_19[num//100], 'Hundred'] + to_words(num%100)
            for power,chunk in enumerate(chunks,1):
                if num < 1000**(power+1):
                    return to_words(num//1000**(power)) + [chunk] + to_words(num%1000**(power))
        return ' '.join(to_words(num)) or 'Zero'
                
                
                
                
        
        
        
        
        
   