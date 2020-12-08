class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        
        paragraph = re.sub(r'[^\w]', ' ', paragraph)
        
        words = [word for word in paragraph.lower().split() if word not in banned]
        
        a = {}
        
        for i in words:
            if i not in a:
                a[i] = 0
            a[i] += 1
        
        count = 0
        result = 't'
        
        for j in a:
            if a[j] > count:
                count = a[j]
                result = j
                
                
        return result
        
