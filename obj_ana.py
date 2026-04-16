import google.generativeai as genai 
from PIL import Image
img=Image.open(r"C:\Users\DELL\Downloads\retail store.jpg")
model = genai.configure(api_key="AIzaSyDJf4_XVQe7R70Jsq-YumalC0zm9um5S9s")
model = genai.GenerativeModel("gemini-2.5-flash")
prompt = input("enter the question")
response=model.generate_content([prompt,img])
print(response.text)