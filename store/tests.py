from django.test import SimpleTestCase, TestCase, Client
from django.urls import reverse,resolve
from django.contrib.auth import get_user_model
from django.conf import settings
from django.contrib.auth.models import User

# from store.models import Customer, Product
# from views import  Index,Collections, Login, OrderView, Signup,Cart,Artists, CheckOut
from store.views.collections import Collections
# from home import Index
class TestUrls(SimpleTestCase):
    # def test_home_url(self):
    #     url = reverse(Index)
    #     print(url)
    #     self.assertEquals(resolve(url).func,Index)

    def test_Collections(self):
        url = reverse(Collections, args='1')
        print(url)
        self.assertEquals(resolve(url).func,Collections)
    
    # def test_Login(self):
    #     url = reverse(Login, args='1')
    #     print(url)
    #     self.assertEquals(resolve(url).func,Login)

    # def test_OrderView(self):
    #     url = reverse(OrderView, args='1')
    #     print(url)
    #     self.assertEquals(resolve(url).func,OrderView)
    
    # def test_Signup(self):
    #     url = reverse(Signup, args='1')
    #     print(url)
    #     self.assertEquals(resolve(url).func,Signup)
    # def test_Cart(self):
    #     url = reverse(Cart)
    #     print(url)
    #     self.assertEquals(resolve(url).func,Cart)
    # def test_Artists(self):
    #     url = reverse(Artists)
    #     print(url)
    #     self.assertEquals(resolve(url).func,Artists)
    # def test_CheckOut(self):
    #     url = reverse(CheckOut)
    #     print(url)
    #     self.assertEquals(resolve(url).func,CheckOut)
    
User = get_user_model()
class TestView(TestCase):
    def setUp(self):
        user_a = User(username='testuser')
        user_a_pw = '12345'
        self.user_a_pw = user_a_pw
        user_a.set_password(user_a_pw)
        user_a.save()
        self.user_a = user_a


    def test_user_exists(self):
        user_count = User.objects.all().count()
        print(user_count)
        self.assertEqual(user_count, 1)
        self.assertNotEqual(user_count, 0)

    def test_user_password(self):
        self.assertTrue(self.user_a.check_password(self.user_a_pw))

    def test_user_login(self):
        login_url = settings.LOGIN_URL
        data = {"username": "testuser", "password": "12345"}
        response = self.client.post(login_url, data, follow=True)   
    

    
   

# class TestProView(TestCase):
#     def setUp(self):
#         self.user = User.objects.create(username='testuser')
#         self.user.set_password('12345')
#         self.user.save()
#         self.c = Client()
#         self.c.login(username='testuser', password='12345')
#         self.admin = Client()
#         self.admin.login(username='admin', password='admin')


#     def test_product_view(self):
#         c = Client()
#         req = self.c.get("/product/")
#         self.assertEqual(req.status_code, 404)

#     def test_add_product(self):
#         response = self.c.post(reverse(admin_add_product_view),{
#         "name": "meow",
#         "product_image": "default.jpg",
#         "price": "123",
#         "description": "test_decription",
#       })
#         self.assertEqual(response.status_code, 302)

#     def test_delete_product(self):
#         client = Client()
#         p = Product.objects.create(pk="1234", name="meow", product_image="default.jpg",price="123", description="test_decription")
#         print("this")
#         print(p.pk)
#         response = client.delete(reverse(delete_product_view, args=[p.pk]))
#         self.assertEqual(response.status_code, 302)

#     def test_delete_order(self):
#         client = Client()
#         p = Product.objects.create(pk="1234", name="meow", product_image="default.jpg",price="123", description="test_decription")
#         print("this")
#         print(p.pk)
#         response = client.delete(reverse(delete_order_view, args=[p.pk]))
#         self.assertEqual(response.status_code, 302)
    
#     def test_booking_view(self):
#         c = Client()
#         req = self.c.get("/booking_view/")
#         self.assertEqual(req.status_code, 404)