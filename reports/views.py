from django.shortcuts import render
from django.http import HttpResponse

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



def reports_dashboard(request):

    context = {

        "total_patients": Patient.objects.count(),

        "total_doctors": Doctor.objects.count(),

        "total_appointments": Appointment.objects.count(),

        "total_bills": Billing.objects.count(),

    }

    return render(
        request,
        "reports/dashboard_reports.html",
        context
    )


def patient_report(request):

    patients = Patient.objects.all()

    return render(
        request,
        "reports/patient_report.html",
        {
            "patients": patients
        }
    )

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
            "Disease",
        ]
    ]

    patients = Patient.objects.all()

    for patient in patients:

        data.append([

            patient.patient_id,

            patient.full_name,

            str(patient.age),

            patient.gender,

            patient.disease,

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


def doctor_report(request):

    doctors = Doctor.objects.all()

    return render(
        request,
        "reports/doctor_report.html",
        {
            "doctors": doctors
        }
    )

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
        "Specialization",
        "Experience"
    ]]

    doctors = Doctor.objects.all()

    for doctor in doctors:

        data.append([
            doctor.doctor_id,
            doctor.full_name,
            doctor.specialization,
            str(doctor.experience)
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
        "Status"
    ]]

    appointments = Appointment.objects.all()

    for appointment in appointments:

        data.append([
            appointment.id,
            str(appointment.patient),
            str(appointment.doctor),
            str(appointment.appointment_date),
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
        "Amount",
        "Status"
    ]]

    bills = Billing.objects.all()

    for bill in bills:

        data.append([
            bill.bill_id,
            str(bill.patient),
            str(bill.doctor),
            f"₹{bill.total_amount}",
            bill.payment_status,
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

def analytics_dashboard(request):

    total_patients = Patient.objects.count()
    total_doctors = Doctor.objects.count()
    total_appointments = Appointment.objects.count()

    total_revenue = Billing.objects.aggregate(
        Sum("total_amount")
    )["total_amount__sum"] or 0

    monthly_appointments = (
        Appointment.objects
        .annotate(month=ExtractMonth("appointment_date"))
        .values("month")
        .annotate(total=Count("id"))
        .order_by("month")
    )

    monthly_billing = (
        Billing.objects
        .annotate(month=ExtractMonth("bill_date"))
        .values("month")
        .annotate(total=Sum("total_amount"))
        .order_by("month")
    )

    context = {
        "total_patients": total_patients,
        "total_doctors": total_doctors,
        "total_appointments": total_appointments,
        "total_revenue": total_revenue,

        "appointment_labels":
            [item["month"] for item in monthly_appointments],

        "appointment_data":
            [item["total"] for item in monthly_appointments],

        "billing_labels":
            [item["month"] for item in monthly_billing],

        "billing_data":
            [item["total"] for item in monthly_billing],
    }

    return render(
        request,
        "reports/analytics_dashboard.html",
        context
    )