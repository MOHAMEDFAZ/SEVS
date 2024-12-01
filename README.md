# Senate Election Voting System

The **Senate Election Voting System** is a Python-based application designed to facilitate the process of conducting and managing school senate elections. This application allows administrators to enter candidate details, manage student votes, and display election results in a secure and user-friendly way.

---

## Features

1. **Candidate Management**  
   - Add details for candidates contesting for various posts.
   - Supports posts like President, Vice President, Arts Club Secretary, Vice Arts Club Secretary, Magazine Editor, Vice Magazine Editor, Sports Captain, and Vice Sports Captain.

2. **Student Login and Voting**  
   - Students can log in using their school ID to cast their votes.
   - The system ensures each student can vote only once.

3. **Vote Counting and Results**  
   - Automatically tallies votes for each candidate.
   - Displays election results in a tabular format.

4. **Reset Functionality**  
   - Resets all voting data to start a new election session.

5. **Security**  
   - Admin access is protected by a security PIN for sensitive operations like viewing results or resetting data.

---

## File Structure

- `studentdetails.csv`: Stores student information, including their voting status.
- `votes.csv`: Records the results of the election.
- **Code**: Python script with the core functionality.

---

## How to Use

### 1. Setup
Ensure you have the following:
- Python 3 installed on your system.
- Required CSV files (`studentdetails.csv` and `votes.csv`) present in the same directory as the script.

### 2. Main Menu
Run the script and follow the prompts in the main menu:
1. **Enter Candidate Details**  
   Input the candidates' names, IDs, and classes for various posts.
2. **Start the Voting Session**  
   Allows students to log in and vote.
3. **Print Results**  
   Displays the winners for each post in a tabular format (requires admin PIN).
4. **Print All Votes**  
   Shows a detailed list of all candidates and their vote counts (requires admin PIN).
5. **Reset the Program**  
   Resets all data to begin a new election session.
6. **Exit**  
   Closes the application.

### 3. Security PIN
To access sensitive functions like printing results or resetting data, you need the security PIN:
- **Default PIN**: `9003`

---

## Functionality Overview

### Key Functions:
- **`encad()`**: Adds candidates to various posts.
- **`login()`**: Handles student login and voting validation.
- **`votechoice()`**: Allows students to vote for a specific candidate.
- **`results()`**: Calculates and displays election results.
- **`reset()`**: Resets student voting status and clears vote data.
- **`allvotes()`**: Displays the vote count for all candidates.

### Helper Functions:
- **`details()`**: Marks a student as having voted.
- **`maxvotes()`**: Identifies the candidate(s) with the highest votes.
- **`display()`**: Outputs CSV data in a formatted table.

---

## Prerequisites

- Basic knowledge of Python.
- Familiarity with CSV files.

---

## Future Improvements

- Add graphical user interface (GUI) for better usability.
- Enhance security with individual user passwords.
- Allow dynamic post creation.

---

## Authors

Developed by: Mohamed Fazil 
For feedback or contributions, please contact: mohamedfazil478@gmail.com

---

## License

This project is licensed under the MIT License.
