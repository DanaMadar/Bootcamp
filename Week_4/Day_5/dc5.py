#user_input = (print(",".join(sorted(input("type in any words seperated by a coma: ").split(",")))))
user_input = input("type in any words seperated by a coma: ")

output = [word for word in user_input.split(",")]
print(",".join(sorted(list(output))))