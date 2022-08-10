## Models
Database table definition/blueprint

### Define Model
```
class Room(models.Model):
    host = models.ForeignKey(User, on_delete= models.SET_NULL, null=True)
    topic = models.ForeignKey(Topic, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    # participants = 
    updated = models.DateTimeField(auto_now=True)
```

Prepare The Migration
```python3 manage.py makemigrations```
Run Migrations
```python3 manage.py migrate ```
## NB 
Creating a super user ```python3 manage.py createsuperuser```