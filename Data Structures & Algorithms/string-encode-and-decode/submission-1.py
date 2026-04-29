class Solution:

    def encode(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ""
        sizes = [len(s) for s in strs]
        sizeStr = '#'.join([str(s) for s in sizes])
        # print(sizeStr)
        wordStr = ''.join(strs)
        result = sizeStr + '\0' + wordStr
        # print(result.split('\0'))
        return result
        
        

    def decode(self, s: str) -> List[str]:
        if len(s) == 0:
            return []
        sizeWordSplit = s.split('\0')
        sizeStr = sizeWordSplit[0]
        wordStr = sizeWordSplit[1]
        sizeStrings = sizeStr.split('#')
        print(sizeStrings)
        i = 0
        result = []
        for size in sizeStrings:
            length = int(size)
            word = wordStr[i:i+length]
            i += length
            result.append(word)
        return result
