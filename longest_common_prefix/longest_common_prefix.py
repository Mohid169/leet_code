def longestCommonPrefix(strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ""

        answer = ''
        min_length = min(len(word) for word in strs)

        for i in range(min_length):
            current_char = strs[0][i]
            for j in range(len(strs)):
                if current_char != strs[j][i]:
                    return answer
            answer += current_char

        return answer