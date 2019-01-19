from django.db import models
import re
import bcrypt

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

# Create your models for users here.

class UserManager(models.Manager):
    def validate(self, form_data):
        errors = []

        if len(form_data['first_name']) < 1:
            errors.append('Please enter first name.')
        if len(form_data['last_name']) < 1:
            errors.append('Please enter last name.')
        if not EMAIL_REGEX.match(form_data['email']):
            errors.append('Please enter a valid email address.')
        if len(form_data['password']) < 8:
            errors.append('Please enter a password that is 8 characters long.')
        if form_data['password'] != form_data['confirm_pw']:
            errors.append('Passwwords must match. Try again.')
        #now lets verify if the user is not in the db.
        if self.filter(email=form_data['email']):
            errors.append('Email already exits.')
        print(form_data)
        return errors

        #if all passes above let's create the user now.

        #hash the password
    def create_user(self, form):
        pw_hash = bcrypt.hashpw(form['password'].encode(), bcrypt.gensalt())
        return self.create(
            first_name=form['first_name'],
            last_name=form['last_name'],
            email=form['email'],
            pw_hash=pw_hash
        )

    def login_user(self, form):
        user_list = self.filter(email=form['email'])
        if len(user_list) > 0:
            user = user_list[0]
            if bcrypt.checkpw(form['password'].encode(), user.pw_hash.encode()):
                return(True, user.id)
            else:
                return(False, "Email or password not valid.")
        else:
            return(False, "Email or password not valid.")

    def update_validate(self, update_form, user_id):
        errors = []
        if len(update_form['first_name']) < 1:
            errors.append('First name must not be emptied.')
        if len(update_form['last_name']) < 1:
            errors.append('Last name should not be empty. Try again.')
        if not EMAIL_REGEX.match(update_form['email']):
            errors.append('Please enter a valid email address.')
        if self.filter(email = update_form['email']):
            errors.append('Email aready exits. Please try another.')
        return errors
    
    def update_user(self, update_form, user_id):
        user = User.objects.get(id=user_id)
        user.first_name = update_form['first_name']
        user.last_name = update_form['last_name']
        user.email = update_form['email']
        user.save()




class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    pw_hash = models.CharField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()

    def __str__(self):
        return self.first_name
