from openai_client import client
from utils.tool_handler import handle_tool_call
import json

# Step 1: Initial Chat Completion (with tool definition)
response = client.chat.completions.create(
    model="gpt-4o",
    messages=[
        {
            "role": "system",
            "content": "You are a wealth management assistant providing compliant portfolio advice."
        },
        {
            "role": "user",
            "content": "Please suggest a suitable investment strategy for client CLIENT_12345."
        }
    ],
    tools=[
        {
            "type": "function",
            "function": {
                "name": "get_client_risk_score",
                "description": "Retrieve the client's risk assessment score.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "client_id": {
                            "type": "string",
                            "description": "Unique identifier of the client"
                        }
                    },
                    "required": ["client_id"]
                }
            }
        }
    ],
    tool_choice="auto"
)

message = response.choices[0].message

# Step 2: Check if the model requested a tool
if message.tool_calls:
    tool_call = message.tool_calls[0]

    # Execute the tool
    tool_result = handle_tool_call({
        "name": tool_call.function.name,
        "arguments": json.loads(tool_call.function.arguments)
    })

    # Step 3: Resume conversation with tool result
    final_response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {
                "role": "system",
                "content": "You are a wealth management assistant providing compliant portfolio advice."
            },
            {
                "role": "user",
                "content": "Please suggest a suitable investment strategy for client CLIENT_12345."
            },
            {
                "role": "tool",
                "tool_name": tool_call.function.name,
                "content": json.dumps(tool_result)
            }
        ]
    )

    print("\n📊 Final Portfolio Advice:\n")
    print(final_response.choices[0].message.content)

else:
    # Model answered directly
    print(message.content)
