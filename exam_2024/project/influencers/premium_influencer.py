from exam_2024.project.campaigns.base_campaign import BaseCampaign
from project.influencers.base_influencer import BaseInfluencer


class PremiumInfluencer(BaseInfluencer):
    #INITIAL_PAYMENT_PERCENTAGE = 0.85

    def __init__(self, username: str, followers: int, engagement_rate: float):
        super().__init__(username, followers, engagement_rate)

    def calculate_payment(self, campaign: BaseCampaign) -> float:
        payment = campaign.budget * 0.85
        return payment

    def reached_followers(self, campaign_type: str) -> int:
        if campaign_type == "HighBudgetCampaign":
            return self.engagement_rate * 1.5
        elif campaign_type == "LowBudgetCampaign":
            return self.engagement_rate * 0.8