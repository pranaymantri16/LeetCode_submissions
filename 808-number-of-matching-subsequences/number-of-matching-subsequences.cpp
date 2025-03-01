#include <vector>
#include <string>
#include <unordered_map>
using namespace std;

class Solution {
public:
    bool isSubsequence(const string &s, const string &word) {
        int sp = 0, wp = 0;
        while (sp < s.size() && wp < word.size()) {
            if (s[sp] == word[wp]) {
                wp++;
            }
            sp++;
        }
        return wp == word.size();
    }

    int numMatchingSubseq(string s, vector<string>& words) {
        unordered_map<string, int> wordCount;
        int count = 0;
        for (const string &word : words) {
            wordCount[word]++;
        }
        
        for (const auto &entry : wordCount) {
            if (isSubsequence(s, entry.first)) {
                count += entry.second;
            }
        }
        
        return count;
    }
};