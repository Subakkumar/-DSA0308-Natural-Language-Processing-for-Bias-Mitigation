class FiniteStateAutomaton:
    def __init__(self):
        self.current_state = 'start'

    def transition(self, input_char):
        if self.current_state == 'start':
            if input_char == 'a':
                self.current_state = 'seen_a'
            else:
                self.current_state = 'start'
        elif self.current_state == 'seen_a':
            if input_char == 'b':
                self.current_state = 'found_ab'
            elif input_char == 'a':
                self.current_state = 'seen_a'
            else:
                self.current_state = 'start'
        elif self.current_state == 'found_ab':
            if input_char == 'a':
                self.current_state = 'seen_a'
            else:
                self.current_state = 'start'

    def match(self, input_string):
        for char in input_string:
            self.transition(char)
        return self.current_state == 'found_ab'


def main():
    automaton = FiniteStateAutomaton()
    
    # Test cases
    test_strings = ["", "ab", "aab", "abb", "aabb", "abab", "abc", "b", "ba", "cba"]
    for string in test_strings:
        print(f"String '{string}' ends with 'ab': {automaton.match(string)}")


if __name__ == "__main__":
    main()
