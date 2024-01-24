import textwrap
import PIL.Image
import google.generativeai as genai
from IPython.display import Markdown


def to_markdown(text):
    text = text.replace("•", "  *")
    return Markdown(textwrap.indent(text, "> ", predicate=lambda _: True)).data


GOOGLE_API_KEY = "AIzaSyAL3dHXSUQUc-USfddY6rWsLh45oCrtvCA"

genai.configure(api_key=GOOGLE_API_KEY)


model_gemini_pro_vision = genai.GenerativeModel("gemini-pro-vision")
model_gemini_pro = genai.GenerativeModel("gemini-pro")

img1 = PIL.Image.open("hawamahal.jpeg")

img2 = PIL.Image.open("North_Western_Railway_Jaipur.jpg")

with open("docker_images_delete.pdf", "rb") as file:
    pdf = file.read()

response_1 = model_gemini_pro_vision.generate_content(
    ["describe about the images in almost 300 words", img1, img2]
)

response_2 = model_gemini_pro.generate_content("who are you")

print(to_markdown(response_2.text))
