def isPalindrome(x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        else:
            x_str = str(x)
            palindrome = [""]*len(x_str)
            for i in range(len(x_str)):
                palindrome[i] = x_str[len(x_str)-1 - i]
            palindrome_str = ''.join(palindrome)
            return palindrome_str == x_str
        
test_cases = [121, -10, 21]
answers = []

for i in range(len(test_cases)):
    answers.append(isPalindrome(test_cases[i]))
