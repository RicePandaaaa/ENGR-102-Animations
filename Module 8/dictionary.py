from manim import *

class LoopingThroughDictionary(Scene):
    def construct(self):
        code_text = (
            "stats = {'name': 'hoid', 'likes': 'ramen', 'instrument': 'flute'}\n"
            "for key in stats:\n"
            "    print(key, stats[key])"
        )
        code_display = Code(
            code=code_text,
            tab_width=4,
            background="window",
            language="python",
            font="Monospace",
        ).scale(0.8).to_edge(UP)

        self.wait(5)
        self.play(FadeIn(code_display))
        self.wait(3)

        output_box = Rectangle(width=6, height=5, color=WHITE).next_to(code_display, DOWN * 3).to_edge(LEFT)
        output_text = Text("Output:", font_size=24).next_to(output_box, UP)

        debugger_box = Rectangle(width=6, height=5, color=WHITE).next_to(code_display, DOWN * 3).to_edge(RIGHT)
        debugger_text = Text("Debugger:", font_size=24).next_to(debugger_box, UP)

        key_value_pairs = [
            VGroup(Text("'name'", font_size=24), Text(":", font_size=20), Text("'hoid'", font_size=24)).arrange(RIGHT),
            VGroup(Text("'likes'", font_size=24), Text(":", font_size=20), Text("'ramen'", font_size=24)).arrange(RIGHT),
            VGroup(Text("'instrument'", font_size=24), Text(":", font_size=20), Text("'flute'", font_size=24)).arrange(RIGHT),
        ]
        dict_box = Rectangle(width=3.4, height=2, color=PINK).next_to(debugger_box, UP).shift(DOWN * 2.6)
        dict_text = Text("stats", font_size=20, color=PINK).next_to(dict_box, UP).shift(DOWN * 0.20)
        key_value_column = VGroup(*key_value_pairs).arrange(DOWN, buff=0.3).next_to(dict_text, DOWN * 1.5)
        
        loop_variable_box = Rectangle(width=2, height=1, color=BLUE).next_to(dict_box, DOWN).shift(LEFT * 1.1 + DOWN * 0.2)
        loop_variable_text = Text("key", font_size=20, color=BLUE).next_to(loop_variable_box, UP).shift(DOWN * 0.20)

        stats_key_box = Rectangle(width=2, height=1, color=GREEN).next_to(dict_box, DOWN).shift(RIGHT * 1.1 + DOWN * 0.2)
        stats_key_text = Text("stats[key]", font_size=20, color=GREEN).next_to(stats_key_box, UP).shift(DOWN * 0.20)

        self.play(FadeIn(output_box), FadeIn(output_text), 
                  FadeIn(debugger_box), FadeIn(debugger_text))

        self.wait(10)

        arrow = Arrow(start=LEFT, end=RIGHT, color=RED, stroke_width=6)
        arrow.next_to(code_display, LEFT).shift(UP * 0.13)
        self.play(Create(arrow))
        self.wait(3)

        self.play(FadeIn(dict_box), FadeIn(dict_text), FadeIn(key_value_column))
        self.wait(5)

        self.play(arrow.animate.shift(DOWN * 0.25))
        self.wait(5)

        self.play(FadeIn(loop_variable_box), FadeIn(loop_variable_text))
        self.wait(10)

        previous_key, previous_value = None, None
        original_output = None

        for _, (key_text, _, value_text) in enumerate(key_value_pairs):
            key_box = SurroundingRectangle(key_text, color=BLUE, buff=0.1)
            value_box = SurroundingRectangle(value_text, color=GREEN, buff=0.1)
            self.play(Create(key_box))
            self.wait(10)

            if previous_key is not None:
                self.play(FadeOut(previous_key))
            previous_key = key_text.copy()
            self.play(previous_key.animate.next_to(loop_variable_text, UP).shift(DOWN * 1.15))
            self.wait(10)

            self.play(arrow.animate.shift(DOWN * 0.25))
            self.wait(10)

            if previous_value is not None:
                self.play(FadeOut(previous_value))
            else:
                self.play(FadeIn(stats_key_box), FadeIn(stats_key_text))
                self.wait(10)

            self.play(Create(value_box))
            self.wait(10)
            previous_value = value_text.copy()
            self.play(previous_value.animate.next_to(stats_key_text, UP).shift(DOWN * 1.15))
            self.wait(10)

            output_key = Text(key_text.text[1:-1], font_size = 20).next_to(loop_variable_text, UP).shift(DOWN * 1.15)
            output_value = Text(value_text.text[1:-1], font_size=20).next_to(dict_box, DOWN).shift(RIGHT * 1.1 + DOWN * 0.2)
            if not original_output:
                self.play(output_key.animate.next_to(output_text, DOWN * 1.7 + LEFT * 6, aligned_edge=LEFT))
                self.play(output_value.animate.next_to(output_key, RIGHT, buff=0.15).align_to(output_key, DOWN))
            else:
                self.play(output_key.animate.next_to(original_output, DOWN, aligned_edge=LEFT))
                self.play(output_value.animate.next_to(output_key, RIGHT, buff=0.15).align_to(output_key, DOWN))

            original_output = output_key.copy()

            self.wait(10)

            self.play(FadeOut(key_box), FadeOut(value_box))
            self.wait(10)

            self.play(arrow.animate.shift(UP * 0.25))
            self.wait(10)

        self.wait(2)

class DictionaryIndexing(Scene):
    def construct(self):
        dict_text = Text('stats = {"name": "hoid", "likes": "ramen", "instrument": "flute"}', font_size=36).to_edge(UP)
        self.play(Write(dict_text, run_time=3))
        self.wait(1)

        key_value_pairs = [
            VGroup(Text('"name"', font_size=36), Text(":", font_size=36), Text('"hoid"', font_size=36)).arrange(RIGHT, buff=0.5),
            VGroup(Text('"likes"', font_size=36), Text(":", font_size=36), Text('"ramen"', font_size=36)).arrange(RIGHT, buff=0.5),
            VGroup(Text('"instrument"', font_size=36), Text(":", font_size=36), Text('"flute"', font_size=36)).arrange(RIGHT, buff=0.5)
        ]
        key_value_column = VGroup(*key_value_pairs).arrange(DOWN, buff=0.5).move_to(RIGHT * 3)

        self.play(Transform(dict_text, key_value_column))
        self.wait(1)

        stats_index_text = Text("stats[]", font_size=36).move_to(LEFT * 3 + UP * 1)
        self.play(Write(stats_index_text))
        self.wait(0.5)

        arrow = Arrow(start=UP, end=DOWN, color=WHITE).next_to(stats_index_text, DOWN, buff=0.5)
        self.play(Create(arrow))

        indexes = ['"name"', '"likes"', '"instrument"']

        for i, index in enumerate(indexes):
            self.play(FadeOut(stats_index_text), run_time=0.3)

            stats_index_text = Text(f"stats[{index}]", font_size=36).move_to(LEFT * 3 + UP * 1)
            self.play(FadeIn(stats_index_text), run_time=0.5)
            self.wait(1)

            key, _, value = key_value_pairs[i]
            key_box = SurroundingRectangle(key, color=BLUE, buff=0.2)
            value_box = SurroundingRectangle(value, color=GREEN, buff=0.2)
            self.play(Create(key_box))
            self.wait(1)
            self.play(Create(value_box))
            self.wait(0.5)

            value_copy = value.copy().next_to(arrow, DOWN, buff=0.5)
            self.play(Transform(value, value_copy))
            self.wait(1)

            self.play(FadeOut(key_box), FadeOut(value_box), FadeOut(value))
            value.move_to(key_value_pairs[i][1])

        self.play(FadeOut(stats_index_text), run_time=0.3)
        stats_index_text = Text('stats["random"]', font_size=36).move_to(LEFT * 3 + UP * 1)
        self.play(FadeIn(stats_index_text), run_time=0.5)

        self.wait(2)

        error_text = Text("Error", font_size=36, color=RED).next_to(arrow, DOWN, buff=0.5)
        self.play(Write(error_text))
        self.wait(2)

class DictionaryComparison(Scene):
    def construct(self):
        real_dict_label = Text("Real Dictionary", font_size=40, color=WHITE).shift(UP * 3)
        python_dict_label = Text("Python Dictionary", font_size=40, color=WHITE).shift(UP * 3)

        real_dict_label.move_to(LEFT * 3.5 + UP * 3)
        python_dict_label.move_to(RIGHT * 3.5 + UP * 3)

        self.play(Write(real_dict_label), Write(python_dict_label))
        self.wait(1)

        page = Rectangle(height=5, width=5, color=WHITE).move_to(LEFT * 3.5)

        ellipsis_top_1 = Text("...", font_size=36, color=WHITE).next_to(page.get_top(), DOWN, buff=0.5)
        ellipsis_top_2 = Text("...", font_size=36, color=WHITE).next_to(ellipsis_top_1, DOWN, buff=0.5)

        ellipsis_bottom_1 = Text("...", font_size=36, color=WHITE).next_to(page.get_bottom(), UP, buff=0.5)
        ellipsis_bottom_2 = Text("...", font_size=36, color=WHITE).next_to(ellipsis_bottom_1, UP, buff=0.5)

        word_text = Text("Word: 'banana'", font_size=36, color=BLUE).move_to(page.get_center() + UP * 0.5)
        definition_text = Text("Definition: 'A fruit'", font_size=36, color=GREEN).next_to(word_text, DOWN, buff=0.5)

        page_content = VGroup(page, ellipsis_top_1, ellipsis_top_2, word_text, definition_text, ellipsis_bottom_1, ellipsis_bottom_2)
        
        page_content.move_to(LEFT * 3.5)
        
        self.play(Create(page), Write(ellipsis_top_1), Write(ellipsis_top_2), Write(ellipsis_bottom_1), Write(ellipsis_bottom_2), Write(word_text), Write(definition_text))
        self.wait(1)

        divider = Line(start=UP * 3.5, end=DOWN * 3.5, color=WHITE)
        self.play(Create(divider))
        self.wait(4)

        self.play(definition_text.animate.scale(1.25), run_time=0.5)
        self.play(definition_text.animate.scale(1 / 1.25), run_time=0.5)

        self.wait(2)

        self.play(word_text.animate.scale(1.25), run_time=0.5)
        self.play(word_text.animate.scale(1 / 1.25), run_time=0.5)

        word_text_copy = word_text.copy()
        definition_text_copy = definition_text.copy()

        self.play(
            word_text_copy.animate.move_to(RIGHT * 3.5 + UP * 0.5),
            definition_text_copy.animate.move_to(RIGHT * 3.5 + DOWN * 0.5),
        )
        self.wait(1)

        key_text = Text("'banana'", font_size=36, color=BLUE)
        colon = Text(":", font_size=36, color=WHITE)
        value_text = Text("'A fruit'", font_size=36, color=GREEN)

        dict_pair = VGroup(key_text, colon, value_text).arrange(RIGHT, buff=0.2).move_to(RIGHT * 3.5)
        self.play(ReplacementTransform(VGroup(word_text_copy, definition_text_copy), dict_pair))
        self.wait(1)

        key_box = SurroundingRectangle(key_text, color=BLUE, buff=0.1)
        value_box = SurroundingRectangle(value_text, color=GREEN, buff=0.1)

        key_label = Text("Key", font_size=24, color=BLUE).next_to(key_box, UP)
        value_label = Text("Value", font_size=24, color=GREEN).next_to(value_box, UP)
        value_label.align_to(key_label, UP)

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
        self.wait(2)

        self.play(FadeOut(Group(*self.mobjects)))


class IntroScene(Scene):
    def construct(self):
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

        actions = []
        for factor, pair in enumerate(pair_objects):
            actions.append(pair.animate.move_to(LEFT * 3 + UP * (2 - (1 * factor))))

        self.play(*actions)

        self.wait(1)

        all_pairs = VGroup(*pair_objects)
        surrounding_box = SurroundingRectangle(all_pairs, color=WHITE, buff=0.2)
        question_mark = Text("?", font_size=50, color=WHITE).next_to(surrounding_box, UP)

        self.play(Create(surrounding_box), Write(question_mark))
        self.wait(1)

        data_types = [
            Text("string", font_size=40),
            Text("int", font_size=40),
            Text("float", font_size=40),
            Text("bool", font_size=40),
            Text("list", font_size=40),
        ]

        data_types_group = VGroup(*data_types).arrange(DOWN, buff=0.5).shift(RIGHT * 3)

        self.play(FadeIn(data_types_group))
        self.wait(1)

        for data_type in data_types:
            strike_through = Line(start=data_type.get_left(), end=data_type.get_right(), color=RED, stroke_width=4)
            self.play(Create(strike_through))
            self.wait(0.5)

        self.wait(2)

        self.play(FadeOut(Group(*self.mobjects)))
        self.wait(1)

        dictionary_title = Text("Dictionary", font_size=50, color=WHITE)
        definition_line_one = Text("A special collection, defined using curly braces, that contains key-value pairs,", font_size=30, color=WHITE)
        definition_line_two = Text("where every value has a unique key that the value is associated to.", font_size=30, color=WHITE)
        definitions = VGroup(definition_line_one, definition_line_two).arrange(DOWN, buff=0.1)

        key_text = Text('"name"', font_size=36, color=BLUE)
        colon = Text(":", font_size=36, color=WHITE)
        value_text = Text('"alice"', font_size=36, color=GREEN)
        left_brace = Text("{", font_size=36, color=RED).next_to(key_text, LEFT)
        right_brace = Text("}", font_size=36, color=RED).next_to(value_text, RIGHT)

        dict_example = VGroup(left_brace, key_text, colon, value_text, right_brace).arrange(RIGHT, buff=0.3)

        all_text = VGroup(dictionary_title, definitions, dict_example).arrange(DOWN, buff=0.8).move_to(ORIGIN)

        key_box = SurroundingRectangle(key_text, color=BLUE, buff=0.1)
        value_box = SurroundingRectangle(value_text, color=GREEN, buff=0.1)

        key_label = Text("Key", font_size=24, color=BLUE).next_to(key_box, UP * 0.5)
        value_label = Text("Value", font_size=24, color=GREEN).next_to(value_box, UP * 0.5)
        value_label.align_to(key_label, UP)


        self.play(Write(dictionary_title), Write(definitions))
        self.play(Write(dict_example), Create(key_box), Create(value_box), Create(key_label), Create(value_label))
        self.wait(2)

        self.play(FadeOut(Group(*self.mobjects)))


class KeysAndValuesAnimation(Scene):
    def construct(self):
        keys_function = Text("stats.keys()", font_size=48, color=BLUE).move_to(LEFT * 3)
        values_function = Text("stats.values()", font_size=48, color=GREEN).move_to(RIGHT * 3)

        self.play(Write(keys_function), Write(values_function))
        self.wait(1)

        self.play(keys_function.animate.scale(1.25), run_time=0.5)
        self.play(keys_function.animate.scale(1 / 1.25), run_time=0.5)

        self.play(values_function.animate.scale(1.25), run_time=0.5)
        self.play(values_function.animate.scale(1 / 1.25), run_time=0.5)

        self.play(FadeOut(keys_function), FadeOut(values_function))
        self.wait(1)

        dict_text = Text('stats = {"name": "hoid", "likes": "ramen", "instrument": "flute"}', font_size=36).to_edge(UP)
        self.play(Write(dict_text))
        self.wait(1)

        keys_label = Text("stats.keys()", font_size=36, color=BLUE).move_to(LEFT * 5 + UP * 2)
        values_label = Text("stats.values()", font_size=36, color=GREEN).move_to(LEFT + UP * 2)

        self.play(Write(keys_label), Write(values_label))
        self.wait(1)

        key_value_pairs = [
            VGroup(Text('"name"', font_size=36), Text(":", font_size=36), Text('"hoid"', font_size=36)).arrange(RIGHT),
            VGroup(Text('"likes"', font_size=36), Text(":", font_size=36), Text('"ramen"', font_size=36)).arrange(RIGHT),
            VGroup(Text('"instrument"', font_size=36), Text(":", font_size=36), Text('"flute"', font_size=36)).arrange(RIGHT)
        ]

        key_value_column = VGroup(*key_value_pairs).arrange(DOWN, buff=0.5).move_to(RIGHT * 4)
        self.play(FadeIn(key_value_column))
        self.wait(1)

        for i, pair in enumerate(key_value_pairs):
            key, _, value = pair

            key_box = SurroundingRectangle(key, color=BLUE, buff=0.1)
            value_box = SurroundingRectangle(value, color=GREEN, buff=0.1)

            self.play(Create(key_box), Create(value_box))
            self.wait(0.5)

            key_copy = key.copy().move_to(keys_label.get_center() + DOWN * (i + 1))
            value_copy = value.copy().move_to(values_label.get_center() + DOWN * (i + 1))

            self.play(TransformFromCopy(key, key_copy), TransformFromCopy(value, value_copy))
            self.wait(0.5)

            self.play(FadeOut(key_box), FadeOut(value_box))

        self.wait(2)

        self.play(FadeOut(Group(*self.mobjects)))
        self.wait(1)

        keys_function = Text("stats.keys()", font_size=48, color=BLUE).move_to(LEFT * 3 + UP * 1.5)
        values_function = Text("stats.values()", font_size=48, color=GREEN).move_to(RIGHT * 3 + UP * 1.5)

        self.play(FadeIn(keys_function), FadeIn(values_function))
        self.wait(1)

        arrow_keys = Arrow(start=UP, end=DOWN, color=WHITE).next_to(keys_function, DOWN)
        arrow_values = Arrow(start=UP, end=DOWN, color=WHITE).next_to(values_function, DOWN)
        self.play(Create(arrow_keys), Create(arrow_values))
        self.wait(0.5)

        list_text_keys = Text("list", font_size=36, color=WHITE).next_to(arrow_keys, DOWN)
        list_text_values = Text("list", font_size=36, color=WHITE).next_to(arrow_values, DOWN)
        self.play(FadeIn(list_text_keys), FadeIn(list_text_values))

        strike_through_keys = Line(start=list_text_keys.get_left(), end=list_text_keys.get_right(), color=RED, stroke_width=4)
        strike_through_values = Line(start=list_text_values.get_left(), end=list_text_values.get_right(), color=RED, stroke_width=4)

        self.play(Create(strike_through_keys), Create(strike_through_values))
        self.wait(2)

        iterator_text_keys = Text("view object", font_size=36, color=WHITE).next_to(arrow_keys, DOWN)
        iterator_text_values = Text("view object", font_size=36, color=WHITE).next_to(arrow_values, DOWN)
        note_top = Text("*You can iterate through a view object like a list,", font_size=36, color=RED).shift(DOWN * 2.5)
        note_bot = Text("but you cannot use any of the list functions!", font_size=36, color=RED).next_to(note_top, DOWN)
        self.play(ReplacementTransform(list_text_keys, iterator_text_keys),
                  ReplacementTransform(list_text_values, iterator_text_values),
                  FadeOut(strike_through_keys), FadeOut(strike_through_values), FadeIn(note_top), FadeIn(note_bot))
        self.wait(5)

        list_keys_function = Text("list(stats.keys())", font_size=48, color=BLUE).move_to(LEFT * 3 + UP)
        list_values_function = Text("list(stats.values())", font_size=48, color=GREEN).move_to(RIGHT * 3 + UP)

        list_text_keys = Text("list", font_size=36, color=WHITE).next_to(arrow_keys, DOWN)
        list_text_values = Text("list", font_size=36, color=WHITE).next_to(arrow_values, DOWN)

        self.play(ReplacementTransform(keys_function, list_keys_function), 
                  ReplacementTransform(values_function, list_values_function),
                  ReplacementTransform(iterator_text_keys, list_text_keys),
                  ReplacementTransform(iterator_text_values, list_text_values),
                  FadeOut(note_top), FadeOut(note_bot))
        self.wait(2)

        self.play(FadeOut(Group(*self.mobjects)))
        self.wait(2)

class TitleAnimation(Scene):
    def construct(self):
        # Step 1: Display the title and subheader
        title = Text("Dictionaries", font_size=64)
        subtitle = Text("& Top Down Design", font_size=48).next_to(title, DOWN)
        course_info = Text("ENGR 102 - Fall 2024", font_size=36).next_to(subtitle, DOWN)

        # Center the text and display
        title_group = VGroup(title, subtitle, course_info).arrange(DOWN, buff=0.5).move_to(ORIGIN)
        self.play(Write(title_group))
        self.wait(10)

        # Step 2: Fade out the title group
        self.play(FadeOut(title_group))
        self.wait(1)

        # Step 3: Fade in the table of contents
        table_of_contents = [
            Text("1. Why we use dictionaries", font_size=30),
            Text("2. What they look like", font_size=30),
            Text("3. Indexing a dictionary", font_size=30),
            Text("4. Looping through a dictionary", font_size=30),
            Text("5. keys() and values()", font_size=30),
            Text("6. What is top down design", font_size=30),
            Text("7. Practice Problem: Average Grade", font_size=30),
        ]

        # Step 4: Slowly write each content line by line
        previous_line = None
        for line in table_of_contents:
            current_line = line.to_edge(UP).shift(LEFT * 0.75 + DOWN)
            if previous_line is not None:
                current_line = line.next_to(previous_line, DOWN).align_to(previous_line, LEFT)

            self.play(FadeIn(current_line))
            previous_line = current_line.copy()

            self.wait(1)

        self.play(FadeOut(Group(*self.mobjects)))
        self.wait(2)


