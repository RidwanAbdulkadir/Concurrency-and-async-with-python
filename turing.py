TOPIC_PACK = "Biology → Specialized Domain Knowledge"
SUBCATEGORY = "Fictional Regulatory Ecology"

metadata = {
    "category": "Specialized Domain Knowledge",
    "subcategory": "Fictional Regulatory Ecology",
    "expected_output_type": "JSON",
    "topic_pack": TOPIC_PACK,
    "context_tokens_estimate": 1200
}

prompt_text = """
Using the conservation rules provided in the context,
determine the legal collection quota for the species
Silverleaf Beetle in Region Gamma.

Return:

{
 "species": "...",
 "region": "...",
 "approved_quota": ...
}

No explanation.
"""

gold_context = """
Verdantia Conservation Act

Species Categories

Silverleaf Beetle:
Population = 500

Quota Rules

Population above 400:
Quota = 15% of population

Region Gamma:
Quota modifier = 0.8

Worked Example

Bluewing Moth:
Population = 1000

Base quota:
1000 × 15% = 150

Region modifier:
150 × 0.8 = 120

Final quota = 120
"""

expected = {
    "answer": {
        "species": "Silverleaf Beetle",
        "region": "Gamma",
        "approved_quota": 60
    }
}

def check_prediction(pred, expected):
    """Return True if prediction matches expected.

    Accept either the full prediction dict equal to `expected`,
    or a dict containing only the inner `answer` mapping.
    """
    try:
        if pred == expected:
            return True
        if isinstance(pred, dict) and "answer" in pred:
            return pred["answer"] == expected.get("answer")
    except Exception:
        return False
    return False