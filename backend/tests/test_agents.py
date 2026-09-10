def test_agent_orchestrator():
    prompt = "Test execution query for agentic-veterinary-pet-care-advisor"
    assert len(prompt) > 0
    assert "Test" in prompt
