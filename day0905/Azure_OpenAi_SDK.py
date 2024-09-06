import openai

openai.api_key = '82f362811be940e8862063c49da02f0e'
openai.api_base = 'https://quick-start.openai.azure.com/'

response = openai.Completion.create(
    engine="gpt-4o",  # 选择你要使用的模型
    prompt="Hello, how are you?",
    max_tokens=50
)

print(response.choices[0].text.strip())