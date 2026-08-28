class Solution:
    def lexGreaterPermutation(self, s: str, target: str) -> str:
        n = len(s)
        freq = [0]*26
        for i in s:
            freq[ord(i) - ord('a')] += 1
        
        result_string = []
        # Walk left-right until target[i] is equal to the current character
        for i in range(n):
            current_character = ord(target[i]) - ord('a')

            if freq[current_character] > 0:
                result_string.append(target[i])
                freq[current_character] -= 1
            else:
                # If target[i] is not equal to current character then find smallest character than target[i]
                for ch in range(current_character + 1, 26):
                    if freq[ch] > 0:
                        character = chr(ch + ord('a'))
                        result_string.append(character)
                        freq[ch] -= 1

                        # Remaining character in sorted order
                        for c in range(26):
                            result_string.extend([chr(c + ord('a'))] * freq[c])
                        
                        return ''.join(result_string)
                break
        print(result_string)
        print(freq)
        # When we matched the entire target we need greater than that so we backtrach by characters
        for i in range(len(result_string)-1, -1, -1):
            character = ord(result_string[i]) - ord('a')
            freq[character] += 1

            # Now smallest character greater than current
            for ch in range(character+1, 26):
                if freq[ch] > 0:
                    result = result_string[:i]
                    result.append(chr(ch + ord('a')))
                    freq[ch] -= 1

                    # Once found, fill in the rest of characters
                    for c in range(26):
                        result.extend([chr(c + ord('a'))] * freq[c])
                    
                    return ''.join(result)
        return ""