def substring_without_repeating_character(s: str) -> int:
    set_ = set()
    n = len(s)

    ml = 0
    i = 0
    j = 0

    while i < n and j < n:
        if s[j] not in set_:
            set_.add(s[j])
            j = j + 1
            ml = max(ml, j-i)

        else:
            set_.remove(s[i])
            i = i + 1

    return ml



if __name__ == "__main__":
    s = "pwwkew"
    print(substring_without_repeating_character(s))
