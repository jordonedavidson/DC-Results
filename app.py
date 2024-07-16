from controllers.action_check import ActionCheck

ac = ActionCheck()

print(f"To hit is: {ac.get_to_hit(3, 6)}")

print(f"Rolled a 21. Result is: {ac.attack_result(13, 21)}")
