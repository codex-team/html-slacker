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
    expected = "*Hello*\n There is _something_ interesting about `this doc` \n And <http://example.com/|here is a link in a paragraph!>"
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
    html = '<ul><li>Hello</li><li>Goodbye</li></ul>'
    expected = """
    - Hello
    - Goodbye
    """
    output = HTMLSlacker(html).get_output()
    assert(output == expected)

def test_ordered_list():
    html = '<ol><li>one</li><li>two</li></ol>'
    expected = """
    1. one
    2. two
    """
    output = HTMLSlacker(html).get_output()
    assert(output == expected)


def test_pre():
    html = """
    <pre>
        let x = true; \n
        x = 'true'
    </pre>
    """
    expected = """
    ```
    let x = true;
    ```
    """
    output = HTMLSlacker(html).get_output()
    assert(output == expected)
