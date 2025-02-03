class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        morse_code = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        morse_dict = {chr(97 + i): morse_code[i] for i in range(26)}
        fin_arr = {}
        for word in words:
            st = ""
            for char in word:
                st+=morse_dict[char]
            
            if not st in fin_arr:
                fin_arr[st]=1
        return len(fin_arr)