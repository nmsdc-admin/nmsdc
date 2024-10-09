html_content = '''<!doctype html>
<html lang="en" translate>
  <head>
    <meta charset="UTF-8" />
    <link rel="icon" type="image/svg+xml" href="https://b3336080.smushcdn.com/3336080/wp-content/uploads/2023/09/favicon.png?lossy=1&strip=1&webp=1" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <link href="https://fonts.googleapis.com/css2?family=Roboto+Slab:wght@350&display=swap" rel="stylesheet">
    <title>Vanna.AI</title>
    <script src="https://cdn.plot.ly/plotly-latest.min.js" type="text/javascript"></script>
    <script type="module" crossorigin src="/assets/index-35bab439.js"></script>
    <link rel="stylesheet" href="/assets/index-f228f78f.css">
  </head>
  <body class="bg-white dark:bg-slate-900">
    <div id="app"></div>
    <div id="speech-avatar-container">
    <img id="speech-avatar" src="https://i.ibb.co/XYQ2Tfs/image-3.png" alt="Speech Avatar" />
    <div id="speech-status">Click me to ask a question</div>
</div>

  </body>


</html>
'''



with open('miniconda3/lib/python3.12/site-packages/vanna/flask/index-b1a5a2f1.css', 'r') as file:
    css_content = '''{}'''.format(file.read())

# Path to the JavaScript file
js_file_path = 'miniconda3/lib/python3.12/site-packages/vanna/flask/index-d29524f4.js'

# Read the content of the JavaScript file
with open(js_file_path, 'r') as file:
    js_content = file.read()

# Optionally, you can minify or format it here if needed
js_content = '''{}'''.format(js_content)