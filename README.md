🧠 AI Image Question Answering System
📌 Overview

This project is an AI-powered Image Question Answering system that allows users to upload an image and ask questions about it. The system uses Google Generative AI (Gemini model) to analyze the image and generate intelligent, context-aware responses.

It combines computer vision + natural language processing (NLP) to deliver accurate insights from visual data.
🚀 Features

    🖼️ Image input support

    ❓ User-defined question prompt

    🤖 AI-powered response generation

    ⚡ Fast processing using Gemini 2.5 Flash model

    🧩 Simple and lightweight Python implementation

🛠️ Tech Stack

    Python

    Google Generative AI (Gemini API)

    Pillow (PIL) – Image processing

📂 Project Structure

├── obj_ana.py        # Main Python script
├── image.jpg         # Input image (user-defined)
└── README.md         # Project documentation

⚙️ How It Works

    Load an image using PIL

    Accept a user query (question about the image)

    Send both image + prompt to Gemini AI

    AI processes the input and generates a response

    Output is displayed in the console

▶️ Usage
1. Install Dependencies

Bash
pip install pillow google-generativeai

2. Run the Script

Bash
python obj_ana.py

3. Enter Your Question

enter the question: What is happening in the image?

🔑 Configuration

Replace your API key in the script:

Python
Run
genai.configure(api_key="YOUR_API_KEY")

📸 Example Use Cases

    Retail store analysis

    Object detection queries

    Scene understanding

    Smart surveillance systems

    AI-based assistants

⚠️ Notes

    Ensure the image path is correct

    Keep your API key secure

    Requires internet connection for AI processing

📈 Future Enhancements

    Web interface (HTML, Bootstrap, JS)

    Real-time camera integration

    Multi-image support

    Voice-based input

🤝 Contributing

Contributions are welcome! Feel free to fork this repo and submit a pull request.
📜 License

This project is open-source and available under the MIT License.
