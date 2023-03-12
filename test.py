from structure import Database

db = Database("myDatabase")
db.create_vector("users", [603, 401, 301, 235])
db.create_vector("permissions", [1, 0, 1, 0])

def get_admins(users, permissions):
    # returns the admins (ids who correspond to 1 in the permissions vector)
    return users.get_selected_values(permissions.show())

print(get_admins(db.vectors["users"], db.vectors["permissions"]))


def create_user(new_user_id):
    # Adds an item (user id) to the users vector
    db.vectors["users"].add_value(new_user_id)
    # Adds permission (0) as default value
    db.vectors["permissions"].add_value(0)

create_user(750);

print(db.vectors["users"].show())
print(db.vectors["permissions"].show())