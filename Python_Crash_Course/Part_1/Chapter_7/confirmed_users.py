unconfirmed_users = ['alice', 'brian', 'candace']
confirmed_users = []

while unconfirmed_users:
    current_user = unconfirmed_users.pop()
    print("Verifying user: " + current_user.title())
    confirmed_users.append(current_user)

print(unconfirmed_users)
if not unconfirmed_users:
    print("???")

print("\nThe following users have been confirmed:")
for current_user in confirmed_users:
    print(current_user)
