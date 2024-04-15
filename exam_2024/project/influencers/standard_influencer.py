from project.campaigns.base_campaign import BaseCampaign
from project.influencers.base_influencer import BaseInfluencer


class StandardInfluencer(BaseInfluencer):
    INITIAL_PAYMENT_PERCENTAGE = 0.45

    def __init__(self, username: str, followers: int, engagement_rate: float):
        super().__init__(username, followers, engagement_rate)

    def calculate_payment(self, campaign: BaseCampaign) -> float:
        payment = campaign.budget * StandardInfluencer.INITIAL_PAYMENT_PERCENTAGE
        return payment

    def reached_followers(self, campaign_type: str) -> int:
        if campaign_type == "HighBudgetCampaign":
            return self.engagement_rate * 1.2
        elif campaign_type == "LowBudgetCampaign":
            return self.engagement_rate * 0.9