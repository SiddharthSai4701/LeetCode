/**
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

 

Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
 

Constraints:

1 <= strs.length <= 200
0 <= strs[i].length <= 200
strs[i] consists of only lowercase English letters if it is non-empty.

 */

/**
 * @param {string[]} strs
 * @return {string}
 */
var longestCommonPrefix = function(strs) {
    if (strs.length === 0) return "";

    strs.sort((a, b) => a.length - b.length);
    let prefix = strs[0];

    for (let str of strs) {
        let i = 0;
        while (i < prefix.length && str[i] === prefix[i]) {
            i++;
        }
        prefix = prefix.slice(0, i);

        if (prefix === "") return "";
    }

    return prefix;
};
