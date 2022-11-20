# Generated by Django 4.1.2 on 2022-11-18 05:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Bank_details',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bank_name', models.CharField(max_length=255, null=True)),
                ('bank_identifier_code', models.CharField(max_length=255, null=True)),
                ('branch', models.CharField(max_length=255, null=True)),
                ('swift_code', models.CharField(max_length=255, null=True)),
                ('address', models.CharField(max_length=500, null=True)),
                ('country', models.CharField(max_length=255, null=True)),
                ('status', models.CharField(max_length=255, null=True)),
                ('dt', models.DateField(auto_now_add=True)),
                ('tm', models.TimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Customer_details',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dt', models.DateField(auto_now=True)),
                ('tm', models.TimeField(auto_now=True)),
                ('updated', models.DateTimeField(default=django.utils.timezone.now)),
                ('status', models.CharField(max_length=255, null=True)),
                ('name', models.CharField(max_length=255, null=True)),
                ('phone', models.CharField(max_length=255, null=True)),
                ('customer_id', models.CharField(max_length=255, null=True)),
                ('bank', models.CharField(max_length=255, null=True)),
                ('customer_type', models.CharField(choices=[('individual', 'individual'), ('company', 'company')], max_length=255, null=True)),
                ('company_name', models.CharField(max_length=255, null=True)),
                ('street1', models.CharField(max_length=255, null=True)),
                ('street2', models.CharField(max_length=255, null=True)),
                ('city', models.CharField(max_length=255, null=True)),
                ('satte', models.CharField(max_length=255, null=True)),
                ('zip', models.CharField(max_length=255, null=True)),
                ('email', models.CharField(max_length=255, null=True)),
                ('customer_doc_id', models.FileField(null=True, upload_to='customer_document')),
                ('contract_certi', models.FileField(null=True, upload_to='customer_document')),
                ('tax_certificate', models.FileField(null=True, upload_to='customer_document')),
                ('other_document', models.FileField(null=True, upload_to='customer_document')),
                ('profile_pic', models.FileField(null=True, upload_to='customer_document')),
                ('customer_doc_id_update_dt', models.DateField(null=True)),
                ('contract_certi_update_dt', models.DateField(null=True)),
                ('tax_certificate_update_dt', models.DateField(null=True)),
                ('other_document_update_dt', models.DateField(null=True)),
                ('customer_doc_id_extesion', models.CharField(max_length=255, null=True)),
                ('contract_certi_extesion', models.CharField(max_length=255, null=True)),
                ('tax_certificate_extesion', models.CharField(max_length=255, null=True)),
                ('other_document_extesion', models.CharField(max_length=255, null=True)),
                ('customer_doc_id_name', models.CharField(max_length=255, null=True)),
                ('contract_certi_name', models.CharField(max_length=255, null=True)),
                ('tax_certificate_name', models.CharField(max_length=255, null=True)),
                ('other_document_name', models.CharField(max_length=255, null=True)),
                ('bank_relation_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Customer_details_Bank_details_id', to='super_admin.bank_details')),
                ('created_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Customer_details_created_by', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='intractive_map',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=255, null=True)),
                ('customer_id', models.CharField(max_length=255, null=True)),
                ('Phoneno', models.CharField(max_length=255, null=True)),
                ('UnitNo', models.IntegerField(null=True)),
                ('UnitNo_primary', models.IntegerField(null=True)),
                ('BlockNo', models.CharField(max_length=255, null=True)),
                ('UnitArea', models.FloatField(max_length=255, null=True)),
                ('LandArea', models.FloatField(max_length=255, null=True)),
                ('UType', models.CharField(max_length=255, null=True)),
                ('Price', models.FloatField(blank=True, null=True)),
                ('Bank', models.CharField(max_length=255, null=True)),
                ('Status', models.CharField(max_length=255, null=True)),
                ('dt', models.DateField(auto_now_add=True)),
                ('tm', models.TimeField(auto_now_add=True)),
                ('current_status', models.CharField(max_length=255, null=True)),
                ('attached_file', models.FileField(null=True, upload_to='property_image')),
                ('currency', models.CharField(default='SAR', max_length=255, null=True)),
                ('Price_currency', models.CharField(max_length=255, null=True)),
                ('bank_relation_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='intractive_map_Bank_details_id', to='super_admin.bank_details')),
                ('customer_id_mapping', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='intractive_map_customer_id', to='super_admin.customer_details')),
            ],
        ),
        migrations.CreateModel(
            name='status_code',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dt', models.DateField(auto_now=True)),
                ('tm', models.TimeField(auto_now=True)),
                ('updated', models.DateTimeField(default=django.utils.timezone.now)),
                ('status', models.CharField(max_length=255, null=True)),
                ('text', models.CharField(max_length=255, null=True)),
                ('status_code', models.IntegerField(null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='user_Details',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dt', models.DateField(auto_now=True)),
                ('tm', models.TimeField(auto_now=True)),
                ('updated', models.DateTimeField(default=django.utils.timezone.now)),
                ('status', models.CharField(max_length=255, null=True)),
                ('name', models.CharField(max_length=255, null=True)),
                ('phone', models.CharField(max_length=255, null=True)),
                ('email', models.EmailField(max_length=254, null=True)),
                ('mobile', models.CharField(max_length=255, null=True)),
                ('emp_id', models.CharField(max_length=255, null=True)),
                ('address1', models.CharField(max_length=255, null=True)),
                ('address2', models.CharField(max_length=255, null=True)),
                ('city', models.CharField(max_length=255, null=True)),
                ('state', models.CharField(max_length=255, null=True)),
                ('country', models.CharField(max_length=255, null=True)),
                ('zip', models.CharField(max_length=255, null=True)),
                ('password_geration_type', models.CharField(choices=[('Automatic', 'Automatic'), ('Manual', 'Manual')], max_length=255, null=True)),
                ('user_type', models.CharField(choices=[('manager', 'manager'), ('salesman', 'salesman'), ('admin', 'admin')], max_length=255, null=True)),
                ('atatchment', models.FileField(null=True, upload_to='user_image')),
                ('plot_list_view', models.CharField(max_length=255, null=True)),
                ('price_visibility', models.IntegerField(default=1, null=True)),
                ('property_access', models.CharField(choices=[('all', 'all'), ('plot_based', 'plot_based')], max_length=255, null=True)),
                ('manager_nav_ploat_permission', models.IntegerField(default=0)),
                ('manager_nav_user_permission', models.IntegerField(default=0)),
                ('manager_nav_plot_edit_permission', models.IntegerField(default=0)),
                ('manager_nav_booking_cancel_permission', models.IntegerField(default=0)),
                ('manager_nav_customer_read_permission', models.IntegerField(default=0)),
                ('manager_nav_customer_write_permission', models.IntegerField(default=0)),
                ('manager_nav_customer_edit_permission', models.IntegerField(default=0)),
                ('manager_nav_document_read_permission', models.IntegerField(default=0)),
                ('manager_nav_document_write_permission', models.IntegerField(default=0)),
                ('manager_nav_document_edit_permission', models.IntegerField(default=0)),
                ('auth_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='auth_user_login_id', to=settings.AUTH_USER_MODEL)),
                ('created_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='added_by_user_id', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='user_request_plot',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dt', models.DateField(auto_now=True)),
                ('tm', models.TimeField(auto_now=True)),
                ('updated', models.DateTimeField(default=django.utils.timezone.now)),
                ('status', models.CharField(max_length=255, null=True)),
                ('name', models.CharField(max_length=255, null=True)),
                ('booking_id', models.CharField(max_length=255, null=True)),
                ('phone', models.CharField(max_length=255, null=True)),
                ('bank', models.CharField(max_length=255, null=True)),
                ('read_status', models.IntegerField(default=0)),
                ('booking_status', models.IntegerField(null=True)),
                ('reset_to_availale', models.IntegerField(null=True)),
                ('available_status', models.IntegerField(default=1)),
                ('customer_doc_id', models.FileField(null=True, upload_to='customer_document')),
                ('contract_certi', models.FileField(null=True, upload_to='customer_document')),
                ('tax_certificate', models.FileField(null=True, upload_to='customer_document')),
                ('other_document', models.FileField(null=True, upload_to='customer_document')),
                ('Price', models.FloatField(blank=True, null=True)),
                ('auth_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_request_plot_login_id', to=settings.AUTH_USER_MODEL)),
                ('bank_relation_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_request_plot_Bank_details_id', to='super_admin.bank_details')),
                ('customer_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_request_plot_customer_id', to='super_admin.customer_details')),
                ('manager_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_request_plot_manager_id', to='super_admin.user_details')),
                ('property_mapping_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_request_plot_user_login_id', to='super_admin.intractive_map')),
                ('user_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_request_plot_user_login_id', to='super_admin.user_details')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='user_manger_mapping',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dt', models.DateField(auto_now=True)),
                ('tm', models.TimeField(auto_now=True)),
                ('updated', models.DateTimeField(default=django.utils.timezone.now)),
                ('status', models.CharField(max_length=255, null=True)),
                ('manager_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_manger_mapping_manager_id', to='super_admin.user_details')),
                ('user_auth_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_manger_mapping_auth_id', to=settings.AUTH_USER_MODEL)),
                ('user_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_manger_mapping_user_login_id', to='super_admin.user_details')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='user_log',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dt', models.DateField(auto_now=True)),
                ('tm', models.TimeField(auto_now=True)),
                ('updated', models.DateTimeField(default=django.utils.timezone.now)),
                ('status', models.CharField(max_length=255, null=True)),
                ('d_text', models.TextField(null=True)),
                ('status_content', models.TextField(null=True)),
                ('user_type', models.CharField(choices=[('administrator', 'administrator'), ('staff', 'staff')], max_length=255, null=True)),
                ('action_appy_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_log_user_login_id', to='super_admin.user_details')),
                ('action_auth_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_log_auth_login_id', to=settings.AUTH_USER_MODEL)),
                ('user_mapping_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_log_login_id', to='super_admin.user_details')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='user_access_property_mapping',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dt', models.DateField(auto_now=True)),
                ('tm', models.TimeField(auto_now=True)),
                ('updated', models.DateTimeField(default=django.utils.timezone.now)),
                ('status', models.CharField(max_length=255, null=True)),
                ('auth_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_access_property_mapping_auth_id', to=settings.AUTH_USER_MODEL)),
                ('mapping_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_access_property_mapping_id', to='super_admin.user_details')),
                ('property_mapping_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_access_property_mapping_property_id', to='super_admin.intractive_map')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='intractive_map_plot_view_image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('attached_file', models.FileField(null=True, upload_to='property_multiple_image_plot_view')),
                ('image_type', models.CharField(max_length=255, null=True)),
                ('image_name', models.CharField(max_length=255, null=True)),
                ('dt', models.DateField(auto_now_add=True)),
                ('tm', models.TimeField(auto_now_add=True)),
                ('plot_type', models.CharField(max_length=255, null=True)),
                ('status', models.CharField(max_length=255, null=True)),
                ('mapping_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='intractive_map_plot_view_image_map_id', to='super_admin.intractive_map')),
            ],
        ),
        migrations.CreateModel(
            name='intractive_map_multiple_image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('attached_file', models.FileField(null=True, upload_to='property_multiple_image')),
                ('image_type', models.CharField(max_length=255, null=True)),
                ('image_name', models.CharField(max_length=255, null=True)),
                ('dt', models.DateField(auto_now_add=True)),
                ('tm', models.TimeField(auto_now_add=True)),
                ('status', models.CharField(max_length=255, null=True)),
                ('mapping_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='intractive_map_multiple_image_id', to='super_admin.intractive_map')),
            ],
        ),
        migrations.CreateModel(
            name='booking_log',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dt', models.DateField(auto_now=True)),
                ('tm', models.TimeField(auto_now=True)),
                ('updated', models.DateTimeField(default=django.utils.timezone.now)),
                ('status', models.CharField(max_length=255, null=True)),
                ('user_type', models.CharField(choices=[('administrator', 'administrator'), ('staff', 'staff')], max_length=255, null=True)),
                ('d_text', models.TextField(null=True)),
                ('status_content', models.TextField(null=True)),
                ('log_type', models.CharField(choices=[('administrator', 'administrator'), ('staff', 'staff')], max_length=255, null=True)),
                ('action_appy_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='booking_log_user_login_id', to='super_admin.user_details')),
                ('assigned_user_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='booking_log_assign_user_login_id', to='super_admin.user_details')),
                ('auth_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='booking_log_auth_login_id', to=settings.AUTH_USER_MODEL)),
                ('booking_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='booking_log_id', to='super_admin.user_request_plot')),
                ('intractive_map_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='booking_log_intractive_map_id_id', to='super_admin.intractive_map')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
