import streamlit as st
import os

from jinja2 import Environment, FileSystemLoader
import pdfkit

env = Environment(loader=FileSystemLoader("."))
template = env.get_template("template.html")

html_out = template.render()

with open("output.html", "w") as f:
    f.write(html_out)

options = {
        "enable-local-file-access": "",  # Enabling local file access
        "margin-top": "0mm",  # Set margin to accommodate header
        "margin-left": "0mm",
        "margin-right": "0mm",
        "margin-bottom": "0mm",  # Set margin to accommodate footer
        "page-size": "Letter",
    }


pdfkit.from_file("output.html", "output.pdf", options=options)

with open("output.pdf", "rb") as pdf_file:
        PDFbyte = pdf_file.read()
        
st.download_button(
            label="Download Report",
            data=PDFbyte,
            file_name="report.pdf",
            mime="application/octet-stream",
        )


