import json

def load_prompt():
with open("prompt_template.txt", "r") as file:
return file.read()

def generate_email(intent, tone, key_facts):
prompt = load_prompt()

```
email = f"""
```

Intent: {intent}
Tone: {tone}
Key Facts: {key_facts}

Generated Email:
Dear Sir/Madam,

I am writing regarding {intent}. {key_facts}

Thank you for your time.

Sincerely,
[Your Name]
"""
return email

if **name** == "**main**":
print("=== Email Generation Assistant ===")

```
intent = input("Enter intent: ")
tone = input("Enter tone: ")
key_facts = input("Enter key facts: ")

email = generate_email(intent, tone, key_facts)

print("\n--- Generated Email ---")
print(email)
```
