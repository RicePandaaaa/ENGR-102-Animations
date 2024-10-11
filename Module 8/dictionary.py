from manim import *

class DictionaryIndexing(Scene):
    def construct(self):
        # Step 1: Typing the dictionary onto the screen
        dict_text = Text('stats = {"name": "hoid", "likes": "ramen", "instrument": "flute"}', font_size=36).to_edge(UP)
        self.play(Write(dict_text, run_time=3))  # Type the dictionary quickly
        self.wait(1)

        # Step 2: Transform the dictionary into a vertical column of key-value pairs
        key_value_pairs = [
            Text('"name": "tony"', font_size=36, color=WHITE),
            Text('"likes": "books"', font_size=36, color=WHITE),
            Text('"age": 21', font_size=36, color=WHITE),
        ]
        key_value_column = VGroup(*key_value_pairs).arrange(DOWN, buff=0.5).move_to(RIGHT * 3)  # Right side column

        self.play(Transform(dict_text, key_value_column))
        self.wait(1)

        # Step 3: Typing out "stats[]" on the left side for indexing
        stats_index_text = Text("stats[]", font_size=36).move_to(LEFT * 3)
        self.play(Write(stats_index_text))
        self.wait(0.5)

        # Step 4: Create the down arrow and position it below the index
        arrow = Arrow(start=UP, end=DOWN, color=WHITE).next_to(stats_index_text, DOWN, buff=0.5)
        self.play(Create(arrow))

        # Function to highlight the corresponding key-value pair
        def highlight_pair(pair):
            highlight_box = SurroundingRectangle(pair, color=YELLOW, buff=0.2)
            return highlight_box

        # List of index strings and corresponding key-value pairs
        indexes = ['"name"', '"likes"', '"age"']
        values = ['"tony"', '"books"', '21']  # Corresponding values

        for i, index in enumerate(indexes):
            # Update the index inside the square brackets
            new_index_text = Text(f"stats[{index}]", font_size=36).move_to(LEFT * 3)
            highlight = highlight_pair(key_value_pairs[i])

            # Display the value below the arrow
            value_text = Text(values[i], font_size=36).next_to(arrow, DOWN, buff=0.5)

            self.play(Transform(stats_index_text, new_index_text), Create(highlight))
            self.play(Write(value_text))
            self.wait(1)
            self.play(FadeOut(highlight), FadeOut(value_text))  # Remove the highlight and value for the next iteration

        # Step 5: Typing a random index that produces an error
        random_index_text = Text('stats["random"]', font_size=36).move_to(LEFT * 3)
        error_text = Text("Error", font_size=36, color=RED).next_to(arrow, DOWN, buff=0.5)

        # Show error message when indexing with a non-existent key
        self.play(Transform(stats_index_text, random_index_text))
        self.wait(1)
        self.play(Write(error_text))
        self.wait(2)



class DictionaryComparison(Scene):
    def construct(self):
        # Step 1: Add titles to the top of each side
        real_dict_label = Text("Real Dictionary", font_size=40, color=WHITE).shift(UP * 3)
        python_dict_label = Text("Python Dictionary", font_size=40, color=WHITE).shift(UP * 3)

        # Center titles to their respective halves
        real_dict_label.move_to(LEFT * 3.5 + UP * 3)
        python_dict_label.move_to(RIGHT * 3.5 + UP * 3)

        # Animate both titles appearing at the start
        self.play(Write(real_dict_label), Write(python_dict_label))
        self.wait(1)

        # Step 2: Represent a physical dictionary page on the left
        page = Rectangle(height=5, width=5, color=WHITE).move_to(LEFT * 3.5)

        # Two ellipses above the word-definition pair
        ellipsis_top_1 = Text("...", font_size=36, color=WHITE).next_to(page.get_top(), DOWN, buff=0.5)
        ellipsis_top_2 = Text("...", font_size=36, color=WHITE).next_to(ellipsis_top_1, DOWN, buff=0.5)

        # Two ellipses below the word-definition pair
        ellipsis_bottom_1 = Text("...", font_size=36, color=WHITE).next_to(page.get_bottom(), UP, buff=0.5)
        ellipsis_bottom_2 = Text("...", font_size=36, color=WHITE).next_to(ellipsis_bottom_1, UP, buff=0.5)

        # Word and definition in the middle of the page
        word_text = Text("Word: 'banana'", font_size=36, color=BLUE).move_to(page.get_center() + UP * 0.5)
        definition_text = Text("Definition: 'A fruit'", font_size=36, color=GREEN).next_to(word_text, DOWN, buff=0.5)

        # Group all elements on the left page
        page_content = VGroup(page, ellipsis_top_1, ellipsis_top_2, word_text, definition_text, ellipsis_bottom_1, ellipsis_bottom_2)
        
        # Align the entire page content to the center of the left half
        page_content.move_to(LEFT * 3.5)
        
        # Animate the page and its contents appearing
        self.play(Create(page), Write(ellipsis_top_1), Write(ellipsis_top_2), Write(ellipsis_bottom_1), Write(ellipsis_bottom_2), Write(word_text), Write(definition_text))
        self.wait(1)

        # Step 3: Add a vertical line to separate the two halves
        divider = Line(start=UP * 3.5, end=DOWN * 3.5, color=WHITE)
        self.play(Create(divider))
        self.wait(4)

        self.play(definition_text.animate.scale(1.25), run_time=0.5)
        self.play(definition_text.animate.scale(1 / 1.25), run_time=0.5)

        self.wait(2)

        # Enlarge and then shrink the word
        self.play(word_text.animate.scale(1.25), run_time=0.5)
        self.play(word_text.animate.scale(1 / 1.25), run_time=0.5)

        # Step 4: Duplicate the word and definition to move to the right side
        word_text_copy = word_text.copy()
        definition_text_copy = definition_text.copy()

        # Animate pulling the word-definition pair to the right
        self.play(
            word_text_copy.animate.move_to(RIGHT * 3.5 + UP * 0.5),
            definition_text_copy.animate.move_to(RIGHT * 3.5 + DOWN * 0.5),
        )
        self.wait(1)

        # Step 5: Create separate key and value text in the dictionary format
        key_text = Text("'banana'", font_size=36, color=BLUE)
        colon = Text(":", font_size=36, color=WHITE)
        value_text = Text("'A fruit'", font_size=36, color=GREEN)

        # Arrange key, colon, and value as a dictionary pair
        dict_pair = VGroup(key_text, colon, value_text).arrange(RIGHT, buff=0.2).move_to(RIGHT * 3.5)
        self.play(ReplacementTransform(VGroup(word_text_copy, definition_text_copy), dict_pair))
        self.wait(1)

        # Step 6: Add boxes and labels for key and value
        key_box = SurroundingRectangle(key_text, color=BLUE, buff=0.1)  # Surrounding 'apple'
        value_box = SurroundingRectangle(value_text, color=GREEN, buff=0.1)  # Surrounding 'A fruit'

        # Key and Value labels
        key_label = Text("Key", font_size=24, color=BLUE).next_to(key_box, UP)
        value_label = Text("Value", font_size=24, color=GREEN).next_to(value_box, UP)
        value_label.align_to(key_label, UP)

        # Animate the creation of the boxes and labels
        self.play(Create(key_box), Write(key_label), Create(value_box), Write(value_label))
        self.wait(1.5)

        self.play(value_box.animate.scale(1.25), 
                  value_label.animate.scale(1.25), 
                  value_text.animate.scale(1.25), run_time=0.5)

        self.play(value_box.animate.scale(1 / 1.25), 
                  value_label.animate.scale(1 / 1.25), 
                  value_text.animate.scale(1 / 1.25), run_time=0.5)
        
        self.wait(1)
        
        self.play(key_box.animate.scale(1.25), 
                  key_label.animate.scale(1.25), 
                  key_text.animate.scale(1.25), run_time=0.5)

        self.play(key_box.animate.scale(1 / 1.25), 
                  key_label.animate.scale(1 / 1.25), 
                  key_text.animate.scale(1 / 1.25), run_time=0.5)
        # Final pause to view the transition
        self.wait(2)

        self.play(FadeOut(Group(*self.mobjects)))

from manim import *

class IntroScene(Scene):
    def construct(self):
        # Step 1: Scatter key-value pairs onto the screen
        key_value_pairs = [
            ("married", "No"),
            ("name", "Alice"), 
            ("age", "25"), 
            ("city", "New York"),
            ("height", "5.8")
        ]
        
        pair_objects = []
        for key, value in key_value_pairs:
            pair = VGroup(
                Text(f"'{key}'", font_size=36, color=BLUE),
                Text(f"'{value}'", font_size=36, color=GREEN)
            ).arrange(RIGHT, buff=0.3)
            pair_objects.append(pair)

        # Scatter them around the screen
        pair_positions = [
            LEFT * 4 + UP * 2, 
            LEFT * 2 + UP * 1,
            LEFT * 3 + DOWN * 2,
            RIGHT * 2 + UP * 3,
            RIGHT * 3 + DOWN * 2,
        ]

        for pair, pos in zip(pair_objects, pair_positions):
            pair.move_to(pos)
            self.play(FadeIn(pair))

        self.wait(1)

        # Step 2: Move the pairs smoothly to the left center of the screen
        actions = []
        for factor, pair in enumerate(pair_objects):
            actions.append(pair.animate.move_to(LEFT * 3 + UP * (2 - (1 * factor))))

        self.play(*actions)

        self.wait(1)

        # Step 3: Surround all five key-value pairs with a box and add a question mark above
        all_pairs = VGroup(*pair_objects)
        surrounding_box = SurroundingRectangle(all_pairs, color=WHITE, buff=0.2)
        question_mark = Text("?", font_size=50, color=WHITE).next_to(surrounding_box, UP)

        # Animate the box and question mark appearing
        self.play(Create(surrounding_box), Write(question_mark))
        self.wait(1)

        # Step 4: List data types on the right side
        data_types = [
            Text("string", font_size=40),
            Text("int", font_size=40),
            Text("float", font_size=40),
            Text("bool", font_size=40),
            Text("list", font_size=40),
        ]

        # Arrange the data types vertically, centered on the right side
        data_types_group = VGroup(*data_types).arrange(DOWN, buff=0.5).shift(RIGHT * 3)

        self.play(FadeIn(data_types_group))
        self.wait(1)

        # Step 5: Cross out each data type one by one
        for data_type in data_types:
            strike_through = Line(start=data_type.get_left(), end=data_type.get_right(), color=RED, stroke_width=4)
            self.play(Create(strike_through))
            self.wait(0.5)

        self.wait(2)

        # Step 6: Fade out the entire screen
        self.play(FadeOut(Group(*self.mobjects)))  # Using Group instead of VGroup to avoid TypeError
        self.wait(1)

        # Step 7: Introduce "Dictionary" with a technical definition
        dictionary_title = Text("Dictionary", font_size=50, color=WHITE)
        definition_line_one = Text("A special collection, defined using curly braces, that contains key-value pairs,", font_size=30, color=WHITE)
        definition_line_two = Text("where every value has a unique key that the value is associated to.", font_size=30, color=WHITE)
        definitions = VGroup(definition_line_one, definition_line_two).arrange(DOWN, buff=0.1)

        # Code example {"name": "alice"} with boxed key and value
        key_text = Text('"name"', font_size=36, color=BLUE)
        colon = Text(":", font_size=36, color=WHITE)
        value_text = Text('"alice"', font_size=36, color=GREEN)
        left_brace = Text("{", font_size=36, color=RED).next_to(key_text, LEFT)
        right_brace = Text("}", font_size=36, color=RED).next_to(value_text, RIGHT)

        # Arrange the dictionary text
        dict_example = VGroup(left_brace, key_text, colon, value_text, right_brace).arrange(RIGHT, buff=0.3)

        # Group the title, definition, and code example together
        all_text = VGroup(dictionary_title, definitions, dict_example).arrange(DOWN, buff=0.8).move_to(ORIGIN)

        # Boxes around the key and value
        key_box = SurroundingRectangle(key_text, color=BLUE, buff=0.1)
        value_box = SurroundingRectangle(value_text, color=GREEN, buff=0.1)

        # Key and Value labels
        key_label = Text("Key", font_size=24, color=BLUE).next_to(key_box, UP * 0.5)
        value_label = Text("Value", font_size=24, color=GREEN).next_to(value_box, UP * 0.5)
        value_label.align_to(key_label, UP)


        # Animate the introduction of the dictionary elements
        self.play(Write(dictionary_title), Write(definitions))
        self.play(Write(dict_example), Create(key_box), Create(value_box), Create(key_label), Create(value_label))
        self.wait(2)

        self.play(FadeOut(Group(*self.mobjects)))
    