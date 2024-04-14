class Solution:
  def extractMaximum(self, S):
    max_value = -1
    current_num = ""

    for char in S:
      # Check if character is a digit
      if char.isdigit():
        current_num += char
      # If not a digit or end of string, convert current number and update max
      else:
        if current_num:
          max_value = max(max_value, int(current_num))
          current_num = ""

    # Check for last number at the end of string
    if current_num:
      max_value = max(max_value, int(current_num))

    return max_value
if __name__ == '__main__':
    T = int(input())
    for _ in range(T):
        S = input()
        ob = Solution()
        print(ob.extractMaximum(S)) 
