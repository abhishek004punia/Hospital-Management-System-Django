from django.contrib.auth.decorators import user_passes_test


# ==========================
# Admin Only
# ==========================

def admin_required(view_func):
    return user_passes_test(
        lambda u: (
            u.is_authenticated and
            u.groups.filter(name="Admin").exists()
        ),
        login_url="/users/login/",
    )(view_func)


# ==========================
# Doctor Only
# ==========================

def doctor_required(view_func):
    return user_passes_test(
        lambda u: (
            u.is_authenticated and
            u.groups.filter(name="Doctor").exists()
        ),
        login_url="/users/login/",
    )(view_func)


# ==========================
# Receptionist Only
# ==========================

def receptionist_required(view_func):
    return user_passes_test(
        lambda u: (
            u.is_authenticated and
            u.groups.filter(name="Receptionist").exists()
        ),
        login_url="/users/login/",
    )(view_func)


# ==========================
# Admin + Doctor + Receptionist
# Patients / Appointments
# ==========================

def patient_access_required(view_func):
    return user_passes_test(
        lambda u: (
            u.is_authenticated and (
                u.groups.filter(name="Admin").exists() or
                u.groups.filter(name="Doctor").exists() or
                u.groups.filter(name="Receptionist").exists()
            )
        ),
        login_url="/users/login/",
    )(view_func)


def appointment_access_required(view_func):
    return user_passes_test(
        lambda u: (
            u.is_authenticated and (
                u.groups.filter(name="Admin").exists() or
                u.groups.filter(name="Doctor").exists() or
                u.groups.filter(name="Receptionist").exists()
            )
        ),
        login_url="/users/login/",
    )(view_func)


# ==========================
# Admin + Receptionist
# Billing / Pharmacy
# ==========================

def billing_access_required(view_func):
    return user_passes_test(
        lambda u: (
            u.is_authenticated and (
                u.groups.filter(name="Admin").exists() or
                u.groups.filter(name="Receptionist").exists()
            )
        ),
        login_url="/users/login/",
    )(view_func)


def pharmacy_access_required(view_func):
    return user_passes_test(
        lambda u: (
            u.is_authenticated and (
                u.groups.filter(name="Admin").exists() or
                u.groups.filter(name="Receptionist").exists()
            )
        ),
        login_url="/users/login/",
    )(view_func)


# ==========================
# Admin + Doctor
# Laboratory / Prescriptions
# ==========================

def laboratory_access_required(view_func):
    return user_passes_test(
        lambda u: (
            u.is_authenticated and (
                u.groups.filter(name="Admin").exists() or
                u.groups.filter(name="Doctor").exists()
            )
        ),
        login_url="/users/login/",
    )(view_func)


def prescription_access_required(view_func):
    return user_passes_test(
        lambda u: (
            u.is_authenticated and (
                u.groups.filter(name="Admin").exists() or
                u.groups.filter(name="Doctor").exists()
            )
        ),
        login_url="/users/login/",
    )(view_func)