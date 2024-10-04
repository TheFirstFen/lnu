# 2DT902 : Assaignment 2 : [Samuel Berg(sb224sc)](mailto:sb224sc@student.lnu.se)

## Uppgift 1.
System beskrivningen för Pet Shop saknar konkreta kvalitetskrav. Det blir därför ditt ansvar som arkitekt att arbeta med säkerhetsattributet, som är en viktig angelägenhet (concern) för den här typen av system. Modellera med hjälp av en usecase-modell hur en mekanism för identifiering, autentisering och auktorisering skall fungera utifrån ett användarperspektiv.

### Identification (User Registration):

* **Primary Actor**: User
* **Goal**: The user provides their identity (e.g., username, email) to create an account in the system.
* **Process**:
    - The user navigates to the registration page and enters personal details such as username, password, and contact information.
    - The system validates the information (e.g., ensuring the email is unique) and creates a new account.
* **Outcome**: The user is registered and assigned a unique identity in the system.

### Authentication (Login):

* **Primary Actor**: User
* **Goal**: The user logs into the system using previously created credentials.
* **Process**:
    - The user enters their username and password on the login page.
    - The system compares the entered credentials with stored ones and grants access if they match.
* **Alternative Path**: If the credentials are incorrect, the system returns an error message.
* **Outcome**: The user is authenticated and granted access to their account.

### Authorization (Access Control):

* **Primary Actor**: User
* **Goal**: The system restricts access to certain actions or resources based on user roles.
* **Process**: 
    - After login, the system checks the user’s role (e.g., customer, employee, supplier) to determine what functions they can perform.
    - For example, an employee may access product management, while a customer can only view their order history and manage personal details.
* **Outcome**: The user is granted appropriate access based on their role.

## Uppgift 2. (WIP!!)
Modellera tre kvalitetsattributscenarios som visar hur systemet skall bete sig för att begränsa tillgången till resurser och information i systemet.

### QAS 1

**Confidentiality Scenario**: Unauthorized Data Access

* **Stimulus**: A user attempts to access data or resources they are not authorized to view, such as another user's account details or sensitive product information.
* **Environment**: The system is operational, and the user is logged in but only has customer-level access rights.
* **Response**: The system detects the user’s role and restricts access to only the resources they are permitted to view. The attempt to access restricted information is logged for security monitoring.
* **Response Measure**: Unauthorized access is prevented 100% of the time, and an alert or log entry is generated within 1 second of the attempted breach.

### QAS 2

**Integrity Scenario**: Tampering with Data

* **Stimulus**: An employee with product management privileges tries to manipulate sensitive data, such as changing product prices without proper authorization.
* **Environment**: The system is live and handling multiple transactions, with role-based access control (RBAC) enabled.
* **Response**: The system verifies the employee’s role and privileges before allowing any modification. If the user lacks the required authorization, the modification is rejected, and a security alert is generated.
* **Response Measure**: Unauthorized modifications are rejected instantly, with an error message shown to the user, and the attempted action is logged for audit purposes.

### QAS 3

**Availability Scenario**: Denial of Service Protection

* **Stimulus**: A malicious actor attempts a Denial of Service (DoS) attack by sending a large number of requests to overwhelm the server hosting the Pet Shop system.
* **Environment**: The system is under attack, but the user-facing components are still functional.
* **Response**: The system detects the abnormally high number of requests and activates rate-limiting and firewall measures to block malicious traffic while maintaining service availability for legitimate users.
* **Response Measure**: The system continues to serve legitimate users with a 99% uptime during the attack, and the attack is neutralized within 5 minutes of detection.

## Uppgift 3.
Rita ett UML komponentdiagram med de komponentabstraktioner, ansvar och relationer som behövs för den säkerhetsfunktionalitet som modellerats i uppgift 1 och 2.


## Uppgift 4.
Integrera komponenterna från uppgift 3 med den modell av systemets funktionalitet som du tog fram i inlämningsuppgift 1.

Diskutera eventuella anpassningar som behöver göras.
