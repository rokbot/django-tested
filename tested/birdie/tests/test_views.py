from django.test import RequestFactory

from .. import views

class TestHomeView:
    def test_anonymous(self):
        req = RequestFactory().get('/')
        resp = views.HomveView.as_view()(req)
        assert resp == resp.status_code == 200, 'Should be callabe by anyone'
