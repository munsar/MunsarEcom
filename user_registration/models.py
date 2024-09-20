from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin
from django.utils.translation import gettext_lazy as _

class UserManager(BaseUserManager):

	def _create_user(self, username, email, password, **extra_fields):
		if not email:
			raise ValueError('User must have email address')

		email = self.normalize_email(email)
		user = self.model(username=username, email=email, **extra_fields)
		user.set_password(password)
		user.save(using=self._db)
		return user

	def create_user(self, username, email=None, password=None, **extra_fields):
		extra_fields.setdefault('is_staff', False)
		extra_fields.setdefault('is_superuser', False)
		return self._create_user(username, email, password, **extra_fields)

	def create_superuser(self, username, email, password, **extra_fields):
		extra_fields.setdefault('is_staff', True)
		extra_fields.setdefault('is_superuser', True)

		if extra_fields.get('is_staff') is not True:
			raise ValueError('Superuser must have is_staff=True.')

		if extra_fields.get('is_superuser') is not True:
			raise ValueError('Superuser must have is_superuser=True.')

		return self._create_user(username, email, password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):

	username = models.CharField(
		_('username'),
		max_length=150,
		blank=True,
		help_text=_('Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.'),
		error_messages={
			'unique': _("A user with that phone already exists."),
		},

	)
	email = models.EmailField(_('email address'), max_length=50, unique=True, null=True, blank=True)

	is_staff = models.BooleanField(
		_('staff status'),
		default=False,
		help_text=_('Designates whether the user can log into this admin site.'),
	)

	is_active = models.BooleanField(
		_('active'),
		default=True,
		help_text=_(
			'Designates whether this user should be treated as active. '
			'Unselect this instead of deleting accounts.'
		),
	)
	email_confirmed = models.BooleanField(
		_('email active'),
		default=False,
		help_text=_(
			'Designates whether this user should be treated as active. '
			'Unselect this instead of deleting accounts.'
		),
	)

	last_login =  models.DateTimeField(_('last_login'), auto_now_add=False, auto_now=False, null=True)

	date_joined = models.DateTimeField(_('date joined'), auto_now_add=True, auto_now=False)

	objects = UserManager()

	EMAIL_FIELD = 'email'
	USERNAME_FIELD = 'email'
	REQUIRED_FIELDS = ['username']


class UserProfile(models.Model):

	user= models.OneToOneField(User, on_delete= models.CASCADE)
	firstname = models.CharField(max_length=50, null=True, blank=True)
	lastname = models.CharField(max_length=50, null=True, blank=True)
	country = models.CharField(max_length=50, blank=True, null=True)
	phone_number = models.CharField(max_length=20, null=True, blank=True)
	street_address_one = models.CharField(max_length=50, null=True, blank=True)
	street_address_two = models.CharField(max_length=50, null=True, blank=True)
	city = models.CharField(max_length=50, null=True, blank=True)
	zip_postal_code = models.CharField(max_length=50, null=True, blank=True)

	

	def __str__(self):
		return ('{} , {}'.format(self.firstname,self.lastname))
