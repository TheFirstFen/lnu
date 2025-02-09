<style>
  .page-break { page-break-before: always; }
</style>

# Assignment 2 2DT902

## Emil Ulvagården (<eu222dq@student.lnu.se>)

### Task 1

The user is identifide by Identification where they provide username, email, phone number or email. After being identified the user can be authenticated by providing a password. After the user is authenticated the system provides them with their authorization depending on there account privileges. When the users whats to complete a purchase there payment information will be authorized by a payment API.

![UML-Diagram](../UML/Ass_2_Upg_1.png)

<div class="page-break"></div>

### Task 2

QAS 1:

* Source: Unauthorized user
* Stimulus: Attempted login but failed multiple times
* Artifact: Login system
* Environment: Normal operation
* Responce: Detects attempted login attempts and logs it
* Response Measure: Detects login attemps and temporarily bans the ip or makes the account in question inactiv

QAS 2:

* Source: Unidentifid user
* Stimulus: Multiple request per second
* Artifact: Login System and Resource
* Environment: Slower sytem (Overloaded system)
* Responce: Detects the requests, logs information and limits resourser
* Response Measure: Detects that multiple requests are sent and logs what the user is trying to do while limiting the amount of resources that the user can access to not disrupt other users.

QAS 3:

* Source: Unknown user
* Stimulus: Tries to create multiple acconts in a short time
* Artifact: Registration
* Environment: Normal operation
* Responce: Logs the created accounts together with the ip address for further investigation
* Response Measure: The system logs the created accounts and flags them togeter with the IP-address and temporarily blocks the IP to prevent further accounts from being created

<div class="page-break"></div>

### Task 3

The Database provides Resource with IP and requiers IP from Blocked IP. It also requiers Log IP and Account info from the Log component. The Database requiers Login info and authorization from the Identification, Authentication, Authorization component.

The database provieds login info and authorization to identification, authentication, authorization component. It also provides log IP and account info to log and it provides IP to Blocked IP. The Database component lastly provides IP to the Resource component.

Blocked IP provides IP for the Database.

Identification, Authentication, Authorization provides the database with login info and autorization.

Log provides the database with account info and Log IP.

Resource requiers IP from the Database.

![UML-Diagram](../UML/Ass_2_Upg_3.png)

<div class="page-break"></div>

### Task 4

Adaptation from task 3 are that the database is exanged for the data storage. Another change is that the component Identification, Authentication, Authorization dose not directly connect to the database anymore but provides the user component with the information directly. The Reporting component have been merged with the log component. The last adoptation from the first assignment is that the employee and user components have been merged to now be one component.

![UML-Diagram](../UML/Ass_2_Upg_4.png)

---

### Change log

|Task|part|
|----|----|
|Task 1|Use case diagram|
|Task 1|Text describing the diagram|
|Task 2|QAS 2 changed|
|Task 3|Description of the components in the diagram|
|Task 3|Component diagram|
|Task 4|Component diagram|
|Task 4|Text adaptations|

<div class="page-break"></div>

### Extra

#### Two ASR

* The system should be accessable from computers aswell as on smartphones.

* The system should offer recommendations and personalized settings based on past behavior.

The system should be accessable to computers aswell as smartphones as it increasses the amount of possible customers. This is due to that one mat not have access to a computer and only a smartphone or they have access to computer but not a smartphone. So when the possibility of accessing the system using both, there is a greater chance that we acquire a new customer. With the possibility of users accessing the system using both types of devices, the system should have a dynamic layout so that the system can be optimized depending on the screen size ensuring an enhanced user experience.

The system should offer recommendations and personalized settings based on past behavior to enhance the users experience on the system. This can make it easier for the customer to find the product that they are looking, or find new products based on the recommendation they are receving. With a better user experience it is more likly that the user is going to return in the future.

#### Trade offs

By blocking IPs or deactivation accounts after repeated failed login attempts will significantly reduce the risk for brute force attacks. This also limits the amount of login attempts and mitigating unauthorized access, therefore making the system more secure.

While this security measure is effective in preventing brute force attacks it can lead to usability problems for authorized users. For instance if a user where to forget there password or enters the password incorrectly multiple times, there IP could get blocked, looking them out of there account. If the users do not get fast feedback on why they are looked out of there account they could become angry or start wondering if there account has been comprimized.

The mesaure of limiting resources to protect the system from overloading due to distributed denial of service or from resource consumption by individual users. By limiting the rate at which users can make requests the system can ensure that legitimate users are not negatively affected by malicious users that try to overload the system.

While this security measure limits resource usage it could lead to slower response times for legitimate users, especially during high traffic periods. If the system restricts to many requests per second users may experience delay in accessing the system, which can reduce their overall satisfaction.

By blocking IPs where users create multiple accounts in a short period of time helps prevent fraudulent activity such as spamming or creating fake accounts for malicious purposes. This measure also ensures that the system's resources are not overwhelmed with non legitimate account creation.

One of the biggest usability issues is the risk of false positives, where legitimate users are blocked because they created to many accounts in a short amount of time. Users that share a network can also be affected due to other peoples actions.

When the system employ strict security measures, users who might make mistakes or face technical problems could experience frustration. While the system needs to be secure and minimize the possibility of a brute force attack it should still allow a user to access their account even if they have forgotten there password without being blocked. The people that share a network should also not be affected due to other peoples actions. So when using strict IP blocks there needs to be considerations for public networks where a lot of people may access the system from.

While the system should limit resources to users who make multiple requests under a short period of time it should not effect legitimate users, such as people with slow internet who might end up sending multiple requests in frustration.

#### How to solve trade offs

Instead of using immediate IP blocks I would implement a method for gradual lockout of the system where after a number of failed attempts the user can not make a new loggin attempt untill after a delay. If the user continues to make failed loggin attempts the delay will increase. The user should also have access to a method of reseting the password of the account to minimize the amount of loggin attempts that the user makes. For added security there should be a minimum of two factor authentication for the accounts if the amounts of attempts that the users get are large, to minimize the risk of unauthorized account access.

I would implement dynamic rate limiting on the amount of resources that a user can get so that during high traffic periods, the amount of resources that the users get are fairly distributed. The users that send to many requests in a short time period whould get a notification that says that they can not send more requests for a period of time while blocking the requests. If they continue to try and send a lot of requests they will get temporaraly blcoked from sending more requests and the time for the block will increase gradually.

I would implement a method for temporary blocks with a longer period of time so that an investigation can take place. The system should flag the IP that are creating the accounts and block access to account creation but still allow the user to verify the accounts through phone number or email. This whould prevent the system from wrongly blocking legitimate users while still protecting against fraudulent activity. The implementation of CAPTCHA between account creations whould also prevent automated account creations while not effecting other users.
