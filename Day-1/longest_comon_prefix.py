from typing import List
def longest_prefix(words: List[str]) -> List[str]:
    if words == "":
        return ""
    if len(words) == 1:
        return words[0]
    words.sort()
    prefix = ""
    for i in range(len(words[0])):
        if words[0][i] == words[-1][i]:
            prefix = prefix + words[0][i]
        else:
            break
    return prefix


if __name__ == "__main__":
    strs = ["flower", "flow", "flight", "flacter"]
    print(longest_prefix(strs))
