# simple-hospital-management-system

The Hospital Management System (HMS) is a Python-based desktop application developed to modernize the administrative workflow in healthcare facilities. It enables hospitals and clinics to efficiently manage patient records, prescriptions, appointments, and generate reports — all from a user-friendly graphical interface.

## 🖥️ Tech Stack

| Component              | Technology Used            |
|------------------------|----------------------------|
| GUI                    | Tkinter (Python)           |
| Backend                | Python 3.x                 |
| Database               | MySQL                      |
| PDF Reports            | FPDF / ReportLab (optional)|
| Database Connector     | `mysql-connector-python`   |

### Dependencies
- **Python 3.x**
- **MySQL Database Server**
- **MySQL Workbench** 
- **PDF Viewer** 
- **Python Libraries:**
 ```
  pip install mysql-connector-python
  ```
## 🗃️ Database Setup

1. Install **MySQL Server** and **MySQL Workbench**
2. Create a database:
   ```sql
   CREATE DATABASE mydata;
   ```
3. Inside the application, update your DB credentials as per your system:

   ```python
   user = "root"
   password = "your_mysql_password"
   database = "mydata"
   ```

4. Import the required tables (SQL schema or create via Workbench manually)

---

## 🛠️ How to Run

1. **Clone the repository**
   ```bash
   git clone https://github.com/your-username/simple-hospital-management-system.git
   cd simple-hospital-management-system
   ```

2. **Install Python dependencies**
   ```bash
   pip install mysql-connector-python
   ```

3. **Ensure MySQL Server is running**

4. **Run the application**
   ```bash
   python main.py
   ```

---

## 📝 Notes
- Ensure your MySQL password, user, and database name in the code match your system.
- If PDF generation is not included yet, use libraries like `fpdf`, `reportlab`, or `pdfkit` for implementation.

---

## 🙌 Acknowledgments
This project was created as a part of academic learning to demonstrate real-world software development using Python and MySQL.
