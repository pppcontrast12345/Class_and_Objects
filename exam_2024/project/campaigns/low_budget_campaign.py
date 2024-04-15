from project.campaigns.base_campaign import BaseCampaign


class LowBudgetCampaign(BaseCampaign):
    LOW_BUDGET = 2500.0
    #PERCENTAGE = 0.9

    def __init__(self, campaign_id: int, brand: str, required_engagement: float):
        super().__init__(campaign_id, brand, LowBudgetCampaign.LOW_BUDGET, required_engagement)

    def check_eligibility(self, engagement_rate: float) -> bool:
        if engagement_rate >= self.required_engagement * 0.9:
            return True
        return False