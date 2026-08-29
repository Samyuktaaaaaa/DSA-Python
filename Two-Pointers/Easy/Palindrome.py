def is_palindrome(s):
    s = s.lower()

    left = 0
    right = len(s) - 1

    while left < right:
        if s[left] != s[right]:
            return False

        left += 1
        right -= 1

    return True


s = input("Enter a string: ")
print(is_palindrome(s))