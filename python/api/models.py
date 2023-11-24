from django.db import models


class Administrador(models.Model):
    idadmin = models.AutoField(db_column='idAdmin', primary_key=True)  # Field name made lowercase.
    nombreadmin = models.CharField(db_column='nombreAdmin', max_length=30)  # Field name made lowercase.
    appatadmin = models.CharField(db_column='apPatAdmin', max_length=30)  # Field name made lowercase.
    apmatadmin = models.CharField(db_column='apMatAdmin', max_length=30)  # Field name made lowercase.
    contraadmin = models.CharField(db_column='contraAdmin', max_length=10)  # Field name made lowercase.
    correoadmin = models.CharField(db_column='correoAdmin', max_length=35)  # Field name made lowercase.

    objects = models.Manager()

    class Meta:
        managed = False
        db_table = 'administrador'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Catalogozonas(models.Model):
    idzona = models.AutoField(db_column='idZona', primary_key=True)  # Field name made lowercase.
    colonia = models.CharField(db_column='Colonia', max_length=50)  # Field name made lowercase.
    codigopostal = models.IntegerField(db_column='codigoPostal')  # Field name made lowercase.

    objects = models.Manager()
    class Meta:
        managed = False
        db_table = 'catalogozonas'


class Cliente(models.Model):
    idcliente = models.IntegerField(db_column='idCliente', primary_key=True)  # Field name made lowercase.
    nombrecliente = models.CharField(db_column='nombreCliente', max_length=30)  # Field name made lowercase.
    appatcliente = models.CharField(db_column='apPatCliente', max_length=30)  # Field name made lowercase.
    apmatcliente = models.CharField(db_column='apMatCliente', max_length=30)  # Field name made lowercase.
    contracliente = models.CharField(db_column='contraCliente', max_length=10)  # Field name made lowercase.
    correocliente = models.CharField(db_column='correoCliente', max_length=35)  # Field name made lowercase.
    callecliente = models.CharField(db_column='calleCliente', max_length=15)  # Field name made lowercase.
    colcliente = models.CharField(db_column='colCliente', max_length=20)  # Field name made lowercase.
    numextcliente = models.CharField(db_column='numExtCliente', max_length=5)  # Field name made lowercase.
    cpcliente = models.IntegerField(db_column='cpCliente')  # Field name made lowercase.

    objects = models.Manager()
    class Meta:
        managed = False
        db_table = 'cliente'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Reportefallas(models.Model):
    idfalla = models.AutoField(db_column='idFalla', primary_key=True)  # Field name made lowercase.
    motivorep = models.CharField(db_column='motivoRep', max_length=50)  # Field name made lowercase.
    fecharep = models.DateField(db_column='fechaRep')  # Field name made lowercase.
    estatusrep = models.CharField(db_column='estatusRep', max_length=20)  # Field name made lowercase.
    clavecliente = models.ForeignKey(Cliente, models.DO_NOTHING, db_column='claveCliente')  # Field name made lowercase.

    objects = models.Manager()
    class Meta:
        managed = False
        db_table = 'reportefallas'
