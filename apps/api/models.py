from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

# Create your models here.
class Restaurant(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='restaurant')
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    logo = CloudinaryField('image')

    def __str__(self):
        return self.name
    

class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='customer')
    avatar = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    address = models.CharField(max_length=255)

    def __str__(self):
        return self.user.get_full_name()
    
class Driver(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='driver')
    avatar = models.CharField(max_length=255)
    phone = models.CharField(max_length=255, blank=True)
    vehicle_type = models.CharField(max_length=255)
    vehicle_model = models.CharField(max_length=255)
    vehicle_plate_number = models.CharField(max_length=255)
    location = models.CharField(max_length=255)

    def __str__(self):
        return self.user.get_full_name()



""""
tching for file changes with StatReloader
Performing system checks...

System check identified no issues (0 silenced).
August 11, 2023 - 17:12:51
Django version 3.2.5, using settings 'eat4me.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.
[11/Aug/2023 17:12:53] "GET /admin/api/restaurant/ HTTP/1.1" 200 6679
[11/Aug/2023 17:12:53] "GET /admin/jsi18n/ HTTP/1.1" 200 3325
[11/Aug/2023 17:12:56] "GET /admin/api/customer/ HTTP/1.1" 200 5513
[11/Aug/2023 17:12:56] "GET /admin/jsi18n/ HTTP/1.1" 200 3325
Internal Server Error: /admin/api/driver/
Traceback (most recent call last):
  File "/Users/kN-dev/Documents/foodapp/lib/python3.11/site-packages/django/db/backends/utils.py", line 84, in _execute
    return self.cursor.execute(sql, params)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/Users/kN-dev/Documents/foodapp/lib/python3.11/site-packages/django/db/backends/sqlite3/base.py", line 423, in execute
    return Database.Cursor.execute(self, query, params)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
sqlite3.OperationalError: no such column: api_driver.phone

The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "/Users/kN-dev/Documents/foodapp/lib/python3.11/site-packages/django/core/handlers/exception.py", line 47, in inner
    response = get_response(request)
               ^^^^^^^^^^^^^^^^^^^^^
  File "/Users/kN-dev/Documents/foodapp/lib/python3.11/site-packages/django/core/handlers/base.py", line 181, in _get_response
    response = wrapped_callback(request, *callback_args, **callback_kwargs)
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/Users/kN-dev/Documents/foodapp/lib/python3.11/site-packages/django/contrib/admin/options.py", line 616, in wrapper
    return self.admin_site.admin_view(view)(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/Users/kN-dev/Documents/foodapp/lib/python3.11/site-packages/django/utils/decorators.py", line 130, in _wrapped_view
    response = view_func(request, *args, **kwargs)
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/Users/kN-dev/Documents/foodapp/lib/python3.11/site-packages/django/views/decorators/cache.py", line 44, in _wrapped_view_func
    response = view_func(request, *args, **kwargs)
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/Users/kN-dev/Documents/foodapp/lib/python3.11/site-packages/django/contrib/admin/sites.py", line 232, in inner
    return view(request, *args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/Users/kN-dev/Documents/foodapp/lib/python3.11/site-packages/django/utils/decorators.py", line 43, in _wrapper
    return bound_method(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/Users/kN-dev/Documents/foodapp/lib/python3.11/site-packages/django/utils/decorators.py", line 130, in _wrapped_view
    response = view_func(request, *args, **kwargs)
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/Users/kN-dev/Documents/foodapp/lib/python3.11/site-packages/django/contrib/admin/options.py", line 1815, in changelist_view
    'selection_note': _('0 of %(cnt)s selected') % {'cnt': len(cl.result_list)},
                                                           ^^^^^^^^^^^^^^^^^^^
  File "/Users/kN-dev/Documents/foodapp/lib/python3.11/site-packages/django/db/models/query.py", line 262, in __len__
    self._fetch_all()
  File "/Users/kN-dev/Documents/foodapp/lib/python3.11/site-packages/django/db/models/query.py", line 1324, in _fetch_all
    self._result_cache = list(self._iterable_class(self))
                         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/Users/kN-dev/Documents/foodapp/lib/python3.11/site-packages/django/db/models/query.py", line 51, in __iter__
    results = compiler.execute_sql(chunked_fetch=self.chunked_fetch, chunk_size=self.chunk_size)
              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/Users/kN-dev/Documents/foodapp/lib/python3.11/site-packages/django/db/models/sql/compiler.py", line 1175, in execute_sql
    cursor.execute(sql, params)
  File "/Users/kN-dev/Documents/foodapp/lib/python3.11/site-packages/django/db/backends/utils.py", line 98, in execute
    return super().execute(sql, params)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/Users/kN-dev/Documents/foodapp/lib/python3.11/site-packages/django/db/backends/utils.py", line 66, in execute
    return self._execute_with_wrappers(sql, params, many=False, executor=self._execute)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/Users/kN-dev/Documents/foodapp/lib/python3.11/site-packages/django/db/backends/utils.py", line 75, in _execute_with_wrappers
    return executor(sql, params, many, context)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/Users/kN-dev/Documents/foodapp/lib/python3.11/site-packages/django/db/backends/utils.py", line 79, in _execute
    with self.db.wrap_database_errors:
  File "/Users/kN-dev/Documents/foodapp/lib/python3.11/site-packages/django/db/utils.py", line 90, in __exit__
    raise dj_exc_value.with_traceback(traceback) from exc_value
  File "/Users/kN-dev/Documents/foodapp/lib/python3.11/site-packages/django/db/backends/utils.py", line 84, in _execute
    return self.cursor.execute(sql, params)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/Users/kN-dev/Documents/foodapp/lib/python3.11/site-packages/django/db/backends/sqlite3/base.py", line 423, in execute
    return Database.Cursor.execute(self, query, params)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
django.db.utils.OperationalError: no such column: api_driver.phone
[11/Aug/2023 17:12:58] "GET /admin/api/driver/ HTTP/1.1" 500 157746
"""