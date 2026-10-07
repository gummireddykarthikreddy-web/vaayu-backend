from typing import Dict, List, Any

class ClinicalAgent:
    REFERENCE_RANGES = {
        "serum_creatinine": {"max": 1.2, "unit": "mg/dL"},
        "serum_potassium": {"max": 5.0, "unit": "mEq/L"},
        "hba1c": {"max": 5.7, "unit": "%"}
    }

    def analyze_lab_report(self, metrics: Dict[str, float]) -> List[str]:
        anomalies = []
        for key, val in metrics.items():
            if key in self.REFERENCE_RANGES:
                if val > self.REFERENCE_RANGES[key]["max"]:
                    anomalies.append(f"HIGH_{key.upper()}")
        return anomalies

class NutritionAgent:
    CONSTRAINT_RULES = {
        "HIGH_SERUM_CREATININE": {
            "restricted_nutrients": ["High-protein", "Sodium"],
            "avoid_ingredients": ["Red meat", "Processed cheese"],
            "reason": "Reduce renal workload."
        },
        "HIGH_HBA1C": {
            "restricted_nutrients": ["Simple Carbohydrates"],
            "avoid_ingredients": ["Refined flour", "White sugar"],
            "reason": "Manage blood glucose spikes."
        }
    }

    def generate_dietary_constraints(self, anomalies: List[str]) -> Dict[str, Any]:
        avoid_set = set()
        nutrient_set = set()
        reasons = []

        for anomaly in anomalies:
            if anomaly in self.CONSTRAINT_RULES:
                rule = self.CONSTRAINT_RULES[anomaly]
                avoid_set.update(rule["avoid_ingredients"])
                nutrient_set.update(rule["restricted_nutrients"])
                reasons.append(rule["reason"])

        return {
            "restricted_nutrients": list(nutrient_set),
            "forbidden_ingredients": list(avoid_set),
            "clinical_reasons": reasons
        }