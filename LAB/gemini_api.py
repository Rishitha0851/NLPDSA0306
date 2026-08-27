from google import genai

client = genai.Client(api_key="AQ.Ab8RN6KxQex3qAZr-8wCl8sQFiD4DA-I_-R6T7NJMfiTFSDpmQ")

prompt = input("Enter your prompt: ")

response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents=prompt
)

print("\nGenerated text:")
print(response.text)