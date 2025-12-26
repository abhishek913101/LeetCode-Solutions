class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        result = []
        i = 0
        while i < len(words):
            line_words = []
            current_len = 0
            start_index = i
            while i < len(words) and current_len + len(words[i]) + len(line_words) <= maxWidth:
                line_words.append(words[i])
                current_len += len(words[i])
                i += 1
            num_words = len(line_words)
            total_spaces = maxWidth - current_len

            if num_words == 1 or i == len(words):
                formatted_line = " ".join(line_words)
                formatted_line += " " * (maxWidth - len(formatted_line))
            else:
                gaps = num_words - 1
                base_spaces = total_spaces // gaps
                extra_spaces = total_spaces % gaps
                
                formatted_line = ""
                for j in range(num_words):
                    formatted_line += line_words[j]
                    if j < gaps:
                        spaces_to_add = base_spaces + (1 if j < extra_spaces else 0)
                        formatted_line += " " * spaces_to_add
            
            result.append(formatted_line)
        return result