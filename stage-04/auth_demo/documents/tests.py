from django.contrib.auth.models import Group, Permission
from django.test import TestCase

from accounts.models import User
from .models import Document


class DocumentPermissionTest(TestCase):

    def setUp(self):

        self.viewer = User.objects.create_user(
            username="viewer",
            password="ViewerPass123!",
        )

        self.editor = User.objects.create_user(
            username="editor",
            password="EditorPass123!",
        )

        self.viewer_group = Group.objects.create(
            name="Viewer"
        )

        self.editor_group = Group.objects.create(
            name="Editor"
        )

        view_permission = Permission.objects.get(
            codename="view_document"
        )

        add_permission = Permission.objects.get(
            codename="add_document"
        )

        change_permission = Permission.objects.get(
            codename="change_document"
        )

        self.viewer_group.permissions.add(
            view_permission
        )

        self.editor_group.permissions.add(
            view_permission,
            add_permission,
            change_permission,
        )

        self.viewer.groups.add(
            self.viewer_group
        )

        self.editor.groups.add(
            self.editor_group
        )

    def test_viewer_has_view_permission(self):

        self.assertTrue(
            self.viewer.has_perm(
                "documents.view_document"
            )
        )
    def test_viewer_does_not_have_add_permission(self):

        self.assertFalse(
            self.viewer.has_perm(
                "documents.add_document"
            )
        )
    def test_editor_has_view_permission(self):

        self.assertTrue(
            self.editor.has_perm(
                "documents.view_document"
            )
        )
    def test_editor_has_add_permission(self):

        self.assertTrue(
            self.editor.has_perm(
                "documents.add_document"
            )
        )
    def test_editor_has_change_permission(self):

        self.assertTrue(
            self.editor.has_perm(
                "documents.change_document"
            )
        )
    def test_anonymous_user_cannot_view_documents(self):

        response = self.client.get(
            "/documents/"
        )

        self.assertEqual(
            response.status_code,
            302,
        )
    def test_viewer_can_view_documents(self):

        self.client.force_login(self.viewer)

        response = self.client.get(
            "/documents/"
        )

        self.assertEqual(
            response.status_code,
            200,
        )
    def test_user_without_permission_gets_403(self):

        user = User.objects.create_user(
            username="normaluser",
            password="NormalPass123!",
        )

        self.client.force_login(user)

        response = self.client.get(
            "/documents/"
        )

        self.assertEqual(
            response.status_code,
            403,
        )
    def test_editor_can_view_documents(self):

        self.client.force_login(self.editor)

        response = self.client.get(
            "/documents/"
        )

        self.assertEqual(
            response.status_code,
            200,
        )