from django.db import models
# Models and ModelManager - of the auth app
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


class UserManager(BaseUserManager):
	#general user - register Form
	def create_user(self, email, mobile, full_name, password = None, is_active = True, is_staff = False, is_admin = False):

		if not email:
			raise ValueError("Email is mandatory.")

		if not password:
			raise ValueError("Password is mandatory.")

		if not mobile:
			raise ValueError("Mobile no. is mandatory.")

		if not full_name:
			raise ValueError("Full name is mandatory.")


		user_obj = self.model(email = self.normalize_email(email))
		user_obj.set_password(password)
		user_obj.staff = is_staff
		user_obj.admin = is_admin
		user_obj.active = is_active
		user_obj.mobile = mobile
		user_obj.full_name = full_name
		user_obj.save(using = self._db)
		return user_obj


	# creating staff user
	def create_staffuser(self, email, mobile, full_name, password = None):
		user_obj = self.create_user(email, mobile, full_name, password=password, is_staff = True)
		return user_obj

	#creting super user
	def create_superuser(self, email, mobile, full_name, password = None):
		user_obj = self.create_user(email, mobile, full_name, password=password, is_staff = True, is_admin = True)
		return user_obj



class User(AbstractBaseUser):
	email = models.EmailField(max_length = 255, unique = True)
	full_name = models.CharField(max_length = 200, blank = True, null = True)
	mobile = models.BigIntegerField()
	active = models.BooleanField(default = True)
	staff = models.BooleanField(default = False) # Staff user
	admin = models.BooleanField(default = False) # Superuser
	timestamp = models.DateTimeField(auto_now_add = True)

	objects = UserManager()

	USERNAME_FIELD = 'email'
	# python manage.py createsuperuser
	REQUIRED_FIELDS = ['full_name', 'mobile']


	def __str__(self):
		return self.email

	def get_full_name(self):
		return self.full_name

	def get_short_name(self):
		return self.full_name

	@property  #annotation
	def is_staff(self):
		return self.staff

	@property
	def is_admin(self):
		return self.admin

	@property
	def is_active(self):
		return self.active

	def has_perm(self, perm, obj = None):
		return True

	def  has_module_perms(self, app_label):
		return True
	
	

	