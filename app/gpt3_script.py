import openai
import constants
import requests
from flask import Flask, render_template

app = Flask(__name__)

# Add your OpenAI API key
openai.api_key = constants.API_KEY

def generate_text(prompt):
    completions = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        max_tokens=2048,
        n=1,
        stop=None,
        temperature=0.7,
    )

    message = completions.choices[0].text
    return message.strip()

def save_text(generated_text):
    with open('generated_text.txt', 'w') as f:
        f.write(generated_text)

@app.route('/',  methods=['GET', 'POST'])

def index():
    if request.method == 'POST':
        prompt = request.form['prompt']
        generated_text = generate_text(prompt)
        save_text(generated_text)
        return render_template('index.html', generated_text=generate_text)
    return render_template('index.html')

@app.route('/download')
def download():
    return send_file('generated_text.txt', as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)