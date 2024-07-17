from controllers.action_check import ActionCheck

ac = ActionCheck()

print(ac.get_result(1, 1, 0))

print(ac.get_result(2, 1, 0))

print(ac.get_result(3, 1, 0))
print(ac.get_result(3, 1, 3))

print(ac.get_result(1, 4, 0))
