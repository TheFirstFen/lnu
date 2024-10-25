# Assignment 1 2DT902

## Emil Ulvagården (eu222dq@student.lnu.se)

### Uppgift 1

User Component:

- Registration and Authentication
    * Account creation
    * Account authentication
- Profile management
    * Profile Information
- Product search
    * View products in store or soon to be available
- Place orders

Employee Component:# Assignment 1 2DT902

## Emil Ulvagården (eu222dq@student.lnu.se)

### Uppgift 1

User Component:

- Registration and Authentication
    * Account creation
    * Account authentication
- Profile management
    * Profile Information
- Product search
    * View products in store or soon to be available
- Place orders

Employee Component:

- Manage inventory
    * Create new products, read information about existing products, update information on existing products and delete existing products.
- Manage Users
    * View user profiles, Create profiles, Update profile information, delete or inactivate profiles
- Manage Orders
    * Create orders, view orders and there status, update order information, delete orders
- Supplier management
    * View supplier information, Create new suppliers, View and create orders with the suppliers, update information on the suppliers, delete supplier information

Order Component:

- Order information
    * Customer information, product information, date of purchase, expected delivery date, cost
- Transaction
    * Manage Payments for products and refunds

Reporting Component

- Sales Report
    * Report how many products where bought and with what method, who sold the product
- Inventory level
    * Report on how full the inventory is and warns if the inventory is close to empty
- Customer Orders
    * Report if customers order are needed to be collected or if they are to be picked up

Data Storage:

- Store Data of the different components

The User Component is responsible for creating account and authenticating the users. The commponent is also responsible for manage profile information and deleting the accout. With the component you can check the different products that are available in the store or that are yet to be available.

The Employee component is responsible for managing inventory by viewing the current inventory, creating new products, updating information on existing products or deleting products that are not being sold any longer. The component is also capable of viewing user account, creating user accounts, updating user information and deleting user account. The component is able to view, create, update and delete orders. The component is responsible for managing information on the suppliers such as viewing there information and there stock, update information, create suppliers, delete supplier information and place orders with the suppliers aswell as view current order information with the supplier.

The Order Component is responsible for keeping track of the order informations such as the customer who made the purchase, what products where bought, when the product was made, when its expected to be delivered or if it was collected as the purchase was made and the cost of the products. The component is also responsible for managing the payments of different purchases aswell as possible refunds.

The Reporting Component is responsible for reporting how many products where bought, how they where bought and if an employee made the sale. Its responsible for sending reports on the inventory level and make a warning if its close to empty. Its also responsible for making a report if a customers order is soon to be picked up or needs to be collected by the employees.

The Data Storage is responsible for storing the information on the account for users and empoyees aswell as storing the information on what products are inputed in the system. Its also respinsible for storing the different information on orders aswell as the different reports that are made. 

### Uppgift 2

#### Reporting Component

This component requiers the Data Storage and provides to the Data Storage. The component fetches data from the Data Storage and creates reports on the data and stores it in the Data Storage. 

#### User Component

This component requiers the Data Storage and provides to the Data Storage and the Order Component. The component fetches user information and product information from the Data Storage. The component can update the user information stored in the Data Storage. It also provides the user information when a order is to be created.

#### Order Component

This component requiers Data Storage, User Component and Employee Component. The component provides to the Data Storage. The component fetches information about the products that are selected and avalable from the Data Storage. The component also requiers information about the user that it can get from either the User component or the Employee component. The component provides the order entry to the Data Storage where the order is stored. 

#### Employee Component

This component requiers Data Storage and provides to the Data Storage and to the Order Component. The component fetches information about reports, orders, users, employees and products from the Data Storage. The component provides information to the Data Storage and user information to the order component. 

#### Data Storage

The data storage requiers the Reporting Component, the User Component, the Order Component and the Employee component. This component provides to the Reporting Component, the User Component, the Order Component and the Employee Component. The component gets new or updated information from the four different components that are to be stored in the Data Storage. This component provides information to the four other components. 

### Uppgift 3

![Component Diagram](.\UML\Ass_1_Upg_3.png)

### Uppgift 4

#### Backend

- Database storage such as a mySQL, MongoDB or Oracle Database. This database is mainly for the component Data Storage. 
- Server for hosting a website running on linux.
- Backend server for the website such as java, Python, rust or NodeJS.

#### Frontend

- Website for the user to acces via a web browser on a device such as a computer or a phone. 
- The frontend is where the components 

#### Maintenance

- An IDE on an device capable of conecting to the website and the databases for updates, fixes and changes. 

#### Extra services 

- Payment API to handle transactions for costumers that pay through the webstore.
- A notification system that works with email for both costumers and employees.

### Uppgift 5

![Component Diagram](.\UML\Ass_1_Upg_5.png)


- Manage inventory
    * Create new products, read information about existing products, update information on existing products and delete existing products.
- Manage Users
    * View user profiles, Create profiles, Update profile information, delete or inactivate profiles
- Manage Orders
    * Create orders, view orders and there status, update order information, delete orders
- Supplier management
    * View supplier information, Create new suppliers, View and create orders with the suppliers, update information on the suppliers, delete supplier information

Order Component:

- Order information
    * Customer information, product information, date of purchase, expected delivery date, cost
- Transaction
    * Manage Payments for products and refunds

Reporting Component

- Sales Report
    * Report how many products where bought and with what method, who sold the product
- Inventory level
    * Report on how full the inventory is and warns if the inventory is close to empty
- Customer Orders
    * Report if customers order are needed to be collected or if they are to be picked up

Data Storage:

- Store Data of the different components

The User Component is responsible for creating account and authenticating the users. The commponent is also responsible for manage profile information and deleting the accout. With the component you can check the different products that are available in the store or that are yet to be available.

The Employee component is responsible for managing inventory by viewing the current inventory, creating new products, updating information on existing products or deleting products that are not being sold any longer. The component is also capable of viewing user account, creating user accounts, updating user information and deleting user account. The component is able to view, create, update and delete orders. The component is responsible for managing information on the suppliers such as viewing there information and there stock, update information, create suppliers, delete supplier information and place orders with the suppliers aswell as view current order information with the supplier.

The Order Component is responsible for keeping track of the order informations such as the customer who made the purchase, what products where bought, when the product was made, when its expected to be delivered or if it was collected as the purchase was made and the cost of the products. The component is also responsible for managing the payments of different purchases aswell as possible refunds.

The Reporting Component is responsible for reporting how many products where bought, how they where bought and if an employee made the sale. Its responsible for sending reports on the inventory level and make a warning if its close to empty. Its also responsible for making a report if a customers order is soon to be picked up or needs to be collected by the employees.

The Data Storage is responsible for storing the information on the account for users and empoyees aswell as storing the information on what products are inputed in the system. Its also respinsible for storing the different information on orders aswell as the different reports that are made. 

### Uppgift 2

#### Reporting Component

This component requiers the Data Storage and provides to the Data Storage. The component fetches data from the Data Storage and creates reports on the data and stores it in the Data Storage. 

#### User Component

This component requiers the Data Storage and provides to the Data Storage and the Order Component. The component fetches user information and product information from the Data Storage. The component can update the user information stored in the Data Storage. It also provides the user information when a order is to be created.

#### Order Component

This component requiers Data Storage, User Component and Employee Component. The component provides to the Data Storage. The component fetches information about the products that are selected and avalable from the Data Storage. The component also requiers information about the user that it can get from either the User component or the Employee component. The component provides the order entry to the Data Storage where the order is stored. 

#### Employee Component

This component requiers Data Storage and provides to the Data Storage and to the Order Component. The component fetches information about reports, orders, users, employees and products from the Data Storage. The component provides information to the Data Storage and user information to the order component. 

#### Data Storage

The data storage requiers the Reporting Component, the User Component, the Order Component and the Employee component. This component provides to the Reporting Component, the User Component, the Order Component and the Employee Component. The component gets new or updated information from the four different components that are to be stored in the Data Storage. This component provides information to the four other components. 

### Uppgift 3

![Component Diagram](.\UML\Ass_1_Upg_3.png)

### Uppgift 4

#### Backend

- Database storage such as a mySQL, MongoDB or Oracle Database. This database is mainly for the component Data Storage. 
- Server for hosting a website running on linux.
- Backend server for the website such as java, Python, rust or NodeJS.

#### Frontend

- Website for the user to acces via a web browser on a device such as a computer or a phone. 
- The frontend is where the components 

#### Maintenance

- An IDE on an device capable of conecting to the website and the databases for updates, fixes and changes. 

#### Extra services 

- Payment API to handle transactions for costumers that pay through the webstore.
- A notification system that works with email for both costumers and employees.

### Uppgift 5

![Component Diagram](.\UML\Ass_1_Upg_5.png)
