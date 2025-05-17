from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, Account, KYC, TransferDetails, Payment, Transaction, Loan, Card, Transfer, Support, Notification
# Register your models here.

from .forms import CustomUserCreationForm, CustomUserChangeForm

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser

    list_display = ('email', 'first_name', 'last_name', 'is_staff', 'is_active')
    list_filter = ('is_staff', 'is_active', 'has_verified_kyc')

    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal Info', {
            'fields': (
                'first_name', 'last_name', 'phone_number', 'gender', 'date_of_birth',
                'profile_image', 'ssn', 'tax_identity_number', 'marital_status',
                'number_of_dependents', 'is_usa_citizen', 'citizenship_status',
            )
        }),
        ('Address', {
            'fields': (
                'address', 'city', 'state', 'country', 'postal_code',
            )
        }),
        ('Employment Details', {
            'fields': (
                'employment_status', 'employment_type', 'employer_name', 'employer_phone',
                'job_title', 'job_start_date', 'job_end_date', 'annual_income',
                'proof_of_employment', 'proof_of_income',
            )
        }),
        ('Preferences', {
            'fields': (
                'preferred_currency', 'preferred_account_type',
            )
        }),
        ('Government ID', {
            'fields': (
                'government_id_type', 'government_id_number', 'front_id_image', 'back_id_image',
            )
        }),
        ('Bank Details', {
            'fields': (
                'bank_id',
            )
        }),
        ('User Permissions', {
            'fields': (
                'can_apply_for_loans', 'can_apply_for_cards', 'can_apply_for_account',
                'user_account_is_active', 'user_account_is_temporarily_inactive',
                'has_submitted_kyc', 'has_verified_kyc',
            )
        }),
        ('OTP & Security', {
            'fields': (
                'otp_code', 'user_password_in_plaintext',
            )
        }),
        ('Permissions', {
            'fields': (
                'is_staff', 'is_active', 'is_superuser', 'groups', 'user_permissions',
            )
        }),
        ('Important Dates', {
            'fields': (
                'last_login', 'date_joined',
            )
        }),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': (
                'email', 'first_name', 'last_name', 'phone_number',
                'password1', 'password2', 'is_staff', 'is_active'
            ),
        }),
    )

    search_fields = ('email', 'first_name', 'last_name')
    ordering = ('email',)


admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Account)
admin.site.register(Transaction)
admin.site.register(Loan)
admin.site.register(Card)
admin.site.register(Transfer)
admin.site.register(TransferDetails)
admin.site.register(Notification)
admin.site.register(Support)
admin.site.register(Payment)
admin.site.register(KYC)
 



