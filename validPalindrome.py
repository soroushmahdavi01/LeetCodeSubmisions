class Solution:
    def isPalindrome(self, s: str) -> bool:
        news = [];
        for current_read in range(len(s)):
            if (s[current_read].isalnum()):
                news.append(s[current_read].lower());

        front = 0;
        back = len(news) - 1;
        if len(news) == 0:
            return True
        while True:
            if (news[front] != news[back]):
                return False;
            front = front + 1;
            back = back - 1;
            if (front >= back):
                break;
        return True;
