import openai
from flask import Flask, render_template, request
from dotenv import dotenv_values
import json

config = dotenv_values('.env')

openai.api_key = config['OPENAI_API_KEY']

app = Flask(__name__,
            template_folder='templates',
            static_url_path='',
            static_folder='static'
)


def get_colors(msg):
    prompt = f"""
    You are a color generating assistant that responds to text prompts for color palettes
    You should generate color palettes that fit the theme, mood, or instructions in the prompt.
    The palettes should be between 2 and 8 colors each.

    Q: Convert the following text to a color palette: The Mediterranean Sea
    A: ["#006699", "#66ccff", "#99ccff", "#6699cc", "#336699", "#003366"]

    Q: Convert the following text to a color palette: 4 Google brand colors
    A: ["#4285F4", "#EA4335", "#FBBC05", "#34A853"]

    Desired format: a JSON array of hexadecimal color codes

    Q: Convert the following text to a color palette: {msg}
    A:
    """

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": prompt},
        ],
        max_tokens=100
    )

    colors = json.loads(response.choices[0].message['content'])
    return colors
    # print(response)
    # print(response.choices[0].message['content'])

@app.route("/palette", methods=['POST'])
def prompt_to_palette():
    query = request.form.get("query")
    colors = get_colors(query)
    return {"colors": colors}
    # OPEN AI COMPLETION CALL

    # RETURN LIST OF COLORS

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)