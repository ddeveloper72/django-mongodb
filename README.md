# Reference on using a non-relational db, MongoDB, with Django

My reading materials comes from:
[Djongo](https://djongo.readthedocs.io/)

For more detailed information on the connection settings required for remote access to your MongoDB collection, please see:
[Django and MongoDB connector](https://nesdis.github.io/djongo/get-started/)

The connection0n settings for this project were simplified to parsing the mongo_db uri as a string.

## Setting up the remote MongoDB database connection

### Workspace environment settings

```json

{
	"settings": {
		"terminal.integrated.env.windows": {
			"DJANGO_SETTINGS_MODULE" : "mysite.settings",
			"MONGODB_URI ": "mongodb://<db_username>:<dn_password>@ds050539.mlab.com:50539/<db-name>",
		}
	}
}

```

### my app settings

``` python

DATABASES = {
    'default': {
        'ENGINE': 'djongo',
        'NAME': '<db_name>',
        'CLIENT': {
            'host': str(os.environ.get('MONGODB_URI '))
        }
    }
}

```

Once the fresh from start app was run using the workspace settings, I was able to run `python manage.py makemigrations`

How ever when I ran `python manage.py migrate`, I 
got a `djongo.database.DatabaseError`. The cause, `djongo.exceptions.SQLDecodeError: FAILED SQL: INSERT INTO "django_migrations" ("app", "name", "applied")`

In order to trouble shoot this, I found many references by developers commenting on stackoverflow to use this older version of sqlparse==0.2.4.  Having installed the current version of Djongo v1.3.2 at the time of writing this document, sqlparse v0.2.4 along with Django v2.2.13 is installed by default.

Further trouble-shooting referenced the database error:

    "Pymongo error: OrderedDict([('operationTime', Timestamp(1591137961, 1)), ('ok', 0.0), ('errmsg', 'Transaction numbers are only allowed on storage engines that support document-level locking'), ('code', 20), ('codeName', 'IllegalOperation'), ('$clusterTime', OrderedDict([('clusterTime', Timestamp(1591137961, 1)), ('signature', OrderedDict([('hash', b'c\xd2I\xbf\x1f\xc4\xd8\xdc\xb4>\x85&=e\xdc!\x11\x08\x7fO'), ('keyId', 6796109932815974401)]))]))]) Version: 1.3.2"

    This MongoDB deployment does not support "retryable writes". Please add **retryWrites=false** to your connection string.

Searching for the source of the error, led me a post by contributor funkenstrahlen on GitHub, [parse-community/parse-server](https://github.com/parse-community/parse-server/issues/5983)

The parse error, that was preventing the `manage.py migrate` from happening was resolve by adding retryWrites=false to my mongoDB database uri.  Once added, when running `manage.py migrate`, the migrations were sent to the db., how ever Django still reports the same `djongo.database.DatabaseError`.

On foot of this, now that the migrations had been applied and I was able to see the new documents added to my collections on mLab.

![MongoDB collection](https://github.com/ddeveloper72/django-mongodb/blob/master/static/img/db-collections-1.png "db collections")

I was then able to create a the superuser and store that data to a new document in the  auth-user collection.

![auth_user document](https://github.com/ddeveloper72/django-mongodb/blob/master/static/img/db-auth_user-document-2.png "db collections")


This is work is still in progress.

![Figuring out stuff](https://github.com/ddeveloper72/django-mongodb/blob/master/static/img/wip.png "working hard!")