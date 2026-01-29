from tools.risk_assessment import get_client_risk_score

def handle_tool_call(tool_call: dict) -> dict:
    name = tool_call["name"]
    arguments = tool_call["arguments"]

    if name == "get_client_risk_score":
        return get_client_risk_score(**arguments)

    raise ValueError(f"Unknown tool: {name}")
