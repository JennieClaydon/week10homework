from flask import Flask, Response, request, url_for

from flask import Flask, url_for, render_template

app = Flask(__name__)

@app.route("/")
def homepage():
    about_me_url = url_for('about_me')
    cornwall_url = url_for('cornwall')
    devon_url = url_for('devon')
    return """
        <html>
    <head>
    <title>Travel Blog</title>
    </head>
    <body>
        <h1>Travel Blog Home Page</h1>
        <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. In congue tempor justo ac dignissim. Quisque a metus dui. Suspendisse potenti. Proin pretium ut ipsum sit amet cursus. Duis eget arcu ut ante laoreet mollis. Integer elementum ante eu purus vulputate, in convallis diam rutrum. Mauris eget quam non felis elementum fermentum. Nulla sed magna non nibh venenatis viverra. Aliquam erat volutpat. Nam vitae ligula consectetur, mattis nisi in, blandit ante. Proin auctor felis diam, eu congue risus tincidunt at. Nulla ullamcorper eu leo nec feugiat. Proin porta scelerisque vehicula.<p>
        <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. In congue tempor justo ac dignissim. Quisque a metus dui. Suspendisse potenti. Proin pretium ut ipsum sit amet cursus. Duis eget arcu ut ante laoreet mollis. Integer elementum ante eu purus vulputate, in convallis diam rutrum. Mauris eget quam non felis elementum fermentum. Nulla sed magna non nibh venenatis viverra. Aliquam erat volutpat. Nam vitae ligula consectetur, mattis nisi in, blandit ante. Proin auctor felis diam, eu congue risus tincidunt at. Nulla ullamcorper eu leo nec feugiat. Proin porta scelerisque vehicula.<p>
        <hr>
        <nav>
        <a href="{}">About Me</a>
        <a href="{}">Cornwall</a>
        <a href="{}">Devon</a>
        </nav>

    </body>
    </html>
    """.format(about_me_url, cornwall_url, devon_url)

@app.route('/about_me')
def about_me():
    return """
        <html>
    <head>
        <title>About Me</title>
    </head>
    <body>
        <h1>About Me</h1>
        <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. In congue tempor justo ac dignissim. Quisque a metus dui. Suspendisse potenti. Proin pretium ut ipsum sit amet cursus. Duis eget arcu ut ante laoreet mollis. Integer elementum ante eu purus vulputate, in convallis diam rutrum. Mauris eget quam non felis elementum fermentum. Nulla sed magna non nibh venenatis viverra. Aliquam erat volutpat. Nam vitae ligula consectetur, mattis nisi in, blandit ante. Proin auctor felis diam, eu congue risus tincidunt at. Nulla ullamcorper eu leo nec feugiat. Proin porta scelerisque vehicula.<p>
        <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. In congue tempor justo ac dignissim. Quisque a metus dui. Suspendisse potenti. Proin pretium ut ipsum sit amet cursus. Duis eget arcu ut ante laoreet mollis. Integer elementum ante eu purus vulputate, in convallis diam rutrum. Mauris eget quam non felis elementum fermentum. Nulla sed magna non nibh venenatis viverra. Aliquam erat volutpat. Nam vitae ligula consectetur, mattis nisi in, blandit ante. Proin auctor felis diam, eu congue risus tincidunt at. Nulla ullamcorper eu leo nec feugiat. Proin porta scelerisque vehicula.<p>
    </body>
    </html>
    """


@app.route('/cornwall')
def cornwall():
    return """
        <html>
    <head>
        <title>Cornish Adventures</title>
    </head>
    <body>
        <h1>Cornish Adventures</h1>
        <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. In congue tempor justo ac dignissim. Quisque a metus dui. Suspendisse potenti. Proin pretium ut ipsum sit amet cursus. Duis eget arcu ut ante laoreet mollis. Integer elementum ante eu purus vulputate, in convallis diam rutrum. Mauris eget quam non felis elementum fermentum. Nulla sed magna non nibh venenatis viverra. Aliquam erat volutpat. Nam vitae ligula consectetur, mattis nisi in, blandit ante. Proin auctor felis diam, eu congue risus tincidunt at. Nulla ullamcorper eu leo nec feugiat. Proin porta scelerisque vehicula.<p>
        <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. In congue tempor justo ac dignissim. Quisque a metus dui. Suspendisse potenti. Proin pretium ut ipsum sit amet cursus. Duis eget arcu ut ante laoreet mollis. Integer elementum ante eu purus vulputate, in convallis diam rutrum. Mauris eget quam non felis elementum fermentum. Nulla sed magna non nibh venenatis viverra. Aliquam erat volutpat. Nam vitae ligula consectetur, mattis nisi in, blandit ante. Proin auctor felis diam, eu congue risus tincidunt at. Nulla ullamcorper eu leo nec feugiat. Proin porta scelerisque vehicula.<p>
    </body>
    </html>
    """


@app.route('/devon')
def devon():
    salcombe_url = url_for('salcombe')
    return """
        <html>
    <head>
        <title>Exploring Devon</title>
    </head>
    <body>
        <h1>Exploring Devon</h1>
        <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. In congue tempor justo ac dignissim. Quisque a metus dui. Suspendisse potenti. Proin pretium ut ipsum sit amet cursus. Duis eget arcu ut ante laoreet mollis. Integer elementum ante eu purus vulputate, in convallis diam rutrum. Mauris eget quam non felis elementum fermentum. Nulla sed magna non nibh venenatis viverra. Aliquam erat volutpat. Nam vitae ligula consectetur, mattis nisi in, blandit ante. Proin auctor felis diam, eu congue risus tincidunt at. Nulla ullamcorper eu leo nec feugiat. Proin porta scelerisque vehicula.<p>
        <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. In congue tempor justo ac dignissim. Quisque a metus dui. Suspendisse potenti. Proin pretium ut ipsum sit amet cursus. Duis eget arcu ut ante laoreet mollis. Integer elementum ante eu purus vulputate, in convallis diam rutrum. Mauris eget quam non felis elementum fermentum. Nulla sed magna non nibh venenatis viverra. Aliquam erat volutpat. Nam vitae ligula consectetur, mattis nisi in, blandit ante. Proin auctor felis diam, eu congue risus tincidunt at. Nulla ullamcorper eu leo nec feugiat. Proin porta scelerisque vehicula.<p>
        <hr>
        <nav>
        <a href="{}">Salcombe Blog Post</a>
    </body>
    </html>
    """.format(salcombe_url)

@app.route('/devon/salcombe')
def salcombe():
    return """
        <html>
    <head>
        <title>Salcombe</title> 
    </head>
    <body>
        <h1>Salcombe</h1>
        <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. In congue tempor justo ac dignissim. Quisque a metus dui. Suspendisse potenti. Proin pretium ut ipsum sit amet cursus. Duis eget arcu ut ante laoreet mollis. Integer elementum ante eu purus vulputate, in convallis diam rutrum. Mauris eget quam non felis elementum fermentum. Nulla sed magna non nibh venenatis viverra. Aliquam erat volutpat. Nam vitae ligula consectetur, mattis nisi in, blandit ante. Proin auctor felis diam, eu congue risus tincidunt at. Nulla ullamcorper eu leo nec feugiat. Proin porta scelerisque vehicula.<p>
        <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. In congue tempor justo ac dignissim. Quisque a metus dui. Suspendisse potenti. Proin pretium ut ipsum sit amet cursus. Duis eget arcu ut ante laoreet mollis. Integer elementum ante eu purus vulputate, in convallis diam rutrum. Mauris eget quam non felis elementum fermentum. Nulla sed magna non nibh venenatis viverra. Aliquam erat volutpat. Nam vitae ligula consectetur, mattis nisi in, blandit ante. Proin auctor felis diam, eu congue risus tincidunt at. Nulla ullamcorper eu leo nec feugiat. Proin porta scelerisque vehicula.<p>
    </body>
    </html>
    """


# Test of having separate HTML sheet
@app.route('/test')
def htmltest():
    return render_template('test.html')

if __name__ == "__main__":
    app.run(debug=True)