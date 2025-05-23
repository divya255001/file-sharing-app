# 📁 File Sharing App

A secure website where users can log in, upload, download, and manage their files — like a mini Google Drive, built with Django.

---

## ❓ Why this project?

In real life, we often need a private and secure way to share files — not just through WhatsApp or email. Whether for companies, teams, or individuals, this web app provides a personal space to upload and download documents, images, and more.

This project also helps developers learn how to build a functional file management system using Django.

---

## 💡 Key Features

- 🔐 **User Login & Logout**  
  Only registered users can access upload/download features.

- 📤 **Upload Files**  
  Supports PDFs, DOCX, images, and more.  
  *(You can extend it to support drag-and-drop.)*

- 👁️ **Preview Files**  
  (Optional) Preview images or PDFs before downloading.

- 📂 **User Dashboard**  
  Each user has a private dashboard to:
  - View their uploaded files
  - Download files
  - Delete files

---

## 🛠 Tools Used

- **Django** – backend web framework  
- **Django FileField** – handles file uploads  
- **HTML/CSS** – front-end interface  
- **SQLite / PostgreSQL** – database to store files & users  
- **Django Admin** – admin dashboard for managing users & files

---

## 🚀 How to Run Locally

1. Clone the repository:
   ```bash
   git clone https://github.com/divya255001/file-sharing-app.git
   cd file-sharing-app
