import streamlit as st

from jinja2 import Environment, FileSystemLoader
import pdfkit

env = Environment(loader=FileSystemLoader("."))
template = env.get_template("template.html")

html_out = template.render()
wkhtml_path = pdfkit.configuration(wkhtmltopdf = "wkhtmltopdfQT/bin/wkhtmltopdf")
with open("output.html", "w") as f:
    f.write(html_out)

options = {
        "enable-local-file-access": "",  # Enabling local file access
        "header-html": "header.html",  # Path to header HTML file
        "footer-html": "footer.html",  # Path to footer HTML file
        "margin-top": "30mm",  # Set margin to accommodate header
        "margin-left": "0mm",
        "margin-right": "0mm",
        "margin-bottom": "25mm",  # Set margin to accommodate footer
        "page-size": "Letter",
    }

st.write(wkhtml_path)


pdfkit.from_file("output.html", "output.pdf", options=options, configuration=wkhtml_path)

with open("output.pdf", "rb") as pdf_file:
        PDFbyte = pdf_file.read()
        
st.download_button(
            label="Download Report",
            data=PDFbyte,
            file_name="report.pdf",
            mime="application/octet-stream",
        )


