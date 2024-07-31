import openai
from dotenv import dotenv_values
from IPython.display import display, Markdown

config = dotenv_values('.env')

openai.api_key = config['OPENAI_API_KEY']

def get_and_render_colors(msg):
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

    print(response)
    print(response.choices[0].message['content'])

get_and_render_colors("Thanksgiving color palette")
# print(response.choices[0].message['content'])



