# Senate Election Voting System 🗳️

Welcome to the **Senate Election Voting System**! A streamlined Python-based tool to make your school senate elections smooth, fair, and efficient. 🎯

---

## 🌟 Features

### 🎖️ Candidate Management  
- Add candidate details for key positions, including:  
  - 🏆 President  
  - 🏅 Vice President  
  - 🎨 Arts Club Secretary  
  - 🎭 Vice Arts Club Secretary  
  - ✍️ Magazine Editor  
  - 🖌️ Vice Magazine Editor  
  - 🏀 Sports Captain  
  - ⚽ Vice Sports Captain  

### 🔐 Secure Student Login and Voting  
- Students log in using their **school ID**.  
- Ensures each student can vote only **once**—no double voting!  

### 📊 Automated Vote Counting and Results  
- Automatically counts votes for each candidate.  
- Displays winners in a clean, tabular format for easy readability.  

### 🔄 Reset Functionality  
- Admins can reset all data to prepare for a new election session.  

### 🛡️ Security PIN Protection  
- Admin-only functions like viewing results or resetting data require a PIN to ensure privacy.

---

## 🗂️ File Structure

- **`studentdetails.csv`**: Stores student information, including their voting status.  
- **`votes.csv`**: Records all candidate votes.  
- **Python Script**: The core functionality of the system.

---

## 🚀 How to Use

### Step 1️⃣: Setup  
Make sure you have:  
- **Python 3** installed.  
- Required CSV files (`studentdetails.csv` and `votes.csv`) in the same directory.  

### Step 2️⃣: Explore the Main Menu  
Run the program and choose from these options:  
1. **🏷️ Enter Candidate Details**  
   Input candidate information for various posts.  

2. **🙋‍♂️ Start Voting**  
   Allow students to securely log in and vote.  

3. **🏆 Print Results**  
   View the winners for each post (admin PIN required).  

4. **📋 Print All Votes**  
   See a detailed vote count for all candidates (admin PIN required).  

5. **🔄 Reset the Program**  
   Clear all data to prepare for a new election session.  

6. **❌ Exit**  
   Close the application.  

### Step 3️⃣: Security PIN  
The default admin PIN is `9003`. Update it in the code for added security.

---

## 🛠️ Key Features Explained

- **`encad()`**: Add candidates for each post.  
- **`login()`**: Manage student logins and voting validation.  
- **`votechoice()`**: Enable students to cast their votes.  
- **`results()`**: Automatically calculate and display winners.  
- **`reset()`**: Reset all data to start fresh.  
- **`allvotes()`**: Show vote counts for all candidates.  

---

## 🌟 Future Improvements  
- Add a **GUI** for enhanced usability.  
- Introduce individual passwords for students.  
- Enable custom post creation by the admin.

---

## 👩‍💻 Author

Developed by: **Mohamed Fazil**  
For feedback or contributions, reach out at: **mohamedfazil478@gmail.com**

---

## 📜 License

This project is licensed under the **MIT License**.  
