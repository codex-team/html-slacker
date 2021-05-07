from htmlslacker import HTMLSlacker


def test_example_1():
    html = """
    <b>Hello</b><br>
    There is <i>something</i> interesting about <code>this doc</code>

    <p>
    And <a href="http://example.com/">here is a
    link in a paragraph!</a>
    </p>
    """
    expected = "*Hello*\nThere is _something_ interesting about `this doc`\nAnd <http://example.com/|here is a link in a paragraph!>"
    output = HTMLSlacker(html).get_output()
    assert(output == expected)


def test_style_not_rendered():
    html = '''<style><!-- /* stuff */ --></style>Dear Prudence'''
    expected = "Dear Prudence"
    output = HTMLSlacker(html).get_output()
    assert(output == expected)


def test_script_not_rendered():
    html = '''<script><!-- /* stuff */ --></script>Dear Prudence'''
    expected = "Dear Prudence"
    output = HTMLSlacker(html).get_output()
    assert(output == expected)


def test_link_with_target():
    html = 'Please click <a href="http://xxx.com/t.html" target="_blank">here</a>'
    expected = "Please click <http://xxx.com/t.html|here>"
    output = HTMLSlacker(html).get_output()
    assert(output == expected)

def test_unordered_list():
    html = 'Here is my cool list <ul><li>The Shining</li><li>Memento</li><li>Blade Runner</li></ul>'
    expected = 'Here is my cool list • The Shining\n• Memento\n• Blade Runner'
    output = HTMLSlacker(html).get_output()
    assert(output == expected)

def test_ordered_list():
    html = 'Here is my cool list <ol><li>The Shining</li><li>Memento</li><li>Blade Runner</li></ol>'
    expected = 'Here is my cool list 1. The Shining\n2. Memento\n3. Blade Runner'
    output = HTMLSlacker(html).get_output()
    assert(output == expected)

def test_unordered_list_with_text_modifications():
    html = 'Here is my cool list <ul><li>The Shining</li><li>Memento</li><li>Blade <b>Runner</b></li></ul>'
    expected = 'Here is my cool list • The Shining\n• Memento\n• Blade *Runner*'

def test_headers_rendered():
    html = '''<h2>Hello</h2> <h7>new</h7> <h2><b>world</b></h2>'''
    expected = "*Hello*\nnew *world*"
    output = HTMLSlacker(html).get_output()
    assert(output == expected)

def test_headers_rendered_no_spaces():
    html = '''<h2>Hello</h2><h7>new</h7><h2><b>world</b></h2>'''
    expected = "*Hello*\nnew *world*"
    output = HTMLSlacker(html).get_output()
    assert(output == expected)

def test_task_list_rendered():
    html = '''[] Grocery<br>[x] Laundary'''
    expected = "☐ Grocery\n☑︎ Laundary"
    output = HTMLSlacker(html).get_output()
    assert(output == expected)
