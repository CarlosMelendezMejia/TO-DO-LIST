from . import db

# Association table linking users and roles
user_roles = db.Table(
    'user_roles',
    db.Column('user_id', db.Integer, db.ForeignKey('user.id'), primary_key=True),
    db.Column('role_id', db.Integer, db.ForeignKey('role.id'), primary_key=True)
)

# Association table linking roles and permissions
role_permissions = db.Table(
    'role_permissions',
    db.Column('role_id', db.Integer, db.ForeignKey('role.id'), primary_key=True),
    db.Column('permission_id', db.Integer, db.ForeignKey('permission.id'), primary_key=True)
)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)

    roles = db.relationship('Role', secondary=user_roles, back_populates='users')

    def has_role(self, role_name: str) -> bool:
        """Return True if user has a role with the given name."""
        return any(role.name == role_name for role in self.roles)

    def has_permission(self, permission_name: str) -> bool:
        """Return True if user has a permission via its roles."""
        return any(role.has_permission(permission_name) for role in self.roles)


class Role(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True, nullable=False)

    users = db.relationship('User', secondary=user_roles, back_populates='roles')
    permissions = db.relationship(
        'Permission',
        secondary=role_permissions,
        back_populates='roles',
    )

    def has_permission(self, permission_name: str) -> bool:
        """Return True if the role includes a permission with the given name."""
        return any(permission.name == permission_name for permission in self.permissions)


class Permission(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True, nullable=False)
    descripcion = db.Column(db.String(255))

    roles = db.relationship(
        'Role',
        secondary=role_permissions,
        back_populates='permissions',
    )
