# Permissions and Groups Setup

## Custom Permissions
- The `Book` model has the following custom permissions:
  - `can_view`: Allows viewing books.
  - `can_create`: Allows creating new books.
  - `can_edit`: Allows editing existing books.
  - `can_delete`: Allows deleting books.

## Groups
- **Editors**: Can create and edit books.
- **Viewers**: Can only view books.
- **Admins**: Can view, create, edit, and delete books.

## Usage
- Use the `@permission_required` decorator in views to enforce permissions.
- Assign users to groups in the Django admin interface to control access.