"""
s1 = a
s2 = a
"""

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_count = Counter(s1)

        for i in range(len(s2)):
            if s2[i] in s1_count:
                counter = sum(s1_count.values())
                character_counts = s1_count.copy()
                # window
                for j in range(i, len(s2)):
                    # If this value is counted
                    # and is still a permutation
                    if s2[j] in character_counts and character_counts[s2[j]]:
                        counter -= 1
                        character_counts[s2[j]] -= 1
                    else:
                        # move window
                        break
                if counter == 0:
                    return True
        return False
