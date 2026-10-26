import click
import frappe

from ury.setup_customizations import after_install as setup


def after_install():
    try:
        print("Setting up URY...")
        setup()

        click.secho("Thank you for installing URY App!", fg="green")

    except Exception:
        frappe.log_error(title="URY after_install failed")
        raise
