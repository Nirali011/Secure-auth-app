## 🔐 Security Design Document 

### Authentication
- Login/signup with secure validation
- Incorrect credentials handled safely

### Authorization
- Role-based access control (Admin / User)
- Admin routes protected

### Password Security
- Used bcrypt hashing to securely store passwords
- Plain text passwords are never stored

### Session Security
- Secure session handling using Flask sessions
- Session timeout and HTTPOnly cookies

### Attack Prevention
- SQL Injection prevented using parameterized queries
- XSS prevented using input sanitization