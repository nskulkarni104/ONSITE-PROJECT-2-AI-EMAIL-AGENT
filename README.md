# ONSITE-PROJECT-2-AI-EMAIL-AGENT
AI-powered sick leave email generator built with flask and gemini 2.5 flash, featuring automated SMTP email and delivery.


AI Email Agent – Sick Leave Generator

Overview
This project implements an AI-based email automation system using Flask and Google Gemini 2.5 Flash.
The system generates professional sick leave emails dynamically based on user input and sends them automatically using Gmail SMTP.

Models Used: Google Gemini

Gemini 2.5 Flash (Large Language Model)
Purpose: Professional email generation

Backend Framework: Flask (Python), Email Service and Gmail SMTP (SSL connection).

Workflow:

Collect user input from HTML interface
Format dates into natural readable format
Construct structured LLM prompt
Generate professional email using Gemini 2.5 Flash
Clean formatting artifacts (markdown removal)
Send generated email via Gmail SMTP

Features:

Optional colleague handover mention
Natural human-like email generation
Secure environment variable configuration
End-to-end AI automation pipeline

Dataset: No dataset required.
Email content is dynamically generated using Gemini LLM.

Note: API keys and email credentials are excluded for security reasons.

Author: Nishchal Kulkarni
USN: 2BA22EC058
