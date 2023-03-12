from structure import Database

db = Database("myDatabase")
db.create_vector("users", [603, 401, 301, 235])
db.create_vector("permissions", [1, 0, 1, 0])

users_vector = db.get_vector("users")
permissions_vector = db.get_vector("permissions")

def get_admins(users, permissions):
    # returns the admins (ids who correspond to 1 in the permissions vector)
    return users.get_selected_values(permissions.show())

print(get_admins(users_vector, permissions_vector))


def create_user(new_user_id):
    # Adds an item (user id) to the users vector
    users_vector.add_value(new_user_id)
    # Adds permission (0) as default value
    permissions_vector.add_value(0)

create_user(750);

print(db.vectors["users"].show())
print(db.vectors["permissions"].show())