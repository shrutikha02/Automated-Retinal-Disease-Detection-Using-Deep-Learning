# recommendation.py

def get_recommendation(disease):

    recommendations = {

        "CNV": """
        Immediate referral to retinal specialist.
        Treatment: Anti-VEGF therapy, photodynamic therapy.
        Monitoring: OCT scans every 1-3 months.
        Lifestyle: Diet rich in antioxidants.
        """,

        "DME": """
        Endocrinology consultation for diabetes management.
        Treatment: Anti-VEGF injections, corticosteroid implants.
        Maintain HbA1c below 7%.
        Monitoring: OCT every 3-6 months.
        """,

        "DRUSEN": """
        Dietary modifications: AREDS2 supplements.
        Lifestyle changes: Smoking cessation, UV protection.
        Monitoring: OCT every 6-12 months.
        """,

        "NORMAL": """
        Routine eye examination.
        Follow-up every 1-2 years.
        Preventive health maintenance.
        """
    }

    return recommendations.get(disease, "Consult ophthalmologist.")
