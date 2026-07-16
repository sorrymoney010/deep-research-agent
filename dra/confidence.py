from .models import SourceTier


def score(claim):
    if not claim.citations:
        return 0.0

    base = {
        SourceTier.PRIMARY: 0.7,
        SourceTier.SECONDARY: 0.5,
        SourceTier.INTERPRETATION: 0.25,
        SourceTier.SPECULATION: 0.05,
    }

    value = max(base.get(c.tier, 0.05) for c in claim.citations)

    if len(claim.citations) > 1:
        value += min(0.2, len(claim.citations) * 0.05)

    if claim.disputed:
        value -= 0.25

    return max(0.0, min(1.0, round(value, 2)))
