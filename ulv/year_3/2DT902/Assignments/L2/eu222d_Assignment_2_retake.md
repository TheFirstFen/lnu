# Assignment 2 2DT902

## Emil Ulvagården (eu222dq@student.lnu.se)

### Task 1

The user is identifid by using an username of email by checking the backend server and then by using there password the user is authenticated. Once the user is both identified and authenticated the user can be authorized by checking with the backent to give the right amount of privlages. Once a user procides with the checkout their payment information is confirmed by a third party patment API.

![UML-Diagram](../UML/Ass_2_Upg_1.png)

### Task 2

QAS 1:

* Source: Unauthorized user
* Stimulus: Attempted login but failed multiple times
* Artifact: Login system
* Environment: Normal operation
* Responce: Detects attempted login attempts and logs it
* Response Measure: Detects login attemps and temporarily bans the ip or makes the account in question inactiv

QAS 2:

* Source: Identified user
* Stimulus: Tries to login from a new device
* Artifact: Authentication
* Environment: Normal operation
* Responce: Detects a new device and asks what authentication medthod they would like to use
* Response Measure: Send a two factor authentication code to the accounts email address or phone number

QAS 3:

* Source: Unknown user
* Stimulus: Tries to create multiple acconts in a short time
* Artifact: Registration
* Environment: Normal operation
* Responce: Logs the created accounts together with the ip address for further investigation
* Response Measure: The system logs the created accounts and flags them togeter with the IP-address and temporarily blocks the IP to prevent further accounts from being created

### Task 3

The database provieds login info and authorization to identification, authentication, authorization component. It also provides log IP and account info to log and it provides IP to Blocked IP.

Blocked IP provides the IP to identification, authentication, authorization and requiers IP from Database.

Identification, Authentication, Authorization requiers IP from Blocked IP and login info and autorization from the database and provides the log with identification, authentication, authorization.

Log requiers Log IP and account info from Database and requiers identification, authentication, authorization from Identification, Authentication, Authorization.

![UML-Diagram](../UML/Ass_2_Upg_3.png)

### Task 4

Adaptation from task 3 are that the  database is exanged for the data storage. There are also some extra relations between added to the Employee, User and Data Storage components.

![UML-Diagram](../UML/Ass_2_Upg_4.png)

### Change log

|Task|part|
|----|----|
|Task 1|Use case diagram|
|Task 1|Text describing the diagram|
|Task 2|QAS 2 changed|
|Task 3| |
|Task 4|Component diagram and text |

### Extra

#### Two ASR

#### Trade offs

#### How to solve trade offs
