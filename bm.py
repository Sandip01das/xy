def bad_char_table(pattern):
  badCharTable = {}
  for i in range(len(pattern) - 1):
    badCharTable[pattern[i]] = len(pattern) - i - 1
  return badCharTable

def boyer_moore(text, pattern):
  n = len(text)
  m = len(pattern)
  badCharTable = bad_char_table(pattern)

  i = 0
  while i <= n - m:
    j = m - 1
    while j >= 0 and text[i + j] == pattern[j]:
      j -= 1
    if j == -1:  # Pattern found
      return i
    shift = badCharTable.get(text[i + m - 1], m)  # Use bad character heuristic
    i += max(1, shift)  # Consider a minimum shift of 1
  return -1  # Pattern not found

# Example usage
text = "THIS IS A SAMPLE TEXT"
pattern = "hhf"
result = boyer_moore(text, pattern)
if result != -1:
  print("Pattern found at index:", result)
else:
  print("Pattern not found in the text")
