from django.shortcuts import render
from django.http import HttpResponse
from departments.models import Department
from reportlab.pdfgen import canvas

from reportlab.platypus import (
    SimpleDocTemplate,
    Table,
    TableStyle,
    Paragraph,
)

from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet

from patients.models import Patient
from doctors.models import Doctor
from appointments.models import Appointment
from billing.models import Billing

from django.db.models import Q
from django.db.models import Sum

from datetime import datetime
from django.db.models import Count, Sum
from django.db.models.functions import ExtractMonth
from pharmacy.models import Medicine
from laboratory.models import LabTest
from django.contrib.auth.decorators import login_required
from accounts.decorators import admin_required

@login_required
@admin_required
def reports_dashboard(request):

    context = {

        "total_patients": Patient.objects.count(),

        "total_doctors": Doctor.objects.count(),

        "total_appointments": Appointment.objects.count(),

        "total_bills": Billing.objects.count(),
        "total_departments": Department.objects.count(),

    }

    return render(
        request,
        "reports/dashboard_reports.html",
        context
    )

@login_required
@admin_required
def patient_report(request):

    patients = Patient.objects.all()

    return render(
        request,
        "reports/patient_report.html",
        {
            "patients": patients
        }
    )


@login_required
@admin_required
def department_report(request):

    departments = Department.objects.all()

    return render(
        request,
        "reports/department_report.html",
        {
            "departments": departments
        }
    )


@login_required
@admin_required
def patient_report_pdf(request):

    response = HttpResponse(content_type="application/pdf")

    response["Content-Disposition"] = (
        'attachment; filename="patient_report.pdf"'
    )

    doc = SimpleDocTemplate(response)

    elements = []

    styles = getSampleStyleSheet()

    elements.append(
        Paragraph("Hospital Management System", styles["Heading1"])
    )

    elements.append(
        Paragraph("Patient Report", styles["Heading2"])
    )

    data = [
        [
            "Patient ID",
            "Name",
            "Age",
            "Gender",
            "Mobile",
            "Email",
            "Disease",
            "Admission Date"
        ]
    ]

    patients = Patient.objects.all()

    for patient in patients:

        data.append([

            patient.patient_id,

            patient.full_name,

            str(patient.age),

            patient.gender,

            patient.mobile,
            
            patient.email,

            patient.disease,

            patient.admission_date.strftime("%d-%m-%Y"),

        ])

    table = Table(data)

    table.setStyle(

        TableStyle([

            ("BACKGROUND", (0,0), (-1,0), colors.grey),

            ("TEXTCOLOR", (0,0), (-1,0), colors.white),

            ("GRID", (0,0), (-1,-1), 1, colors.black),

            ("BACKGROUND", (0,1), (-1,-1), colors.beige),

            ("ALIGN", (0,0), (-1,-1), "CENTER"),

        ])

    )

    elements.append(table)

    doc.build(elements)

    return response

@login_required
@admin_required
def doctor_report(request):

    doctors = Doctor.objects.all()

    return render(
        request,
        "reports/doctor_report.html",
        {
            "doctors": doctors
        }
    )

@login_required
@admin_required
def doctor_report_pdf(request):

    response = HttpResponse(content_type="application/pdf")

    response["Content-Disposition"] = (
        'attachment; filename="doctor_report.pdf"'
    )

    doc = SimpleDocTemplate(response)

    elements = []

    styles = getSampleStyleSheet()

    elements.append(
        Paragraph("Hospital Management System", styles["Heading1"])
    )

    elements.append(
        Paragraph("Doctor Report", styles["Heading2"])
    )

    data = [[
        "Doctor ID",
        "Name",
        "Department",
        "Specialization",
        "Qualification",
        "Experience",
        "Mobile",
        "Email",
        "Fee",
        "Stats",
    ]]

    doctors = Doctor.objects.all()

    print(Doctor.objects.values().first())

    for doctor in doctors:

        data.append([
            doctor.doctor_id,
            doctor.full_name,
            doctor.department,
            doctor.specialization,
            doctor.qualification,
            str(doctor.experience),
            doctor.mobile,
            doctor.email,
            f"₹{doctor.consultation_fee}",
            doctor.status,
        ])

    table = Table(data)

    table.setStyle(TableStyle([
        ("BACKGROUND",(0,0),(-1,0),colors.grey),
        ("TEXTCOLOR",(0,0),(-1,0),colors.white),
        ("GRID",(0,0),(-1,-1),1,colors.black),
        ("BACKGROUND",(0,1),(-1,-1),colors.beige),
        ("ALIGN",(0,0),(-1,-1),"CENTER"),
        ("FONTSIZE", (0,0), (-1,-1), 8),
        ("BOTTOMPADDING",(0,0),(-1,0),8),
    ]))

    elements.append(table)

    doc.build(elements)

    return response


@login_required
@admin_required
def appointment_report(request):

    appointments = Appointment.objects.all()

    search_date = request.GET.get("date")

    if search_date:
        appointments = appointments.filter(
            appointment_date=search_date
        )

    return render(
        request,
        "reports/appointment_report.html",
        {
            "appointments": appointments,
            "search_date": search_date,
        }
    )


@login_required
@admin_required
def appointment_report_pdf(request):

    response = HttpResponse(content_type="application/pdf")

    response["Content-Disposition"] = (
        'attachment; filename="appointment_report.pdf"'
    )

    doc = SimpleDocTemplate(response)

    elements = []

    styles = getSampleStyleSheet()

    elements.append(
        Paragraph("Hospital Management System", styles["Heading1"])
    )

    elements.append(
        Paragraph("Appointment Report", styles["Heading2"])
    )

    data = [[
        "Appointment ID",
        "Patient",
        "Doctor",
        "Date",
        "Time",
        "Status"
    ]]

    appointments = Appointment.objects.all()

    for appointment in appointments:

        data.append([
            appointment.appointment_id,
            str(appointment.patient),
            str(appointment.doctor),
            appointment.appointment_date.strftime("%d-%m-%y"),
            appointment.appointment_time.strftime("%I:%M %p"),
            appointment.status,
        ])

    table = Table(data)

    table.setStyle(TableStyle([
        ("BACKGROUND",(0,0),(-1,0),colors.grey),
        ("TEXTCOLOR",(0,0),(-1,0),colors.white),
        ("GRID",(0,0),(-1,-1),1,colors.black),
        ("BACKGROUND",(0,1),(-1,-1),colors.beige),
        ("ALIGN",(0,0),(-1,-1),"CENTER"),
    ]))

    elements.append(table)

    doc.build(elements)

    return response


@login_required
@admin_required
def billing_report(request):

    bills = Billing.objects.all()

    total_revenue = sum(bill.total_amount for bill in bills)

    paid_bills = bills.filter(payment_status="Paid").count()

    pending_bills = bills.filter(payment_status="Pending").count()

    context = {

        "bills": bills,
        "total_revenue": total_revenue,
        "paid_bills": paid_bills,
        "pending_bills": pending_bills,

    }

    return render(
        request,
        "reports/billing_report.html",
        context
    )


@login_required
@admin_required
def monthly_report(request):

    month = request.GET.get("month")

    patients = 0
    appointments = 0
    bills = 0
    revenue = 0

    if month:

        year, month_number = month.split("-")

        patients = Patient.objects.filter(
            created_at__year=year,
            created_at__month=month_number
        ).count()

        appointments = Appointment.objects.filter(
            appointment_date__year=year,
            appointment_date__month=month_number
        ).count()

        bill_queryset = Billing.objects.filter(
            bill_date__year=year,
            bill_date__month=month_number
        )

        bills = bill_queryset.count()

        revenue = bill_queryset.aggregate(
            Sum("total_amount")
        )["total_amount__sum"] or 0

    context = {

        "selected_month": month,

        "patients": patients,

        "appointments": appointments,

        "bills": bills,

        "revenue": revenue,

    }

    return render(
        request,
        "reports/monthly_report.html",
        context
    )


@login_required
@admin_required
def billing_report_pdf(request):

    response = HttpResponse(content_type="application/pdf")

    response["Content-Disposition"] = (
        'attachment; filename="billing_report.pdf"'
    )

    doc = SimpleDocTemplate(response)

    elements = []

    styles = getSampleStyleSheet()

    elements.append(
        Paragraph("Hospital Management System", styles["Heading1"])
    )

    elements.append(
        Paragraph("Billing Report", styles["Heading2"])
    )

    data = [[
        "Bill ID",
        "Patient",
        "Doctor",
        "Total Amount",
        "Payment Status",
        "Bill Date"
    ]]

    bills = Billing.objects.all()

    for bill in bills:

        data.append([
            bill.bill_id,
            str(bill.patient),
            str(bill.doctor),
            str(bill.total_amount),
            bill.payment_status,
            bill.bill_date.strftime("%d-%m-%y"),
        ])

    table = Table(data)

    table.setStyle(TableStyle([
        ("BACKGROUND",(0,0),(-1,0),colors.grey),
        ("TEXTCOLOR",(0,0),(-1,0),colors.white),
        ("GRID",(0,0),(-1,-1),1,colors.black),
        ("BACKGROUND",(0,1),(-1,-1),colors.beige),
        ("ALIGN",(0,0),(-1,-1),"CENTER"),
    ]))

    elements.append(table)

    doc.build(elements)

    return response

@login_required
@admin_required
def analytics_dashboard(request):

    total_patients = Patient.objects.count()
    total_doctors = Doctor.objects.count()
    total_appointments = Appointment.objects.count()

    total_revenue = float(Billing.objects.aggregate(
        Sum("total_amount")
    )["total_amount__sum"] or 0)

    # Monthly Appointments
    monthly_appointments = (
        Appointment.objects
        .annotate(month=ExtractMonth("appointment_date"))
        .values("month")
        .annotate(total=Count("id"))
        .order_by("month")
    )

    # Monthly Revenue
    monthly_billing = (
        Billing.objects
        .annotate(month=ExtractMonth("bill_date"))
        .values("month")
        .annotate(total=Sum("total_amount"))
        .order_by("month")
    )

    # Payment Status
    paid_count = Billing.objects.filter(
        payment_status="Paid"
    ).count()

    pending_count = Billing.objects.filter(
        payment_status="Pending"
    ).count()

    cancelled_count = Billing.objects.filter(
        payment_status="Cancelled"
    ).count()

    # Top Doctors
    top_doctors = (
        Appointment.objects
        .values("doctor__full_name")
        .annotate(total=Count("id"))
        .order_by("-total")[:5]
    )

    context = {

        "total_patients": total_patients,
        "total_doctors": total_doctors,
        "total_appointments": total_appointments,
        "total_revenue": total_revenue,

        "appointment_labels": [
            item["month"] for item in monthly_appointments
        ],

        "appointment_data": [
            item["total"] for item in monthly_appointments
        ],

        "billing_labels": [
            item["month"] for item in monthly_billing
        ],

        "billing_data": [
            float(item["total"] or 0) for item in monthly_billing
        ],

        "paid_count": paid_count,
        "pending_count": pending_count,
        "cancelled_count": cancelled_count,

        "doctor_labels": [
            item["doctor__full_name"]
            for item in top_doctors
        ],

        "doctor_data": [
            item["total"]
            for item in top_doctors
        ],
    }

    return render(
        request,
        "reports/analytics_dashboard.html",
        context
    )


@login_required
@admin_required
def pharmacy_report(request):

    medicines = Medicine.objects.all()

    return render(
        request,
        "reports/pharmacy_report.html",
        {
            "medicines": medicines
        }
    )


@login_required
@admin_required
def laboratory_report(request):

    tests = LabTest.objects.all()

    return render(
        request,
        "reports/laboratory_report.html",
        {
            "tests": tests,
        },
    )



def department_report_pdf(request):

    response = HttpResponse(content_type="application/pdf")
    response["Content-Disposition"] = 'attachment; filename="department_report.pdf"'

    p = canvas.Canvas(response)

    p.setFont("Helvetica-Bold", 16)
    p.drawString(180, 800, "Department Report")

    p.setFont("Helvetica", 12)

    y = 760

    departments = Department.objects.all()

    for dept in departments:

        p.drawString(
            50,
            y,
            f"{dept.department_name} | {dept.department_head} | {dept.location}"
        )

        y -= 20

        if y < 50:
            p.showPage()
            p.setFont("Helvetica", 12)
            y = 800

    p.save()

    return response


def pharmacy_report_pdf(request):

    response = HttpResponse(content_type="application/pdf")

    response["Content-Disposition"] = (
        'attachment; filename="pharmacy_report.pdf"'
    )

    p = canvas.Canvas(response)

    # Title
    p.setFont("Helvetica-Bold", 18)
    p.drawString(180, 800, "Hospital Management System")

    p.setFont("Helvetica-Bold", 16)
    p.drawString(210, 775, "Pharmacy Report")

    # Header
    y = 740

    p.setFont("Helvetica-Bold", 11)

    p.drawString(30, y, "ID")
    p.drawString(70, y, "Medicine")
    p.drawString(220, y, "Manufacturer")
    p.drawString(340, y, "Category")
    p.drawString(430, y, "Price")
    p.drawString(500, y, "Stock")

    y -= 20

    p.setFont("Helvetica", 10)

    medicines = Medicine.objects.all()

    for medicine in medicines:

        p.drawString(30, y, str(medicine.medicine_id))
        p.drawString(70, y, medicine.medicine_name[:20])
        p.drawString(220, y, medicine.manufacturer[:18])
        p.drawString(340, y, medicine.category[:12])
        p.drawString(430, y, str(medicine.price))
        p.drawString(500, y, str(medicine.stock))

        y -= 20

        # New Page
        if y < 50:

            p.showPage()

            y = 800

            p.setFont("Helvetica-Bold", 11)

            p.drawString(30, y, "ID")
            p.drawString(70, y, "Medicine")
            p.drawString(220, y, "Manufacturer")
            p.drawString(340, y, "Category")
            p.drawString(430, y, "Price")
            p.drawString(500, y, "Stock")

            y -= 20

            p.setFont("Helvetica", 10)

    p.save()

    return response


def monthly_report_pdf(request):

    response = HttpResponse(content_type="application/pdf")
    response["Content-Disposition"] = (
        'attachment; filename="monthly_report.pdf"'
    )

    p = canvas.Canvas(response)

    p.setFont("Helvetica-Bold", 18)
    p.drawString(170, 800, "Hospital Management System")

    p.setFont("Helvetica-Bold", 16)
    p.drawString(220, 775, "Monthly Report")

    y = 740

    p.setFont("Helvetica-Bold", 11)

    p.drawString(40, y, "Bill ID")
    p.drawString(120, y, "Patient")
    p.drawString(280, y, "Doctor")
    p.drawString(430, y, "Amount")

    y -= 20

    p.setFont("Helvetica", 10)

    bills = Billing.objects.all()

    for bill in bills:

        p.drawString(40, y, str(bill.bill_id))
        p.drawString(120, y, bill.patient.full_name[:20])
        p.drawString(280, y, bill.doctor.full_name[:20])
        p.drawString(430, y, str(bill.total_amount))

        y -= 20

        if y < 50:
            p.showPage()
            y = 800

            p.setFont("Helvetica-Bold", 11)

            p.drawString(40, y, "Bill ID")
            p.drawString(120, y, "Patient")
            p.drawString(280, y, "Doctor")
            p.drawString(430, y, "Amount")

            y -= 20
            p.setFont("Helvetica", 10)

    p.save()

    return response


def analytics_pdf(request):

    response = HttpResponse(content_type="application/pdf")
    response["Content-Disposition"] = (
        'attachment; filename="analytics_dashboard.pdf"'
    )

    p = canvas.Canvas(response)

    p.setFont("Helvetica-Bold", 18)
    p.drawString(140, 800, "Hospital Management System")

    p.setFont("Helvetica-Bold", 16)
    p.drawString(200, 775, "Analytics Dashboard")

    p.setFont("Helvetica", 12)

    y = 730

    p.drawString(60, y, f"Total Patients : {Patient.objects.count()}")
    y -= 25

    p.drawString(60, y, f"Total Doctors : {Doctor.objects.count()}")
    y -= 25

    p.drawString(60, y, f"Total Appointments : {Appointment.objects.count()}")
    y -= 25

    p.drawString(60, y, f"Total Bills : {Billing.objects.count()}")
    y -= 25

    p.drawString(60, y, f"Total Medicines : {Medicine.objects.count()}")
    y -= 25

    p.drawString(60, y, f"Total Lab Tests : {LabTest.objects.count()}")

    p.save()

    return response