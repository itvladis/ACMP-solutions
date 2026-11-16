# Power of a string

The k-th power of a string s is s repeated k times. The k-th root of s is a string t such that
t repeated k times equals s. Given s and a nonzero integer k, output the k-th power of s if k is
positive, or the |k|-th root of s if k is negative.

**Input** (`input.txt`): a string s of lowercase Latin letters (length 1 to 1000), then the integer k.
**Output** (`output.txt`): the resulting string, truncated to its first 1023 characters if it
is longer; `NO SOLUTION` if the root does not exist.

Examples: `abc`, `3` → `abcabcabc`; `abcdabcd`, `-2` → `abcd`; `abcd`, `-4` → `NO SOLUTION`.

https://acmp.ru/index.asp?main=task&id_task=70
