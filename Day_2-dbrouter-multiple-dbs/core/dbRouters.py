class AuthRouter:
    """
    A router to control all database operations on 'auth', 'contenttypes','admin'and 'sessions' app models.
    """
    route_app_labels = {'auth', 'contenttypes','admin','sessions'}

    def db_for_read(self, model, **hints):
        """
        Attempts to read.
        """
        if model._meta.app_label in self.route_app_labels:
            return 'auth_db'
        return None

    def db_for_write(self, model, **hints):
        """
        Attempts to write.
        """
        if model._meta.app_label in self.route_app_labels:
            return 'auth_db'
        return None

    def allow_relation(self, obj1, obj2, **hints):
        """
        Allow relations if a model in apps is
        involved.
        """
        if (
            obj1._meta.app_label in self.route_app_labels or
            obj2._meta.app_label in self.route_app_labels
        ):
           return True
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        """
        Make sure apps only appear in the
        'auth_db' database.
        """
        if app_label in self.route_app_labels:
            return db == 'auth_db'
        return None


class App1Router:
    """
    A router to control all database operations on app1 app models.
    """
    route_app_labels = {'app1'}

    def db_for_read(self, model, **hints):
        """
        Attempts to read.
        """
        if model._meta.app_label in self.route_app_labels:
            return 'app1_db'
        return None

    def db_for_write(self, model, **hints):
        """
        Attempts to write.
        """
        if model._meta.app_label in self.route_app_labels:
            return 'app1_db'
        return None


    def allow_migrate(self, db, app_label, model_name=None, **hints):
        """
        Make sure app1 app only appear in the
        'app1_db' database.
        """
        if app_label in self.route_app_labels:
            return db == 'app1_db'
        return None