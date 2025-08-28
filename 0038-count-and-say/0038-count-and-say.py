class Solution(object):
    def countAndSay(self, n):
        s = "1"  # Start with the base case

        for _ in range(n - 1):  # Repeat n-1 times
            temp = ""           # To build the next string
            i = 0               # Pointer for reading the string

            while i < len(s):
                count = 1  # At least one character found

                # Count how many times this char repeats consecutively
                while i + 1 < len(s) and s[i] == s[i + 1]:
                    count += 1
                    i += 1

                # Add "count + character" to the temp result
                temp += str(count) + s[i]

                # Move to the next new character
                i += 1

            # Update s for the next iteration
            s = temp

        return s
