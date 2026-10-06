# Group C, Problem 2 Solution (Python): Athlete Performance Rating
# This system assigns the top applicable performance rating.
# Made by Cody Watkins 10/6/2026

def check_performance(speed_score, strength_score):

    print("--- Athlete Performance Rating ---")
    print(f"Speed Score: {speed_score}")
    print(f"Strength Score: {strength_score}")

    if speed_score >= 90 and strength_score >= 80:
        rating = "ELITE"

    elif speed_score >= 70 or strength_score >= 70:
        rating = "ADVANCED"

    elif speed_score >= 50:
        rating = "INTERMEDIATE"

    else:
        rating = "BEGINNER"

    print(f"Performance Rating: {rating}")
    print("----------------------------------")


# Example 1: Elite
print("Example 1: Elite")
check_performance(95, 85)

print("Example 2: Advanced")
# Example 2: Advanced
check_performance(75, 60)

print("Example 3: Intermediate")
# Example 3: Intermediate
check_performance(55, 40)

print("Example 4: Beginner")
# Example 4: Beginner
check_performance(30, 45)