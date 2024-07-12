import openai
from utils.config import get_openai_api_key

# Initialize the OpenAI client
client = openai.OpenAI(api_key=get_openai_api_key())

def get_prompt_tips(user_prompt, lang):
    """
    Generate prompt improvement tips based on the user's input in the specified language.
    
    Args:
    user_prompt (str): The prompt submitted by the user.
    lang (str): The language to use for generating tips ('English' or 'Deutsch').
    
    Returns:
    str: Two tips for improving the prompt in the specified language.
    """
    system_messages = {
        "English": """You are an AI assistant specializing in helping journalists improve their prompts for AI-based research and writing. 
        Analyze the given prompt and provide two concise tips for improvement, focusing on aspects such as:
        1. Clarity and specificity
        2. Use of few-shot examples
        3. Implementing chain-of-thought reasoning
        4. Providing necessary context
        5. Ethical considerations in journalism
        Keep each tip brief and actionable.""",
        
        "Deutsch": """Sie sind ein KI-Assistent, der sich darauf spezialisiert hat, Journalisten bei der Verbesserung ihrer Prompts für KI-basierte Recherchen und Schreibarbeiten zu unterstützen.
        Analysieren Sie den gegebenen Prompt und geben Sie zwei prägnante Tipps zur Verbesserung, wobei Sie sich auf Aspekte wie die folgenden konzentrieren:
        1. Klarheit und Spezifität
        2. Verwendung von Few-Shot-Beispielen
        3. Implementierung von Chain-of-Thought-Reasoning
        4. Bereitstellung des notwendigen Kontexts
        5. Ethische Überlegungen im Journalismus
        Halten Sie jeden Tipp kurz und umsetzbar."""
    }

    user_messages = {
        "English": f"Please provide two tips to improve this prompt: '{user_prompt}'",
        "Deutsch": f"Bitte geben Sie zwei Tipps zur Verbesserung dieses Prompts: '{user_prompt}'"
    }

    response = client.chat.completions.create(
        model="gpt-4o",  # or whichever model you prefer
        messages=[
            {"role": "system", "content": system_messages[lang]},
            {"role": "user", "content": user_messages[lang]}
        ],
        max_tokens=150  # Adjust as needed
    )

    return response.choices[0].message.content

# Example usage:
# tips_en = get_prompt_tips("What are the main economic challenges facing the EU in 2023?", "English")
# tips_de = get_prompt_tips("Was sind die wichtigsten wirtschaftlichen Herausforderungen für die EU im Jahr 2023?", "Deutsch")
# print(tips_en)
# print(tips_de)