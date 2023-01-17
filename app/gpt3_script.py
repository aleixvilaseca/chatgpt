import openai
import constants

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

generated_text = generate_text("Write the difference between a class and an object in Python.")
print(generated_text)