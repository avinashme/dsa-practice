class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        final_dict = {}

        for i in strs:
            sort_string = "".join(sorted(i))

            if sort_string not in final_dict:
                final_dict[sort_string] = [i]
            else:
                final_dict[sort_string].append(i)

        return list(final_dict.values())
