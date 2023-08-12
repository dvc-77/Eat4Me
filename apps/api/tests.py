from django.test import TestCase
from django.contrib.auth.models import User
from api.models import Restaurant
from api.forms import UserForm, RestaurantForm

class RestaurantTest(TestCase):
    SIGN_UP_URL = '/api/v1/auth/signup/'
    LOGIN_URL = '/api/v1/auth/login/'
    LOGOUT_URL = '/api/v1/auth/logout/'
    DASHBOARD_URL = '/api/v1/auth/dashboard/'
    ACCOUNT_URL = '/api/v1/auth/restaurant/account/'
    MEAL_URL = '/api/v1/auth/restaurant/meal/'
    ORDER_URL = '/api/v1/auth/restaurant/order/'
    REPORT_URL = '/api/v1/auth/restaurant/report/'

    # Tests that index view renders index.html template
    def test_index_view(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'index.html')

    # Tests that restaurant_sign_up view renders sign_up.html template with UserForm and RestaurantForm on GET request to /restaurant/sign_up/ endpoint
    def test_restaurant_sign_up_view(self):
        response = self.client.get(self.SIGN_UP_URL)
        self.assertTemplateUsed(response, 'sign_up.html')
        self.assertIsInstance(response.context['uf'], UserForm)
        self.assertIsInstance(response.context['rf'], RestaurantForm)

    # Tests that restaurant_sign_up view creates new User and Restaurant objects, logs in user and redirects to restaurant_dashboard on successful POST request to /restaurant/sign_up/ endpoint
    def test_restaurant_sign_up_view_with_valid_data(self):
        response = self.client.post('/api/v1/auth/signup/', {
            'username': 'testuser',
            'password': 'testpass',
            'first_name': 'Test',
            'last_name': 'User',
            'email': 'testuser@example.com',
            'name': 'Test Restaurant',
            'phone': '1234567890',
            'address': 'Test Address'
        }, follow=True)
        self.assertRedirects(response, self.DASHBOARD_URL)
        self.assertTemplateUsed(response, 'dashboard.html')

    # Tests that unauthenticated user is redirected to /login/ on GET request to /restaurant/dashboard/, /restaurant/account/, /restaurant/meal/, /restaurant/order/, and /restaurant/report/ endpoints
    def test_unauthenticated_user_redirected_to_login(self):
        response = self.client.get(self.DASHBOARD_URL)
        self.assertRedirects(response, f'{self.LOGIN_URL}?next={self.DASHBOARD_URL}')
        response = self.client.get(self.ACCOUNT_URL)
        self.assertRedirects(response, f'{self.LOGIN_URL}?next={self.ACCOUNT_URL}')
        response = self.client.get(self.MEAL_URL)
        self.assertRedirects(response, f'{self.LOGIN_URL}?next={self.MEAL_URL}')
        response = self.client.get(self.ORDER_URL)
        self.assertRedirects(response, f'{self.LOGIN_URL}?next={self.ORDER_URL}')
        response = self.client.get(self.REPORT_URL)
        self.assertRedirects(response, f'{self.LOGIN_URL}?next={self.REPORT_URL}')

    # Tests that restaurant_sign_up view does not create new User or Restaurant objects and does not log in user on invalid POST request to /restaurant/sign_up/ endpoint
    def test_restaurant_sign_up_view_with_invalid_data(self):
        response = self.client.post(self.SIGN_UP_URL, {
            'username': 'testuser',
            'password': 'testpass',
            'first_name': 'Test',
            'last_name': 'User',
            'email': 'invalidemail',
            'name': '',
            'phone': '',
            'address': ''
        })
        self.assertTemplateUsed(response, 'sign_up.html')
        self.assertFalse(User.objects.filter(username='testuser').exists())
        self.assertFalse(Restaurant.objects.filter(name='Test Restaurant').exists())

    # Tests that user is redirected to / on successful logout
    def test_successful_logout(self):
        self.client.login(username='testuser', password='testpass')
        response = self.client.get(self.LOGOUT_URL, follow=True)
        self.assertRedirects(response, '/')