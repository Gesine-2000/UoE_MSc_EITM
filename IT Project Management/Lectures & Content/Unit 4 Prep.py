import numpy as np

class ProjectEstimator:
    def __init__(self, method="three_point"):
        self.method = method

    def analogous_estimate(self, past_project_hours, adjustment_factor=1.0):
        """
        Uses past project data to estimate new project effort.
        """
        return past_project_hours * adjustment_factor

    def parametric_estimate(self, num_units, unit_rate):
        """
        Uses historical data per unit to estimate effort.
        """
        return num_units * unit_rate

    def three_point_estimate(self, optimistic, most_likely, pessimistic):
        """
        Uses the PERT formula for estimation: (O + 4M + P) / 6
        """
        return (optimistic + 4 * most_likely + pessimistic) / 6

    def estimate(self, **kwargs):
        """
        Calls the appropriate estimation method.
        """
        if self.method == "analogous":
            return self.analogous_estimate(**kwargs)
        elif self.method == "parametric":
            return self.parametric_estimate(**kwargs)
        elif self.method == "three_point":
            return self.three_point_estimate(**kwargs)
        else:
            raise ValueError("Unknown estimation method")

    def risk_assessment(self, estimate, risk_factor):
        """
        Adjusts estimate based on a risk multiplier.
        """
        return estimate * (1 + risk_factor)

# Interactive input system:
if __name__ == "__main__":
    method = input("Enter estimation method (analogous, parametric, three_point): ")
    estimator = ProjectEstimator(method=method)

    if method == "analogous":
        past_project_hours = float(input("Enter past project hours: "))
        adjustment_factor = float(input("Enter adjustment factor (default is 1.0): "))
        base_estimate = estimator.estimate(past_project_hours=past_project_hours, adjustment_factor=adjustment_factor)
    elif method == "parametric":
        num_units = int(input("Enter number of units: "))
        unit_rate = float(input("Enter effort per unit: "))
        base_estimate = estimator.estimate(num_units=num_units, unit_rate=unit_rate)
    elif method == "three_point":
        optimistic = float(input("Enter optimistic estimate: "))
        most_likely = float(input("Enter most likely estimate: "))
        pessimistic = float(input("Enter pessimistic estimate: "))
        base_estimate = estimator.estimate(optimistic=optimistic, most_likely=most_likely, pessimistic=pessimistic)
    else:
        raise ValueError("Invalid estimation method selected.")
    
    risk_factor = float(input("Enter risk factor (as a decimal, e.g., 0.2 for 20%): "))
    final_estimate = estimator.risk_assessment(base_estimate, risk_factor)
    
    print(f"Base Estimate: {base_estimate:.2f} hours")
    print(f"Final Estimate after Risk Assessment: {final_estimate:.2f} hours")
