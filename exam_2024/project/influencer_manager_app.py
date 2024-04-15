from project.campaigns.low_budget_campaign import LowBudgetCampaign
from project.campaigns.high_budget_campaign import HighBudgetCampaign
from project.influencers.standard_influencer import StandardInfluencer
from project.influencers.premium_influencer import PremiumInfluencer

class InfluencerManagerApp:

    VALID_TYPE_INFLUENCERS = {"PremiumInfluencer": PremiumInfluencer, "StandardInfluencer": StandardInfluencer}
    VALID_TYPE_CAMPAIGNS = {"HighBudgetCampaign": HighBudgetCampaign, "LowBudgetCampaign": LowBudgetCampaign}

    def __init__(self):
        self.influencers = []
        self.campaigns = []

    def register_influencer(self, influencer_type: str, username: str, followers: int, engagement_rate: float):
        if influencer_type not in self.VALID_TYPE_INFLUENCERS:
            return f"{influencer_type} is not an allowed influencer type."

        try:
            next(filter(lambda i: i.username == username, self.influencers))
            return f"{username} is already registered."
        except StopIteration:
            new_influencer = self.VALID_TYPE_INFLUENCERS[influencer_type](username, followers, engagement_rate)
            self.influencers.append(new_influencer)
            return f"{username} is successfully registered as a {influencer_type}."

    def create_campaign(self, campaign_type: str, campaign_id: int, brand: str, required_engagement: float):
        if campaign_type not in self.VALID_TYPE_CAMPAIGNS:
            return f"{campaign_type} is not a valid campaign type."

        try:
            next(filter(lambda c: c.campaign_id == campaign_id, self.campaigns))
            return f"Campaign ID {campaign_id} has already been created."
        except StopIteration:
            new_campaign = self.VALID_TYPE_CAMPAIGNS[campaign_type](campaign_id, brand, required_engagement)
            self.campaigns.append(new_campaign)
            return f"Campaign ID {campaign_id} for {brand} is successfully created as a {campaign_type}."

    def participate_in_campaign(self, influencer_username: str, campaign_id: int):
        try:
            influencer = next(filter(lambda i: i.username == influencer_username, self.influencers))
        except StopIteration:
            return f"Influencer '{influencer_username}' not found."

        try:
            campaign = next(filter(lambda c: c.campaign_id == campaign_id, self.campaigns))
        except StopIteration:
            return f"Campaign with ID {campaign_id} not found."

        if not campaign.check_eligibility(influencer.engagement_rate):
            return f"Influencer '{influencer_username}' does not meet the eligibility criteria for the campaign with ID {campaign_id}."

        influencer_payment = campaign.check_eligibility(influencer.engagement_rate)
        if influencer_payment > 0.0:
            campaign.approved_influencers.append(influencer)
            campaign.budget -= influencer_payment
            influencer.campaigns_participated.append(campaign)
            return f"Influencer '{influencer_username}' has successfully participated in the campaign with ID {campaign_id}."

    def calculate_total_reached_followers(self):
        return {campaign: sum(influencer.reached_followers() for influencer in campaign.approved_influencers)
                for campaign in self.campaigns if campaign.approved_influencers}

    def influencer_campaign_report(self, username: str):
        influencer = next(filter(lambda i: i.username == username, self.influencers))

        if not influencer.campaigns_participated:
            return f"{username} has not participated in any campaigns."

        return influencer.display_campaigns_participated()

    def campaign_statistics(self):
        header = "$$ Campaign Statistics $$\n"
        sorted_campaigns = sorted(self.campaigns, key=lambda campaign: (len(campaign.approved_influencers), -campaign.budget))
        statistics = ""
        for campaign in sorted_campaigns:
            brand = campaign.brand
            approved_influencers = len(campaign.approved_influencers)
            budget = sum(campaign.budget)
            total_reached_followers = campaign.calculate_total_reached_followers()

            statistics += (f"  * Brand: {brand}, Total influencers: {approved_influencers},"
                           f" Total budget: {budget}, Total reached followers: {total_reached_followers}\n")

        return header + statistics

