# 🚀 CEIS400 Course Project – Equipment Checkout System (ECS)

Welcome to the collaborative project for CEIS400 – Software Engineering!  
This repository showcases our Week 2 milestone: the **Equipment Checkout System (ECS)** – a software solution designed to modernize and streamline how organizations manage tools, equipment, and inventory in real time.

---

## 📌 Project Overview

The **ECS** project was initiated to solve inefficiencies in tool management and accountability within maintenance departments. Our goal is to develop a secure, role-aware system that tracks tool check-ins/check-outs, enforces access permissions, and maintains accurate inventory data — all while supporting administrative oversight and compliance.

This system isn't just about automation — it’s about control, transparency, and smart resource management.

---

## 🎯 Objectives

- ✅ Automate tool check-in/check-out processes
- ✅ Provide serialized inventory tracking
- ✅ Enforce employee tool permissions by job role and work zone
- ✅ Generate digital receipts and maintain audit logs
- ✅ Support tool and employee management by administrators
- ✅ Alert key personnel with automated system notifications

---

## 🛠️ Key Features

- **Smart Check-In/Check-Out**: Employees interact via kiosks to handle tools, with all actions logged securely.
- **Serialized Inventory**: Tools are uniquely tagged and traceable at all times.
- **Zone-Based Control**: Access rules are based on job type, location, and certification.
- **Role-Based Permissions**: Only qualified users can perform specific actions.
- **Automated Receipts**: Every transaction includes timestamped confirmations.
- **Enforced Returns**: Tools can only be returned by the original checkout user, ensuring accountability.
- **Inventory Updates**: Admins can modify tool/employee records and generate reports.

---

## 👥 Project Team

We proudly collaborated as **Team 4** in the July 2025 session of CEIS400:

- **Brandon Barrett**
- **Heather Skabialka**
- **Clayton Seeber**
- **Antonio Hancock**
- **Jonathan Krueger**

---

## 🧑‍💻 System Actors

The ECS involves multiple human and system entities:

- **Maintenance Worker** – Primary tool user
- **Administrator** – Oversees system configuration, permissions, and data
- **ECS System** – Manages business rules and operations
- **ECS Database** – Stores all transactional and reference data
- **Email System** – Sends notifications and alerts
- **Project Manager** – Coordinates ECS usage and workflow
- **Warehouse & Equipment Manager** – Maintains tool inventory
- **HR/Safety/Finance Managers** – Ensure policy and process compliance
- **Auditor & Compliance Officer** – Reviews records and system behavior

---

## 💡 Use Case Examples

- **Check Out Tool**  
  A Maintenance Worker authenticates via kiosk, selects a tool, and (if authorized) successfully checks it out. A digital receipt is generated, and the inventory updates.

- **Return Tool**  
  The same employee must return the tool. ECS verifies identity, updates the tool’s status, and logs the return.

- **Request Denial**  
  If a user lacks clearance or the tool is unavailable, ECS blocks the transaction and notifies the relevant supervisor.

- **Admin Tool Management**  
  Admins can register new tools, retire broken items, or update employee roles in real time.

---

## 🧪 Testing & Validation

To ensure system reliability, we’ve structured a formal test plan based on industry standards. The test plan validates:

- Functional performance of key use cases
- Proper enforcement of role and zone restrictions
- Integrity of tool tracking across transactions
- Error handling and edge cases

---

## 🔮 Future Enhancements

We envision ECS expanding into a fully deployed enterprise tool, with:

- 🌐 A responsive web or mobile interface
- 🧾 Real-time analytics dashboards
- 🔐 Integration with HR/finance platforms
- 🎯 Predictive alerts and usage forecasting

---

## 📚 Course Context

**Course**: CEIS400 – Software Engineering  
**Instructor**: Prof. Kohlbus  
**Session**: July 2025  

---

Thank you for exploring our project! 🎉  
We welcome feedback, suggestions, or ideas for evolving the Equipment Checkout System.

