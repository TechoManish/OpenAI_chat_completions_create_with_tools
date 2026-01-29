def get_client_risk_score(client_id: str) -> dict:
    """
    Simulates retrieving a client's risk score from
    a risk engine or database.
    """

    # Mocked data (replace with DB / service call)
    return {
        "client_id": client_id,
        "risk_score": 72,
        "risk_category": "Moderate to High"
    }
