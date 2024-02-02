def levenshtein_distance(s1, s2):
    if len(s1) < len(s2):
        return levenshtein_distance(s2, s1)

    if len(s2) == 0:
        return len(s1)

    previous_row = range(len(s2) + 1)

    for i, c1 in enumerate(s1):
        current_row = [i + 1]

        for j, c2 in enumerate(s2):
            insertions = previous_row[j + 1] + 1
            deletions = current_row[j] + 1
            substitutions = previous_row[j] + (c1 != c2)

            current_row.append(min(insertions, deletions, substitutions))

        previous_row = current_row

    return previous_row[-1]

# Examples
string1 = "ULTRAMARINE BLUE"
string2 = "HIBISCUS" #"5858-81-1"
string3 = "Talk to me"

distance_1_2 = levenshtein_distance(string1, string2)
distance_1_3 = levenshtein_distance(string1, string3)
distance_2_3 = levenshtein_distance(string2, string3)

print(f"Levenshtein distance between 'ULTRAMARINE BLUE' and '5858-81-1': {distance_1_2}")
print(f"Levenshtein distance between 'ULTRAMARINE BLUE' and 'forest': {distance_1_3}")
print(f"Levenshtein distance between '5858-81-1' and 'forest': {distance_2_3}")
