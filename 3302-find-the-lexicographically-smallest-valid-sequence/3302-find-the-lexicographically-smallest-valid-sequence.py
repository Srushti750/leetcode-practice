from bisect import bisect_left

class Solution:
    def validSequence(self, word1: str, word2: str) -> List[int]:
        n = len(word1)
        m = len(word2)
        if m>n:
            return []
        
        positions = [[] for _ in range(26)]
        for i, ch in enumerate(word1):
            positions[ord(ch) - ord('a')].append(i)

        exact = [-1] * (m+1)
        one = [-1] * (m+1)
        exact[m] = n
        one[m] = n

        for j in range(m-1, -1, -1):
            ch = ord(word2[j]) - ord('a')
            arr = positions[ch]
            # To find the exact match
            k = bisect_left(arr, exact[j+1])
            if k==0:
                exact[j] = -1
            else:
                exact[j] = arr[k-1]
            
            # Matches the current character
            k = bisect_left(arr, one[j+1])
            if k == 0:
                candidate_exact = -1
            else:
                candidate_exact = arr[k-1]
            # Mismatched the current character
            limit = exact[j+1]
            candidate_mismatch = limit - 1
            if candidate_mismatch >= 0:
                if word1[candidate_mismatch] == word2[j]:
                    candidate_mismatch -= 1
            if candidate_mismatch < 0:
                candidate_misamatch = -1
            
            one[j] = max(candidate_exact, candidate_mismatch)
            if one[j] == -1:
                return []
        result = []
        previous = -1
        mismatch_used = False
        for j in range(m):
            start = previous + 1
            # If mismatch has already used
            if mismatch_used:
                ch = ord(word2[j]) - ord('a')
                arr = positions[ch]
                k = bisect_left(arr, start)
                if k == len(arr):
                    return []
                
                candidate = arr[k]
                if candidate >= exact[j+1]:
                    return []
                result.append(candidate)
                previous = candidate
                continue
            
            # If mismatch has not used
            c = ord(word2[j]) - ord('a')
            arr = positions[c]
            k = bisect_left(arr, start)
            if k == len(arr):
                exact_candidate = -1
            else:
                exact_candidate = arr[k]
            
            if exact_candidate != -1:
                if exact_candidate >= one[j+1]:
                    exact_candidate = -1
            mismatch_candidate = -1
            if start < n:
                if word1[start] != word2[j]:
                    mismatch_candidate = start
                elif start+1 < n:
                    mismatch_candidate = start + 1
            if mismatch_candidate != -1:
                if mismatch_candidate >= exact[j+1]:
                    mismatch_candidate = -1
            
            if exact_candidate == -1 and mismatch_candidate == -1:
                return []
            
            if(mismatch_candidate != -1 and (exact_candidate == -1 or mismatch_candidate < exact_candidate)):
                result.append(mismatch_candidate)
                previous = mismatch_candidate
                mismatch_used = True
            else:
                result.append(exact_candidate)
                previous = exact_candidate
        return result