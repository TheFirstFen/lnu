# 2DT902 : Assaignment 1 : [Samuel Berg](mailto:sb224sc@student.lnu.se)

## Uppgift 1.

**User/Supplier components**
- User Authentication & Registration
    * Account creation
    * Login
- Profile Management
    * Delivery Address
    * Payment Information/Option
    * Order Managment(including previous orders)
- Search & Products Management
    * Start page with popular/recommended products
    * Search feature

**Employee components**
- Product management
    * Manage availability of products
    * Manage services
- Manage Customer accounts
    * View Delivery options
- Manage Orders
    * Change order status
    * Cancel/Refund Orders
- Supplier Management
    * Manage Supplier Information
- Reporting
    * View Daily/Weekly/Monthly/Yearly reports

**Transaction components**
- Cart
    * Adding & Removing of products
- Delivery Options
    * Pick-up at store
    * Delivery Service
- Payment API
    * Third-party payment integration
- Reporting
    * Number of Sales
    * Value of Sales
    * Number of Sold Products(of each product)

**Communication components**
- Order status
    * Notified on updates on your order(recived, sent, delivered, ready for pick-up)
- Product reviews/feedback
    * Can leave reviews on products and services that they have ordered and recived
- Reporting
    * Collect Summary of Reviews

**Data storage component**
- Stores the data of all other components

The ***user/supplier component*** provides the user and supplier interactions with the system. For users, they provide a way to manage personal information, browse products, and place orders. For suppliers, they ensure that product availability is updated and relevant.

The ***employee component*** are crucial for the operational management of the pet shop. They ensure that the inventory is up-to-date, customers receive the correct orders, and management has the necessary information for effective business decisions.

The ***transaction component*** are essential for the core transactional functions of the pet shop, enabling customers to purchase products and services while providing the business with detailed insights into the preformance of sales.

The ***communication component*** are important for maintaining a positive customer experience. They keep customers informed and engaged, and the feedback mechanism provides valuable insights into customer satisfaction and product quality.

The ***data storage component*** is the backbone of the system, ensuring that all information is securely stored, accessible, and retrievable for various functionalities across the system. It supports all operations and reporting needs by providing a central repository for all data.

## Uppgift 2. 

**User/supplier component**
- Provides
    * User/supplier data to *Data storage*, *Employee* & *Communication*
    * Order data to *Transaction*
    * Review data to *Communication*
- Requires
    * Fetch user/supplier data from *Data storage*
    * Fetch product data from *Data storage*
    * Order & payment processing from *Transaction*

**Employee component**
- Provides
    * Product data to *Data storage*
    * Order data to *Data storage*
    * Order status to *Communication*
- Requires
    * User/supplier data from *User/supplier*
    * Employee data from *Data storage*
    * Review data from *Communication*
    * Order data from *Transaction*

**Transaction component**
- Provides
    * Order & payment processing to *User/supplier*
    * Sale data to *Data storage*
    * Order data to *Communication* & *Employee*
- Requires
    * Order data from *User/supplier* & *Data storage*
    * Product data from *Data storage*
    * Order status from *Communication*

**Communication component**
- Provides
    * Order status to *Transaction*
    * Review data to *Employee* & *Data storage*
- Requires
    * Order data from *Transaction*
    * Review data from *Data storage* & *User/supplier*
    * Order status from *Employee*
    * User/supplier data from *User/supplier*

**Data Storage component**
- Provides
    * Order data to *Transaction*
    * Product data to *Transaction*
    * User/supplier data to *User/supplier*
    * Employee data to *Empolyee*
    * Review data to *Communication*
- Requires
    * Review data from *Communication*
    * Sale data from *Transaction*
    * User/supplier data from *User/supplier*
    * Product data from *Employee* & *User/supplier*
    * Order status from *Employee*

***User/Supplier component*** **requires** user/supplier data to provide the user with the details from previous orders and previous visit to the site where they may have put something into their cart, product data to make sure they have the most up-to date prices and in-stock details and order & payment processing to be able to purchase and check-out the items in their cart. **Provides** authentication to be able to make sure someone other the the actual user/supplier access the account in question, profile managment to be able to update their personal details such as payment options and delivery address and order history interfaces to be able to view order status and view their previous purchases with out store.

***Employee component*** **requires** user/supplier data to be able to view this data incase of user/supplier is in need of support, employee data(to give employee privleages throughout to store and data storage) to be able to view, handle, manage and update details of things such as products, review data to be able to see sale statistics and to be able to think of possible ways to improve the store for future user/suppliers as well as improve to stock that the store provides and order data to be able to update orders status for example when they have been prepared and sent out for delivery. **Provides** product, customer, supplier management interfaces for the empolyees to be able to carry out their day-to-day tasks and to be able to provide the customers with good services.

***Transaction component*** **requires** *user/supplier component* data for order processing and payment, product data from the *employee component* and order status from the *communication component*. **Provides** cart, order processing and payment intergration interfaces.

***Communication component*** **requires** order data from the *transaction component* and user contact information for effective communication from the *user/supplier component*. **Provides** order status notifications and review management interfaces.

***Data Storage component*** **requires** *user/supplier*, *employee*, *transaction* and *communication components* and **provides** to *user/supplier*, *employee*, *transaction* and *communication components*.


## Uppgift 3.

![UML component](./img/task3.drawio.png)

## Uppgift 4.
Fundera lite på den fysiska arkitekturen (systemarkitekturen). Vilka delar består
systemet av, vilka enheter ingår och vilken mjukvara installeras på respektive enhet?
Redovisa i textform.

## Uppgift 5.
Rita ett UML deploymentdiagram som illustrerar det du identifierat i uppgift 4.
![UML deployment](./img/)
