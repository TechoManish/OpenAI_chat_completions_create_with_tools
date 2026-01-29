# OpenAI_chat_completions_create_with_tools
Calling openai chat completions create with tools parameter



This project demonstrates how to use `openai.chat.completions.create()`  
with **tools (function calling)** to provide portfolio advice based on a
client's risk assessment score.

### Scenario
- User asks for portfolio advice
- Model requests the client's risk score via a tool
- Backend executes the tool
- Model resumes and gives tailored investment advice

### Flow
User → OpenAI → Tool Call → Backend → OpenAI → Final Advice
